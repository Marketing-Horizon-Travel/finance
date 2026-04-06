import ModulePage from '../../components/ModulePage';
import { ReconciliationOutlined, FormOutlined, SwapOutlined, FileProtectOutlined, UnlockOutlined } from '@ant-design/icons';

const config = {
  title: 'Tổng hợp',
  icon: <ReconciliationOutlined />,
  module: 'general',
  tabs: [
    { key: 'journal', label: 'Chứng từ NV khác' },
    { key: 'closing', label: 'Kết chuyển lãi lỗ' },
    { key: 'financial', label: 'Lập BCTC' },
  ],
  voucherTypes: [
    { key: 'journal', label: 'Bút toán', color: 'blue' },
    { key: 'closing', label: 'Kết chuyển', color: 'green' },
    { key: 'advance', label: 'Quyết toán tạm ứng', color: 'orange' },
  ],
  summaryCards: [
    { label: 'Bút toán trong kỳ', value: 0, color: '#1890ff', icon: <FormOutlined /> },
    { label: 'Kết chuyển', value: 0, color: '#52c41a', icon: <SwapOutlined /> },
    { label: 'BCTC', value: 0, color: '#fa8c16', icon: <FileProtectOutlined /> },
    { label: 'Chưa khóa sổ', value: 0, color: '#f5222d', icon: <UnlockOutlined /> },
  ],
};

export default function TongHopPage() {
  return <ModulePage config={config} />;
}
