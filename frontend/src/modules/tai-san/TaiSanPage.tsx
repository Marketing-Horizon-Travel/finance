import ModulePage from '../../components/ModulePage';
import { CarOutlined, HomeOutlined, DollarOutlined, FallOutlined, FundOutlined } from '@ant-design/icons';

const config = {
  title: 'Tài sản cố định',
  icon: <CarOutlined />,
  module: 'asset',
  tabs: [
    { key: 'register', label: 'Sổ tài sản' },
    { key: 'increase', label: 'Ghi tăng' },
    { key: 'depreciation', label: 'Tính khấu hao' },
    { key: 'revalue', label: 'Đánh giá lại' },
    { key: 'transfer', label: 'Điều chuyển' },
    { key: 'decrease', label: 'Ghi giảm' },
    { key: 'stocktake', label: 'Kiểm kê' },
  ],
  voucherTypes: [
    { key: 'increase', label: 'Ghi tăng', color: 'green' },
    { key: 'depreciation', label: 'Khấu hao', color: 'blue' },
    { key: 'decrease', label: 'Ghi giảm', color: 'red' },
  ],
  summaryCards: [
    { label: 'Tổng TSCĐ', value: 0, color: '#1890ff', icon: <HomeOutlined /> },
    { label: 'Nguyên giá', value: 0, color: '#52c41a', icon: <DollarOutlined /> },
    { label: 'Khấu hao lũy kế', value: 0, color: '#f5222d', icon: <FallOutlined /> },
    { label: 'Giá trị còn lại', value: 0, color: '#fa8c16', icon: <FundOutlined /> },
  ],
};

export default function TaiSanPage() {
  return <ModulePage config={config} />;
}
