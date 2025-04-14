import React, { useEffect, useState } from "react";
import axios from "axios";
import { API_BASE_URL } from "../../services/api";

function Achievements() {
  const [achievements, setAchievements] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`${API_BASE_URL}achievement/`)
      .then((response) => {
        setAchievements(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Ошибка при загрузке достижений:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Загрузка достижений...</p>;

  return (
    <div className="container my-4">
      <h2>Достижения</h2>
      <div className="row">
        {achievements.map((ach) => (
          <div key={ach.id} className="col-md-4 mb-3">
            <div className="card h-100 shadow-sm">
              {ach.icon_url ? (
                <img 
                  src={ach.icon_url} 
                  className="card-img-top" 
                  alt={ach.name} 
                  style={{ objectFit: 'cover', height: '150px' }} 
                />
              ) : (
                <div className="card-img-top bg-secondary d-flex align-items-center justify-content-center" style={{ height: '150px' }}>
                  <span className="text-white">Нет изображения</span>
                </div>
              )}
              <div className="card-body">
                <h5 className="card-title">{ach.name}</h5>
                <p className="card-text">{ach.description}</p>
                <p className="card-text">
                  <small className="text-muted">Требуется: {ach.points_required} очков</small>
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Achievements;
