import React from "react";

function StatusBadge({ status }) {

  const statusConfig = {

    VERIFIED: {
      label: "Verified",
      className: "status-verified",
      icon: "✓"
    },

    REVIEW_REQUIRED: {
      label: "Review Required",
      className: "status-review",
      icon: "!"
    },

    PENDING: {
      label: "Pending",
      className: "status-pending",
      icon: "○"
    },

    FAILED: {
      label: "Failed",
      className: "status-failed",
      icon: "×"
    },

    EXPIRED: {
      label: "Expired",
      className: "status-expired",
      icon: "!"
    }

  };

  const current =
    statusConfig[status] || statusConfig.PENDING;

  return (

    <span className={`status-badge ${current.className}`}>

      <span className="status-badge-icon">
        {current.icon}
      </span>

      {current.label}

    </span>

  );
}

export default StatusBadge;