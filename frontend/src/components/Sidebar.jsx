import React, { useContext, useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";
import { getUserProfile } from "../services/api";

function Sidebar() {
  const { authState, logout } = useContext(AuthContext);
  const { isAuthenticated } = authState;

  const [user, setUser] = useState({
    username: "UserName",
    avatar: "",
  });
  const [loading, setLoading] = useState(true);
  const [showMobileSidebar, setShowMobileSidebar] = useState(false);

  useEffect(() => {
    if (isAuthenticated) {
      getUserProfile()
        .then((response) => {
          setUser(response.data);
          setLoading(false);
        })
        .catch((error) => {
          console.error("Ошибка при получении данных пользователя:", error);
          setLoading(false);
        });
    }
  }, [isAuthenticated]);

  const defaultAvatar =
    "https://cdn2.iconfinder.com/data/icons/squircle-ui/32/Avatar-512.png";

  const sidebarContent = (
    <>
      <NavLink
        to="/"
        className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none"
        onClick={() => setShowMobileSidebar(false)}
      >
        <span className="fs-4">Музей Геймификации ЛЭТИ</span>
      </NavLink>
      <hr />
      <ul className="nav nav-pills flex-column mb-auto">
        {isAuthenticated ? (
          <>
            <li className="nav-item">
              <NavLink
                to="/quest"
                className={({ isActive }) =>
                  "nav-link text-white" + (isActive ? " active" : "")
                }
                onClick={() => setShowMobileSidebar(false)}
              >
                <i className="fa-solid fa-gamepad"></i> Интерактивный квест
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                to="/exhibits"
                className={({ isActive }) =>
                  "nav-link text-white" + (isActive ? " active" : "")
                }
                onClick={() => setShowMobileSidebar(false)}
              >
                <i className="fa-solid fa-landmark"></i> Экспозиции музея
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                to="/virtual-tour"
                className={({ isActive }) =>
                  "nav-link text-white" + (isActive ? " active" : "")
                }
                onClick={() => setShowMobileSidebar(false)}
              >
                <i className="fa-solid fa-globe"></i> Виртуальный тур
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                to="/leaderboard"
                className={({ isActive }) =>
                  "nav-link text-white" + (isActive ? " active" : "")
                }
                onClick={() => setShowMobileSidebar(false)}
              >
                <i className="fa-solid fa-trophy"></i> Лидерборд участников
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                to="/achievements"
                className={({ isActive }) =>
                  "nav-link text-white" + (isActive ? " active" : "")
                }
                onClick={() => setShowMobileSidebar(false)}
              >
                <i className="fa-solid fa-award"></i> Достижения
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                to="/events"
                className={({ isActive }) =>
                  "nav-link text-white" + (isActive ? " active" : "")
                }
                onClick={() => setShowMobileSidebar(false)}
              >
                <i className="fa-solid fa-calendar"></i> Мероприятия
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                to="/map"
                className={({ isActive }) =>
                  "nav-link text-white" + (isActive ? " active" : "")
                }
                onClick={() => setShowMobileSidebar(false)}
              >
                <i className="fa-solid fa-map-marker-alt"></i> Интерактивная карта
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                to="/feedback"
                className={({ isActive }) =>
                  "nav-link text-white" + (isActive ? " active" : "")
                }
                onClick={() => setShowMobileSidebar(false)}
              >
                <i className="fa-solid fa-comments"></i> Обратная связь
              </NavLink>
            </li>
          </>
        ) : (
          <li className="nav-item">
            <NavLink
              to="/login"
              className={({ isActive }) =>
                "nav-link text-white" + (isActive ? " active" : "")
              }
              onClick={() => setShowMobileSidebar(false)}
            >
              <i className="fa-solid fa-right-to-bracket"></i> Войти
            </NavLink>
          </li>
        )}
      </ul>
      <hr />
      <div className="dropdown">
        {isAuthenticated ? (
          <>
            <button
              className="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
              id="dropdownUser1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style={{
                background: "none",
                border: "none",
                padding: 0,
                fontSize: "inherit",
                lineHeight: "inherit",
                cursor: "pointer",
              }}
            >
              <img
                src={user.avatar || defaultAvatar}
                alt="Avatar"
                className="rounded-circle me-2"
                style={{
                  width: "32px",
                  height: "32px",
                  border: "2px solid #fff",
                }}
              />
              <strong>{user.username || "Пользователь"}</strong>
            </button>
            <ul
              className="dropdown-menu dropdown-menu-dark text-small shadow"
              aria-labelledby="dropdownUser1"
            >
              <li>
                <NavLink
                  className="dropdown-item"
                  to="/profile"
                  onClick={() => setShowMobileSidebar(false)}
                >
                  <i className="fa-solid fa-user"></i> Профиль
                </NavLink>
              </li>
              <li>
                <NavLink
                  className="dropdown-item"
                  to="/settings"
                  onClick={() => setShowMobileSidebar(false)}
                >
                  <i className="fa-solid fa-gear"></i> Настройки
                </NavLink>
              </li>
              <li>
                <hr className="dropdown-divider" />
              </li>
              <li>
                <button
                  className="dropdown-item"
                  onClick={() => {
                    logout();
                    setShowMobileSidebar(false);
                  }}
                  style={{
                    border: "none",
                    background: "none",
                    padding: 0,
                    color: "inherit",
                  }}
                >
                  <i className="fa-solid fa-right-from-bracket"></i> Выйти
                </button>
              </li>
            </ul>
          </>
        ) : (
          <NavLink
            to="/login"
            className="d-flex align-items-center text-white text-decoration-none"
            onClick={() => setShowMobileSidebar(false)}
          >
            <img
              src={defaultAvatar}
              alt="Аватар"
              width="32"
              height="32"
              className="rounded-circle me-2"
            />
            <strong>Войти</strong>
          </NavLink>
        )}
      </div>
    </>
  );

  return (
    <>
      <button
        className="btn btn-dark d-lg-none m-2"
        onClick={() => setShowMobileSidebar(true)}
        style={{
          position: "fixed",
          top: "10px",
          left: "10px",
          zIndex: 1040,
        }}
      >
        <i className="fa-solid fa-bars"></i>
      </button>

      <div
        className="d-none d-lg-flex flex-column flex-shrink-0 p-3 text-white bg-dark sidebar"
        style={{
          width: "280px",
          height: "100vh",
          position: "fixed",
          left: 0,
          top: 0,
          overflowY: "auto",
        }}
      >
        {sidebarContent}
      </div>

      {showMobileSidebar && (
        <div
          className="mobile-sidebar-overlay"
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            backgroundColor: "#343a40",
            zIndex: 1050,
            display: "flex",
            flexDirection: "column",
            padding: "1rem",
            overflowY: "auto",
          }}
        >
          <button
            className="btn btn-dark align-self-end mb-3"
            onClick={() => setShowMobileSidebar(false)}
            style={{ fontSize: "1.5rem" }}
          >
            &times;
          </button>
          {sidebarContent}
        </div>
      )}
    </>
  );
}

export default Sidebar;
