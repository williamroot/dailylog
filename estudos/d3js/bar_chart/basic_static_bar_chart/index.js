import {
  select,
  csv,
  scaleLinear,
  max,
  scaleBand,
  axisLeft,
  axisBottom
} from 'd3';

// Aqui damos a 'select(element)' uma variável

const svg = select('svg');

// 'attr()' pega o atributo definido no HTML

/* ----------------------------------------
	Observação:
	> O símbolo '+' indica conversão do valor 
	> para float, já que ele vem em string
	--------------------------------------- */

const width = +svg.attr('width');
const height = +svg.attr('height');

// Criamos a função 'render()' como variável

/* ----------------------------------------
	Observação:
	> Como a função atuará sobre 'data', ela
  > indica sobre onde atuará com '=':
  >		const render = data 
	> Em seguida, damos os atributos da função
  > com outras variáveis usando '=>':
  >		=> {...}
  > O resultado é:
  >		const render = data => {
  >			const var1;
  >			const var2;
  >			...
  >		};
	--------------------------------------- */

const render = data => {
  
  // Valor de xValue vem de d, definido abaixo
  // Neste caso, extraímos de d 'population'
  
  const xValue = d => d.population;
  
  // Valor de yValue vem de d, definido abaixo
  // Neste caso, extraímos de d 'country'
  
  const yValue = d => d.country;
  
	// Definimos margens, em dicionário
  // Apenas definimos; não aplicamos
  
  const margin = { top: 20, right: 40, bottom: 20, left: 100 };
  
  // Aplicamos as margens para definir a disposição do gráfico
  // Tanto 'width' quanto 'height' foram definidos acima (ln 25,26)
  
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;
  
  // Definimos a escala de x
  
  /* ----------------------------------------
	Observação:
	> Para definir a escala de x, usamos 
  > scaleLinear() com alguns atributos usados
  > para correlacionar o que está nos dados e
  > o que será exibido na tela. Funciona como
  > "original" (domain) e "tradução" (range):
  >		- .domain() toma a escala dos dados, que
  >			vai de 0 até o número máximo em 'data'
  >		- .range() toma a escala do gráfico, que
  >			vai de 0 até o limite do espaço
	--------------------------------------- */
  
  const xScale = scaleLinear()
    .domain([0, max(data, xValue)])
    .range([0, innerWidth]);
  
  const yScale = scaleBand()
    .domain(data.map(yValue))
    .range([0, innerHeight])
    .padding(0.1);
  
  const g = svg.append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`);
  
  g.append('g').call(axisLeft(yScale));
  g.append('g').call(axisBottom(xScale))
    .attr('transform', `translate(0,${innerHeight})`);
  
  g.selectAll('rect').data(data)
    .enter().append('rect')
      .attr('y', d => yScale(yValue(d)))
      .attr('width', d => xScale(xValue(d)))
      .attr('height', yScale.bandwidth());
};

csv('data.csv').then(data => {
  data.forEach(d => {
    d.population = +d.population * 1000;
  });
  render(data);
});
