// -- THE DATA --

const data = {
  labels: ["Volume"], // One label because we work with one category
  /*
  Labels (above) and dataset data values must come within brackets for
  which they will be iterated over one single position/axis
  */
  datasets: [
    {
      label: "Arctic",
      data: [18750],
      backgroundColor: "hsla(0,100%,50%,0.5)"
    }, {
      label: "North Atlantic",
      data: [146000],
      backgroundColor: "hsla(60,100%,50%,0.5)"
    }, {
      label: "South Atlantic",
      data: [160000],
      backgroundColor: "hsla(120,100%,50%,0.5)"
    }, {
      label: "Indian",
      data: [264000],
      backgroundColor: "hsla(180,100%,50%,0.5)"
    }, {
      label: "North Pacific",
      data: [341000],
      backgroundColor: "hsla(240,100%,50%,0.5)"
    }, {
      label: "South Pacific",
      data: [329000],
      backgroundColor: "hsla(300,100%,50%,0.5)"
    }, {
      label: "Southern",
      data: [71800],
      backgroundColor: "hsla(340,100%,50%,0.5)"
    }
  ]
};

// -- THE OPTIONS --

const options = {
  maintainAspectRatio: false,
  title: {
    display: true,
    text: "Volume of oceans (km3)",
    fontSize: 16
  },
  legend: {
    position: "right"
  },
  scales: { // Scale options to refer to stacked bar...
    xAxes: [{
      stacked: true // ...on x-axis...
    }],
    yAxes: [{
      stacked: true // ...and on y-axis
    }]
  }
}

// -- THE CHART --

new Chart("ocean-volume-bar-chart", {
  type: "bar",
  data: data,
  options: options
});
