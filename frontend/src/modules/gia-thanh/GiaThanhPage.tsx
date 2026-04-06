import ModulePage from '../../components/ModulePage';
import { FundProjectionScreenOutlined, AimOutlined, NodeIndexOutlined, CalculatorOutlined, AppstoreOutlined } from '@ant-design/icons';

const config = {
  title: 'Giá thành',
  icon: <FundProjectionScreenOutlined />,
  module: 'costing',
  tabs: [
    { key: 'simple', label: 'Giản đơn' },
    { key: 'ratio', label: 'Hệ số tỷ lệ' },
    { key: 'project', label: 'Công trình' },
    { key: 'order', label: 'Đơn hàng' },
    { key: 'contract', label: 'Hợp đồng' },
  ],
  voucherTypes: [
    { key: 'collect_cost', label: 'Tập hợp CP', color: 'blue' },
    { key: 'calculate', label: 'Tính giá thành', color: 'green' },
  ],
  summaryCards: [
    { label: 'CP trực tiếp', value: 0, color: '#1890ff', icon: <AimOutlined /> },
    { label: 'CP gián tiếp', value: 0, color: '#52c41a', icon: <NodeIndexOutlined /> },
    { label: 'Giá thành', value: 0, color: '#fa8c16', icon: <CalculatorOutlined /> },
    { label: 'Sản phẩm', value: 0, color: '#7B1FA2', icon: <AppstoreOutlined /> },
  ],
};

export default function GiaThanhPage() {
  return <ModulePage config={config} />;
}
