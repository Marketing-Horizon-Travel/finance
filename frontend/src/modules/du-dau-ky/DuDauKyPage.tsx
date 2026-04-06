import { Card, Col, Row, Typography } from 'antd';
import {
  DollarOutlined, BankOutlined, UserOutlined, ShopOutlined,
  TeamOutlined, InboxOutlined, ToolOutlined, CarOutlined,
  FileProtectOutlined, FileDoneOutlined, DatabaseOutlined,
} from '@ant-design/icons';

const { Title, Text } = Typography;

const balanceTypes = [
  { key: 'account', label: 'Số dư tài khoản', icon: <DollarOutlined style={{ fontSize: 32, color: '#2E7D32' }} />, desc: 'TK 111, 112, 131...' },
  { key: 'bank', label: 'Số dư TK ngân hàng', icon: <BankOutlined style={{ fontSize: 32, color: '#1565C0' }} />, desc: 'TK 1121, 1122' },
  { key: 'customer', label: 'Công nợ khách hàng', icon: <UserOutlined style={{ fontSize: 32, color: '#FF6F00' }} />, desc: 'TK 131' },
  { key: 'supplier', label: 'Công nợ nhà cung cấp', icon: <ShopOutlined style={{ fontSize: 32, color: '#C62828' }} />, desc: 'TK 331' },
  { key: 'employee', label: 'Công nợ nhân viên', icon: <TeamOutlined style={{ fontSize: 32, color: '#7B1FA2' }} />, desc: 'TK 334, 141' },
  { key: 'inventory', label: 'Tồn kho VTHH', icon: <InboxOutlined style={{ fontSize: 32, color: '#2E7D32' }} />, desc: 'TK 152, 153, 155, 156' },
  { key: 'tool', label: 'CCDC đầu kỳ', icon: <ToolOutlined style={{ fontSize: 32, color: '#1565C0' }} />, desc: 'TK 153, 242' },
  { key: 'asset', label: 'Tài sản cố định đầu kỳ', icon: <CarOutlined style={{ fontSize: 32, color: '#FF6F00' }} />, desc: 'TK 211, 214' },
  { key: 'prepaid', label: 'Chi phí trả trước đầu kỳ', icon: <FileProtectOutlined style={{ fontSize: 32, color: '#C62828' }} />, desc: 'TK 242' },
  { key: 'wip', label: 'Chi phí dở dang', icon: <FileDoneOutlined style={{ fontSize: 32, color: '#7B1FA2' }} />, desc: 'TK 154' },
];

export default function DuDauKyPage() {
  return (
    <div>
      <Title level={4} style={{ marginBottom: 20 }}>
        <DatabaseOutlined style={{ marginRight: 8 }} />
        Nhập số dư ban đầu
      </Title>

      <Row gutter={[16, 16]}>
        {balanceTypes.map((item) => (
          <Col xs={24} sm={12} lg={6} xl={4} key={item.key}>
            <Card
              hoverable
              style={{ textAlign: 'center', minHeight: 160 }}
              styles={{ body: { padding: 20, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8 } }}
            >
              {item.icon}
              <Text strong style={{ fontSize: 13 }}>{item.label}</Text>
              <Text type="secondary" style={{ fontSize: 11 }}>{item.desc}</Text>
            </Card>
          </Col>
        ))}
      </Row>
    </div>
  );
}
