fetch("https://delivery-analytics-dashboard.onrender.com/analytics/summary")
  .then((response) => {
    if (!response.ok) {
      throw new Error("API error: ${response.status}");
    }
    return response.json();
  })
  .then((data) => {
    document.getElementById("dashboard-error").textContent = "";
    document.getElementById("total-order-value").textContent =
      data.total_orders;
    document.getElementById("total-revenue-value").textContent =
      "₹" + Number(data.total_revenue).toLocaleString("en-IN");
    document.getElementById("avg-delivery-value").textContent =
      data.average_delivery_time.toFixed(2) + "min";
  })
  .catch((error) => {
    console.log("DashBoard-error:", error);
    document.getElementById("dashboard-error").textContent =
      "Unable to load data. Please check the server and refresh the page";
  });

fetch(
  "https://delivery-analytics-dashboard.onrender.com/analytics/status",
).then((response) =>
  response.json().then((data) => {
    const labels = data.map((item) => item.status);
    const values = data.map((item) => item.total_orders);

    new Chart(document.getElementById("status-chart"), {
      type: "doughnut",
      data: { labels: labels, datasets: [{ data: values }] },
    });
  }),
);

fetch(
  "https://delivery-analytics-dashboard.onrender.com/analytics/cities",
).then((response) =>
  response.json().then((data) => {
    const labels = data.map((item) => item.city);
    const values = data.map((item) => item.total_orders);
    new Chart(document.getElementById("city-chart"), {
      type: "bar",
      data: {
        labels: labels,
        datasets: [{ label: "total-order", data: values }],
      },
    });
  }),
);

fetch(
  "https://delivery-analytics-dashboard.onrender.com/analytics/city-revenue",
)
  .then((response) => response.json())
  .then((data) => {
    const labels = data.map((item) => item.city);
    const values = data.map((item) => item.total_revenue);

    new Chart(document.getElementById("revenue-city-chart"), {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Total Revenue",
            data: values,
          },
        ],
      },
    });
  });

fetch("https://delivery-analytics-dashboard.onrender.com/analytics/agents")
  .then((response) => response.json())
  .then((data) => {
    const labels = data.map((item) => item.name);
    const values = data.map((item) => item.total_orders);

    new Chart(document.getElementById("agent-chart"), {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Total Orders",
            data: values,
          },
        ],
      },
    });
  });

fetch(
  "https://delivery-analytics-dashboard.onrender.com/analytics/monthly-revenue",
)
  .then((response) => response.json())
  .then((data) => {
    const labels = data.map((item) => item.month);
    const values = data.map((item) => item.total_revenue);

    new Chart(document.getElementById("monthly-revenue-chart"), {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Monthly Revenue",
            data: values,
            tension: 0.3,
          },
        ],
      },
      options: {
        // responsive: true,
        maintainAspectRatio: false,
      },
    });
  });
