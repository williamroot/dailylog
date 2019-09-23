// -- THE DATA --

fetch('data/waste2.csv')
  .then(response => response.text())
  .then((data) => {
    const labels = [],
          values2010 = [];
          values2025 = [];
    const rows = data.split("\n")
    rows.forEach(r => {
      const item = r.split(",");
      labels.push(item[0]);
      values2010.push(+item[1]/1000000);
      values2025.push(+item[2]/1000000);
    });
    labels.shift();
    values2010.shift();
    values2025.shift();
    draw(labels, [values2010, values2025]);
});

// -- THE CHART --

function draw(labels, values) {
  const canvas = document.getElementById("bar-chart");
  const ctx = canvas.getContext("2d");
  new Chart(ctx, {
    type: "horizontalBar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "2010",
          data: values[0],
          backgroundColor: "hsla(20,100%,50%,0.7)",
        }, {
          label: "2025",
          data: values[1],
          backgroundColor: "hsla(260,100%,50%,0.7)",
        }
      ]
    },
    options: {
      maintainAspectRatio: false,
      title: {
        display: true,
        text: 'Millions of tonnes of plastic waste',
        fontSize: 16
      },
      scales: {
        yAxes: [{
          barPercentage: 1, // The thickness of each bar
          categoryPercentage: .75 // The proportion the pair of bars takes from the space dedicated to each category
        }]
      }
    }
  });
}
