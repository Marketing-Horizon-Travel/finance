import ModulePage from '../../components/ModulePage';
import { AuditOutlined, PercentageOutlined, BankOutlined, UserOutlined, DollarOutlined } from '@ant-design/icons';

const config = {
  title: 'Thuế',
  icon: <AuditOutlined />,
  module: 'tax',
  tabs: [
    { key: 'declare', label: 'Khai thuế' },
    { key: 'payment', label: 'Giấy nộp tiền' },
  ],
  voucherTypes: [
    { key: 'vat', label: 'Thuế GTGT', color: 'blue' },
    { key: 'cit', label: 'Thuế TNDN', color: 'green' },
    { key: 'pit', label: 'Thuế TNCN', color: 'orange' },
  ],
  summaryCards: [
    { label: 'Thuế GTGT', value: 0, color: '#1890ff', icon: <PercentageOutlined /> },
    { label: 'Thuế TNDN', value: 0, color: '#52c41a', icon: <BankOutlined /> },
    { label: 'Thuế TNCN', value: 0, color: '#fa8c16', icon: <UserOutlined /> },
    { label: 'Tổng nộp', value: 0, color: '#f5222d', icon: <DollarOutlined /> },
  ],
};

export default function ThuePage() {
  return <ModulePage config={config} />;
}
