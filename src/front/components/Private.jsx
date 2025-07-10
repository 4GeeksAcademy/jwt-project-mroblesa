import React from 'react';
import { useNavigate } from 'react-router-dom';

const Private = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    sessionStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8">
          <div className="card shadow">
            <div className="card-header bg-primary text-white">
              <h2 className="card-title mb-0">Área Privada</h2>
            </div>
            
            <div className="card-body">
              <div className="text-center mb-4">
                <div className="bg-success text-white p-3 rounded-circle d-inline-block mb-3">
                  <i className="bi bi-shield-lock-fill" style={{ fontSize: '3rem' }}></i>
                </div>
                <p className="lead">¡Bienvenido! Esta es una página protegida.</p>
              </div>
              
              <div className="d-grid">
                <button 
                  onClick={handleLogout} 
                  className="btn btn-danger btn-lg"
                >
                  <i className="bi bi-box-arrow-left me-2"></i>
                  Cerrar Sesión
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Private;