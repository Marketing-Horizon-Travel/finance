import ModulePage from '../../components/ModulePage';
import { InboxOutlined, DatabaseOutlined, ArrowUpOutlined, ArrowDownOutlined, WarningOutlined } from '@ant-design/icons';

const config = {
  title: 'Quản lý Kho',
  icon: <InboxOutlined />,
  module: 'inventory',
  tabs: [
    { key: 'stock_in', label: 'Nhập kho' },
    { key: 'stock_out', label: 'Xuất kho' },
    { key: 'transfer', label: 'Chuyển kho' },
    { key: 'production', label: 'Lệnh sản xuất' },
    { key: 'assembly', label: 'Lắp ráp tháo dỡ' },
    { key: 'stocktake', label: 'Kiểm kê' },
  ],
  voucherTypes: [
    { key: 'stock_in', label: 'Nhập kho', color: 'green' },
    { key: 'stock_out', label: 'Xuất kho', color: 'red' },
    { key: 'transfer', label: 'Chuyển kho', color: 'blue' },
  ],
  summaryCards: [
    { label: 'Tổng tồn kho', value: 0, color: '#1890ff', icon: <DatabaseOutlined /> },
    { label: 'Nhập trong kỳ', value: 0, color: '#52c41a', icon: <ArrowUpOutlined /> },
    { label: 'Xuất trong kỳ', value: 0, color: '#f5222d', icon: <ArrowDownOutlined /> },
    { label: 'Dưới định mức', value: 0, color: '#fa8c16', icon: <WarningOutlined /> },
  ],
};

export default function KhoPage() {
  return <ModulePage config={config} />;
}
