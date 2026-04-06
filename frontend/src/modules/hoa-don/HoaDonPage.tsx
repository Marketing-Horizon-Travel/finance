import ModulePage from '../../components/ModulePage';
import { FileTextOutlined, SyncOutlined, CheckCircleOutlined, CloseCircleOutlined, ExclamationCircleOutlined } from '@ant-design/icons';

const config = {
  title: 'Quản lý Hóa đơn',
  icon: <FileTextOutlined />,
  module: 'invoice',
  tabs: [
    { key: 'inbound', label: 'Hóa đơn đầu vào' },
    { key: 'outbound', label: 'Hóa đơn đầu ra' },
    { key: 'sync', label: 'Lịch sử đồng bộ' },
    { key: 'customs', label: 'Tờ khai hải quan' },
  ],
  voucherTypes: [
    { key: 'inbound', label: 'Đầu vào', color: 'blue' },
    { key: 'outbound', label: 'Đầu ra', color: 'green' },
  ],
  summaryCards: [
    { label: 'Đang xử lý', value: 0, color: '#1890ff', icon: <SyncOutlined /> },
    { label: 'Đã xử lý', value: 0, color: '#52c41a', icon: <CheckCircleOutlined /> },
    { label: 'Có lỗi', value: 0, color: '#f5222d', icon: <CloseCircleOutlined /> },
    { label: 'Chưa hạch toán', value: 0, color: '#fa8c16', icon: <ExclamationCircleOutlined /> },
  ],
};

export default function HoaDonPage() {
  return <ModulePage config={config} />;
}
