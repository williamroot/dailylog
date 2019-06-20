const canvas = document.getElementById("ocean-volume-bar-chart");

// -- THE DATA --

// Add variable for array of categorical values (x-axis)
const oceans = [
  "Arctic", "North Atlantic", "South Atlantic", "Indian",
  "North Pacific", "South Pacific", "Southern"
];

// Add variable for array of numerical values (y-axis)
const volumes = [18750, 146000, 160000, 264000, 341000, 329000, 71800];

// Add another variable for another array of numerical values (y-axis)
const area = [15558, 41900, 40270, 70560, 84000, 84750, 21960];

// -- THE CHART --

// Give the chart a variable so we can call it later, when we update data
const ch = new Chart("ocean-volume-bar-chart", {
  type: "bar",
  data: {
    labels: oceans, // This x-axis works for both y-axes variables (volumes and area)
    datasets: [
      {
        label: "Volume", // We start with volume, and this label will be required for the following if-clause
        data: volumes,
        borderWidth: 2,
        borderWidth: 0,
        backgroundColor: "hsla(20,100%,80%,0.8)",
        borderColor: "hsla(0,100%,50%,1)"
      }
    ]
  },
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
    },
    tooltips: {
      backgroundColor: 'rgba(200,200,255,.9)',
      titleFontColor: 'black',
      caretSize: 5,
      callbacks: {
        labelColor: function(tooltipItem, chart) {
          return {
            borderColor: 'black',
            backgroundColor: chart.data.datasets[0].backgroundColor
          }
        },
        labelTextColor:function(tooltipItem, chart) {
          return chart.data.datasets[0].borderColor;
        }
      }
    }
  }
});

canvas.addEventListener("click", toggle); // Add an event: when click, toggle data inside canvas

// Create a function called toogle, as specified above
function toggle(event) {
  if(ch.data.datasets[0].label == "Volume") { // "If the label is 'Volume'..."
    ch.data.datasets[0].data = area; // ...toggles to data of area...
    ch.data.datasets[0].label = "Area"; // ...and label of area...
    ch.data.datasets[0].borderColor = "hsla(120,100%,50%,1)"; // ...and color of area...
    ch.data.datasets[0].backgroundColor = "hsla(140,100%,80%,0.8)";
    ch.options.title.text = [
      'Surface area of the oceans',
      'in thousands of km²'
    ];
  } else { // "If not the label 'Volume', which means the label 'Area'..."
    ch.data.datasets[0].data = volume;
    ch.data.datasets[0].label = "Volume";
    ch.data.datasets[0].backgroundColor = "hsla(20,100%,80%,0.8)";
    ch.data.datasets[0].borderColor = "hsla(0,100%,50%,1)";
    ch.options.title.text = [
      'Volume of the oceans',
      'in thousands of km³'
    ];
  }
  ch.update(); // Update chart according to if-clause inside toggle function
};
