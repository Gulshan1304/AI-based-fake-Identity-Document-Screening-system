
import React from "react";

function Sidebar({ activePage, setActivePage }) {

  const menuItems = [
    {
      name: "Dashboard",
      icon: "▦"
    },
    {
      name: "New Screening",
      icon: "＋"
    },
    {
      name: "Document History",
      icon: "▤"
    },
    {
      name: "Alerts",
      icon: "◉"
    },
    {
      name: "Watchlist",
      icon: "◈"
    },
    {
      name: "System Settings",
      icon: "⚙"
    }
  ];

  return (
    <aside className="sidebar">

      {/* LOGO */}

      <div className="sidebar-brand">

        <div className="brand-logo">
          AI
        </div>

        <div>
          <h2>IdentityGuard</h2>
          <p>AI Screening Platform</p>
        </div>

      </div>


      {/* MENU */}

      <div className="sidebar-section-title">
        MAIN MENU
      </div>

      <button
        className={`sidebar-item ${
          activePage === "Home" ? "active" : ""
        }`}
        onClick={() => setActivePage("Home")}
      >
        <span>⌂</span>
        Home
      </button>


      {menuItems.map((item) => (

        <button
          key={item.name}
          className={`sidebar-item ${
            activePage === item.name ? "active" : ""
          }`}
          onClick={() => setActivePage(item.name)}
        >

          <span>{item.icon}</span>

          {item.name}

        </button>

      ))}


      {/* SECURITY STATUS */}

      <div className="sidebar-bottom">

        <div className="security-status">

          <div className="security-icon">
            ✓
          </div>

          <div>
            <strong>System Secure</strong>
            <small>Monitoring active</small>
          </div>

        </div>


        {/* USER */}

        <div className="sidebar-user">

          <div className="user-avatar">
            GR
          </div>

          <div>
            <strong>Gulshan Rahangdale</strong>
            <small>Administrator</small>
          </div>

        </div>

      </div>

    </aside>
  );
}

export default Sidebar;