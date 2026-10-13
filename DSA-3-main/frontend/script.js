async function searchPatent() {

    const input = document
        .getElementById("searchInput")
        .value
        .trim();

    const results = document.getElementById("searchResults");

    if (!input) {
        results.innerHTML =
            '<div class="result-card"><p>Please enter a keyword.</p></div>';
        return;
    }

    results.innerHTML =
        '<div class="result-card"><p>Searching database...</p></div>';

    try {
        const response = await fetch(
            `http://127.0.0.1:8000/api/search?keyword=${encodeURIComponent(input)}`
        );

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data = await response.json();

        if (data.count === 0) {
            results.innerHTML =
                '<div class="result-card"><p>No matching patents found.</p></div>';
            return;
        }

        results.innerHTML = data.results.map(patent => `
            <div class="result-card">
                <h3>${patent.patent_id} — ${patent.title}</h3>
                <p><strong>Technology:</strong> ${patent.technology}</p>
                <p><strong>Year:</strong> ${patent.year}</p>
                <p><strong>Abstract:</strong> ${patent.abstract}</p>
                <p><strong>Claims:</strong> ${patent.claims}</p>
            </div>
        `).join("");

    } catch (error) {
        results.innerHTML =
            '<div class="result-card"><p>Unable to connect to the backend.</p></div>';

        console.error(error);
    }
}

document
    .getElementById("searchInput")
    .addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            searchPatent();
        }
    });
async function loadAnalytics() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/stats");
        const data = await response.json();

        document.getElementById("totalPatents").textContent =
            data.total_patents;

        const techContainer = document.getElementById("technologyStats");

        techContainer.innerHTML = data.technologies.map(item => `
            <div class="stat-item">
                <strong>${item.technology}</strong>
                <span>${item.count} patents</span>
            </div>
        `).join("");

    } catch (error) {
        console.error("Analytics error:", error);
    }
}

window.addEventListener('DOMContentLoaded', loadAnalytics);
