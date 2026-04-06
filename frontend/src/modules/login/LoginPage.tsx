import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, Form, Input, Button, Typography, message } from 'antd';
import { UserOutlined, LockOutlined, BankOutlined } from '@ant-design/icons';
import { authService } from '../../services/auth';

const { Title, Text } = Typography;

export default function LoginPage() {
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const onFinish = async (values: { username: string; password: string }) => {
    setLoading(true);
    try {
      const res = await authService.login(values.username, values.password);
      localStorage.setItem('user', JSON.stringify(res.user));
      message.success(`Xin chào, ${res.user.full_name}!`);
      navigate('/dashboard');
    } catch {
      message.error('Sai tài khoản hoặc mật khẩu');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'linear-gradient(135deg, #1A2035 0%, #1565C0 100%)',
    }}>
      <Card
        style={{
          width: 400,
          borderRadius: 12,
          boxShadow: '0 8px 32px rgba(0,0,0,0.2)',
        }}
        styles={{ body: { padding: 32 } }}
      >
        <div style={{ textAlign: 'center', marginBottom: 32 }}>
          <div style={{
            width: 56, height: 56,
            background: '#1565C0',
            borderRadius: 12,
            display: 'inline-flex',
            alignItems: 'center',
            justifyContent: 'center',
            marginBottom: 16,
          }}>
            <BankOutlined style={{ fontSize: 28, color: '#fff' }} />
          </div>
          <Title level={3} style={{ margin: 0 }}>Horizon Finance</Title>
          <Text type="secondary">Phần mềm kế toán trực tuyến</Text>
        </div>

        <Form
          name="login"
          onFinish={onFinish}
          size="large"
          layout="vertical"
        >
          <Form.Item
            name="username"
            rules={[{ required: true, message: 'Vui lòng nhập tài khoản' }]}
          >
            <Input
              prefix={<UserOutlined style={{ color: '#9CA3AF' }} />}
              placeholder="Tài khoản"
              autoFocus
            />
          </Form.Item>

          <Form.Item
            name="password"
            rules={[{ required: true, message: 'Vui lòng nhập mật khẩu' }]}
          >
            <Input.Password
              prefix={<LockOutlined style={{ color: '#9CA3AF' }} />}
              placeholder="Mật khẩu"
            />
          </Form.Item>

          <Form.Item style={{ marginBottom: 16 }}>
            <Button
              type="primary"
              htmlType="submit"
              loading={loading}
              block
              style={{ height: 44, fontWeight: 600 }}
            >
              Đăng nhập
            </Button>
          </Form.Item>
        </Form>

        <div style={{
          textAlign: 'center',
          padding: '12px 0',
          borderTop: '1px solid #f0f0f0',
        }}>
          <Text type="secondary" style={{ fontSize: 12 }}>
            CÔNG TY TNHH LỮ HÀNH QUỐC TẾ CHÂN TRỜI VIỆT
          </Text>
          <br />
          <Text type="secondary" style={{ fontSize: 11 }}>
            Horizon Vietnam Travel © 2024
          </Text>
        </div>
      </Card>
    </div>
  );
}
