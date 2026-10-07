export function initSpendingChart() {

    const canvas = document.getElementById("spendingChart");

    if (!canvas) {
        return;
    }

    new Chart(canvas, {type: "line", data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"],

        datasets: [{label: "Spending",

                data: [1200, 1450, 1100, 1800, 1500, 2100, 1750, 1900, 1850],
                borderColor: "#6366f1",
                backgroundColor: "rgba(99, 102, 241, 0.15)",
                
                borderWidth: 3,

                fill: true,

                tension: 0.4,

                pointBackgroundColor: "#6366f1",
                pointBorderColor: "#ffffff",
                pointBorderWidth: 2,
                pointRadius: 4
            }
        ]
    },

        options: {responsive: true, maintainAspectRatio: false,
            plugins: {legend: {display: false}},

            scales: {x: {grid: {display: false}, ticks: {color: "#94a3b8"}},
                    y: {beginAtZero: true,grid: {color: "rgba(148, 163, 184, 0.15)"},
                    ticks: {color: "#94a3b8",
                            callback: function(value) {
                            return "$" + value;
                        }
                    }
                }
            }
        }
    });
}
