"""
Opening Balance — Dư đầu kỳ.
Maps to 10 types in MISA's "Nhập số dư ban đầu" screen.
"""
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class OpeningBalance(Base):
    """Số dư đầu kỳ cho tất cả loại"""
    __tablename__ = "opening_balances"

    id = Column(Integer, primary_key=True, index=True)
    fiscal_year = Column(Integer, nullable=False, index=True)
    type = Column(String(30), nullable=False, index=True)
    # Types: account, bank, customer, supplier, employee,
    #        inventory, tool, asset, prepaid, wip

    # Account balance
    account_code = Column(String(10))
    debit_amount = Column(Float, default=0)
    credit_amount = Column(Float, default=0)
    currency = Column(String(3), default="VND")
    exchange_rate = Column(Float, default=1)
    debit_amount_fc = Column(Float, default=0)  # foreign currency
    credit_amount_fc = Column(Float, default=0)

    # Entity reference
    customer_id = Column(Integer, ForeignKey("customers.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"))

    # Inventory specifics
    quantity = Column(Float, default=0)
    unit_price = Column(Float, default=0)

    # Asset/Tool specifics
    asset_name = Column(String(200))
    original_cost = Column(Float, default=0)
    accumulated_depreciation = Column(Float, default=0)
    remaining_value = Column(Float, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
