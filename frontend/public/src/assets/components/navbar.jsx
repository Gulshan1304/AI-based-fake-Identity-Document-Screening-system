import React from "react";

function Navbar({ onAdminClick }) {
  return (
    <header className="navbar">

      <div className="navbar-left">
        <button className="mobile-menu">
          ☰
        </button>

        <div className="page-title">
          <span>IdentityGuard</span>
          <small>/ AI Screening Platform</small>
        </div>
      </div>

      <div className="navbar-right">

        <button className="notification-btn">
          🔔
          <span className="notification-count">3</span>
        </button>

        <button
          className="admin-btn"
          onClick={onAdminClick}
        >
          Admin Panel
          <span>→</span>
        </button>

        <div className="navbar-profile">
          <div className="profile-avatar">
            GR
          </div>

          <div className="profile-info">
            <strong>Gulshan Rahangdale</strong>
            <small>Administrator</small>
          </div>
        </div>

      </div>

    </header>
  );
}

export default Navbar;