import ModulePage from '../../components/ModulePage';
import { TeamOutlined, DollarOutlined, SafetyOutlined, AccountBookOutlined, UserOutlined } from '@ant-design/icons';

const config = {
  title: 'Tiền lương',
  icon: <TeamOutlined />,
  module: 'payroll',
  tabs: [
    { key: 'timekeeping', label: 'Chấm công' },
    { key: 'summary', label: 'Tổng hợp chấm công' },
    { key: 'calculate', label: 'Tính lương' },
    { key: 'posting', label: 'Hạch toán chi phí' },
  ],
  voucherTypes: [
    { key: 'payroll', label: 'Bảng lương', color: 'green' },
    { key: 'posting', label: 'Hạch toán', color: 'blue' },
  ],
  summaryCards: [
    { label: 'Tổng lương', value: 0, color: '#1890ff', icon: <DollarOutlined /> },
    { label: 'BHXH', value: 0, color: '#52c41a', icon: <SafetyOutlined /> },
    { label: 'Thuế TNCN', value: 0, color: '#f5222d', icon: <AccountBookOutlined /> },
    { label: 'Nhân viên', value: 0, color: '#fa8c16', icon: <UserOutlined /> },
  ],
};

export default function TienLuongPage() {
  return <ModulePage config={config} />;
}
