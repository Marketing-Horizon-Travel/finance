"""
Vouchers API — Unified CRUD for all accounting vouchers.
Supports filtering by module (cash, bank, purchase, sale, etc.)
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func as sqlfunc
from typing import Optional
from datetime import date

from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.voucher import Voucher, VoucherLine
from app.models.user import User
from app.schemas.voucher import (
    VoucherCreate, VoucherResponse, VoucherListResponse,
)

router = APIRouter(prefix="/api/vouchers", tags=["Vouchers"])


def _generate_number(db: Session, module: str, voucher_type: str, year: int) -> str:
    """Auto-generate voucher number: PT2024-001, PC2024-002, etc."""
    prefix_map = {
        ("cash", "receipt"): "PT",
        ("cash", "payment"): "PC",
        ("bank", "receipt"): "BC",
        ("bank", "payment"): "BN",
        ("purchase", "purchase_invoice"): "MH",
        ("purchase", "purchase_order"): "DM",
        ("sale", "sale_invoice"): "BH",
        ("sale", "quotation"): "BG",
        ("sale", "sale_order"): "DH",
        ("inventory", "stock_in"): "NK",
        ("inventory", "stock_out"): "XK",
        ("inventory", "stock_transfer"): "CK",
        ("general", "journal"): "BT",
    }
    prefix = prefix_map.get((module, voucher_type), "CT")
    count = (
        db.query(sqlfunc.count(Voucher.id))
        .filter(
            Voucher.module == module,
            Voucher.voucher_type == voucher_type,
            sqlfunc.extract("year", Voucher.voucher_date) == year,
        )
        .scalar()
    )
    return f"{prefix}{year}-{count + 1:04d}"


@router.get("", response_model=VoucherListResponse)
def list_vouchers(
    module: Optional[str] = None,
    voucher_type: Optional[str] = None,
    status: Optional[str] = None,
    currency: Optional[str] = None,
    search: Optional[str] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    q = db.query(Voucher)
    if module:
        q = q.filter(Voucher.module == module)
    if voucher_type:
        q = q.filter(Voucher.voucher_type == voucher_type)
    if status:
        q = q.filter(Voucher.status == status)
    if currency:
        q = q.filter(Voucher.currency == currency)
    if search:
        q = q.filter(
            (Voucher.voucher_number.ilike(f"%{search}%"))
            | (Voucher.contact_name.ilike(f"%{search}%"))
            | (Voucher.description.ilike(f"%{search}%"))
        )
    if date_from:
        q = q.filter(Voucher.voucher_date >= date_from)
    if date_to:
        q = q.filter(Voucher.voucher_date <= date_to)

    total = q.count()
    items = (
        q.order_by(Voucher.voucher_date.desc(), Voucher.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    return VoucherListResponse(items=items, total=total, page=page, page_size=page_size)


@router.post("", response_model=VoucherResponse)
def create_voucher(
    data: VoucherCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    number = _generate_number(db, data.module, data.voucher_type, data.voucher_date.year)
    voucher = Voucher(
        voucher_number=number,
        voucher_date=data.voucher_date,
        posting_date=data.posting_date,
        module=data.module,
        voucher_type=data.voucher_type,
        status=data.status,
        customer_id=data.customer_id,
        supplier_id=data.supplier_id,
        employee_id=data.employee_id,
        contact_name=data.contact_name,
        contact_address=data.contact_address,
        currency=data.currency,
        exchange_rate=data.exchange_rate,
        description=data.description,
        reference_doc=data.reference_doc,
        reference_number=data.reference_number,
        reference_date=data.reference_date,
        cashier=data.cashier,
        created_by=current_user.id,
    )

    total = 0
    total_vnd = 0
    for line_data in data.lines:
        line = VoucherLine(**line_data.model_dump(), voucher=voucher)
        line.amount_vnd = line.amount * data.exchange_rate
        total += line.amount
        total_vnd += line.amount_vnd
        db.add(line)

    voucher.total_amount = total
    voucher.total_amount_vnd = total_vnd

    db.add(voucher)
    db.commit()
    db.refresh(voucher)
    return voucher


@router.get("/{voucher_id}", response_model=VoucherResponse)
def get_voucher(voucher_id: int, db: Session = Depends(get_db)):
    voucher = db.query(Voucher).filter(Voucher.id == voucher_id).first()
    if not voucher:
        raise HTTPException(404, "Chứng từ không tồn tại")
    return voucher


@router.put("/{voucher_id}", response_model=VoucherResponse)
def update_voucher(
    voucher_id: int,
    data: VoucherCreate,
    db: Session = Depends(get_db),
):
    voucher = db.query(Voucher).filter(Voucher.id == voucher_id).first()
    if not voucher:
        raise HTTPException(404, "Chứng từ không tồn tại")
    if voucher.status == "posted":
        raise HTTPException(400, "Không thể sửa chứng từ đã hạch toán")

    for key in ["voucher_date", "posting_date", "status", "customer_id", "supplier_id",
                "employee_id", "contact_name", "contact_address", "currency",
                "exchange_rate", "description", "reference_doc", "cashier"]:
        setattr(voucher, key, getattr(data, key))

    # Replace lines
    db.query(VoucherLine).filter(VoucherLine.voucher_id == voucher_id).delete()
    total = 0
    total_vnd = 0
    for line_data in data.lines:
        line = VoucherLine(**line_data.model_dump(), voucher_id=voucher_id)
        line.amount_vnd = line.amount * data.exchange_rate
        total += line.amount
        total_vnd += line.amount_vnd
        db.add(line)

    voucher.total_amount = total
    voucher.total_amount_vnd = total_vnd
    db.commit()
    db.refresh(voucher)
    return voucher


@router.delete("/{voucher_id}")
def delete_voucher(voucher_id: int, db: Session = Depends(get_db)):
    voucher = db.query(Voucher).filter(Voucher.id == voucher_id).first()
    if not voucher:
        raise HTTPException(404, "Chứng từ không tồn tại")
    if voucher.status == "posted":
        raise HTTPException(400, "Không thể xóa chứng từ đã hạch toán. Hãy hủy trước.")
    db.delete(voucher)
    db.commit()
    return {"message": "Đã xóa chứng từ"}


@router.post("/{voucher_id}/post")
def post_voucher(voucher_id: int, db: Session = Depends(get_db)):
    """Hạch toán chứng từ"""
    voucher = db.query(Voucher).filter(Voucher.id == voucher_id).first()
    if not voucher:
        raise HTTPException(404, "Chứng từ không tồn tại")
    if voucher.status == "posted":
        raise HTTPException(400, "Chứng từ đã được hạch toán")
    voucher.status = "posted"
    db.commit()
    return {"message": "Đã hạch toán chứng từ"}


@router.post("/{voucher_id}/cancel")
def cancel_voucher(voucher_id: int, db: Session = Depends(get_db)):
    """Hủy chứng từ"""
    voucher = db.query(Voucher).filter(Voucher.id == voucher_id).first()
    if not voucher:
        raise HTTPException(404, "Chứng từ không tồn tại")
    voucher.status = "cancelled"
    db.commit()
    return {"message": "Đã hủy chứng từ"}


# ─── Summary endpoints for dashboard ─────────────────────

@router.get("/summary/{module}")
def get_module_summary(
    module: str,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    db: Session = Depends(get_db),
):
    """Get summary stats for a module (used by dashboard cards)."""
    q = db.query(Voucher).filter(Voucher.module == module, Voucher.status == "posted")
    if date_from:
        q = q.filter(Voucher.voucher_date >= date_from)
    if date_to:
        q = q.filter(Voucher.voucher_date <= date_to)

    vouchers = q.all()
    total_receipt = sum(v.total_amount_vnd for v in vouchers if "receipt" in (v.voucher_type or ""))
    total_payment = sum(v.total_amount_vnd for v in vouchers if "payment" in (v.voucher_type or ""))

    return {
        "module": module,
        "total_vouchers": len(vouchers),
        "total_receipt": total_receipt,
        "total_payment": total_payment,
        "net": total_receipt - total_payment,
    }
