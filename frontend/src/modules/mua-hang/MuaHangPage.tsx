import ModulePage from '../../components/ModulePage';
import { ShoppingCartOutlined, DollarOutlined, CreditCardOutlined, ClockCircleOutlined, FileTextOutlined } from '@ant-design/icons';

const config = {
  title: 'Quản lý Mua hàng',
  icon: <ShoppingCartOutlined />,
  module: 'purchase',
  tabs: [
    { key: 'order', label: 'Đơn mua hàng' },
    { key: 'contract', label: 'Hợp đồng' },
    { key: 'invoice', label: 'Mua hàng hóa DV' },
    { key: 'receive', label: 'Nhận hóa đơn' },
    { key: 'return', label: 'Trả lại' },
    { key: 'discount', label: 'Giảm giá' },
  ],
  voucherTypes: [
    { key: 'purchase_order', label: 'Đơn MH', color: 'blue' },
    { key: 'purchase_invoice', label: 'Mua hàng', color: 'green' },
    { key: 'return', label: 'Trả lại', color: 'orange' },
  ],
  summaryCards: [
    { label: 'Tổng mua', value: 0, color: '#1890ff', icon: <DollarOutlined /> },
    { label: 'Công nợ NCC', value: 0, color: '#f5222d', icon: <CreditCardOutlined /> },
    { label: 'Đơn chưa nhận', value: 0, color: '#fa8c16', icon: <ClockCircleOutlined /> },
    { label: 'Hóa đơn chưa nhận', value: 0, color: '#7B1FA2', icon: <FileTextOutlined /> },
  ],
};

export default function MuaHangPage() {
  return <ModulePage config={config} />;
}
