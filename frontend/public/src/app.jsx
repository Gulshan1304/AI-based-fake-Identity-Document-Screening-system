import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import UploadBox from "./components/UploadBox";
import VerificationResult from "./components/VerificationResult";
import RiskScore from "./components/RiskScore";
import StatusBadge from "./components/StatusBadge";
import { useState } from "react";

function App() {
  const [activePage, setActivePage] = useState("Home");

  const menu = [
    "Dashboard",
    "New Screening",
    "Document History",
    "Alerts",
    "Watchlist",
    "System Settings"
  ];

  return (
    <div className="app">

      {/* SIDEBAR */}
      <aside className="sidebar">

        <div className="brand">
          <div className="brand-icon">AI</div>

          <div>
            <h2>IdentityGuard</h2>
            <span>AI Screening Platform</span>
          </div>
        </div>

        <div className="menu-title">
          MAIN MENU
        </div>

        <button
          className={`menu-item ${activePage === "Home" ? "active" : ""}`}
          onClick={() => setActivePage("Home")}
        >
          <span>⌂</span>
          Home
        </button>

        {menu.map((item) => (
          <button
            key={item}
            className={`menu-item ${
              activePage === item ? "active" : ""
            }`}
            onClick={() => setActivePage(item)}
          >
            <span>
              {item === "Dashboard" && "▦"}
              {item === "New Screening" && "＋"}
              {item === "Document History" && "▤"}
              {item === "Alerts" && "◉"}
              {item === "Watchlist" && "◈"}
              {item === "System Settings" && "⚙"}
            </span>

            {item}
          </button>
        ))}

        <div className="sidebar-bottom">
          <div className="secure-box">
            <span>●</span>
            <div>
              <strong>System Secure</strong>
              <small>Monitoring active</small>
            </div>
          </div>

          <div className="user-card">
            <div className="avatar">GR</div>
            <div>
              <strong>Gulshan Rahangdale</strong>
              <small>Administrator</small>
            </div>
          </div>
        </div>

      </aside>

      {/* MAIN */}
      <main className="main">

        <header className="topbar">

          <div>
            <span className="breadcrumb">
              IdentityGuard / {activePage}
            </span>
          </div>

          <div className="top-actions">
            <button className="notification">
              🔔
              <span>3</span>
            </button>

            <button className="admin-button">
              Admin Panel →
            </button>
          </div>

        </header>

        {activePage === "Home" && <Home />}

        {activePage !== "Home" && (
          <PlaceholderPage title={activePage} />
        )}

      </main>
    </div>
  );
}


/* ================= HOME ================= */

