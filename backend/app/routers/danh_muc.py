"""
Danh mục API — CRUD for all master data categories.
Generic pattern: each entity gets list/create/update/delete endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.danh_muc import (
    Account, Customer, Supplier, Employee, EmployeeGroup,
    Warehouse, Product, ProductGroup, Unit,
    Bank, BankAccount, Department,
    CostObject, CostItem, Currency, PaymentTerm,
    CashFlowItem, VoucherType, StatCode,
    AssetType, ToolType,
)
from app.schemas.danh_muc import (
    AccountSchema, CustomerSchema, SupplierSchema, EmployeeSchema,
    ProductSchema, WarehouseSchema, SimpleCodeNameSchema,
    BankAccountSchema, DepartmentSchema, CurrencySchema,
)

router = APIRouter(prefix="/api/danh-muc", tags=["Danh mục"])


# ─── Helper: Generic CRUD factory ────────────────────────

def _crud_routes(path: str, Model, Schema, label: str):
    """Generate standard CRUD endpoints for a simple model."""

    @router.get(f"/{path}", response_model=List[Schema], name=f"list_{path}")
    def list_items(
        search: Optional[str] = None,
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
    ):
        q = db.query(Model)
        if search and hasattr(Model, "name"):
            q = q.filter(Model.name.ilike(f"%{search}%"))
        return q.offset(skip).limit(limit).all()

    @router.post(f"/{path}", response_model=Schema, name=f"create_{path}")
    def create_item(data: Schema, db: Session = Depends(get_db)):
        item = Model(**data.model_dump())
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    @router.get(f"/{path}/{{item_id}}", response_model=Schema, name=f"get_{path}")
    def get_item(item_id: int, db: Session = Depends(get_db)):
        item = db.query(Model).filter(Model.id == item_id).first()
        if not item:
            raise HTTPException(404, f"{label} không tồn tại")
        return item

    @router.put(f"/{path}/{{item_id}}", response_model=Schema, name=f"update_{path}")
    def update_item(item_id: int, data: Schema, db: Session = Depends(get_db)):
        item = db.query(Model).filter(Model.id == item_id).first()
        if not item:
            raise HTTPException(404, f"{label} không tồn tại")
        for key, val in data.model_dump().items():
            setattr(item, key, val)
        db.commit()
        db.refresh(item)
        return item

    @router.delete(f"/{path}/{{item_id}}", name=f"delete_{path}")
    def delete_item(item_id: int, db: Session = Depends(get_db)):
        item = db.query(Model).filter(Model.id == item_id).first()
        if not item:
            raise HTTPException(404, f"{label} không tồn tại")
        db.delete(item)
        db.commit()
        return {"message": f"Đã xóa {label}"}


# ─── Register all CRUD routes ────────────────────────────

_crud_routes("accounts", Account, AccountSchema, "Tài khoản")
_crud_routes("customers", Customer, CustomerSchema, "Khách hàng")
_crud_routes("suppliers", Supplier, SupplierSchema, "Nhà cung cấp")
_crud_routes("employees", Employee, EmployeeSchema, "Nhân viên")
_crud_routes("products", Product, ProductSchema, "Vật tư hàng hóa")
_crud_routes("warehouses", Warehouse, WarehouseSchema, "Kho")
_crud_routes("departments", Department, DepartmentSchema, "Phòng ban")
_crud_routes("currencies", Currency, CurrencySchema, "Loại tiền")
_crud_routes("banks", Bank, SimpleCodeNameSchema, "Ngân hàng")
_crud_routes("bank-accounts", BankAccount, BankAccountSchema, "TK ngân hàng")
_crud_routes("units", Unit, SimpleCodeNameSchema, "Đơn vị tính")
_crud_routes("product-groups", ProductGroup, SimpleCodeNameSchema, "Nhóm VTHH")
_crud_routes("customer-groups", EmployeeGroup, SimpleCodeNameSchema, "Nhóm KH/NCC")
_crud_routes("cost-objects", CostObject, SimpleCodeNameSchema, "Đối tượng THCP")
_crud_routes("cost-items", CostItem, SimpleCodeNameSchema, "Khoản mục CP")
_crud_routes("payment-terms", PaymentTerm, SimpleCodeNameSchema, "Điều khoản TT")
_crud_routes("cash-flow-items", CashFlowItem, SimpleCodeNameSchema, "Mục thu/chi")
_crud_routes("stat-codes", StatCode, SimpleCodeNameSchema, "Mã thống kê")
_crud_routes("voucher-types", VoucherType, SimpleCodeNameSchema, "Loại chứng từ")
_crud_routes("asset-types", AssetType, SimpleCodeNameSchema, "Loại TSCĐ")
_crud_routes("tool-types", ToolType, SimpleCodeNameSchema, "Loại CCDC")
