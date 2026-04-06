import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ConfigProvider } from 'antd';
import viVN from 'antd/locale/vi_VN';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

import MainLayout from './layouts/MainLayout';
import LoginPage from './modules/login/LoginPage';
import DashboardPage from './modules/dashboard/DashboardPage';
import DanhMucPage from './modules/danh-muc/DanhMucPage';
import DuDauKyPage from './modules/du-dau-ky/DuDauKyPage';
import TienMatPage from './modules/tien-mat/TienMatPage';
import NganHangPage from './modules/ngan-hang/NganHangPage';
import MuaHangPage from './modules/mua-hang/MuaHangPage';
import BanHangPage from './modules/ban-hang/BanHangPage';
import HoaDonPage from './modules/hoa-don/HoaDonPage';
import KhoPage from './modules/kho/KhoPage';
import CCDCPage from './modules/ccdc/CCDCPage';
import TaiSanPage from './modules/tai-san/TaiSanPage';
import TienLuongPage from './modules/tien-luong/TienLuongPage';
import ThuePage from './modules/thue/ThuePage';
import GiaThanhPage from './modules/gia-thanh/GiaThanhPage';
import TongHopPage from './modules/tong-hop/TongHopPage';
import BaoCaoPage from './modules/bao-cao/BaoCaoPage';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: { staleTime: 5 * 60 * 1000, retry: 1 },
  },
});

const theme = {
  token: {
    colorPrimary: '#1565C0',
    borderRadius: 6,
    fontFamily: "'Segoe UI', 'Inter', -apple-system, sans-serif",
  },
};

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const token = localStorage.getItem('token');
  if (!token) {
    return <Navigate to="/login" replace />;
  }
  return <>{children}</>;
}

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ConfigProvider theme={theme} locale={viVN}>
        <BrowserRouter>
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/" element={<ProtectedRoute><MainLayout /></ProtectedRoute>}>
              <Route index element={<Navigate to="/dashboard" replace />} />
              <Route path="dashboard" element={<DashboardPage />} />
              <Route path="danh-muc/*" element={<DanhMucPage />} />
              <Route path="du-dau-ky" element={<DuDauKyPage />} />
              <Route path="tien-mat" element={<TienMatPage />} />
              <Route path="ngan-hang" element={<NganHangPage />} />
              <Route path="mua-hang" element={<MuaHangPage />} />
              <Route path="ban-hang" element={<BanHangPage />} />
              <Route path="hoa-don" element={<HoaDonPage />} />
              <Route path="kho" element={<KhoPage />} />
              <Route path="ccdc" element={<CCDCPage />} />
              <Route path="tai-san" element={<TaiSanPage />} />
              <Route path="tien-luong" element={<TienLuongPage />} />
              <Route path="thue" element={<ThuePage />} />
              <Route path="gia-thanh" element={<GiaThanhPage />} />
              <Route path="tong-hop" element={<TongHopPage />} />
              <Route path="bao-cao" element={<BaoCaoPage />} />
            </Route>
          </Routes>
        </BrowserRouter>
      </ConfigProvider>
    </QueryClientProvider>
  );
}
