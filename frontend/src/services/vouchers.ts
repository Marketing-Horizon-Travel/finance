import api from './api';

export interface VoucherLine {
  id?: number;
  line_number: number;
  debit_account: string;
  credit_account: string;
  amount: number;
  amount_vnd: number;
  description?: string;
  product_id?: number;
  warehouse_id?: number;
  quantity?: number;
  unit_price?: number;
}

export interface Voucher {
  id?: number;
  voucher_number?: string;
  voucher_date: string;
  posting_date: string;
  module: string;
  voucher_type: string;
  status: string;
  customer_id?: number;
  supplier_id?: number;
  employee_id?: number;
  contact_name?: string;
  contact_address?: string;
  currency: string;
  exchange_rate: number;
  total_amount?: number;
  total_amount_vnd?: number;
  description?: string;
  reference_doc?: string;
  cashier?: string;
  lines: VoucherLine[];
}

export interface VoucherListResponse {
  items: Voucher[];
  total: number;
  page: number;
  page_size: number;
}

export const voucherService = {
  list: async (params: Record<string, any>): Promise<VoucherListResponse> => {
    const { data } = await api.get('/vouchers', { params });
    return data;
  },

  get: async (id: number): Promise<Voucher> => {
    const { data } = await api.get(`/vouchers/${id}`);
    return data;
  },

  create: async (voucher: Voucher): Promise<Voucher> => {
    const { data } = await api.post('/vouchers', voucher);
    return data;
  },

  update: async (id: number, voucher: Voucher): Promise<Voucher> => {
    const { data } = await api.put(`/vouchers/${id}`, voucher);
    return data;
  },

  delete: async (id: number): Promise<void> => {
    await api.delete(`/vouchers/${id}`);
  },

  post: async (id: number): Promise<void> => {
    await api.post(`/vouchers/${id}/post`);
  },

  cancel: async (id: number): Promise<void> => {
    await api.post(`/vouchers/${id}/cancel`);
  },

  summary: async (module: string, params?: Record<string, any>) => {
    const { data } = await api.get(`/vouchers/summary/${module}`, { params });
    return data;
  },
};
