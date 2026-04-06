import ModulePage from '../../components/ModulePage';
import { ShopOutlined, RiseOutlined, DollarOutlined, ClockCircleOutlined, WarningOutlined } from '@ant-design/icons';

const config = {
  title: 'Quản lý Bán hàng',
  icon: <ShopOutlined />,
  module: 'sale',
  tabs: [
    { key: 'quotation', label: 'Báo giá' },
    { key: 'order', label: 'Đơn đặt hàng' },
    { key: 'contract', label: 'Hợp đồng' },
    { key: 'sale', label: 'Bán hàng' },
    { key: 'invoice', label: 'Hóa đơn' },
    { key: 'return', label: 'Trả lại' },
    { key: 'collect', label: 'Thu nợ' },
  ],
  voucherTypes: [
    { key: 'quotation', label: 'Báo giá', color: 'blue' },
    { key: 'sale_order', label: 'Đơn hàng', color: 'cyan' },
    { key: 'sale_invoice', label: 'Bán hàng', color: 'green' },
    { key: 'return', label: 'Trả lại', color: 'orange' },
  ],
  summaryCards: [
    { label: 'Doanh thu', value: 0, color: '#52c41a', icon: <RiseOutlined /> },
    { label: 'Công nợ phải thu', value: 0, color: '#1890ff', icon: <DollarOutlined /> },
    { label: 'Đơn chưa xuất', value: 0, color: '#fa8c16', icon: <ClockCircleOutlined /> },
    { label: 'Quá hạn', value: 0, color: '#f5222d', icon: <WarningOutlined /> },
  ],
};

export default function BanHangPage() {
  return <ModulePage config={config} />;
}
