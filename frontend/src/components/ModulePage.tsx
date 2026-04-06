/**
 * ModulePage — Reusable template for all voucher-based modules.
 * Provides tabs, table, filters, and modal — matching MISA layout.
 */
import { useState } from 'react';
import {
  Card, Table, Button, Space, Tag, Input, Select, DatePicker,
  Tabs, Typography, Row, Col, Statistic, Tooltip, Dropdown,
} from 'antd';
import {
  PlusOutlined, SearchOutlined, ExportOutlined, ImportOutlined,
  DeleteOutlined, EditOutlined, EyeOutlined, PrinterOutlined,
  MoreOutlined, CheckCircleOutlined,
} from '@ant-design/icons';
import type { ColumnsType } from 'antd/es/table';
import dayjs from 'dayjs';

const { Title, Text } = Typography;
const { RangePicker } = DatePicker;

export interface ModuleConfig {
  title: string;
  icon: React.ReactNode;
  module: string;
  tabs: { key: string; label: string }[];
  voucherTypes: { key: string; label: string; color?: string }[];
  summaryCards: { label: string; value: number; color: string; icon: React.ReactNode }[];
  reports?: { label: string; key: string }[];
  extraColumns?: ColumnsType<any>;
}

interface Props {
  config: ModuleConfig;
}

// Sample data for demo
const sampleData: any[] = [];

export default function ModulePage({ config }: Props) {
  const [activeTab, setActiveTab] = useState('all');

  const baseColumns: ColumnsType<any> = [
    {
      title: '#', dataIndex: 'index', width: 50, align: 'center',
      render: (_: any, __: any, i: number) => i + 1,
    },
    {
      title: 'Số chứng từ', dataIndex: 'voucher_number', width: 140,
      render: (t: string) => <Text strong style={{ color: '#1565C0' }}>{t}</Text>,
    },
    {
      title: 'Ngày', dataIndex: 'voucher_date', width: 100,
      render: (d: string) => d ? dayjs(d).format('DD/MM/YYYY') : '',
    },
    {
      title: 'Loại', dataIndex: 'voucher_type', width: 100,
      render: (t: string) => {
        const vt = config.voucherTypes.find(v => v.key === t);
        return <Tag color={vt?.color || 'default'}>{vt?.label || t}</Tag>;
      },
    },
    { title: 'Đối tượng', dataIndex: 'contact_name', ellipsis: true },
    { title: 'Diễn giải', dataIndex: 'description', ellipsis: true },
    {
      title: 'Số tiền', dataIndex: 'total_amount_vnd', width: 140, align: 'right',
      render: (v: number) => <Text strong>{(v || 0).toLocaleString('vi-VN')}</Text>,
    },
    {
      title: 'Trạng thái', dataIndex: 'status', width: 120, align: 'center',
      render: (s: string) => (
        <Tag color={s === 'posted' ? 'success' : s === 'draft' ? 'warning' : 'error'}>
          {s === 'posted' ? 'Đã hạch toán' : s === 'draft' ? 'Nháp' : 'Đã hủy'}
        </Tag>
      ),
    },
    {
      title: '', width: 80, align: 'center',
      render: () => (
        <Space size={4}>
          <Tooltip title="Sửa"><Button type="text" size="small" icon={<EditOutlined />} /></Tooltip>
          <Dropdown menu={{
            items: [
              { key: 'view', icon: <EyeOutlined />, label: 'Xem' },
              { key: 'print', icon: <PrinterOutlined />, label: 'In' },
              { key: 'post', icon: <CheckCircleOutlined />, label: 'Hạch toán' },
              { type: 'divider' },
              { key: 'delete', icon: <DeleteOutlined />, label: 'Xóa', danger: true },
            ],
          }}>
            <Button type="text" size="small" icon={<MoreOutlined />} />
          </Dropdown>
        </Space>
      ),
    },
  ];

  const allColumns = config.extraColumns
    ? [...baseColumns.slice(0, -1), ...config.extraColumns, baseColumns[baseColumns.length - 1]]
    : baseColumns;

  const tabItems = [
    { key: 'all', label: 'Tất cả' },
    ...config.tabs,
  ];

  return (
    <div>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
        <Title level={4} style={{ margin: 0 }}>
          {config.icon}
          <span style={{ marginLeft: 8 }}>{config.title}</span>
        </Title>
        <Space>
          <Button icon={<DeleteOutlined />}>Xóa</Button>
          <Button icon={<ExportOutlined />}>Xuất Excel</Button>
          <Button icon={<ImportOutlined />}>Nhập</Button>
          <Button type="primary" icon={<PlusOutlined />}>Thêm mới</Button>
        </Space>
      </div>

      {/* Summary Cards */}
      <Row gutter={[12, 12]} style={{ marginBottom: 16 }}>
        {config.summaryCards.map((card, i) => (
          <Col xs={24} sm={12} lg={6} key={i}>
            <Card size="small" hoverable style={{ borderTop: `3px solid ${card.color}` }}>
              <Statistic
                title={card.label}
                value={card.value}
                prefix={card.icon}
                valueStyle={{ color: card.color, fontSize: 18 }}
                formatter={(val) => Number(val).toLocaleString('vi-VN')}
                suffix="VND"
              />
            </Card>
          </Col>
        ))}
      </Row>

      {/* Table Card */}
      <Card styles={{ body: { padding: 0 } }}>
        <Tabs
          activeKey={activeTab}
          onChange={setActiveTab}
          items={tabItems}
          style={{ padding: '0 16px' }}
        />

        {/* Filters */}
        <div style={{ padding: '8px 16px', display: 'flex', gap: 8, flexWrap: 'wrap', borderBottom: '1px solid #f0f0f0' }}>
          <Input
            prefix={<SearchOutlined />}
            placeholder="Tìm kiếm..."
            style={{ maxWidth: 250 }}
          />
          <Select
            placeholder="Loại tiền"
            style={{ width: 120 }}
            allowClear
            options={[
              { value: 'VND', label: 'VND' },
              { value: 'USD', label: 'USD' },
              { value: 'EUR', label: 'EUR' },
            ]}
          />
          <Select
            placeholder="Trạng thái"
            style={{ width: 140 }}
            allowClear
            options={[
              { value: 'posted', label: 'Đã hạch toán' },
              { value: 'draft', label: 'Nháp' },
              { value: 'cancelled', label: 'Đã hủy' },
            ]}
          />
          <RangePicker format="DD/MM/YYYY" />
        </div>

        <Table
          columns={allColumns}
          dataSource={sampleData}
          rowKey="id"
          size="small"
          pagination={{ pageSize: 20, showSizeChanger: true, showTotal: (t) => `Tổng: ${t}` }}
          locale={{ emptyText: 'Không có dữ liệu' }}
          rowSelection={{ type: 'checkbox' }}
        />
      </Card>
    </div>
  );
}
