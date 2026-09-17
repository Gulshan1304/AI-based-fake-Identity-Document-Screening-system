/* =========================
   RUN AI SCREENING
   ========================= */

const screenButton = document.querySelector(".screen-btn");

if (screenButton) {

    screenButton.addEventListener("click", async function () {

        const file = documentUpload?.files[0];

        if (!file) {
            alert("Please upload an identity document first.");
            return;
        }

        screenButton.disabled = true;
        screenButton.textContent = "Uploading...";

        try {

            // Create form data
            const formData = new FormData();

            formData.append("file", file);


            // Send document to FastAPI
            const response = await fetch(
                "http://127.0.0.1:8000/api/screening/",
                {
                    method: "POST",
                    body: formData
                }
            );


            // Check API response
            if (!response.ok) {
                throw new Error(
                    `Server error: ${response.status}`
                );
            }


            const result = await response.json();

            console.log("Screening Result:", result);


            // Button update
            screenButton.textContent =
                "Screening Completed";

            screenButton.style.background =
                "#198754";


            // Update screening statuses

            const pendingItems =
                document.querySelectorAll(".pending");


            pendingItems.forEach(function (item) {

                item.textContent = "Review Required";

                item.style.background = "#fff4d6";
                item.style.color = "#946d00";

            });


            // Update risk information

            const riskText =
                document.querySelector(".risk-score p");

            if (riskText) {

                riskText.textContent =
                    "Screening completed";

            }


            console.log(
                "Screening ID:",
                result.screening_id
            );


            alert(
                "Document successfully sent to the AI screening backend."
            );


        } catch (error) {

            console.error(
                "Screening Error:",
                error
            );


            screenButton.disabled = false;

            screenButton.textContent =
                "Run AI Screening";


            alert(
                "Unable to connect to the screening backend."
            );

        }

    });

}
/* =========================
   CONNECT FRONTEND TO BACKEND
   ========================= */

const screenButton = document.querySelector(".screen-btn");
const documentUpload = document.querySelector("#documentUpload");

if (screenButton) {

    screenButton.addEventListener("click", async function () {

        // Check file
        const file = documentUpload?.files[0];

        if (!file) {
            alert("Please upload an identity document first.");
            return;
        }

        // Button loading state
        screenButton.disabled = true;
        screenButton.textContent = "Uploading...";

        try {

            // Create FormData
            const formData = new FormData();

            formData.append("file", file);

            // Send file to FastAPI backend
            const response = await fetch(
                "http://127.0.0.1:8000/api/screening/",
                {
                    method: "POST",
                    body: formData
                }
            );

            // Check response
            if (!response.ok) {
                throw new Error(
                    `Server error: ${response.status}`
                );
            }

            // Convert response to JSON
            const result = await response.json();

            console.log("Screening Result:", result);

            // Update button
            screenButton.textContent = "Screening Completed";
            screenButton.style.background = "#198754";

            // Update pending statuses
            const pendingItems =
                document.querySelectorAll(".pending");

            pendingItems.forEach(function (item) {

                item.textContent = "Review Required";

                item.style.background = "#fff4d6";
                item.style.color = "#946d00";

            });

            // Update risk information
            const riskText =
                document.querySelector(".risk-score p");

            if (riskText) {
                riskText.textContent =
                    "Screening completed";
            }

            // Show screening ID in console
            console.log(
                "Screening ID:",
                result.screening_id
            );

            alert(
                "Document successfully sent to the AI screening backend."
            );

        } catch (error) {

            console.error(
                "Screening Error:",
                error
            );

            screenButton.disabled = false;
            screenButton.textContent =
                "Run AI Screening";

            alert(
                "Unable to connect to the screening backend."
            );
        }
    });
}