import React from "react";
import StatusBadge from "./StatusBadge";

function VerificationResult({
  result = {}
}) {

  const checks = [

    {
      key: "document_authentication",
      title: "Document Authentication",
      description:
        "Document structure and authenticity indicators"
    },

    {
      key: "tamper_detection",
      title: "Tampering Detection",
      description:
        "Checks for potential document alteration indicators"
    },

    {
      key: "face_verification",
      title: "Face Match",
      description:
        "Compares the document photo with the supplied face image"
    },

    {
      key: "expiry_validation",
      title: "Expiry Validation",
      description:
        "Checks document validity information"
    },

    {
      key: "watchlist_screening",
      title: "Watchlist Screening",
      description:
        "Checks authorized watchlist screening results"
    },

    {
      key: "anomaly_detection",
      title: "Anomaly Detection",
      description:
        "Identifies unusual or inconsistent information"
    }

  ];


  return (

    <div className="verification-result">

      <div className="verification-header">

        <div>

          <span className="component-label">
            AI ANALYSIS
          </span>

          <h2>
            Verification Results
          </h2>

        </div>

        <StatusBadge
          status={
            result.status || "PENDING"
          }
        />

      </div>


      <div className="verification-list">

        {checks.map((check) => {

          const status =
            result.checks?.[check.key] ||
            "PENDING";

          return (

            <div
              className="verification-row"
              key={check.key}
            >

              <div className="verification-check-icon">

                {status === "VERIFIED"
                  ? "✓"
                  : status === "FAILED"
                  ? "×"
                  : "○"}

              </div>


              <div className="verification-info">

                <strong>
                  {check.title}
                </strong>

                <p>
                  {check.description}
                </p>

              </div>


              <StatusBadge
                status={status}
              />

            </div>

          );

        })}

      </div>


      <div className="verification-footer">

        <span>
          AI-assisted screening
        </span>

        <span>
          Human review may be required
        </span>

      </div>

    </div>

  );
}

export default VerificationResult;