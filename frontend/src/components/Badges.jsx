import React, { useState, useEffect } from "react";
import axios from "axios";
import { API_BASE_URL } from "../../services/api";

function Badges() {
  const [badges, setBadges] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`${API_BASE_URL}badge/`)
      .then((response) => {
        setBadges(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Ошибка при загрузке бейджей:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Загрузка бейджей...</p>;

  return (
    <div className="container my-4">
      <h2>Бейджи</h2>
      <div className="row">
        {badges.map((badge) => (
          <div key={badge.id} className="col-md-4 mb-3">
            <div className="card h-100 shadow-sm">
              {badge.image_url ? (
                <img 
                  src={badge.image_url} 
                  className="card-img-top" 
                  alt={badge.name} 
                  style={{ objectFit: 'cover', height: '150px' }} 
                />
              ) : (
                <div className="card-img-top bg-secondary d-flex align-items-center justify-content-center" style={{ height: '150px' }}>
                  <span className="text-white">Нет изображения</span>
                </div>
              )}
              <div className="card-body">
                <h5 className="card-title">{badge.name}</h5>
                <p className="card-text">{badge.description}</p>
                <p className="card-text">
                  <small className="text-muted">Редкость: {badge.rarity}</small>
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Badges;
