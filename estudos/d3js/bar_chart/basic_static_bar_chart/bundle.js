(function (d3) {
  'use strict';

  // Aqui damos a 'select(element)' uma variável

  const svg = d3.select('svg');

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
    
    const xScale = d3.scaleLinear()
      .domain([0, d3.max(data, xValue)])
      .range([0, innerWidth]);
    
    const yScale = d3.scaleBand()
      .domain(data.map(yValue))
      .range([0, innerHeight])
      .padding(0.1);
    
    const g = svg.append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);
    
    g.append('g').call(d3.axisLeft(yScale));
    g.append('g').call(d3.axisBottom(xScale))
      .attr('transform', `translate(0,${innerHeight})`);
    
    g.selectAll('rect').data(data)
      .enter().append('rect')
        .attr('y', d => yScale(yValue(d)))
        .attr('width', d => xScale(xValue(d)))
        .attr('height', yScale.bandwidth());
  };

  d3.csv('data.csv').then(data => {
    data.forEach(d => {
      d.population = +d.population * 1000;
    });
    render(data);
  });

}(d3));

//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiaW5kZXguanMiLCJzb3VyY2VzIjpbIi4uL2luZGV4LmpzIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7XG4gIHNlbGVjdCxcbiAgY3N2LFxuICBzY2FsZUxpbmVhcixcbiAgbWF4LFxuICBzY2FsZUJhbmQsXG4gIGF4aXNMZWZ0LFxuICBheGlzQm90dG9tXG59IGZyb20gJ2QzJztcblxuLy8gQXF1aSBkYW1vcyBhICdzZWxlY3QoZWxlbWVudCknIHVtYSB2YXJpw6F2ZWxcblxuY29uc3Qgc3ZnID0gc2VsZWN0KCdzdmcnKTtcblxuLy8gJ2F0dHIoKScgcGVnYSBvIGF0cmlidXRvIGRlZmluaWRvIG5vIEhUTUxcblxuLyogLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXHRPYnNlcnZhw6fDo286XG5cdD4gTyBzw61tYm9sbyAnKycgaW5kaWNhIGNvbnZlcnPDo28gZG8gdmFsb3IgXG5cdD4gcGFyYSBmbG9hdCwgasOhIHF1ZSBlbGUgdmVtIGVtIHN0cmluZ1xuXHQtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gKi9cblxuY29uc3Qgd2lkdGggPSArc3ZnLmF0dHIoJ3dpZHRoJyk7XG5jb25zdCBoZWlnaHQgPSArc3ZnLmF0dHIoJ2hlaWdodCcpO1xuXG4vLyBDcmlhbW9zIGEgZnVuw6fDo28gJ3JlbmRlcigpJyBjb21vIHZhcmnDoXZlbFxuXG4vKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cdE9ic2VydmHDp8Ojbzpcblx0PiBDb21vIGEgZnVuw6fDo28gYXR1YXLDoSBzb2JyZSAnZGF0YScsIGVsYVxuICA+IGluZGljYSBzb2JyZSBvbmRlIGF0dWFyw6EgY29tICc9JzpcbiAgPlx0XHRjb25zdCByZW5kZXIgPSBkYXRhIFxuXHQ+IEVtIHNlZ3VpZGEsIGRhbW9zIG9zIGF0cmlidXRvcyBkYSBmdW7Dp8Ojb1xuICA+IGNvbSBvdXRyYXMgdmFyacOhdmVpcyB1c2FuZG8gJz0+JzpcbiAgPlx0XHQ9PiB7Li4ufVxuICA+IE8gcmVzdWx0YWRvIMOpOlxuICA+XHRcdGNvbnN0IHJlbmRlciA9IGRhdGEgPT4ge1xuICA+XHRcdFx0Y29uc3QgdmFyMTtcbiAgPlx0XHRcdGNvbnN0IHZhcjI7XG4gID5cdFx0XHQuLi5cbiAgPlx0XHR9O1xuXHQtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gKi9cblxuY29uc3QgcmVuZGVyID0gZGF0YSA9PiB7XG4gIFxuICAvLyBWYWxvciBkZSB4VmFsdWUgdmVtIGRlIGQsIGRlZmluaWRvIGFiYWl4b1xuICAvLyBOZXN0ZSBjYXNvLCBleHRyYcOtbW9zIGRlIGQgJ3BvcHVsYXRpb24nXG4gIFxuICBjb25zdCB4VmFsdWUgPSBkID0+IGQucG9wdWxhdGlvbjtcbiAgXG4gIC8vIFZhbG9yIGRlIHlWYWx1ZSB2ZW0gZGUgZCwgZGVmaW5pZG8gYWJhaXhvXG4gIC8vIE5lc3RlIGNhc28sIGV4dHJhw61tb3MgZGUgZCAnY291bnRyeSdcbiAgXG4gIGNvbnN0IHlWYWx1ZSA9IGQgPT4gZC5jb3VudHJ5O1xuICBcblx0Ly8gRGVmaW5pbW9zIG1hcmdlbnMsIGVtIGRpY2lvbsOhcmlvXG4gIC8vIEFwZW5hcyBkZWZpbmltb3M7IG7Do28gYXBsaWNhbW9zXG4gIFxuICBjb25zdCBtYXJnaW4gPSB7IHRvcDogMjAsIHJpZ2h0OiA0MCwgYm90dG9tOiAyMCwgbGVmdDogMTAwIH07XG4gIFxuICAvLyBBcGxpY2Ftb3MgYXMgbWFyZ2VucyBwYXJhIGRlZmluaXIgYSBkaXNwb3Npw6fDo28gZG8gZ3LDoWZpY29cbiAgLy8gVGFudG8gJ3dpZHRoJyBxdWFudG8gJ2hlaWdodCcgZm9yYW0gZGVmaW5pZG9zIGFjaW1hIChsbiAyNSwyNilcbiAgXG4gIGNvbnN0IGlubmVyV2lkdGggPSB3aWR0aCAtIG1hcmdpbi5sZWZ0IC0gbWFyZ2luLnJpZ2h0O1xuICBjb25zdCBpbm5lckhlaWdodCA9IGhlaWdodCAtIG1hcmdpbi50b3AgLSBtYXJnaW4uYm90dG9tO1xuICBcbiAgLy8gRGVmaW5pbW9zIGEgZXNjYWxhIGRlIHhcbiAgXG4gIC8qIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cblx0T2JzZXJ2YcOnw6NvOlxuXHQ+IFBhcmEgZGVmaW5pciBhIGVzY2FsYSBkZSB4LCB1c2Ftb3MgXG4gID4gc2NhbGVMaW5lYXIoKSBjb20gYWxndW5zIGF0cmlidXRvcyB1c2Fkb3NcbiAgPiBwYXJhIGNvcnJlbGFjaW9uYXIgbyBxdWUgZXN0w6Egbm9zIGRhZG9zIGVcbiAgPiBvIHF1ZSBzZXLDoSBleGliaWRvIG5hIHRlbGEuIEZ1bmNpb25hIGNvbW9cbiAgPiBcIm9yaWdpbmFsXCIgKGRvbWFpbikgZSBcInRyYWR1w6fDo29cIiAocmFuZ2UpOlxuICA+XHRcdC0gLmRvbWFpbigpIHRvbWEgYSBlc2NhbGEgZG9zIGRhZG9zLCBxdWVcbiAgPlx0XHRcdHZhaSBkZSAwIGF0w6kgbyBuw7ptZXJvIG3DoXhpbW8gZW0gJ2RhdGEnXG4gID5cdFx0LSAucmFuZ2UoKSB0b21hIGEgZXNjYWxhIGRvIGdyw6FmaWNvLCBxdWVcbiAgPlx0XHRcdHZhaSBkZSAwIGF0w6kgbyBsaW1pdGUgZG8gZXNwYcOnb1xuXHQtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gKi9cbiAgXG4gIGNvbnN0IHhTY2FsZSA9IHNjYWxlTGluZWFyKClcbiAgICAuZG9tYWluKFswLCBtYXgoZGF0YSwgeFZhbHVlKV0pXG4gICAgLnJhbmdlKFswLCBpbm5lcldpZHRoXSk7XG4gIFxuICBjb25zdCB5U2NhbGUgPSBzY2FsZUJhbmQoKVxuICAgIC5kb21haW4oZGF0YS5tYXAoeVZhbHVlKSlcbiAgICAucmFuZ2UoWzAsIGlubmVySGVpZ2h0XSlcbiAgICAucGFkZGluZygwLjEpO1xuICBcbiAgY29uc3QgZyA9IHN2Zy5hcHBlbmQoJ2cnKVxuICAgIC5hdHRyKCd0cmFuc2Zvcm0nLCBgdHJhbnNsYXRlKCR7bWFyZ2luLmxlZnR9LCR7bWFyZ2luLnRvcH0pYCk7XG4gIFxuICBnLmFwcGVuZCgnZycpLmNhbGwoYXhpc0xlZnQoeVNjYWxlKSk7XG4gIGcuYXBwZW5kKCdnJykuY2FsbChheGlzQm90dG9tKHhTY2FsZSkpXG4gICAgLmF0dHIoJ3RyYW5zZm9ybScsIGB0cmFuc2xhdGUoMCwke2lubmVySGVpZ2h0fSlgKTtcbiAgXG4gIGcuc2VsZWN0QWxsKCdyZWN0JykuZGF0YShkYXRhKVxuICAgIC5lbnRlcigpLmFwcGVuZCgncmVjdCcpXG4gICAgICAuYXR0cigneScsIGQgPT4geVNjYWxlKHlWYWx1ZShkKSkpXG4gICAgICAuYXR0cignd2lkdGgnLCBkID0+IHhTY2FsZSh4VmFsdWUoZCkpKVxuICAgICAgLmF0dHIoJ2hlaWdodCcsIHlTY2FsZS5iYW5kd2lkdGgoKSk7XG59O1xuXG5jc3YoJ2RhdGEuY3N2JykudGhlbihkYXRhID0+IHtcbiAgZGF0YS5mb3JFYWNoKGQgPT4ge1xuICAgIGQucG9wdWxhdGlvbiA9ICtkLnBvcHVsYXRpb24gKiAxMDAwO1xuICB9KTtcbiAgcmVuZGVyKGRhdGEpO1xufSk7Il0sIm5hbWVzIjpbInNlbGVjdCIsInNjYWxlTGluZWFyIiwibWF4Iiwic2NhbGVCYW5kIiwiYXhpc0xlZnQiLCJheGlzQm90dG9tIiwiY3N2Il0sIm1hcHBpbmdzIjoiOzs7OztFQVlBLE1BQU0sR0FBRyxHQUFHQSxTQUFNLENBQUMsS0FBSyxDQUFDLENBQUM7Ozs7Ozs7Ozs7RUFVMUIsTUFBTSxLQUFLLEdBQUcsQ0FBQyxHQUFHLENBQUMsSUFBSSxDQUFDLE9BQU8sQ0FBQyxDQUFDO0VBQ2pDLE1BQU0sTUFBTSxHQUFHLENBQUMsR0FBRyxDQUFDLElBQUksQ0FBQyxRQUFRLENBQUMsQ0FBQzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7RUFvQm5DLE1BQU0sTUFBTSxHQUFHLElBQUksSUFBSTs7Ozs7SUFLckIsTUFBTSxNQUFNLEdBQUcsQ0FBQyxJQUFJLENBQUMsQ0FBQyxVQUFVLENBQUM7Ozs7O0lBS2pDLE1BQU0sTUFBTSxHQUFHLENBQUMsSUFBSSxDQUFDLENBQUMsT0FBTyxDQUFDOzs7OztJQUs5QixNQUFNLE1BQU0sR0FBRyxFQUFFLEdBQUcsRUFBRSxFQUFFLEVBQUUsS0FBSyxFQUFFLEVBQUUsRUFBRSxNQUFNLEVBQUUsRUFBRSxFQUFFLElBQUksRUFBRSxHQUFHLEVBQUUsQ0FBQzs7Ozs7SUFLN0QsTUFBTSxVQUFVLEdBQUcsS0FBSyxHQUFHLE1BQU0sQ0FBQyxJQUFJLEdBQUcsTUFBTSxDQUFDLEtBQUssQ0FBQztJQUN0RCxNQUFNLFdBQVcsR0FBRyxNQUFNLEdBQUcsTUFBTSxDQUFDLEdBQUcsR0FBRyxNQUFNLENBQUMsTUFBTSxDQUFDOzs7Ozs7Ozs7Ozs7Ozs7OztJQWlCeEQsTUFBTSxNQUFNLEdBQUdDLGNBQVcsRUFBRTtPQUN6QixNQUFNLENBQUMsQ0FBQyxDQUFDLEVBQUVDLE1BQUcsQ0FBQyxJQUFJLEVBQUUsTUFBTSxDQUFDLENBQUMsQ0FBQztPQUM5QixLQUFLLENBQUMsQ0FBQyxDQUFDLEVBQUUsVUFBVSxDQUFDLENBQUMsQ0FBQzs7SUFFMUIsTUFBTSxNQUFNLEdBQUdDLFlBQVMsRUFBRTtPQUN2QixNQUFNLENBQUMsSUFBSSxDQUFDLEdBQUcsQ0FBQyxNQUFNLENBQUMsQ0FBQztPQUN4QixLQUFLLENBQUMsQ0FBQyxDQUFDLEVBQUUsV0FBVyxDQUFDLENBQUM7T0FDdkIsT0FBTyxDQUFDLEdBQUcsQ0FBQyxDQUFDOztJQUVoQixNQUFNLENBQUMsR0FBRyxHQUFHLENBQUMsTUFBTSxDQUFDLEdBQUcsQ0FBQztPQUN0QixJQUFJLENBQUMsV0FBVyxFQUFFLENBQUMsVUFBVSxFQUFFLE1BQU0sQ0FBQyxJQUFJLENBQUMsQ0FBQyxFQUFFLE1BQU0sQ0FBQyxHQUFHLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQzs7SUFFaEUsQ0FBQyxDQUFDLE1BQU0sQ0FBQyxHQUFHLENBQUMsQ0FBQyxJQUFJLENBQUNDLFdBQVEsQ0FBQyxNQUFNLENBQUMsQ0FBQyxDQUFDO0lBQ3JDLENBQUMsQ0FBQyxNQUFNLENBQUMsR0FBRyxDQUFDLENBQUMsSUFBSSxDQUFDQyxhQUFVLENBQUMsTUFBTSxDQUFDLENBQUM7T0FDbkMsSUFBSSxDQUFDLFdBQVcsRUFBRSxDQUFDLFlBQVksRUFBRSxXQUFXLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQzs7SUFFcEQsQ0FBQyxDQUFDLFNBQVMsQ0FBQyxNQUFNLENBQUMsQ0FBQyxJQUFJLENBQUMsSUFBSSxDQUFDO09BQzNCLEtBQUssRUFBRSxDQUFDLE1BQU0sQ0FBQyxNQUFNLENBQUM7U0FDcEIsSUFBSSxDQUFDLEdBQUcsRUFBRSxDQUFDLElBQUksTUFBTSxDQUFDLE1BQU0sQ0FBQyxDQUFDLENBQUMsQ0FBQyxDQUFDO1NBQ2pDLElBQUksQ0FBQyxPQUFPLEVBQUUsQ0FBQyxJQUFJLE1BQU0sQ0FBQyxNQUFNLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQztTQUNyQyxJQUFJLENBQUMsUUFBUSxFQUFFLE1BQU0sQ0FBQyxTQUFTLEVBQUUsQ0FBQyxDQUFDO0dBQ3pDLENBQUM7O0FBRUZDLFFBQUcsQ0FBQyxVQUFVLENBQUMsQ0FBQyxJQUFJLENBQUMsSUFBSSxJQUFJO0lBQzNCLElBQUksQ0FBQyxPQUFPLENBQUMsQ0FBQyxJQUFJO01BQ2hCLENBQUMsQ0FBQyxVQUFVLEdBQUcsQ0FBQyxDQUFDLENBQUMsVUFBVSxHQUFHLElBQUksQ0FBQztLQUNyQyxDQUFDLENBQUM7SUFDSCxNQUFNLENBQUMsSU