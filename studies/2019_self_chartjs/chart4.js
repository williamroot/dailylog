// -- THE DATA --

fetch('data/waste.csv')
  .then(response => response.text())
  .then((data) => {
    const labels = [],
          values = [];
    const rows = data.split("\n")
    rows.forEach(r => {
      const item = r.split(",");
      labels.push(item[0]);
      values.push(+item[1]);
    });
    labels.shift();
    values.shift();
    draw(labels, values);
});

// -- THE CHART --

function draw(labels, values) {
  const canvas = document.getElementById("bar-chart");
  const ctx = canvas.getContext("2d");
  new Chart(ctx, {
    type: "horizontalBar", // Here we changed for horizontal bar
    data: {
      labels: labels,
      datasets: [
        {
          label: "Tonnes of plastic",
          data: values,
          borderWidth: 2,
          backgroundColor: "hsla(20,100%,80%,0.8)",
          borderColor: "hsla(0,100%,50%,1)"
        }
      ]
    },
    options: {
      maintainAspectRatio: false,
      title: {
        display: true,
        text: 'Tonnes of plastic waste',
        fontSize: 16
      },
      legend: {
        display: false
      }
    }
  });
}
