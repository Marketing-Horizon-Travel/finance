import ModulePage from '../../components/ModulePage';
import { ToolOutlined, AppstoreOutlined, PieChartOutlined, MinusCircleOutlined, HourglassOutlined } from '@ant-design/icons';

const config = {
  title: 'Công cụ dụng cụ, Chi phí trả trước',
  icon: <ToolOutlined />,
  module: 'tool',
  tabs: [
    { key: 'tracking', label: 'Sổ theo dõi' },
    { key: 'manage', label: 'Quản lý CCDC' },
    { key: 'prepaid', label: 'Chi phí trả trước' },
  ],
  voucherTypes: [
    { key: 'increase', label: 'Ghi tăng', color: 'green' },
    { key: 'allocate', label: 'Phân bổ', color: 'blue' },
    { key: 'decrease', label: 'Ghi giảm', color: 'red' },
  ],
  summaryCards: [
    { label: 'Tổng CCDC', value: 0, color: '#1890ff', icon: <AppstoreOutlined /> },
    { label: 'Phân bổ trong kỳ', value: 0, color: '#52c41a', icon: <PieChartOutlined /> },
    { label: 'Đã ghi giảm', value: 0, color: '#f5222d', icon: <MinusCircleOutlined /> },
    { label: 'CPTT còn lại', value: 0, color: '#fa8c16', icon: <HourglassOutlined /> },
  ],
};

export default function CCDCPage() {
  return <ModulePage config={config} />;
}