function Home() {

  const [file, setFile] = useState(null);
  const [screening, setScreening] = useState(false);

  function handleFile(event) {
    const selectedFile = event.target.files[0];

    if (selectedFile) {
      setFile(selectedFile);
    }
  }

  function startScreening() {
    if (!file) return;

    setScreening(true);

    setTimeout(() => {
      setScreening(false);
      alert(
        "Screening completed. This prototype provides AI-assisted indicators for human review."
      );
    }, 1800);
  }

  return (
    <div className="home">

      {/* HERO */}

      <section className="hero">

        <div className="hero-content">

          <div className="status">
            <span></span>
            AI-ASSISTED IDENTITY VERIFICATION
          </div>

          <h1>
            AI-Based Identity &
            <br />
            <strong>Document Screening System</strong>
          </h1>

          <p>
            A secure AI-assisted platform for analyzing identity
            documents, detecting potential inconsistencies, and
            supporting authorized officers during verification.
          </p>

          <div className="hero-buttons">
            <button
              className="primary-button"
              onClick={() =>
                document.getElementById("upload").scrollIntoView({
                  behavior: "smooth"
                })
              }
            >
              Start Screening →
            </button>

            <button
              className="secondary-button"
              onClick={() =>
                document.getElementById("about").scrollIntoView({
                  behavior: "smooth"
                })
              }
            >
              Learn More
            </button>
          </div>

        </div>

        <div className="hero-card">

          <div className="scanner-line"></div>

          <div className="document-icon">
            ▣
          </div>

          <h3>Intelligent Screening</h3>

          <p>
            OCR · Face Verification · Tamper Analysis
          </p>

          <div className="verification-status">
            <span>●</span>
            Screening Engine Ready
          </div>

        </div>

      </section>


      {/* UPLOAD */}

      <section className="upload-section" id="upload">

        <div className="section-heading">

          <span className="eyebrow">
            NEW SCREENING
          </span>

          <h2>
            Upload & Verify
          </h2>

          <p>
            Upload a supported identity document for AI-assisted
            screening.
          </p>

        </div>

        <div className="upload-layout">

          <div className="upload-box">

            <input
              id="document-upload"
              type="file"
              accept=".jpg,.jpeg,.png,.pdf"
              hidden
              onChange={handleFile}
            />

            <label htmlFor="document-upload" className="upload-label">

              <div className="upload-icon">
                ↑
              </div>

              <h3>
                {file ? file.name : "Upload Identity Document"}
              </h3>

              <p>
                PDF, JPG, JPEG or PNG
              </p>

              <span>
                Maximum file size: 10 MB
              </span>

            </label>

            {file && (
              <button
                className="primary-button verify-button"
                onClick={startScreening}
                disabled={screening}
              >
                {screening
                  ? "AI ANALYZING..."
                  : "Analyze Document →"}
              </button>
            )}

          </div>


          {/* CHECKLIST */}

          <div className="verification-card">

            <h3>AI Screening Checks</h3>

            <Check text="Document Authentication" />
            <Check text="Tampering Detection" />
            <Check text="Face Match" />
            <Check text="Expiry Validation" />
            <Check text="Blacklist / Watchlist Screening" />
            <Check text="Data Consistency Analysis" />
            <Check text="Anomaly Detection" />

          </div>

        </div>

      </section>


      {/* BENEFITS */}

      <section className="benefits">

        <div className="section-heading center">

          <span className="eyebrow">
            TRUST & SECURITY
          </span>

          <h2>
            Built for Secure Screening
          </h2>

        </div>

        <div className="benefit-grid">

          <Benefit
            icon="◉"
            title="AI-Assisted"
            text="Multiple analysis modules work together to identify potential document and identity inconsistencies."
          />

          <Benefit
            icon="⌁"
            title="Secure Processing"
            text="Designed around controlled access, audit logs, encryption and data minimization."
          />

          <Benefit
            icon="✓"
            title="Explainable Results"
            text="Screening results can include risk indicators and reason codes instead of unexplained decisions."
          />

          <Benefit
            icon="♢"
            title="Human Review"
            text="Potentially suspicious cases can be escalated to an authorized officer for final verification."
          />

        </div>

      </section>


      {/* FEATURES */}

      <section className="features">

        <div className="section-heading">

          <span className="eyebrow">
            PLATFORM FEATURES
          </span>

          <h2>
            Complete Screening Workspace
          </h2>

        </div>

        <div className="feature-grid">

          <Feature
            number="01"
            title="Document Screening"
            text="OCR, structure analysis, expiry checks and document consistency analysis."
          />

          <Feature
            number="02"
            title="Risk Score"
            text="Combines configurable screening indicators into a transparent risk assessment."
          />

          <Feature
            number="03"
            title="Document History"
            text="Maintain authorized records of previous screening activities and outcomes."
          />

          <Feature
            number="04"
            title="Alerts"
            text="Surface cases requiring additional attention or manual review."
          />

          <Feature
            number="05"
            title="Watchlist"
            text="Compare authorized screening data against applicable watchlist records."
          />

          <Feature
            number="06"
            title="Officer Review"
            text="Allow authorized officers to inspect evidence and record verification decisions."
          />

        </div>

      </section>


      {/* ABOUT */}

      <section className="about" id="about">

        <div className="about-text">

          <span className="eyebrow">
            ABOUT THE SYSTEM
          </span>

          <h2>
            Identity verification,
            <br />
            redesigned with AI.
          </h2>

          <p>
            IdentityGuard is a proposed AI-assisted screening platform
            designed to help authorized organizations analyze identity
            documents and identify potential inconsistencies.
          </p>

          <p>
            The system combines OCR, document analysis, face
            verification, tamper indicators, anomaly detection and
            configurable rules to generate explainable screening
            results.
          </p>

          <div className="important-note">
            <strong>Important</strong>
            <span>
              AI screening is an assistance layer. Final identity
              verification and official decisions remain with the
              authorized organization or officer.
            </span>
          </div>

        </div>

        <div className="about-card">

          <div className="system-row">
            <span>OCR Engine</span>
            <b>READY</b>
          </div>

          <div className="system-row">
            <span>Face Verification</span>
            <b>READY</b>
          </div>

          <div className="system-row">
            <span>Tamper Analysis</span>
            <b>READY</b>
          </div>

          <div className="system-row">
            <span>Anomaly Engine</span>
            <b>READY</b>
          </div>

          <div className="system-row">
            <span>Human Review</span>
            <b>ENABLED</b>
          </div>

        </div>

      </section>


      {/* ABOUT ME */}

      <section className="about-me">

        <div className="section-heading center">

          <span className="eyebrow">
            ABOUT ME
          </span>

          <h2>
            Project Developer
          </h2>

        </div>

        <div className="profile-card">

          <div className="profile-avatar">
            GR
          </div>

          <div>

            <h2>
              Gulshan Rahangdale
            </h2>

            <h3>
              B.Tech Artificial Intelligence & Machine Learning
            </h3>

            <p>
              AI/ML student and aspiring AI Engineer interested in
              Artificial Intelligence, Machine Learning, Deep Learning,
              Generative AI, Python, software development and
              AI-powered real-world applications.
            </p>

            <p>
              This project focuses on combining AI-assisted document
              analysis and identity verification into a structured
              screening workflow with explainable indicators and
              authorized human review.
            </p>

            <div className="profile-links">

              <a
                href="https://github.com/Gulshan1304"
                target="_blank"
                rel="noreferrer"
              >
                GitHub
              </a>

              <a
                href="https://www.linkedin.com/in/gulshan-rahangdale/"
                target="_blank"
                rel="noreferrer"
              >
                LinkedIn
              </a>

              <a
                href="https://www.instagram.com/gulshan_rahangdale_/"
                target="_blank"
                rel="noreferrer"
              >
                Instagram
              </a>

            </div>

          </div>

        </div>

      </section>


      {/* TECHNOLOGY */}

      <section className="technology">

        <div className="section-heading center">

          <span className="eyebrow">
            TECHNOLOGY STACK
          </span>

          <h2>
            System Architecture
          </h2>

        </div>

        <div className="tech-grid">

          <Tech title="Frontend">
            HTML · CSS · JavaScript · React.js
          </Tech>

          <Tech title="Backend">
            Python · FastAPI · REST API
          </Tech>

          <Tech title="AI / ML">
            OCR · Computer Vision · Face Verification
          </Tech>

          <Tech title="Detection">
            Tamper Detection · Anomaly Detection
          </Tech>

          <Tech title="Decision Layer">
            Rules · Risk Score · Reason Codes
          </Tech>

          <Tech title="Data">
            Database · Audit Logs · Screening History
          </Tech>

        </div>

      </section>


      {/* FOOTER */}

      <footer>

        <div>
          <strong>IdentityGuard</strong>
          <p>
            AI-Assisted Identity & Document Screening System
          </p>
        </div>

        <span>
          © 2026 Gulshan Rahangdale
        </span>

      </footer>

    </div>
  );
}


/* ================= COMPONENTS ================= */

function Check({ text }) {
  return (
    <div className="check">
      <span>✓</span>
      {text}
    </div>
  );
}


function Benefit({ icon, title, text }) {
  return (
    <div className="benefit-card">

      <div className="card-icon">
        {icon}
      </div>

      <h3>{title}</h3>

      <p>{text}</p>

    </div>
  );
}


function Feature({ number, title, text }) {
  return (
    <div className="feature-card">

      <span>{number}</span>

      <h3>{title}</h3>

      <p>{text}</p>

      <button>
        Explore →
      </button>

    </div>
  );
}


function Tech({ title, children }) {
  return (
    <div className="tech-card">

      <span>{title}</span>

      <h3>{children}</h3>

    </div>
  );
}


function PlaceholderPage({ title }) {

  return (
    <section className="placeholder">

      <span className="eyebrow">
        IDENTITYGUARD
      </span>

      <h1>{title}</h1>

      <p>
        This module is ready for backend/API integration.
      </p>

      <div className="coming-card">
        <div>◈</div>

        <h3>
          Module Interface
        </h3>

        <p>
          React frontend → FastAPI backend → AI screening
          services → database.
        </p>
      </div>

    </section>
  );
}

export default App;