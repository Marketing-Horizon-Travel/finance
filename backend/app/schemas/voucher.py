from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class VoucherLineCreate(BaseModel):
    line_number: int = 1
    debit_account: str
    credit_account: str
    amount: float = 0
    amount_vnd: float = 0
    description: Optional[str] = None
    product_id: Optional[int] = None
    warehouse_id: Optional[int] = None
    unit_id: Optional[int] = None
    quantity: float = 0
    unit_price: float = 0
    department_id: Optional[int] = None
    cost_object_id: Optional[int] = None
    cost_item_id: Optional[int] = None
    project_id: Optional[int] = None


class VoucherCreate(BaseModel):
    voucher_date: date
    posting_date: date
    module: str
    voucher_type: str
    status: str = "draft"
    customer_id: Optional[int] = None
    supplier_id: Optional[int] = None
    employee_id: Optional[int] = None
    contact_name: Optional[str] = None
    contact_address: Optional[str] = None
    currency: str = "VND"
    exchange_rate: float = 1
    description: Optional[str] = None
    reference_doc: Optional[str] = None
    reference_number: Optional[str] = None
    reference_date: Optional[date] = None
    cashier: Optional[str] = None
    lines: List[VoucherLineCreate] = []


class VoucherLineResponse(VoucherLineCreate):
    id: int
    voucher_id: int

    class Config:
        from_attributes = True


class VoucherResponse(BaseModel):
    id: int
    voucher_number: str
    voucher_date: date
    posting_date: date
    module: str
    voucher_type: str
    status: str
    customer_id: Optional[int] = None
    supplier_id: Optional[int] = None
    employee_id: Optional[int] = None
    contact_name: Optional[str] = None
    currency: str
    exchange_rate: float
    total_amount: float
    total_amount_vnd: float
    vat_amount: float
    description: Optional[str] = None
    reference_doc: Optional[str] = None
    cashier: Optional[str] = None
    lines: List[VoucherLineResponse] = []

    class Config:
        from_attributes = True


class VoucherListResponse(BaseModel):
    items: List[VoucherResponse]
    total: int
    page: int
    page_size: int
