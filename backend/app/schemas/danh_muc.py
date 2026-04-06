from pydantic import BaseModel
from typing import Optional


# ─── Generic CRUD schemas ─────────────────────────────────

class AccountSchema(BaseModel):
    code: str
    name: str
    name_en: Optional[str] = None
    parent_code: Optional[str] = None
    level: int = 1
    type: Optional[str] = None
    nature: Optional[str] = None
    is_parent: bool = False
    is_active: bool = True
    description: Optional[str] = None

    class Config:
        from_attributes = True


class CustomerSchema(BaseModel):
    code: str
    name: str
    tax_code: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    contact_person: Optional[str] = None
    group_id: Optional[int] = None
    account_receivable: str = "131"
    is_active: bool = True

    class Config:
        from_attributes = True


class SupplierSchema(BaseModel):
    code: str
    name: str
    tax_code: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    contact_person: Optional[str] = None
    group_id: Optional[int] = None
    account_payable: str = "331"
    is_active: bool = True

    class Config:
        from_attributes = True


class EmployeeSchema(BaseModel):
    code: str
    name: str
    department_id: Optional[int] = None
    position: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    id_number: Optional[str] = None
    bank_account: Optional[str] = None
    bank_name: Optional[str] = None
    salary_account: str = "334"
    is_active: bool = True

    class Config:
        from_attributes = True


class ProductSchema(BaseModel):
    code: str
    name: str
    group_id: Optional[int] = None
    unit_id: Optional[int] = None
    warehouse_id: Optional[int] = None
    type: str = "goods"
    inventory_account: str = "156"
    cost_account: str = "632"
    revenue_account: str = "511"
    purchase_price: float = 0
    selling_price: float = 0
    vat_rate: float = 10
    is_active: bool = True

    class Config:
        from_attributes = True


class WarehouseSchema(BaseModel):
    code: str
    name: str
    address: Optional[str] = None
    manager: Optional[str] = None
    is_active: bool = True

    class Config:
        from_attributes = True


class SimpleCodeNameSchema(BaseModel):
    """Schema chung cho các danh mục đơn giản (code + name)"""
    code: str
    name: str

    class Config:
        from_attributes = True


class BankAccountSchema(BaseModel):
    account_number: str
    account_name: str
    bank_id: Optional[int] = None
    branch: Optional[str] = None
    currency: str = "VND"
    gl_account: str = "1121"
    is_active: bool = True

    class Config:
        from_attributes = True


class DepartmentSchema(BaseModel):
    code: str
    name: str
    parent_id: Optional[int] = None
    manager: Optional[str] = None
    is_active: bool = True

    class Config:
        from_attributes = True


class CurrencySchema(BaseModel):
    code: str
    name: str
    exchange_rate: float = 1
    is_base: bool = False

    class Config:
        from_attributes = True
