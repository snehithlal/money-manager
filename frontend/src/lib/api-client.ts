/**
 * API Client Configuration
 *
 * Axios instance configured for the FastAPI backend.
 * Automatically handles base URL and common headers.
 */

import axios from 'axios';
import { useAuthStore } from '@/stores/auth-store';

// Base URL for API requests
// In production (Vercel), use relative path so API calls go through the same domain
// In development, use localhost:8000
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL ||
  (typeof window !== 'undefined' && window.location.origin.includes('vercel.app')
    ? '' // Use relative path in production
    : 'http://localhost:8000');

// Create axios instance with default config
export const apiClient = axios.create({
  baseURL: `${API_BASE_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
  },
  // timeout: 10000, // 10 seconds - Removed as per instruction
});

// Add a request interceptor to inject the token
apiClient.interceptors.request.use(
  (config) => {
    const token = useAuthStore.getState().token;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor (for error handling)
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle 401 Unauthorized globally if needed (e.g., logout)
    // Handle 401 Unauthorized globally
    if (error.response?.status === 401) {
      useAuthStore.getState().logout();
      // Force hard redirect to login to clear any stale state and prevent loops
      if (typeof window !== 'undefined') {
        localStorage.removeItem('auth-storage'); // Explicitly clear storage
        if (!window.location.pathname.includes('/login')) {
          window.location.href = '/login';
        }
      }
    }
    return Promise.reject(error);
  }
);

export default apiClient;
