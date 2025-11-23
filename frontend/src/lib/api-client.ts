/**
 * API Client Configuration
 *
 * Axios instance configured for the FastAPI backend.
 * Automatically handles base URL and common headers.
 */

import axios from 'axios';
import { useAuthStore } from '@/stores/auth-store';

// Base URL for API requests
// The API_BASE_URL constant is no longer used directly in apiClient creation
// as the baseURL is now hardcoded to include the API version.
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// Create axios instance with default config
export const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/v1', // Hardcoded baseURL including API version
  headers: {
    'Content-Type': 'application/json',
  },
  // timeout: 10000, // 10 seconds - Removed as per instruction
});

// Add a request interceptor to inject the token
apiClient.interceptors.request.use(
  (config) => {
    // }
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
    // Handle common errors
    if (error.response?.status === 401) {
      // Handle unauthorized (redirect to login when auth is implemented)
      console.error('Unauthorized access');
    }

    if (error.response?.status === 404) {
      console.error('Resource not found');
    }

    if (error.response?.status >= 500) {
      console.error('Server error');
    }

    return Promise.reject(error);
  }
);

export default apiClient;
