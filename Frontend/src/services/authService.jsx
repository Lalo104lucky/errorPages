import axios from "axios";

const REFRESH_URL = "http://127.0.0.1:8000/users/token/refresh/";
//URL de inicio de sesión (JWT)
const API_URL = "http://127.0.0.1:8000/users/token/"

export const login = async (email, password) => {
    const response = await axios.post(API_URL, {email,password});
    if(response.data.access){
        //Guardar el token en React
        localStorage.setItem("accessToken",response.data.access);
        localStorage.setItem("refreshToken",response.data.refresh);
    }
    return response.data;
}

export const refreshAccessToken = async () => {
    const refreshToken = localStorage.getItem("refreshToken");
    if (!refreshToken) {
      console.error("No hay refreshToken disponible.");
      return null;
    }
  
    try {
      const response = await axios.post(REFRESH_URL, { refresh: refreshToken });
      if (response.data.access) {
        localStorage.setItem("accessToken", response.data.access);
        return response.data.access;
      }
    } catch (error) {
      console.error("Error al renovar el accessToken:", error);
      logout();
    }
    return null;
  };


export const logout = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    window.location.reload(); // Recargar para actualizar estado
}