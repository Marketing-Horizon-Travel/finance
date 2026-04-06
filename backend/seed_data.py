"""
Seed data — Dữ liệu mẫu cho Horizon Vietnam Travel.
Chạy: python seed_data.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from datetime import date, timedelta
import random

from app.core.database import engine, SessionLocal, Base
from app.core.auth import hash_password
from app.models.user import User
from app.models.danh_muc import (
    Account, Customer, Supplier, Employee, EmployeeGroup,
    Warehouse, Product, ProductGroup, Unit,
    Bank, BankAccount, Department,
    CostObject, CostItem, Project, ProjectType,
    AssetType, ToolType,
    PaymentTerm, CashFlowItem, StatCode, Currency, VoucherType,
    TimekeepingSymbol, IncomeTaxRate,
)
from app.models.voucher import Voucher, VoucherLine
from app.models.opening_balance import OpeningBalance


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Clear existing data
    for table in reversed(Base.metadata.sorted_tables):
        db.execute(table.delete())
    db.commit()

    print("=== Seeding Users ===")
    users = [
        User(username="admin", email="admin@horizon.vn", full_name="Admin", hashed_password=hash_password("admin123"), role="admin"),
        User(username="binh", email="binh@horizon.vn", full_name="Tran Thi Binh", hashed_password=hash_password("123456"), role="accountant"),
        User(username="hoa", email="hoa@horizon.vn", full_name="Nguyen Thi Hoa", hashed_password=hash_password("123456"), role="accountant"),
        User(username="nam", email="nam@horizon.vn", full_name="Le Van Nam", hashed_password=hash_password("123456"), role="manager"),
    ]
    db.add_all(users)
    db.flush()

    print("=== Seeding Currencies ===")
    currencies = [
        Currency(code="VND", name="Viet Nam Dong", exchange_rate=1, is_base=True),
        Currency(code="USD", name="US Dollar", exchange_rate=25450),
        Currency(code="EUR", name="Euro", exchange_rate=27200),
        Currency(code="GBP", name="British Pound", exchange_rate=32100),
        Currency(code="JPY", name="Japanese Yen", exchange_rate=170),
        Currency(code="AUD", name="Australian Dollar", exchange_rate=16500),
        Currency(code="CAD", name="Canadian Dollar", exchange_rate=18700),
        Currency(code="SGD", name="Singapore Dollar", exchange_rate=18900),
        Currency(code="THB", name="Thai Baht", exchange_rate=720),
        Currency(code="CNY", name="Chinese Yuan", exchange_rate=3500),
        Currency(code="KRW", name="Korean Won", exchange_rate=19),
    ]
    db.add_all(currencies)

    print("=== Seeding Departments ===")
    departments = [
        Department(code="BGD", name="Ban Giam doc"),
        Department(code="KT", name="Phong Ke toan"),
        Department(code="KD", name="Phong Kinh doanh"),
        Department(code="DH", name="Phong Dieu hanh"),
        Department(code="MKT", name="Phong Marketing"),
        Department(code="HR", name="Phong Nhan su"),
        Department(code="IT", name="Phong Cong nghe"),
    ]
    db.add_all(departments)
    db.flush()

    print("=== Seeding Employees ===")
    dept_map = {d.code: d.id for d in departments}
    employees = [
        Employee(code="NV001", name="Tran Thi Binh", department_id=dept_map["KT"], position="Ke toan truong", phone="0901234567", email="binh@horizon.vn"),
        Employee(code="NV002", name="Nguyen Thi Hoa", department_id=dept_map["KT"], position="Ke toan vien", phone="0901234568", email="hoa@horizon.vn"),
        Employee(code="NV003", name="Le Van Nam", department_id=dept_map["BGD"], position="Giam doc", phone="0901234569", email="nam@horizon.vn"),
        Employee(code="NV004", name="Pham Thi Lan", department_id=dept_map["KD"], position="Truong phong KD", phone="0901234570", email="lan@horizon.vn"),
        Employee(code="NV005", name="Hoang Van Duc", department_id=dept_map["DH"], position="Dieu hanh tour", phone="0901234571", email="duc@horizon.vn"),
        Employee(code="NV006", name="Vo Thi Mai", department_id=dept_map["KD"], position="Sale", phone="0901234572", email="mai@horizon.vn"),
        Employee(code="NV007", name="Dang Van Tuan", department_id=dept_map["DH"], position="Dieu hanh tour", phone="0901234573", email="tuan@horizon.vn"),
        Employee(code="NV008", name="Bui Thi Ngoc", department_id=dept_map["MKT"], position="Marketing", phone="0901234574", email="ngoc@horizon.vn"),
        Employee(code="NV009", name="Ngo Van Hai", department_id=dept_map["IT"], position="IT Manager", phone="0901234575", email="hai@horizon.vn"),
        Employee(code="NV010", name="Truong Thi Yen", department_id=dept_map["HR"], position="Nhan su", phone="0901234576", email="yen@horizon.vn"),
    ]
    db.add_all(employees)

    print("=== Seeding Customer/Supplier Groups ===")
    groups = [
        EmployeeGroup(code="KH-EU", name="Khach hang Chau Au", type="customer"),
        EmployeeGroup(code="KH-US", name="Khach hang My", type="customer"),
        EmployeeGroup(code="KH-AS", name="Khach hang Chau A", type="customer"),
        EmployeeGroup(code="KH-VN", name="Khach hang Viet Nam", type="customer"),
        EmployeeGroup(code="NCC-KS", name="Khach san", type="supplier"),
        EmployeeGroup(code="NCC-VC", name="Van chuyen", type="supplier"),
        EmployeeGroup(code="NCC-NH", name="Nha hang", type="supplier"),
        EmployeeGroup(code="NCC-DV", name="Dich vu khac", type="supplier"),
    ]
    db.add_all(groups)
    db.flush()
    grp_map = {g.code: g.id for g in groups}

    print("=== Seeding Customers ===")
    customers = [
        Customer(code="KH001", name="Voyage Prive SAS", tax_code="FR12345678", address="Paris, France", phone="+33612345678", email="booking@voyageprive.fr", group_id=grp_map["KH-EU"]),
        Customer(code="KH002", name="Indochina Travel GmbH", tax_code="DE987654321", address="Berlin, Germany", phone="+49301234567", email="info@indochina-travel.de", group_id=grp_map["KH-EU"]),
        Customer(code="KH003", name="Asia Explorer Tours", tax_code="US123456789", address="New York, USA", phone="+12125551234", email="ops@asiaexplorer.com", group_id=grp_map["KH-US"]),
        Customer(code="KH004", name="Saigontourist", tax_code="0301234567", address="TP Ho Chi Minh", phone="02838291291", email="info@saigontourist.net", group_id=grp_map["KH-VN"]),
        Customer(code="KH005", name="Vietravel", tax_code="0401234567", address="TP Ho Chi Minh", phone="02838228898", email="info@vietravel.com", group_id=grp_map["KH-VN"]),
        Customer(code="KH006", name="Tokyo Travel Agency", address="Tokyo, Japan", phone="+81312345678", email="info@tokyotravel.jp", group_id=grp_map["KH-AS"]),
        Customer(code="KH007", name="Terres d'Aventure", address="Lyon, France", phone="+33478901234", email="contact@terdav.com", group_id=grp_map["KH-EU"]),
        Customer(code="KH008", name="Intrepid Travel", address="Melbourne, Australia", phone="+61396011500", email="ops@intrepidtravel.com", group_id=grp_map["KH-EU"]),
        Customer(code="KH009", name="Bamboo Travel Ltd", address="London, UK", phone="+442071234567", email="sales@bambootravel.co.uk", group_id=grp_map["KH-EU"]),
        Customer(code="KH010", name="Buffalo Tours", tax_code="0101234568", address="Ha Noi", phone="02439287777", email="info@buffalotours.com", group_id=grp_map["KH-VN"]),
    ]
    db.add_all(customers)

    print("=== Seeding Suppliers ===")
    suppliers = [
        Supplier(code="NCC001", name="Khach san Sofitel Legend Metropole", tax_code="0100686871", address="15 Ngo Quyen, Ha Noi", phone="02438266919", email="reservations@sofitel.com", group_id=grp_map["NCC-KS"]),
        Supplier(code="NCC002", name="Khach san Melia Ha Noi", tax_code="0101234001", address="44B Ly Thuong Kiet, Ha Noi", phone="02439343343", email="booking@melia-hanoi.com", group_id=grp_map["NCC-KS"]),
        Supplier(code="NCC003", name="Khach san Vinpearl Nha Trang", tax_code="4200123456", address="Hon Tre, Nha Trang", phone="02583598188", email="info@vinpearl.com", group_id=grp_map["NCC-KS"]),
        Supplier(code="NCC004", name="Vietnam Airlines", tax_code="0100107518", address="200 Nguyen Son, Ha Noi", phone="19001100", email="booking@vietnamairlines.com", group_id=grp_map["NCC-VC"]),
        Supplier(code="NCC005", name="Cong ty TNHH Van chuyen Hoang Long", tax_code="0101234002", address="28 Tran Nhat Duat, Ha Noi", phone="02439287887", email="info@hoanglong.com", group_id=grp_map["NCC-VC"]),
        Supplier(code="NCC006", name="Nha hang Sen Tay Ho", tax_code="0101234003", address="614 Lac Long Quan, Ha Noi", phone="02438293089", email="info@sentayho.vn", group_id=grp_map["NCC-NH"]),
        Supplier(code="NCC007", name="Halong Bay Cruise - Bhaya", tax_code="2200123457", address="Bai Chay, Ha Long", phone="02033846262", email="info@bhayacruises.com", group_id=grp_map["NCC-DV"]),
        Supplier(code="NCC008", name="Khach san La Siesta Hoi An", tax_code="4000123458", address="132 Hung Vuong, Hoi An", phone="02353915915", email="info@lasiesta.vn", group_id=grp_map["NCC-KS"]),
        Supplier(code="NCC009", name="Cong ty Du lich Sapa", tax_code="1000123459", address="Sa Pa, Lao Cai", phone="02143871215", email="info@sapatourism.com", group_id=grp_map["NCC-DV"]),
        Supplier(code="NCC010", name="Grab Taxi (Cong ty TNHH Grab)", tax_code="0314455025", address="TP Ho Chi Minh", phone="19001818", email="corporate@grab.com", group_id=grp_map["NCC-VC"]),
    ]
    db.add_all(suppliers)

    print("=== Seeding Banks ===")
    banks = [
        Bank(code="VCB", name="Ngan hang TMCP Ngoai thuong Viet Nam", short_name="Vietcombank"),
        Bank(code="TCB", name="Ngan hang TMCP Ky thuong Viet Nam", short_name="Techcombank"),
        Bank(code="MB", name="Ngan hang TMCP Quan doi", short_name="MB Bank"),
        Bank(code="BIDV", name="Ngan hang Dau tu va Phat trien", short_name="BIDV"),
        Bank(code="ACB", name="Ngan hang TMCP A Chau", short_name="ACB"),
    ]
    db.add_all(banks)
    db.flush()
    bank_map = {b.code: b.id for b in banks}

    bank_accounts = [
        BankAccount(account_number="0011004025678", account_name="Horizon Vietnam Travel - VND", bank_id=bank_map["VCB"], branch="So giao dich", currency="VND", gl_account="1121"),
        BankAccount(account_number="0011004025679", account_name="Horizon Vietnam Travel - USD", bank_id=bank_map["VCB"], branch="So giao dich", currency="USD", gl_account="1122"),
        BankAccount(account_number="0011004025680", account_name="Horizon Vietnam Travel - EUR", bank_id=bank_map["VCB"], branch="So giao dich", currency="EUR", gl_account="1122"),
        BankAccount(account_number="19133018888019", account_name="Horizon Vietnam Travel", bank_id=bank_map["TCB"], branch="Hoan Kiem", currency="VND", gl_account="1121"),
    ]
    db.add_all(bank_accounts)

    print("=== Seeding Accounts (TT133) ===")
    accounts_data = [
        # Loai 1 - Tai san
        ("111", "Tien mat", None, 1, "debit", "asset", True),
        ("1111", "Tien Viet Nam", "111", 2, "debit", "asset", False),
        ("1112", "Ngoai te", "111", 2, "debit", "asset", False),
        ("112", "Tien gui ngan hang", None, 1, "debit", "asset", True),
        ("1121", "Tien Viet Nam", "112", 2, "debit", "asset", False),
        ("1122", "Ngoai te", "112", 2, "debit", "asset", False),
        ("131", "Phai thu khach hang", None, 1, "both", "asset", False),
        ("133", "Thue GTGT duoc khau tru", None, 1, "debit", "asset", True),
        ("1331", "Thue GTGT dau vao hang hoa dich vu", "133", 2, "debit", "asset", False),
        ("136", "Phai thu noi bo", None, 1, "debit", "asset", False),
        ("138", "Phai thu khac", None, 1, "debit", "asset", False),
        ("141", "Tam ung", None, 1, "debit", "asset", False),
        ("152", "Nguyen lieu, vat lieu", None, 1, "debit", "asset", False),
        ("153", "Cong cu, dung cu", None, 1, "debit", "asset", False),
        ("154", "Chi phi san xuat KD do dang", None, 1, "debit", "asset", False),
        ("155", "Thanh pham", None, 1, "debit", "asset", False),
        ("156", "Hang hoa", None, 1, "debit", "asset", False),
        # Loai 2 - Tai san dai han
        ("211", "Tai san co dinh huu hinh", None, 1, "debit", "asset", True),
        ("2111", "Nha cua, vat kien truc", "211", 2, "debit", "asset", False),
        ("2112", "May moc, thiet bi", "211", 2, "debit", "asset", False),
        ("2113", "Phuong tien van tai", "211", 2, "debit", "asset", False),
        ("2114", "Thiet bi van phong", "211", 2, "debit", "asset", False),
        ("214", "Hao mon TSCD", None, 1, "credit", "asset", True),
        ("2141", "Hao mon TSCD huu hinh", "214", 2, "credit", "asset", False),
        ("242", "Chi phi tra truoc", None, 1, "debit", "asset", False),
        # Loai 3 - No phai tra
        ("331", "Phai tra nguoi ban", None, 1, "both", "liability", False),
        ("333", "Thue va cac khoan phai nop NN", None, 1, "credit", "liability", True),
        ("3331", "Thue GTGT phai nop", "333", 2, "credit", "liability", True),
        ("33311", "Thue GTGT dau ra", "3331", 3, "credit", "liability", False),
        ("3334", "Thue TNDN", "333", 2, "credit", "liability", False),
        ("3335", "Thue TNCN", "333", 2, "credit", "liability", False),
        ("334", "Phai tra nguoi lao dong", None, 1, "credit", "liability", False),
        ("338", "Phai tra khac", None, 1, "credit", "liability", True),
        ("3383", "BHXH", "338", 2, "credit", "liability", False),
        ("3384", "BHYT", "338", 2, "credit", "liability", False),
        ("3386", "BHTN", "338", 2, "credit", "liability", False),
        # Loai 4 - Von chu so huu
        ("411", "Von dau tu cua chu so huu", None, 1, "credit", "equity", False),
        ("421", "Loi nhuan sau thue chua phan phoi", None, 1, "both", "equity", True),
        ("4211", "Loi nhuan chua phan phoi nam truoc", "421", 2, "both", "equity", False),
        ("4212", "Loi nhuan chua phan phoi nam nay", "421", 2, "both", "equity", False),
        # Loai 5 - Doanh thu
        ("511", "Doanh thu ban hang va cung cap DV", None, 1, "credit", "revenue", True),
        ("5111", "Doanh thu ban hang hoa", "511", 2, "credit", "revenue", False),
        ("5113", "Doanh thu cung cap dich vu", "511", 2, "credit", "revenue", False),
        ("515", "Doanh thu hoat dong tai chinh", None, 1, "credit", "revenue", False),
        ("521", "Cac khoan giam tru doanh thu", None, 1, "debit", "revenue", False),
        # Loai 6 - Chi phi
        ("621", "Chi phi nguyen lieu, vat lieu truc tiep", None, 1, "debit", "expense", False),
        ("622", "Chi phi nhan cong truc tiep", None, 1, "debit", "expense", False),
        ("623", "Chi phi su dung may thi cong", None, 1, "debit", "expense", False),
        ("627", "Chi phi san xuat chung", None, 1, "debit", "expense", False),
        ("632", "Gia von hang ban", None, 1, "debit", "expense", False),
        ("635", "Chi phi tai chinh", None, 1, "debit", "expense", False),
        ("641", "Chi phi ban hang", None, 1, "debit", "expense", False),
        ("642", "Chi phi quan ly doanh nghiep", None, 1, "debit", "expense", False),
        # Loai 7,8,9
        ("711", "Thu nhap khac", None, 1, "credit", "revenue", False),
        ("811", "Chi phi khac", None, 1, "debit", "expense", False),
        ("911", "Xac dinh ket qua kinh doanh", None, 1, "both", "equity", False),
    ]
    for code, name, parent, level, typ, nature, is_parent in accounts_data:
        db.add(Account(code=code, name=name, parent_code=parent, level=level, type=typ, nature=nature, is_parent=is_parent))

    print("=== Seeding Units ===")
    units = [
        Unit(code="Tour", name="Tour"),
        Unit(code="Pax", name="Pax (khach)"),
        Unit(code="Dem", name="Dem (phong)"),
        Unit(code="Chuyen", name="Chuyen"),
        Unit(code="Ve", name="Ve"),
        Unit(code="Chiec", name="Chiec"),
        Unit(code="Bo", name="Bo"),
        Unit(code="Cai", name="Cai"),
    ]
    db.add_all(units)
    db.flush()

    print("=== Seeding Product Groups ===")
    product_groups = [
        ProductGroup(code="DV-TOUR", name="Dich vu tour"),
        ProductGroup(code="DV-KS", name="Dich vu khach san"),
        ProductGroup(code="DV-VC", name="Dich vu van chuyen"),
        ProductGroup(code="DV-NH", name="Dich vu nha hang"),
        ProductGroup(code="DV-KHAC", name="Dich vu khac"),
        ProductGroup(code="VPP", name="Van phong pham"),
    ]
    db.add_all(product_groups)
    db.flush()
    pg_map = {g.code: g.id for g in product_groups}
    unit_map = {u.code: u.id for u in units}

    print("=== Seeding Products ===")
    products = [
        Product(code="TOUR-01", name="Tour Ha Noi - Ha Long 2N1D", group_id=pg_map["DV-TOUR"], unit_id=unit_map["Tour"], type="service", selling_price=3500000, cost_account="632", revenue_account="5113"),
        Product(code="TOUR-02", name="Tour Ha Noi - Sapa 3N2D", group_id=pg_map["DV-TOUR"], unit_id=unit_map["Tour"], type="service", selling_price=5200000, cost_account="632", revenue_account="5113"),
        Product(code="TOUR-03", name="Tour Hue - Da Nang - Hoi An 4N3D", group_id=pg_map["DV-TOUR"], unit_id=unit_map["Tour"], type="service", selling_price=7800000, cost_account="632", revenue_account="5113"),
        Product(code="TOUR-04", name="Tour Mekong Delta 2N1D", group_id=pg_map["DV-TOUR"], unit_id=unit_map["Tour"], type="service", selling_price=2800000, cost_account="632", revenue_account="5113"),
        Product(code="KS-01", name="Phong khach san Sofitel Metropole", group_id=pg_map["DV-KS"], unit_id=unit_map["Dem"], type="service", selling_price=5500000, purchase_price=4200000),
        Product(code="KS-02", name="Phong khach san Melia Ha Noi", group_id=pg_map["DV-KS"], unit_id=unit_map["Dem"], type="service", selling_price=2800000, purchase_price=2100000),
        Product(code="VC-01", name="Ve may bay noi dia", group_id=pg_map["DV-VC"], unit_id=unit_map["Ve"], type="service", selling_price=2500000, purchase_price=2200000),
        Product(code="VC-02", name="Xe du lich 16 cho", group_id=pg_map["DV-VC"], unit_id=unit_map["Chuyen"], type="service", selling_price=1800000, purchase_price=1500000),
        Product(code="NH-01", name="Bua an trua/toi", group_id=pg_map["DV-NH"], unit_id=unit_map["Pax"], type="service", selling_price=350000, purchase_price=280000),
        Product(code="DV-01", name="Huong dan vien tieng Anh", group_id=pg_map["DV-KHAC"], unit_id=unit_map["Chuyen"], type="service", selling_price=1200000, purchase_price=900000),
    ]
    db.add_all(products)

    print("=== Seeding Warehouses ===")
    warehouses = [
        Warehouse(code="KHO-VP", name="Kho Van phong Ha Noi", address="25 Bat Su, Hoan Kiem, Ha Noi"),
        Warehouse(code="KHO-HCM", name="Kho Van phong HCM", address="123 Le Loi, Quan 1, HCM"),
    ]
    db.add_all(warehouses)

    print("=== Seeding Cost Objects & Items ===")
    cost_objects = [
        CostObject(code="TOUR-HN", name="Tour Ha Noi", type="department"),
        CostObject(code="TOUR-MT", name="Tour Mien Trung", type="department"),
        CostObject(code="TOUR-MN", name="Tour Mien Nam", type="department"),
    ]
    db.add_all(cost_objects)

    cost_items = [
        CostItem(code="CP-KS", name="Chi phi khach san"),
        CostItem(code="CP-VC", name="Chi phi van chuyen"),
        CostItem(code="CP-AN", name="Chi phi an uong"),
        CostItem(code="CP-HDV", name="Chi phi huong dan vien"),
        CostItem(code="CP-VE", name="Chi phi ve tham quan"),
        CostItem(code="CP-VP", name="Chi phi van phong"),
        CostItem(code="CP-LUONG", name="Chi phi luong"),
        CostItem(code="CP-KHAC", name="Chi phi khac"),
    ]
    db.add_all(cost_items)

    print("=== Seeding Asset & Tool Types ===")
    asset_types = [
        AssetType(code="TS-VP", name="Thiet bi van phong", depreciation_rate=20, useful_life_months=60),
        AssetType(code="TS-XE", name="Phuong tien van tai", depreciation_rate=10, useful_life_months=120),
        AssetType(code="TS-IT", name="Thiet bi CNTT", depreciation_rate=25, useful_life_months=48),
        AssetType(code="TS-NC", name="Nha cua", depreciation_rate=5, useful_life_months=240),
    ]
    db.add_all(asset_types)

    tool_types = [
        ToolType(code="CC-VP", name="Cong cu van phong", allocation_periods=12),
        ToolType(code="CC-IT", name="Cong cu CNTT", allocation_periods=24),
        ToolType(code="CC-DL", name="Cong cu du lich", allocation_periods=12),
    ]
    db.add_all(tool_types)

    print("=== Seeding Payment Terms ===")
    payment_terms = [
        PaymentTerm(code="COD", name="Thanh toan ngay", days=0),
        PaymentTerm(code="NET15", name="Thanh toan sau 15 ngay", days=15),
        PaymentTerm(code="NET30", name="Thanh toan sau 30 ngay", days=30),
        PaymentTerm(code="NET45", name="Thanh toan sau 45 ngay", days=45),
        PaymentTerm(code="PREPAY", name="Thanh toan truoc", days=0),
    ]
    db.add_all(payment_terms)

    print("=== Seeding Cash Flow Items ===")
    cf_items = [
        CashFlowItem(code="TM-01", name="Thu tien ban hang", type="thu"),
        CashFlowItem(code="TM-02", name="Thu tien cong no", type="thu"),
        CashFlowItem(code="TM-03", name="Thu tien tam ung thua", type="thu"),
        CashFlowItem(code="TM-04", name="Thu lai tien gui", type="thu"),
        CashFlowItem(code="TM-05", name="Thu khac", type="thu"),
        CashFlowItem(code="CM-01", name="Chi mua hang hoa dich vu", type="chi"),
        CashFlowItem(code="CM-02", name="Chi tra luong", type="chi"),
        CashFlowItem(code="CM-03", name="Chi tam ung", type="chi"),
        CashFlowItem(code="CM-04", name="Chi nop thue", type="chi"),
        CashFlowItem(code="CM-05", name="Chi van phong", type="chi"),
        CashFlowItem(code="CM-06", name="Chi khac", type="chi"),
    ]
    db.add_all(cf_items)

    print("=== Seeding Voucher Types ===")
    vtypes = [
        VoucherType(code="PT", name="Phieu thu", prefix="PT"),
        VoucherType(code="PC", name="Phieu chi", prefix="PC"),
        VoucherType(code="BC", name="Bao co ngan hang thu", prefix="BC"),
        VoucherType(code="BN", name="Bao no ngan hang chi", prefix="BN"),
        VoucherType(code="MH", name="Hoa don mua hang", prefix="MH"),
        VoucherType(code="BH", name="Hoa don ban hang", prefix="BH"),
        VoucherType(code="NK", name="Phieu nhap kho", prefix="NK"),
        VoucherType(code="XK", name="Phieu xuat kho", prefix="XK"),
        VoucherType(code="BT", name="But toan", prefix="BT"),
    ]
    db.add_all(vtypes)

    print("=== Seeding Stat Codes ===")
    stat_codes = [
        StatCode(code="TK-01", name="Du lich noi dia"),
        StatCode(code="TK-02", name="Du lich quoc te - Inbound"),
        StatCode(code="TK-03", name="Du lich quoc te - Outbound"),
    ]
    db.add_all(stat_codes)

    print("=== Seeding Timekeeping Symbols ===")
    tk_symbols = [
        TimekeepingSymbol(code="X", name="Di lam", standard_hours=8),
        TimekeepingSymbol(code="P", name="Nghi phep", standard_hours=8),
        TimekeepingSymbol(code="O", name="Nghi om", standard_hours=0),
        TimekeepingSymbol(code="K", name="Nghi khong luong", standard_hours=0),
        TimekeepingSymbol(code="CT", name="Cong tac", standard_hours=8),
        TimekeepingSymbol(code="L", name="Nghi le", standard_hours=0),
        TimekeepingSymbol(code="TC", name="Tang ca", standard_hours=0),
    ]
    db.add_all(tk_symbols)

    print("=== Seeding Income Tax Rates ===")
    tax_rates = [
        IncomeTaxRate(level=1, from_amount=0, to_amount=5000000, rate=5),
        IncomeTaxRate(level=2, from_amount=5000000, to_amount=10000000, rate=10),
        IncomeTaxRate(level=3, from_amount=10000000, to_amount=18000000, rate=15),
        IncomeTaxRate(level=4, from_amount=18000000, to_amount=32000000, rate=20),
        IncomeTaxRate(level=5, from_amount=32000000, to_amount=52000000, rate=25),
        IncomeTaxRate(level=6, from_amount=52000000, to_amount=80000000, rate=30),
        IncomeTaxRate(level=7, from_amount=80000000, to_amount=None, rate=35),
    ]
    db.add_all(tax_rates)

    print("=== Seeding Project Types & Projects ===")
    pt = ProjectType(code="TOUR", name="Du an Tour")
    db.add(pt)
    db.flush()
    projects = [
        Project(code="PRJ-2024-01", name="Tour Chau Au Xuan 2024", type_id=pt.id, status="active"),
        Project(code="PRJ-2024-02", name="Tour Nhat Ban Anh Dao 2024", type_id=pt.id, status="active"),
    ]
    db.add_all(projects)

    db.flush()

    print("=== Seeding Opening Balances ===")
    opening_balances = [
        OpeningBalance(fiscal_year=2024, type="account", account_code="1111", debit_amount=125000000, currency="VND"),
        OpeningBalance(fiscal_year=2024, type="account", account_code="1112", debit_amount=5000, currency="USD", exchange_rate=25450, debit_amount_fc=5000),
        OpeningBalance(fiscal_year=2024, type="account", account_code="1121", debit_amount=850000000, currency="VND"),
        OpeningBalance(fiscal_year=2024, type="account", account_code="1122", debit_amount=15000, currency="USD", exchange_rate=25450, debit_amount_fc=15000),
        OpeningBalance(fiscal_year=2024, type="account", account_code="131", debit_amount=320000000, currency="VND"),
        OpeningBalance(fiscal_year=2024, type="account", account_code="331", credit_amount=185000000, currency="VND"),
        OpeningBalance(fiscal_year=2024, type="account", account_code="411", credit_amount=2000000000, currency="VND"),
        OpeningBalance(fiscal_year=2024, type="account", account_code="4211", credit_amount=450000000, currency="VND"),
    ]
    db.add_all(opening_balances)

    print("=== Seeding Sample Vouchers ===")
    cust_ids = {c.code: c.id for c in db.query(Customer).all()}
    supp_ids = {s.code: s.id for s in db.query(Supplier).all()}
    emp_ids = {e.code: e.id for e in db.query(Employee).all()}

    vouchers_data = [
        # === TIEN MAT - Phieu Thu ===
        {
            "number": "PT2024-0001", "date": date(2024, 1, 5), "module": "cash", "type": "receipt",
            "status": "posted", "contact": "Saigontourist", "customer_id": cust_ids["KH004"],
            "currency": "VND", "rate": 1, "desc": "Thu tien tour Ha Long - Saigontourist",
            "lines": [("1111", "131", 35000000, "Thu cong no KH - Tour Ha Long")],
        },
        {
            "number": "PT2024-0002", "date": date(2024, 1, 12), "module": "cash", "type": "receipt",
            "status": "posted", "contact": "Vietravel", "customer_id": cust_ids["KH005"],
            "currency": "VND", "rate": 1, "desc": "Thu tien tour Sapa - Vietravel",
            "lines": [("1111", "131", 52000000, "Thu cong no KH - Tour Sapa")],
        },
        {
            "number": "PT2024-0003", "date": date(2024, 2, 1), "module": "cash", "type": "receipt",
            "status": "posted", "contact": "Voyage Prive SAS", "customer_id": cust_ids["KH001"],
            "currency": "EUR", "rate": 27200, "desc": "Thu tien tour Viet Nam 10 ngay - Voyage Prive",
            "lines": [("1112", "131", 8500, "Thu cong no KH ngoai te")],
        },
        {
            "number": "PT2024-0004", "date": date(2024, 2, 15), "module": "cash", "type": "receipt",
            "status": "draft", "contact": "Buffalo Tours", "customer_id": cust_ids["KH010"],
            "currency": "VND", "rate": 1, "desc": "Thu tien tam ung tour Da Nang",
            "lines": [("1111", "131", 28000000, "Tam ung tour Da Nang - Hoi An")],
        },
        # === TIEN MAT - Phieu Chi ===
        {
            "number": "PC2024-0001", "date": date(2024, 1, 8), "module": "cash", "type": "payment",
            "status": "posted", "contact": "Nha hang Sen Tay Ho", "supplier_id": supp_ids["NCC006"],
            "currency": "VND", "rate": 1, "desc": "Chi tien an trua doan khach Saigontourist",
            "lines": [("632", "1111", 4200000, "Bua trua 15 pax x 280,000")],
        },
        {
            "number": "PC2024-0002", "date": date(2024, 1, 15), "module": "cash", "type": "payment",
            "status": "posted", "contact": "Hoang Van Duc", "employee_id": emp_ids["NV005"],
            "currency": "VND", "rate": 1, "desc": "Tam ung cong tac phi tour Sapa",
            "lines": [("141", "1111", 8000000, "Tam ung cong tac phi")],
        },
        {
            "number": "PC2024-0003", "date": date(2024, 1, 20), "module": "cash", "type": "payment",
            "status": "posted", "contact": "Van phong pham Thien Long", "supplier_id": supp_ids.get("NCC010"),
            "currency": "VND", "rate": 1, "desc": "Mua van phong pham thang 1",
            "lines": [("642", "1111", 1850000, "VPP thang 1/2024")],
        },
        {
            "number": "PC2024-0004", "date": date(2024, 2, 5), "module": "cash", "type": "payment",
            "status": "posted", "contact": "Grab Taxi", "supplier_id": supp_ids["NCC010"],
            "currency": "VND", "rate": 1, "desc": "Chi phi taxi thang 1",
            "lines": [("642", "1111", 3200000, "Taxi di lai thang 1/2024")],
        },
        # === NGAN HANG - Thu ===
        {
            "number": "BC2024-0001", "date": date(2024, 1, 10), "module": "bank", "type": "receipt",
            "status": "posted", "contact": "Indochina Travel GmbH", "customer_id": cust_ids["KH002"],
            "currency": "EUR", "rate": 27200, "desc": "Nhan thanh toan tour Viet Nam 14N - Indochina Travel",
            "lines": [("1122", "131", 15200, "Wire transfer - Invoice INV2024-001")],
        },
        {
            "number": "BC2024-0002", "date": date(2024, 1, 18), "module": "bank", "type": "receipt",
            "status": "posted", "contact": "Asia Explorer Tours", "customer_id": cust_ids["KH003"],
            "currency": "USD", "rate": 25450, "desc": "Thu tien tour Mekong - Asia Explorer",
            "lines": [("1122", "131", 12500, "Wire transfer - Tour Mekong group Jan 2024")],
        },
        {
            "number": "BC2024-0003", "date": date(2024, 2, 3), "module": "bank", "type": "receipt",
            "status": "posted", "contact": "Terres d'Aventure", "customer_id": cust_ids["KH007"],
            "currency": "EUR", "rate": 27200, "desc": "Thu tien tour trekking Sapa",
            "lines": [("1122", "131", 9800, "Payment - Sapa trekking Feb 2024")],
        },
        # === NGAN HANG - Chi ===
        {
            "number": "BN2024-0001", "date": date(2024, 1, 12), "module": "bank", "type": "payment",
            "status": "posted", "contact": "Vietnam Airlines", "supplier_id": supp_ids["NCC004"],
            "currency": "VND", "rate": 1, "desc": "Thanh toan ve may bay thang 1",
            "lines": [("331", "1121", 45000000, "Ve may bay noi dia x 20 ve")],
        },
        {
            "number": "BN2024-0002", "date": date(2024, 1, 25), "module": "bank", "type": "payment",
            "status": "posted", "contact": "Sofitel Metropole", "supplier_id": supp_ids["NCC001"],
            "currency": "VND", "rate": 1, "desc": "Thanh toan phong khach san thang 1",
            "lines": [("331", "1121", 63000000, "15 dem x 4,200,000 VND")],
        },
        {
            "number": "BN2024-0003", "date": date(2024, 2, 1), "module": "bank", "type": "payment",
            "status": "posted", "contact": "Tra luong thang 1/2024",
            "currency": "VND", "rate": 1, "desc": "Chi luong nhan vien thang 1/2024",
            "lines": [("334", "1121", 185000000, "Luong thang 1/2024 - 10 nhan vien")],
        },
        # === MUA HANG ===
        {
            "number": "MH2024-0001", "date": date(2024, 1, 5), "module": "purchase", "type": "purchase_invoice",
            "status": "posted", "contact": "Bhaya Cruise", "supplier_id": supp_ids["NCC007"],
            "currency": "VND", "rate": 1, "desc": "Mua dich vu tau Ha Long - 8 pax",
            "lines": [("632", "331", 32000000, "Tau Bhaya 2N1D x 8 pax"), ("1331", "331", 3200000, "Thue GTGT 10%")],
        },
        {
            "number": "MH2024-0002", "date": date(2024, 1, 20), "module": "purchase", "type": "purchase_invoice",
            "status": "posted", "contact": "La Siesta Hoi An", "supplier_id": supp_ids["NCC008"],
            "currency": "VND", "rate": 1, "desc": "Dat phong La Siesta - doan khach EU",
            "lines": [("632", "331", 18900000, "9 dem x 2,100,000 VND"), ("1331", "331", 1890000, "Thue GTGT 10%")],
        },
        {
            "number": "MH2024-0003", "date": date(2024, 2, 10), "module": "purchase", "type": "purchase_invoice",
            "status": "draft", "contact": "Sapa Tourism", "supplier_id": supp_ids["NCC009"],
            "currency": "VND", "rate": 1, "desc": "Dich vu trekking Sapa 3 ngay",
            "lines": [("632", "331", 12000000, "Trekking guide + homestay")],
        },
        # === BAN HANG ===
        {
            "number": "BH2024-0001", "date": date(2024, 1, 3), "module": "sale", "type": "sale_invoice",
            "status": "posted", "contact": "Voyage Prive SAS", "customer_id": cust_ids["KH001"],
            "currency": "EUR", "rate": 27200, "desc": "Tour Viet Nam Classique 10N - 12 pax",
            "lines": [("131", "5113", 18500, "Tour 10N x 12 pax")],
        },
        {
            "number": "BH2024-0002", "date": date(2024, 1, 8), "module": "sale", "type": "sale_invoice",
            "status": "posted", "contact": "Saigontourist", "customer_id": cust_ids["KH004"],
            "currency": "VND", "rate": 1, "desc": "Tour Ha Long 2N1D - 15 pax",
            "lines": [("131", "5113", 52500000, "Tour HL 2N1D x 15 pax x 3,500,000")],
        },
        {
            "number": "BH2024-0003", "date": date(2024, 1, 22), "module": "sale", "type": "sale_invoice",
            "status": "posted", "contact": "Intrepid Travel", "customer_id": cust_ids["KH008"],
            "currency": "USD", "rate": 25450, "desc": "Tour Mekong Adventure 5N - 8 pax",
            "lines": [("131", "5113", 8800, "Mekong 5N x 8 pax x $1,100")],
        },
        {
            "number": "BH2024-0004", "date": date(2024, 2, 5), "module": "sale", "type": "sale_invoice",
            "status": "draft", "contact": "Bamboo Travel Ltd", "customer_id": cust_ids["KH009"],
            "currency": "GBP", "rate": 32100, "desc": "Tour Luxury Vietnam 14N - 4 pax",
            "lines": [("131", "5113", 12800, "Luxury 14N x 4 pax")],
        },
        # === TONG HOP ===
        {
            "number": "BT2024-0001", "date": date(2024, 1, 31), "module": "general", "type": "journal",
            "status": "posted", "contact": "Ket chuyen T1/2024",
            "currency": "VND", "rate": 1, "desc": "Phan bo chi phi tra truoc T1",
            "lines": [("642", "242", 5000000, "Phan bo CPTT van phong T1")],
        },
    ]

    for vd in vouchers_data:
        v = Voucher(
            voucher_number=vd["number"],
            voucher_date=vd["date"],
            posting_date=vd["date"],
            module=vd["module"],
            voucher_type=vd["type"],
            status=vd["status"],
            contact_name=vd["contact"],
            customer_id=vd.get("customer_id"),
            supplier_id=vd.get("supplier_id"),
            employee_id=vd.get("employee_id"),
            currency=vd["currency"],
            exchange_rate=vd["rate"],
            description=vd["desc"],
            created_by=users[1].id,  # Binh
            cashier="Tran Thi Binh",
        )
        total = 0
        total_vnd = 0
        for i, (dr, cr, amt, desc) in enumerate(vd["lines"]):
            amt_vnd = amt * vd["rate"]
            line = VoucherLine(
                line_number=i + 1,
                debit_account=dr,
                credit_account=cr,
                amount=amt,
                amount_vnd=amt_vnd,
                description=desc,
            )
            v.lines.append(line)
            total += amt
            total_vnd += amt_vnd

        v.total_amount = total
        v.total_amount_vnd = total_vnd
        db.add(v)

    db.commit()

    # Print summary
    print("\n" + "=" * 50)
    print("SEED DATA COMPLETED!")
    print("=" * 50)
    print(f"  Users:            {db.query(User).count()}")
    print(f"  Departments:      {db.query(Department).count()}")
    print(f"  Employees:        {db.query(Employee).count()}")
    print(f"  Customers:        {db.query(Customer).count()}")
    print(f"  Suppliers:        {db.query(Supplier).count()}")
    print(f"  Accounts:         {db.query(Account).count()}")
    print(f"  Products:         {db.query(Product).count()}")
    print(f"  Banks:            {db.query(Bank).count()}")
    print(f"  Bank Accounts:    {db.query(BankAccount).count()}")
    print(f"  Currencies:       {db.query(Currency).count()}")
    print(f"  Vouchers:         {db.query(Voucher).count()}")
    print(f"  Voucher Lines:    {db.query(VoucherLine).count()}")
    print(f"  Opening Balances: {db.query(OpeningBalance).count()}")
    print("=" * 50)
    print("\nLogin: admin/admin123 or binh/123456")

    db.close()


if __name__ == "__main__":
    seed()
