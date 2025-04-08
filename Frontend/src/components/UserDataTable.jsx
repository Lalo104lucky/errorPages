import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import { useNavigate } from "react-router-dom";
import axiosInstance from "../services/axiosInstance";
import Swal from "sweetalert2";
import jwt_decode from "jwt-decode";


const UserDataTable = () => {
  const [data, setData] = useState([]); // Datos para la tabla
  const [loading, setLoading] = useState(true); // Estado de carga
  const navigate = useNavigate();

  // Configuración de columnas
  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name, // Selector de datos
      sortable: true, // Habilitar ordenamiento
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-4"
            onClick={() => navigate(`/users/update/${row.id}`)}
          >
            <i className="bi bi-pencil"></i>
          </button>;
          <button
            className="btn btn-danger me-4"
            onClick={() => handleDelete(row.id)}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  // Obtener datos desde una API (puedes cambiar esta parte)
  useEffect(() => {
    axiosInstance
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  }, []);

  const handleDelete = (id) => {
    const token = localStorage.getItem("accessToken");
    const decodedToken = jwt_decode(token);
    console.log(decodedToken);
    const loggedInUserId = decodedToken.id;

    console.log("ID del usuario:", loggedInUserId);

    if (id === loggedInUserId) {
      Swal.fire("Error", "No puedes eliminar tu propia cuenta.", "error");
      return;
    }

    Swal.fire({
      title: "¿Estás seguro?",
      text: "No podrás revertir esta acción.",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#d33",
      cancelButtonColor: "#3085d6",
      confirmButtonText: "Sí, eliminar",
      cancelButtonText: "Cancelar",
    }).then((result) => {
      if (result.isConfirmed) {
        axiosInstance
          .delete(`http://127.0.0.1:8000/users/api/${id}/`, {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          })
          .then(() => {
            Swal.fire("Eliminado", "El usuario ha sido eliminado con éxito.", "success");
            setData(data.filter((user) => user.id !== id));
          })
          .catch((error) => {
            console.error("Error al eliminar el usuario:", error);
            Swal.fire("Error", "Ocurrió un error al intentar eliminar el usuario.", "error");
          });
      }
    });
  };

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
    </div>
  );
};

export default UserDataTable;
