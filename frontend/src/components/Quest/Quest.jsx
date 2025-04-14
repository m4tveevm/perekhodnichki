import React from "react";
import { useNavigate } from "react-router-dom";
import StepsNav from "../StepsNav";

function Quest() {
  const navigate = useNavigate();

  const handleStartQuest = () => {
    navigate("/quest/task");
  };

  return (
    <div className="container my-5">
      <StepsNav currentStep={4} />

      <div className="quest-content mt-4">
        <h1 className="mb-4 text-center">Первая Искра: Поиск Истинного Начала</h1>
        <div className="row align-items-center">
          <div className="col-md-6 mb-3 mb-md-0">

            <img
              src="https://storage.yandexcloud.net/updspace-s3/etu1.jpg"
              alt="Фасад первого корпуса ЛЭТИ"
              className="img-fluid rounded shadow"
            />
          </div>
          <div className="col-md-6">
            <p className="lead">
              Представьте, что вы стоите перед величественным фасадом первого корпуса ЛЭТИ – стража истории, который шепчет легенды минувших эпох.
              Перед вами развернулась интерактивная сцена: здание с утончённой лепниной, изысканными колоннами и резными наличниками, на которых,
              словно невидимой кистью времени, выложена тайна – дата открытия.
            </p>
            <h2 className="mt-4">Задание "Поиск Истинного Начала"</h2>
            <p>
              Вам предстоит стать настоящим исследователем прошлого. Лишь внимательный взгляд сможет распознать крошечные цифры, скрытые среди орнаментов,
              словно зашифрованное послание великих умов. Кликнув на угол, где время застыло в калейдоскопе узоров, вы откроете вспышку подсказок,
              мерцающих светом истории.
            </p>
            <p>
              Это не просто выбор правильной даты из предложенных вариантов — это волшебное путешествие в прошлое, способное открыть перед вами
              дверь к дальнейшим тайнам и открытиям.
            </p>
            <div className="d-grid gap-2 mt-4">
              <button
                className="btn btn-primary btn-lg"
                type="button"
                onClick={handleStartQuest}
              >
                Начать задание
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Quest;