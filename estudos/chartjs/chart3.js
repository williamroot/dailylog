// -- THE DATA --

// Parsing data from a csv file
fetch('data/waste.csv')
  .then(response => response.text()) // Get data as text within the variable response
  .then((data) => { // Create an empty variable called data
    const labels = [], // Create an empty array
          values = []; // Create an empty array
    const rows = data.split("\n") // Split the rows using newline
    rows.forEach(r => {
      const item = r.split(","); // Split each part of each row using comma
      labels.push(item[0]); // Append items to labels as string
      values.push(+item[1]); // Append items to values as numeric
    });
    labels.shift(); // Remove header
    values.shift(); // Remove header
    draw(labels, values); // Call the function draw with labels and values as args
});

// -- THE CHART --

// Creating a chart from function called draw
function draw(labels, values) {
  const canvas = document.getElementById("bar-chart");
  const ctx = canvas.getContext("2d");
  new Chart(ctx, {
    type: "bar",
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
