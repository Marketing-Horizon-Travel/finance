import ModulePage from '../../components/ModulePage';
import { BankOutlined, DollarOutlined, ArrowUpOutlined, ArrowDownOutlined, ExclamationCircleOutlined } from '@ant-design/icons';

const config = {
  title: 'Quản lý Tiền gửi Ngân hàng',
  icon: <BankOutlined />,
  module: 'bank',
  tabs: [
    { key: 'receipt', label: 'Thu tiền' },
    { key: 'payment', label: 'Chi tiền' },
    { key: 'ebanking', label: 'Ngân hàng điện tử' },
    { key: 'reconcile', label: 'Đối chiếu NH' },
  ],
  voucherTypes: [
    { key: 'receipt', label: 'Thu tiền', color: 'green' },
    { key: 'payment', label: 'Chi tiền', color: 'red' },
    { key: 'transfer', label: 'Chuyển tiền', color: 'blue' },
  ],
  summaryCards: [
    { label: 'Số dư NH', value: 0, color: '#1890ff', icon: <DollarOutlined /> },
    { label: 'Thu trong kỳ', value: 0, color: '#52c41a', icon: <ArrowUpOutlined /> },
    { label: 'Chi trong kỳ', value: 0, color: '#f5222d', icon: <ArrowDownOutlined /> },
    { label: 'Chưa đối chiếu', value: 0, color: '#fa8c16', icon: <ExclamationCircleOutlined /> },
  ],
};

export default function NganHangPage() {
  return <ModulePage config={config} />;
}
