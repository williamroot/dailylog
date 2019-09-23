// -- THE DATA --

fetch('data/waste2.csv')
  .then(response => response.text())
  .then((data) => {
    const labels = [],
          values2010 = []; // Create an empty array...
          values2025 = []; // ...for both datasets
    const rows = data.split("\n")
    rows.forEach(r => {
      const item = r.split(",");
      labels.push(item[0]);
      values2010.push(+item[1]/1000000); // Divide by 1 million to make it easier to read...
      values2025.push(+item[2]/1000000); // ...and again
    });
    labels.shift();
    values2010.shift();
    values2025.shift();
    draw(labels, [values2010, values2025]);
});

// -- THE CHART --

// Creating a chart from function called draw
function draw(labels, values) {
  const canvas = document.getElementById("bar-chart");
  const ctx = canvas.getContext("2d");
  new Chart(ctx, {
    type: "horizontalBar",
    data: {
      labels: labels,
      datasets: [ // We make a distinction between the two datasets
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
      }
    }
  });
}
