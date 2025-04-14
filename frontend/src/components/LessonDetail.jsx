import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { API_BASE_URL } from "../../services/api";

function LessonDetail() {
  const { pk } = useParams();
  const [lesson, setLesson] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`${API_BASE_URL}lessons/${pk}/`)
      .then((response) => {
        setLesson(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Ошибка загрузки урока:", error);
        setLoading(false);
      });
  }, [pk]);

  if (loading) return <p>Загрузка урока...</p>;
  if (!lesson) return <p>Урок не найден</p>;

  return (
    <div className="container my-4">
      <h2>{lesson.title}</h2>
      {lesson.content_url && (
        <img 
          src={lesson.content_url}
          alt={lesson.title}
          className="img-fluid rounded mb-3"
        />
      )}
      <p>{lesson.description}</p>
    </div>
  );
}

export default LessonDetail;
