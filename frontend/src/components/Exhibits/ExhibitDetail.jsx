import React from "react";
import { useParams } from "react-router-dom";

function ExhibitDetail() {
  const { id } = useParams();

  return (
    <div className="container my-4">
      <h1>Детали экспоната</h1>
      <p>
        Здесь будет отображаться подробная информация об экспонате с идентификатором <strong>{id}</strong>.
      </p>
      <p>Скоро появятся все данные.</p>
    </div>
  );
}

export default ExhibitDetail;
