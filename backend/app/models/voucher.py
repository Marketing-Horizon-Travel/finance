"""
Voucher — Chứng từ kế toán tổng quát.
Dùng cho tất cả phân hệ: Tiền mặt, Ngân hàng, Mua hàng, Bán hàng,
Kho, CCDC, TSCĐ, Tiền lương, Tổng hợp.
"""
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, Date, DateTime,
    ForeignKey, Text, Enum,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

import enum


class VoucherStatus(str, enum.Enum):
    DRAFT = "draft"
    POSTED = "posted"
    CANCELLED = "cancelled"


class VoucherModule(str, enum.Enum):
    CASH = "cash"                  # Tiền mặt
    BANK = "bank"                  # Ngân hàng
    PURCHASE = "purchase"          # Mua hàng
    SALE = "sale"                  # Bán hàng
    INVOICE = "invoice"            # Hóa đơn
    INVENTORY = "inventory"        # Kho
    TOOL = "tool"                  # CCDC
    ASSET = "asset"                # Tài sản cố định
    PAYROLL = "payroll"            # Tiền lương
    TAX = "tax"                    # Thuế
    COSTING = "costing"            # Giá thành
    GENERAL = "general"            # Tổng hợp


class Voucher(Base):
    __tablename__ = "vouchers"

    id = Column(Integer, primary_key=True, index=True)
    voucher_number = Column(String(30), unique=True, nullable=False, index=True)
    voucher_date = Column(Date, nullable=False)
    posting_date = Column(Date, nullable=False)
    module = Column(String(20), nullable=False, index=True)
    voucher_type = Column(String(30), nullable=False)  # receipt, payment, purchase_invoice, sale_invoice, etc.
    status = Column(String(20), default="draft", index=True)

    # Counterparty
    customer_id = Column(Integer, ForeignKey("customers.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    contact_name = Column(String(200))
    contact_address = Column(String(300))

    # Amounts
    currency = Column(String(3), default="VND")
    exchange_rate = Column(Float, default=1)
    total_amount = Column(Float, default=0)
    total_amount_vnd = Column(Float, default=0)
    vat_amount = Column(Float, default=0)

    # Description
    description = Column(Text)
    reference_doc = Column(String(200))
    reference_number = Column(String(50))
    reference_date = Column(Date)

    # Metadata
    created_by = Column(Integer, ForeignKey("users.id"))
    approved_by = Column(Integer)
    cashier = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    lines = relationship("VoucherLine", back_populates="voucher", cascade="all, delete-orphan")


class VoucherLine(Base):
    __tablename__ = "voucher_lines"

    id = Column(Integer, primary_key=True, index=True)
    voucher_id = Column(Integer, ForeignKey("vouchers.id", ondelete="CASCADE"), nullable=False)
    line_number = Column(Integer, default=1)

    # Accounting
    debit_account = Column(String(10), nullable=False)
    credit_account = Column(String(10), nullable=False)
    amount = Column(Float, default=0)
    amount_vnd = Column(Float, default=0)
    description = Column(String(300))

    # Inventory details (for kho module)
    product_id = Column(Integer, ForeignKey("products.id"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    unit_id = Column(Integer, ForeignKey("units.id"))
    quantity = Column(Float, default=0)
    unit_price = Column(Float, default=0)

    # Cost tracking
    department_id = Column(Integer, ForeignKey("departments.id"))
    cost_object_id = Column(Integer, ForeignKey("cost_objects.id"))
    cost_item_id = Column(Integer, ForeignKey("cost_items.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    # Relationship
    voucher = relationship("Voucher", back_populates="lines")
