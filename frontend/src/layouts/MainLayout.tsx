import { useState } from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import { Layout, Menu, Input, Avatar, Dropdown, Button, Typography } from 'antd';
import {
  DashboardOutlined,
  DollarOutlined,
  BankOutlined,
  ShoppingCartOutlined,
  ShopOutlined,
  FileTextOutlined,
  InboxOutlined,
  ToolOutlined,
  CarOutlined,
  TeamOutlined,
  AuditOutlined,
  FundProjectionScreenOutlined,
  ReconciliationOutlined,
  BarChartOutlined,
  AppstoreOutlined,
  DatabaseOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  SearchOutlined,
  BellOutlined,
  SettingOutlined,
  LogoutOutlined,
  UserOutlined,
} from '@ant-design/icons';
import type { MenuProps } from 'antd';

const { Header, Sider, Content } = Layout;
const { Text } = Typography;

type MenuItem = Required<MenuProps>['items'][number];

const menuItems: MenuItem[] = [
  {
    key: '/dashboard',
    icon: <DashboardOutlined />,
    label: 'Tổng quan',
  },
  { type: 'divider' },
  {
    key: 'phan-hanh',
    label: 'PHÂN HÀNH',
    type: 'group',
    children: [
      { key: '/tien-mat', icon: <DollarOutlined />, label: 'Tiền mặt' },
      { key: '/ngan-hang', icon: <BankOutlined />, label: 'Ngân hàng' },
      { key: '/mua-hang', icon: <ShoppingCartOutlined />, label: 'Mua hàng' },
      { key: '/ban-hang', icon: <ShopOutlined />, label: 'Bán hàng' },
      { key: '/hoa-don', icon: <FileTextOutlined />, label: 'Quản lý hóa đơn' },
      { key: '/kho', icon: <InboxOutlined />, label: 'Kho' },
      { key: '/ccdc', icon: <ToolOutlined />, label: 'CCDC' },
      { key: '/tai-san', icon: <CarOutlined />, label: 'Tài sản cố định' },
      { key: '/tien-luong', icon: <TeamOutlined />, label: 'Tiền lương' },
      { key: '/thue', icon: <AuditOutlined />, label: 'Thuế' },
      { key: '/gia-thanh', icon: <FundProjectionScreenOutlined />, label: 'Giá thành' },
      { key: '/tong-hop', icon: <ReconciliationOutlined />, label: 'Tổng hợp' },
    ],
  },
  { type: 'divider' },
  {
    key: 'bao-cao-menu',
    label: 'BÁO CÁO',
    type: 'group',
    children: [
      { key: '/bao-cao', icon: <BarChartOutlined />, label: 'Báo cáo' },
    ],
  },
  { type: 'divider' },
  {
    key: 'he-thong',
    label: 'HỆ THỐNG',
    type: 'group',
    children: [
      { key: '/danh-muc', icon: <AppstoreOutlined />, label: 'Danh mục' },
      { key: '/du-dau-ky', icon: <DatabaseOutlined />, label: 'Dư đầu kỳ' },
    ],
  },
];

export default function MainLayout() {
  const [collapsed, setCollapsed] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  const userMenu: MenuProps['items'] = [
    { key: 'profile', icon: <UserOutlined />, label: 'Thông tin cá nhân' },
    { key: 'settings', icon: <SettingOutlined />, label: 'Cài đặt' },
    { type: 'divider' },
    {
      key: 'logout',
      icon: <LogoutOutlined />,
      label: 'Đăng xuất',
      danger: true,
      onClick: () => {
        localStorage.removeItem('token');
        navigate('/login');
      },
    },
  ];

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider
        trigger={null}
        collapsible
        collapsed={collapsed}
        width={250}
        style={{
          background: '#1A2035',
          overflow: 'auto',
          height: '100vh',
          position: 'fixed',
          left: 0,
          top: 0,
          bottom: 0,
          zIndex: 100,
        }}
      >
        <div style={{
          height: 56,
          display: 'flex',
          alignItems: 'center',
          padding: collapsed ? '0 16px' : '0 16px',
          borderBottom: '1px solid rgba(255,255,255,0.08)',
          gap: 10,
        }}>
          <div style={{
            width: 32, height: 32,
            background: '#1565C0',
            borderRadius: 6,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            color: '#fff', fontWeight: 800, fontSize: 16, flexShrink: 0,
          }}>
            H
          </div>
          {!collapsed && (
            <div>
              <div style={{ color: '#fff', fontWeight: 700, fontSize: 14, lineHeight: 1.2 }}>
                HORIZON
              </div>
              <div style={{ color: 'rgba(255,255,255,0.45)', fontSize: 10 }}>
                Finance Platform
              </div>
            </div>
          )}
        </div>
        <Menu
          theme="dark"
          mode="inline"
          selectedKeys={[location.pathname]}
          items={menuItems}
          onClick={({ key }) => navigate(key)}
          style={{ background: 'transparent', borderRight: 0 }}
        />
      </Sider>

      <Layout style={{ marginLeft: collapsed ? 80 : 250, transition: 'margin-left 0.2s' }}>
        <Header style={{
          background: '#fff',
          padding: '0 20px',
          display: 'flex',
          alignItems: 'center',
          gap: 12,
          borderBottom: '1px solid #e0e3e9',
          boxShadow: '0 1px 3px rgba(0,0,0,0.08)',
          position: 'sticky',
          top: 0,
          zIndex: 50,
          height: 56,
        }}>
          <Button
            type="text"
            icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
            onClick={() => setCollapsed(!collapsed)}
          />
          <Input
            prefix={<SearchOutlined style={{ color: '#9CA3AF' }} />}
            placeholder="Tìm kiếm..."
            style={{ maxWidth: 300 }}
            size="middle"
          />
          <div style={{ flex: 1 }} />
          <Text style={{
            background: '#E3F2FD',
            color: '#1565C0',
            fontWeight: 700,
            fontSize: 12,
            padding: '3px 10px',
            borderRadius: 20,
          }}>
            KTNB 2024
          </Text>
          <Button type="text" icon={<BellOutlined />} />
          <Button type="text" icon={<SettingOutlined />} />
          <Dropdown menu={{ items: userMenu }} placement="bottomRight">
            <Avatar
              style={{ background: 'linear-gradient(135deg, #1565C0, #42A5F5)', cursor: 'pointer' }}
              size={32}
            >
              TB
            </Avatar>
          </Dropdown>
        </Header>

        <Content style={{ padding: 20, background: '#F0F2F5', minHeight: 'calc(100vh - 56px)' }}>
          <Outlet />
        </Content>
      </Layout>
    </Layout>
  );
}
