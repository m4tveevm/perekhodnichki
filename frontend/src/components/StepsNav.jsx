import React from "react";
import { NavLink } from "react-router-dom";

function StepsNav({ currentStep }) {
  const steps = [
    { step: 1, title: "Регистрация участника", path: "/register" },
    { step: 2, title: "Настройка профиля", path: "/profile" },
    { step: 3, title: "Выбор экспозиции музея", path: "/exhibits" },
    { step: 4, title: "Начало интерактивного квеста", path: "/quest/start" },
    { step: 5, title: "Разгадывание загадок", path: "/quest/puzzles" },
    { step: 6, title: "Получение достижений", path: "/achievements" },
    { step: 7, title: "Лидерборд участников", path: "/leaderboard" },
    { step: 8, title: "Экскурсии и мероприятия", path: "/events" },
    { step: 9, title: "Интерактивная карта", path: "/map" },
    { step: 10, title: "Обратная связь и бонусы", path: "/feedback" },
  ];

  return (
    <div className="steps-nav">
      <div className="d-none d-md-flex">
        {steps.map((s) => (
          <NavLink
            key={s.step}
            to={s.path}
            className={`step-item ${currentStep === s.step ? "active" : ""}`}
          >
            {s.step}
          </NavLink>
        ))}
      </div>

      <div className="d-flex d-md-none flex-column align-items-center">
        <div className="mb-2">
          <strong>
            Шаг {currentStep} из {steps.length}
          </strong>
          : {steps.find((s) => s.step === currentStep)?.title}
        </div>
        <div className="progress" style={{ width: "100%" }}>
          <div
            className="progress-bar"
            role="progressbar"
            style={{ width: `${(currentStep / steps.length) * 100}%` }}
            aria-valuenow={currentStep}
            aria-valuemin="0"
            aria-valuemax={steps.length}
          ></div>
        </div>
      </div>
    </div>
  );
}

export default StepsNav;
