import { Card, Col, Row, Typography } from 'antd';
import {
  UserOutlined,
  ShopOutlined,
  TeamOutlined,
  UsergroupAddOutlined,
  ShoppingOutlined,
  InboxOutlined,
  AppstoreOutlined,
  DashboardOutlined,
  BankOutlined,
  CreditCardOutlined,
  ApartmentOutlined,
  FundOutlined,
  OrderedListOutlined,
  ProjectOutlined,
  BuildOutlined,
  CarOutlined,
  ToolOutlined,
  PercentageOutlined,
  GoldOutlined,
  FileProtectOutlined,
  DollarOutlined,
  BarChartOutlined,
  MoneyCollectOutlined,
  FileTextOutlined,
  ScheduleOutlined,
  CalculatorOutlined,
} from '@ant-design/icons';
import { useNavigate } from 'react-router-dom';

const { Title, Text } = Typography;

interface CategoryItem {
  key: string;
  label: string;
  icon: React.ReactNode;
  path: string;
}

interface CategoryGroup {
  title: string;
  items: CategoryItem[];
}

const categories: CategoryGroup[] = [
  {
    title: 'Đối tượng',
    items: [
      { key: 'customers', label: 'Khách hàng', icon: <UserOutlined />, path: '/danh-muc/customers' },
      { key: 'suppliers', label: 'Nhà cung cấp', icon: <ShopOutlined />, path: '/danh-muc/suppliers' },
      { key: 'employees', label: 'Nhân viên', icon: <TeamOutlined />, path: '/danh-muc/employees' },
      { key: 'groups', label: 'Nhóm KH, NCC', icon: <UsergroupAddOutlined />, path: '/danh-muc/groups' },
    ],
  },
  {
    title: 'Vật tư hàng hóa',
    items: [
      { key: 'products', label: 'Vật tư hàng hóa', icon: <ShoppingOutlined />, path: '/danh-muc/products' },
      { key: 'warehouses', label: 'Kho', icon: <InboxOutlined />, path: '/danh-muc/warehouses' },
      { key: 'product-groups', label: 'Nhóm VTHH, dịch vụ', icon: <AppstoreOutlined />, path: '/danh-muc/product-groups' },
      { key: 'units', label: 'Đơn vị tính', icon: <DashboardOutlined />, path: '/danh-muc/units' },
    ],
  },
  {
    title: 'Tài khoản',
    items: [
      { key: 'accounts', label: 'Hệ thống tài khoản', icon: <OrderedListOutlined />, path: '/danh-muc/accounts' },
    ],
  },
  {
    title: 'Ngân hàng',
    items: [
      { key: 'banks', label: 'Ngân hàng', icon: <BankOutlined />, path: '/danh-muc/banks' },
      { key: 'bank-accounts', label: 'Tài khoản ngân hàng', icon: <CreditCardOutlined />, path: '/danh-muc/bank-accounts' },
    ],
  },
  {
    title: 'Chi nhánh, phòng ban',
    items: [
      { key: 'departments', label: 'Cơ cấu tổ chức', icon: <ApartmentOutlined />, path: '/danh-muc/departments' },
    ],
  },
  {
    title: 'Chi phí',
    items: [
      { key: 'cost-objects', label: 'Đối tượng THCP', icon: <FundOutlined />, path: '/danh-muc/cost-objects' },
      { key: 'cost-items', label: 'Khoản mục chi phí', icon: <OrderedListOutlined />, path: '/danh-muc/cost-items' },
      { key: 'projects', label: 'Công trình', icon: <ProjectOutlined />, path: '/danh-muc/projects' },
      { key: 'project-types', label: 'Loại công trình', icon: <BuildOutlined />, path: '/danh-muc/project-types' },
    ],
  },
  {
    title: 'Tài sản',
    items: [
      { key: 'tool-types', label: 'Loại CCDC', icon: <ToolOutlined />, path: '/danh-muc/tool-types' },
      { key: 'asset-types', label: 'Loại TSCĐ', icon: <CarOutlined />, path: '/danh-muc/asset-types' },
    ],
  },
  {
    title: 'Thuế',
    items: [
      { key: 'tax-special', label: 'Biểu thuế TTĐB', icon: <PercentageOutlined />, path: '/danh-muc/tax-special' },
      { key: 'tax-resource', label: 'Biểu thuế tài nguyên', icon: <GoldOutlined />, path: '/danh-muc/tax-resource' },
    ],
  },
  {
    title: 'Khác',
    items: [
      { key: 'payment-terms', label: 'Điều khoản thanh toán', icon: <FileProtectOutlined />, path: '/danh-muc/payment-terms' },
      { key: 'cash-flow-items', label: 'Mục thu/chi', icon: <DollarOutlined />, path: '/danh-muc/cash-flow-items' },
      { key: 'stat-codes', label: 'Mã thống kê', icon: <BarChartOutlined />, path: '/danh-muc/stat-codes' },
      { key: 'currencies', label: 'Loại tiền', icon: <MoneyCollectOutlined />, path: '/danh-muc/currencies' },
      { key: 'voucher-types', label: 'Loại chứng từ', icon: <FileTextOutlined />, path: '/danh-muc/voucher-types' },
    ],
  },
  {
    title: 'Tiền lương',
    items: [
      { key: 'timekeeping', label: 'Ký hiệu chấm công', icon: <ScheduleOutlined />, path: '/danh-muc/timekeeping' },
      { key: 'income-tax', label: 'Biểu tính thuế thu nhập', icon: <CalculatorOutlined />, path: '/danh-muc/income-tax' },
    ],
  },
];

export default function DanhMucPage() {
  const navigate = useNavigate();

  return (
    <div>
      <Title level={4} style={{ marginBottom: 20 }}>
        <AppstoreOutlined style={{ marginRight: 8 }} />
        Danh mục
      </Title>

      <Row gutter={[16, 16]}>
        {categories.map((group) => (
          <Col xs={24} sm={12} lg={8} key={group.title}>
            <Card
              title={<Text strong>{group.title}</Text>}
              size="small"
              styles={{ body: { padding: '8px 16px' } }}
            >
              {group.items.map((item) => (
                <div
                  key={item.key}
                  onClick={() => navigate(item.path)}
                  style={{
                    padding: '8px 0',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: 8,
                    color: '#1565C0',
                    borderBottom: '1px solid #f0f0f0',
                  }}
                >
                  {item.icon}
                  <Text style={{ color: '#1565C0' }}>{item.label}</Text>
                </div>
              ))}
            </Card>
          </Col>
        ))}
      </Row>
    </div>
  );
}
