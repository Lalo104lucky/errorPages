import React, { useState, useEffect } from "react";
import axiosInstance from "../services/axiosInstance";
import { motion } from "framer-motion";
import { useNavigate, useParams } from "react-router-dom";
import Swal from "sweetalert2";

const UpdateUserForm = () => {
  const navigate = useNavigate();
  const { id } = useParams(); // Obtén el ID del usuario desde la URL
  const [loading, setLoading] = useState(true);
  const [formFields, setFormFields] = useState([]);
  const [formData, setFormData] = useState({
    email: "",
    name: "",
    surname: "",
    control_number: "",
    age: "",
    tel: "",
  });
  const [errors, setErrors] = useState({});

  // Cargar los datos del usuario y los campos del formulario
  useEffect(() => {
    // Obtener los datos del formulario desde el backend
    axiosInstance
      .get("http://127.0.0.1:8000/users/form/")
      .then((response) => {
        setFormFields(response.data);
      })
      .catch((error) => {
        console.error("Error al obtener los datos del formulario:", error);
        Swal.fire("Error", "No se pudieron cargar los campos del formulario.", "error");
      });

    // Obtener los datos del usuario por ID
    axiosInstance
      .get(`http://127.0.0.1:8000/users/api/${id}/`)
      .then((response) => {
        setFormData(response.data); // Cargar los datos del usuario en el formulario
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos del usuario:", error);
        Swal.fire("Error", "No se pudieron cargar los datos del usuario.", "error");
        setLoading(false);
      });
  }, [id]);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setLoading(true);
    const token = localStorage.getItem("accessToken");

    axiosInstance
      .put(`http://127.0.0.1:8000/users/api/${id}/`, formData, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then((response) => {
        Swal.fire("Actualizado", "El usuario ha sido actualizado con éxito.", "success");
        setErrors({});
        setLoading(false);
        setTimeout(() => navigate("/"), 500); // Redirige a la lista de usuarios
      })
      .catch((error) => {
        if (error.response && error.response.data) {
          setErrors(error.response.data); // Guardar errores en el estado
          Swal.fire("Error", "Hubo errores al actualizar el usuario. Revisa los campos.", "error");
        } else {
          Swal.fire("Error", "Ocurrió un error inesperado, contacta al administrador.", "error");
        }
        console.error("Error al actualizar el usuario:", error);
        setLoading(false);
        window.scrollTo(0, 0);
      });
  };

  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center vh-100">
        <div
          className="spinner-border text-primary"
          style={{ width: "5rem", height: "5rem" }}
          role="status"
        >
          <span className="visually-hidden">Cargando...</span>
        </div>
      </div>
    );
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0, transition: { duration: 0.5 } }}
      exit={{ opacity: 0, y: -50, transition: { duration: 0.5 } }}
      className="page"
    >
      <div>
        <h1>Actualizar Usuario</h1>
        <form onSubmit={handleSubmit}>
          {formFields &&
            Object.keys(formFields).map((field) => {
              const { label, input, type } = formFields[field];
              return (
                <div key={field}>
                  <label htmlFor={input.id}>{label}</label>
                  <input
                    {...input}
                    value={formData[field] || ""}
                    onChange={handleInputChange}
                    name={field}
                    type={type || "text"}
                  />
                  {errors[field] && (
                    <span autoFocus className="text-danger">
                      {errors[field].map((errorMsg, index) => (
                        <span key={index}>
                          <i className="bi bi-exclamation-circle-fill me-1"></i>
                          {errorMsg}
                        </span>
                      ))}
                    </span>
                  )}
                  <br />
                </div>
              );
            })}
          <button type="submit">Actualizar</button>
        </form>
      </div>
    </motion.div>
  );
};

export default UpdateUserForm;