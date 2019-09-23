// -- THE DATA --

const chart8_values = [
  1.17,1.35,1.3,1.09,0.93,0.76,0.83,0.98,0.87,0.89,0.93,0.81
];

const chart8_labels = [
  "Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"
];

// -- THE DATA OBJ --

const chart8_data_obj = {
  labels: chart8_labels,
  datasets: [{
    data: chart8_values,
    borderColor: 'hsla(300,100%,50%,1)',
    backgroundColor: 'transparent',
    borderWidth: 1,
    pointStyle: 'crossRot',
    pointRadius: 10,
    pointBorderColor: 'black',
    steppedLine: 'before'
  }]
}

// -- THE CHART

const chart8_chart_obj = {
  type: "line",
  data: chart8_data_obj
};

new Chart("chart8", chart8_chart_obj);
