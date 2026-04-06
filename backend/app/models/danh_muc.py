"""
Danh mục — All master data models for the 10 category groups.
Maps to MISA's Danh mục screen.
"""
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


# ─── ĐỐI TƯỢNG ───────────────────────────────────────────

class Customer(Base):
    """Khách hàng"""
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    tax_code = Column(String(20))
    address = Column(String(300))
    phone = Column(String(20))
    email = Column(String(100))
    contact_person = Column(String(100))
    group_id = Column(Integer, ForeignKey("customer_supplier_groups.id"))
    account_receivable = Column(String(10), default="131")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Supplier(Base):
    """Nhà cung cấp"""
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    tax_code = Column(String(20))
    address = Column(String(300))
    phone = Column(String(20))
    email = Column(String(100))
    contact_person = Column(String(100))
    group_id = Column(Integer, ForeignKey("customer_supplier_groups.id"))
    account_payable = Column(String(10), default="331")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Employee(Base):
    """Nhân viên"""
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    position = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    id_number = Column(String(20))
    bank_account = Column(String(30))
    bank_name = Column(String(100))
    salary_account = Column(String(10), default="334")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class EmployeeGroup(Base):
    """Nhóm khách hàng, nhà cung cấp"""
    __tablename__ = "customer_supplier_groups"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    type = Column(String(20))  # customer, supplier, both


# ─── VẬT TƯ HÀNG HÓA ────────────────────────────────────

class Product(Base):
    """Vật tư hàng hóa"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    group_id = Column(Integer, ForeignKey("product_groups.id"))
    unit_id = Column(Integer, ForeignKey("units.id"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    type = Column(String(20), default="goods")  # goods, service, material
    inventory_account = Column(String(10), default="156")
    cost_account = Column(String(10), default="632")
    revenue_account = Column(String(10), default="511")
    purchase_price = Column(Float, default=0)
    selling_price = Column(Float, default=0)
    vat_rate = Column(Float, default=10)
    min_stock = Column(Float, default=0)
    max_stock = Column(Float, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ProductGroup(Base):
    """Nhóm vật tư, hàng hóa, dịch vụ"""
    __tablename__ = "product_groups"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    parent_id = Column(Integer, ForeignKey("product_groups.id"))


class Warehouse(Base):
    """Kho"""
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    manager = Column(String(100))
    is_active = Column(Boolean, default=True)


class Unit(Base):
    """Đơn vị tính"""
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(50), nullable=False)


# ─── TÀI KHOẢN ───────────────────────────────────────────

class Account(Base):
    """Hệ thống tài khoản (TT133)"""
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    name_en = Column(String(200))
    parent_code = Column(String(10))
    level = Column(Integer, default=1)
    type = Column(String(20))  # debit, credit, both
    nature = Column(String(20))  # asset, liability, equity, revenue, expense
    is_parent = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    description = Column(Text)


# ─── NGÂN HÀNG ────────────────────────────────────────────

class Bank(Base):
    """Ngân hàng"""
    __tablename__ = "banks"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    short_name = Column(String(50))


class BankAccount(Base):
    """Tài khoản ngân hàng"""
    __tablename__ = "bank_accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String(30), unique=True, nullable=False)
    account_name = Column(String(200), nullable=False)
    bank_id = Column(Integer, ForeignKey("banks.id"))
    branch = Column(String(200))
    currency = Column(String(3), default="VND")
    gl_account = Column(String(10), default="1121")
    is_active = Column(Boolean, default=True)


# ─── CHI NHÁNH, PHÒNG BAN ────────────────────────────────

class Department(Base):
    """Cơ cấu tổ chức"""
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    parent_id = Column(Integer, ForeignKey("departments.id"))
    manager = Column(String(100))
    is_active = Column(Boolean, default=True)


# ─── CHI PHÍ ─────────────────────────────────────────────

class CostObject(Base):
    """Đối tượng tập hợp chi phí"""
    __tablename__ = "cost_objects"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    type = Column(String(20))


class CostItem(Base):
    """Khoản mục chi phí"""
    __tablename__ = "cost_items"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    parent_id = Column(Integer, ForeignKey("cost_items.id"))


class Project(Base):
    """Công trình"""
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    type_id = Column(Integer, ForeignKey("project_types.id"))
    status = Column(String(20), default="active")


class ProjectType(Base):
    """Loại công trình"""
    __tablename__ = "project_types"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)


# ─── TÀI SẢN ─────────────────────────────────────────────

class AssetType(Base):
    """Loại tài sản cố định"""
    __tablename__ = "asset_types"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    depreciation_rate = Column(Float)
    useful_life_months = Column(Integer)


class ToolType(Base):
    """Loại công cụ dụng cụ"""
    __tablename__ = "tool_types"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    allocation_periods = Column(Integer, default=12)


# ─── THUẾ ─────────────────────────────────────────────────

class TaxRateSpecial(Base):
    """Biểu thuế tiêu thụ đặc biệt"""
    __tablename__ = "tax_rates_special"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    rate = Column(Float, nullable=False)


class TaxRateResource(Base):
    """Biểu thuế tài nguyên"""
    __tablename__ = "tax_rates_resource"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    rate = Column(Float, nullable=False)


# ─── KHÁC ─────────────────────────────────────────────────

class PaymentTerm(Base):
    """Điều khoản thanh toán"""
    __tablename__ = "payment_terms"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    days = Column(Integer, default=0)


class CashFlowItem(Base):
    """Mục thu/chi"""
    __tablename__ = "cash_flow_items"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    type = Column(String(10))  # thu, chi


class StatCode(Base):
    """Mã thống kê"""
    __tablename__ = "stat_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)


class Currency(Base):
    """Loại tiền"""
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(3), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    exchange_rate = Column(Float, default=1)
    is_base = Column(Boolean, default=False)


class VoucherType(Base):
    """Loại chứng từ"""
    __tablename__ = "voucher_types"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    prefix = Column(String(10))


# ─── TIỀN LƯƠNG ───────────────────────────────────────────

class TimekeepingSymbol(Base):
    """Ký hiệu chấm công"""
    __tablename__ = "timekeeping_symbols"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    standard_hours = Column(Float, default=8)


class IncomeTaxRate(Base):
    """Biểu tính thuế thu nhập"""
    __tablename__ = "income_tax_rates"

    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, nullable=False)
    from_amount = Column(Float, nullable=False)
    to_amount = Column(Float)
    rate = Column(Float, nullable=False)
