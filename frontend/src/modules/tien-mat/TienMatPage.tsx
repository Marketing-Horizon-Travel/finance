import ModulePage from '../../components/ModulePage';
import { DollarOutlined, WalletOutlined, ArrowUpOutlined, ArrowDownOutlined, GlobalOutlined } from '@ant-design/icons';

const config = {
  title: 'Quản lý Thu - Chi Tiền Mặt',
  icon: <DollarOutlined />,
  module: 'cash',
  tabs: [
    { key: 'receipt', label: 'Phiếu Thu' },
    { key: 'payment', label: 'Phiếu Chi' },
    { key: 'check', label: 'Kiểm kê' },
    { key: 'forecast', label: 'Dự báo dòng tiền' },
  ],
  voucherTypes: [
    { key: 'receipt', label: 'Thu tiền', color: 'green' },
    { key: 'payment', label: 'Chi tiền', color: 'red' },
  ],
  summaryCards: [
    { label: 'Tồn quỹ', value: 0, color: '#1890ff', icon: <WalletOutlined /> },
    { label: 'Tổng thu', value: 0, color: '#52c41a', icon: <ArrowUpOutlined /> },
    { label: 'Tổng chi', value: 0, color: '#f5222d', icon: <ArrowDownOutlined /> },
    { label: 'Ngoại tệ', value: 0, color: '#fa8c16', icon: <GlobalOutlined /> },
  ],
};

export default function TienMatPage() {
  return <ModulePage config={config} />;
}
