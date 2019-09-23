// Add variable for array of categorical values (x-axis)
const oceans = [
  "Arctic", "North Atlantic", "South Atlantic", "Indian",
  "North Pacific", "South Pacific", "Southern"
];

// Add variable for array of numerical values (y-axis)
const volumes = [18750, 146000, 160000, 264000, 341000, 329000, 71800];

/*
Merge variables into dataset and give it a variable
Args:
  labels = categories (mandatory)
  datasets = at least one dataset (mandatory), which contains, at least:
    label = the name we give to the dataset
    data = the variable containing numerical values
*/
const data = {
  labels: oceans,
  /*
  Another way, in case we have not assigned a variable:
  labels: [
    "Arctic", "North Atlantic", "South Atlantic", "Indian",
    "North Pacific", "South Pacific", "Southern"
  ],
  */
  datasets: [
    {
      label: "Volume",
      data: volumes,
      // The following is optional
      borderWidth: 2,
      borderWidth: 0,
      backgroundColor: "rgba(204, 0, 0, .75)",
      hoverBackgroundColor: "rgba(179, 0, 0, 1)"
    }
  ]
}

/*
Build the chart
Function: new Chart(x, y, z);
Args:
 x = where to plot (the canvas' id)
 y = what to plot (the data)
 z = how to plot (the options)
*/
new Chart("ocean-volume-bar-chart", {
  type: "bar",
  data: data,
  // The following is optional
  options: {
    maintainAspectRatio: false, // Override aspect ratio
    legend: {
      display: false // Hide the categorical value of the top
    },
    title: {
      display: true, // Show title
      text: ['Volume of the oceans','in thousands of km³'], // Add title text
      fontFamily: "TrebuchetMS", // Choose font family
      fontSize: 18, // Choose font size
      fontColor: 'rgba(0,0,0,.5)' // Choose font color
    }
  }
});
