import { useState } from 'react';
import { Card, Typography, Collapse, List, Tag, Input, Select, Space, Button } from 'antd';
import {
  BarChartOutlined,
  StarOutlined,
  StarFilled,
  SearchOutlined,
  FileExcelOutlined,
} from '@ant-design/icons';

const { Title } = Typography;
const { Panel } = Collapse;

const reportPanels = [
  {
    key: 'favorites',
    title: 'Yêu thích',
    reports: [],
  },
  {
    key: 'financial',
    title: 'Báo cáo tài chính',
    reports: [
      'Bảng cân đối kế toán',
      'Báo cáo kết quả kinh doanh',
      'Báo cáo lưu chuyển tiền tệ (trực tiếp)',
      'Báo cáo lưu chuyển tiền tệ (gián tiếp)',
      'Thuyết minh báo cáo tài chính',
    ],
  },
  {
    key: 'management',
    title: 'Báo cáo quản trị nội bộ',
    reports: [
      'Báo cáo tổng hợp doanh thu - chi phí',
      'Báo cáo phân tích lợi nhuận',
      'Báo cáo dòng tiền theo bộ phận',
    ],
  },
  {
    key: 'cash',
    title: 'Tiền mặt',
    reports: [
      'Sổ quỹ tiền mặt',
      'Sổ chi tiết tiền mặt',
      'Báo cáo tồn quỹ tiền mặt',
    ],
  },
  {
    key: 'bank',
    title: 'Tiền gửi',
    reports: [
      'Sổ tiền gửi ngân hàng',
      'Báo cáo số dư tiền gửi',
      'Bảng đối chiếu ngân hàng',
    ],
  },
  {
    key: 'purchase',
    title: 'Mua hàng',
    reports: [
      'Sổ chi tiết mua hàng',
      'Tổng hợp công nợ phải trả',
      'Chi tiết công nợ phải trả',
      'Báo cáo tuổi nợ phải trả',
    ],
  },
  {
    key: 'sale',
    title: 'Bán hàng',
    reports: [
      'Sổ chi tiết bán hàng',
      'Tổng hợp công nợ phải thu',
      'Chi tiết công nợ phải thu',
      'Báo cáo tuổi nợ phải thu',
      'Báo cáo doanh thu theo mặt hàng',
    ],
  },
  {
    key: 'inventory',
    title: 'Kho',
    reports: [
      'Thẻ kho',
      'Sổ chi tiết vật tư hàng hóa',
      'Tổng hợp tồn kho',
      'Bảng kê nhập xuất tồn',
    ],
  },
  {
    key: 'tool',
    title: 'Công cụ dụng cụ',
    reports: [
      'Sổ theo dõi CCDC',
      'Bảng tính phân bổ CCDC',
      'Sổ theo dõi chi phí trả trước',
    ],
  },
  {
    key: 'asset',
    title: 'Tài sản cố định',
    reports: [
      'Sổ tài sản cố định',
      'Bảng tính khấu hao TSCĐ',
      'Sổ theo dõi TSCĐ tại nơi sử dụng',
    ],
  },
  {
    key: 'payroll',
    title: 'Tiền lương',
    reports: [
      'Bảng lương',
      'Bảng chấm công',
      'Báo cáo chi phí nhân công',
    ],
  },
  {
    key: 'tax',
    title: 'Thuế',
    reports: [
      'Tờ khai thuế GTGT',
      'Tờ khai thuế TNDN',
      'Tờ khai thuế TNCN',
      'Bảng kê hóa đơn hàng hóa dịch vụ mua vào',
      'Bảng kê hóa đơn hàng hóa dịch vụ bán ra',
    ],
  },
  {
    key: 'costing',
    title: 'Giá thành',
    reports: [
      'Thẻ tính giá thành sản phẩm',
      'Tổng hợp chi phí sản xuất',
      'Báo cáo giá thành theo đơn hàng',
    ],
  },
  {
    key: 'general',
    title: 'Tổng hợp',
    reports: [
      'Sổ nhật ký chung',
      'Sổ cái',
      'Sổ chi tiết tài khoản',
      'Bảng cân đối số phát sinh',
    ],
  },
];

export default function BaoCaoPage() {
  const [favorites, setFavorites] = useState<string[]>([]);
  const [searchText, setSearchText] = useState('');

  const toggleFavorite = (reportName: string) => {
    setFavorites((prev) =>
      prev.includes(reportName)
        ? prev.filter((r) => r !== reportName)
        : [...prev, reportName]
    );
  };

  const filteredPanels = reportPanels.map((panel) => ({
    ...panel,
    reports:
      panel.key === 'favorites'
        ? favorites
        : panel.reports.filter((r) =>
            r.toLowerCase().includes(searchText.toLowerCase())
          ),
  }));

  return (
    <div style={{ padding: 24 }}>
      <div style={{ marginBottom: 24, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <Title level={3} style={{ margin: 0 }}>
          <BarChartOutlined style={{ marginRight: 8 }} />
          Báo cáo
        </Title>
        <Space>
          <Input
            placeholder="Tìm kiếm báo cáo..."
            prefix={<SearchOutlined />}
            value={searchText}
            onChange={(e) => setSearchText(e.target.value)}
            style={{ width: 300 }}
            allowClear
          />
          <Select
            placeholder="Kỳ báo cáo"
            style={{ width: 180 }}
            options={[
              { value: 'month', label: 'Tháng này' },
              { value: 'quarter', label: 'Quý này' },
              { value: 'year', label: 'Năm này' },
            ]}
          />
          <Button icon={<FileExcelOutlined />}>Xuất Excel</Button>
        </Space>
      </div>

      <Card>
        <Collapse defaultActiveKey={['favorites', 'financial']}>
          {filteredPanels.map((panel) => (
            <Panel
              header={
                <span>
                  {panel.title}
                  <Tag style={{ marginLeft: 8 }}>{panel.reports.length}</Tag>
                </span>
              }
              key={panel.key}
            >
              <List
                size="small"
                dataSource={panel.reports}
                locale={{ emptyText: 'Không có báo cáo' }}
                renderItem={(item) => (
                  <List.Item
                    style={{ cursor: 'pointer' }}
                    onClick={() => console.log('Open report:', item)}
                    actions={[
                      <Button
                        type="text"
                        size="small"
                        icon={
                          favorites.includes(item) ? (
                            <StarFilled style={{ color: '#faad14' }} />
                          ) : (
                            <StarOutlined />
                          )
                        }
                        onClick={(e) => {
                          e.stopPropagation();
                          toggleFavorite(item);
                        }}
                      />,
                    ]}
                  >
                    {item}
                  </List.Item>
                )}
              />
            </Panel>
          ))}
        </Collapse>
      </Card>
    </div>
  );
}
