import { Card, Col, Row, Statistic, Typography, Table, Tag } from 'antd';
import {
  DollarOutlined,
  BankOutlined,
  ShoppingCartOutlined,
  ShopOutlined,
  ArrowUpOutlined,
  ArrowDownOutlined,
  FileTextOutlined,
  TeamOutlined,
} from '@ant-design/icons';

const { Title, Text } = Typography;

const summaryCards = [
  { title: 'Tồn quỹ tiền mặt', value: 0, prefix: <DollarOutlined />, color: '#1565C0', suffix: 'VND' },
  { title: 'Tiền gửi ngân hàng', value: 0, prefix: <BankOutlined />, color: '#2E7D32', suffix: 'VND' },
  { title: 'Công nợ phải thu', value: 0, prefix: <ShopOutlined />, color: '#FF6F00', suffix: 'VND' },
  { title: 'Công nợ phải trả', value: 0, prefix: <ShoppingCartOutlined />, color: '#C62828', suffix: 'VND' },
];

const recentVouchers = [
  { key: '1', number: 'PT2024-0001', type: 'Thu', contact: 'SAIGONTOURIST', amount: 25000000, status: 'posted', date: '2024-01-15' },
  { key: '2', number: 'PC2024-0001', type: 'Chi', contact: 'VP AIRLINES', amount: 15000000, status: 'posted', date: '2024-01-15' },
  { key: '3', number: 'BC2024-0001', type: 'Thu NH', contact: 'INDOCHINA TRAVEL', amount: 50000000, status: 'draft', date: '2024-01-14' },
];

const columns = [
  { title: 'Số chứng từ', dataIndex: 'number', key: 'number', render: (t: string) => <Text strong style={{ color: '#1565C0' }}>{t}</Text> },
  {
    title: 'Loại', dataIndex: 'type', key: 'type',
    render: (t: string) => <Tag color={t.includes('Thu') ? 'green' : 'red'}>{t}</Tag>,
  },
  { title: 'Đối tượng', dataIndex: 'contact', key: 'contact' },
  {
    title: 'Số tiền', dataIndex: 'amount', key: 'amount', align: 'right' as const,
    render: (v: number) => <Text strong>{v.toLocaleString('vi-VN')}</Text>,
  },
  {
    title: 'Trạng thái', dataIndex: 'status', key: 'status',
    render: (s: string) => (
      <Tag color={s === 'posted' ? 'success' : s === 'draft' ? 'warning' : 'error'}>
        {s === 'posted' ? 'Đã hạch toán' : s === 'draft' ? 'Nháp' : 'Đã hủy'}
      </Tag>
    ),
  },
  { title: 'Ngày', dataIndex: 'date', key: 'date' },
];

export default function DashboardPage() {
  return (
    <div>
      <Title level={4} style={{ marginBottom: 20 }}>
        <DollarOutlined style={{ marginRight: 8 }} />
        Tổng quan tài chính
      </Title>

      <Row gutter={[16, 16]}>
        {summaryCards.map((card, i) => (
          <Col xs={24} sm={12} lg={6} key={i}>
            <Card hoverable style={{ borderTop: `3px solid ${card.color}` }}>
              <Statistic
                title={card.title}
                value={card.value}
                prefix={card.prefix}
                suffix={card.suffix}
                valueStyle={{ color: card.color, fontSize: 20 }}
                formatter={(val) => Number(val).toLocaleString('vi-VN')}
              />
            </Card>
          </Col>
        ))}
      </Row>

      <Row gutter={[16, 16]} style={{ marginTop: 20 }}>
        <Col xs={24} lg={16}>
          <Card title="Chứng từ gần đây" extra={<a href="/tien-mat">Xem tất cả</a>}>
            <Table
              columns={columns}
              dataSource={recentVouchers}
              pagination={false}
              size="small"
            />
          </Card>
        </Col>
        <Col xs={24} lg={8}>
          <Card title="Thống kê nhanh">
            <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
              <Statistic
                title="Tổng thu tháng này"
                value={0}
                prefix={<ArrowUpOutlined />}
                valueStyle={{ color: '#2E7D32', fontSize: 16 }}
                suffix="VND"
              />
              <Statistic
                title="Tổng chi tháng này"
                value={0}
                prefix={<ArrowDownOutlined />}
                valueStyle={{ color: '#C62828', fontSize: 16 }}
                suffix="VND"
              />
              <Statistic
                title="Số chứng từ chưa hạch toán"
                value={0}
                prefix={<FileTextOutlined />}
                valueStyle={{ color: '#FF6F00', fontSize: 16 }}
              />
              <Statistic
                title="Nhân viên"
                value={0}
                prefix={<TeamOutlined />}
                valueStyle={{ fontSize: 16 }}
              />
            </div>
          </Card>
        </Col>
      </Row>
    </div>
  );
}
