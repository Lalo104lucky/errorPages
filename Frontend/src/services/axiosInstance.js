import axios from "axios";
import { refreshAccessToken, logout } from "./authService";

const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000/", 
});

axiosInstance.interceptors.request.use(
  async (config) => {
    const token = localStorage.getItem("accessToken");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const newAccessToken = await refreshAccessToken();
      if (newAccessToken) {
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
        return axiosInstance(originalRequest); 
      }
    }

    if (error.response && error.response.status === 401) {
      logout();
    }

    return Promise.reject(error);
  }
);

export default axiosInstance;