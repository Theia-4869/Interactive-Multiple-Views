function drawStackedAreaChart(data) {
	data = data.dataitem;
	
	let div = d3.select('#left_panel');
	let svgWidth = $('#left_panel').width();
	let svgHeight = $('#left_panel').height();
	let padding = {
	    'left': 0.075 * svgWidth,
	    'right': 0.125 * svgWidth,
	    'top': 0.1 * svgHeight,
	    'bottom': 0.15 * svgHeight
	};
	let svg = div.append('svg')
	    .attr('id', 'stackedAreaChartSvg')
	    .attr('width', svgWidth)
	    .attr('height', svgHeight);
		
	svg.append('text')
		.classed('title', true)
		.attr('x', (svgWidth + padding.left - padding.right) / 2 - 125)
		.attr('y', 20)
		.attr('fill', 'black')
		.attr('font-size', '1.2rem')
		.attr("font-weight", "600")
		.text('明進士戶籍-年份堆疊面積圖')
		
	let x_array = [];
	data.forEach(d => {
		x_array.push(d['年份']);
	})
	// console.log(x_array);
	let y_array = ['其他', '竈籍', '匠籍', '官籍', '軍籍', '民籍'];
	
	let stack = d3.stack()
		.keys(y_array)
		.offset(d3.stackOffsetNone);
	let series = stack(data);
	// console.log(series);
	
	let y_max = [];
	series[series.length-1].forEach(d => {
		y_max.push(d[1]);
	})
	console.log(y_max);
	y_max = d3.max(y_max);
	
	let x = d3.scaleBand()
	    .domain(x_array)
	    .range([padding.left, svgWidth - padding.right]);
	let axis_x = d3.axisBottom()
	    .scale(x)
	    .ticks(x_array.length)
	    .tickFormat(d => d);
	
	let y = d3.scaleLinear()
	    .domain([0, y_max])
	    .range([svgHeight - padding.bottom, padding.top]);
	let axis_y = d3.axisLeft()
	    .scale(y)
	    .ticks(10)
	    .tickFormat(d => d);
		
	const x_start = x(x_array[0]);
	const y_start = y(y_max);
	const interval = x(x_array[1]) - x(x_array[0]);
		
	let axes = svg.append('g')
		.classed('axes', true);
		
	axes.append('g')
		.classed('x-axis', true)
	    .attr('transform', `translate(${0}, ${svgHeight-padding.bottom})`)
	    .call(axis_x)
		.selectAll("text")
		.style("font-size", "0.5rem")
		.style("font-weight", "600")
		.style("text-anchor", "start")
		.attr("transform", "rotate(90) translate(8, -12)")
		
	axes.selectAll('g.x-axis g.tick')
		.append('line')
		.classed('grid-line', true)
		.attr('x1', 0)
		.attr('y1', 0)
		.attr('x2', 0)
		.attr('y2', -(svgHeight - padding.top - padding.bottom))
		
	axes.append('g')
		.classed('y-axis', true)
		.attr('transform', `translate(${padding.left}, ${0})`)
		.call(axis_y)
		.attr('font-size', '0.75rem')
		.style("font-weight", "600")
		
	axes.selectAll('g.y-axis g.tick')
		.append('line')
		.classed('grid-line', true)
		.attr('x1', 0)
		.attr('y1', 0)
		.attr('x2', svgWidth - padding.left - padding.right)
		.attr('y2', 0)
		
	axes.select('.x-axis')
		.append('text')
		.attr('class', 'axisText')
		.attr('x', (svgWidth + padding.left - padding.right) / 2)
		.attr('y', 40)
		.attr('fill', 'black')
		.attr('font-size', '0.75rem')
		.attr("font-weight", "600")
		.attr('font-family', '楷体')
		.text('年份')
	
	axes.select('.y-axis')
		.append('text')
		.attr('class', 'axisText')
		.attr('x', - (svgHeight + padding.top - padding.bottom) / 2)
		.attr('y', -35)
		.attr('text-anchor','middle')
		.attr('transform', 'rotate(-90)')
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.attr('font-family', '楷体')
		.text('進士人數')
		
	let body = svg.append('g')
		.classed('body', true)
		.attr('transform', `translate(${padding.left}, ${padding.top})`);
	
	let colors_10 = d3.schemeCategory10.slice();
	let colors = d3.scaleOrdinal(colors_10.reverse());
	
	let line = d3.line()
		.x(d => x(d.data['年份']) - x_start + interval / 2)
		.y(d => y(d[1]) - y_start);
	
	let linePaths = body.selectAll('path.line')
		.data(series);
	
	linePaths.enter()
		.append('path')
		.merge(linePaths)
		.classed('line', true)
		.style('stroke', (d, i) => colors(i))
		.style('stroke-opacity', 0.8)
		.attr('d', d => line(d))
		
	let area = d3.area()
		.x(d => x(d.data['年份']) - x_start + interval / 2)
		.y0(d => y(d[0]) - y_start)
		.y1(d => y(d[1]) - y_start);
	
	let areaPaths = body.selectAll('path.area')
		.data(series);
	
	areaPaths.enter()
		.append('path')
		.merge(areaPaths)
		.classed('area', true)
		.style('fill', (d, i) => colors(i))
		.style("fill-opacity", 0.2)
		.attr('d', d => area(d))
		
	let groups = body.selectAll('.g')
		.data(series);
		
	let points = groups.enter()
		.append('g')
		.merge(groups)
		.attr('class', (d) => 'g ' + d.key)
		.selectAll('.point')
		.data((d) => {
			// console.log(d);
			return d.map((item) => {
				item.index = d.index;
				item.name = d.key;
				return item;
			});
		});
	            
	points.enter()
		.append('circle')
		.attr('class', (d) => 'point year'+d.data['年份'])
		.merge(points)
		.attr('cx', (d) => x(d.data['年份']) - x_start + interval / 2)
		.attr('cy', (d) => y(d[1]) - y_start)
		.attr('r', 3)
		.attr('fill', 'white')
		.attr('stroke', (d) => colors(d.index))
		.attr('stroke-width', 1.5)
		
	let legend = svg.selectAll(".legend") 
	    .data(y_array.slice().reverse())
	    .enter()
		.append("g")
	    .attr("class", "legend")
	    .attr("transform", (d, i) => "translate(-100," + (i * 20) + ")")
	
	legend.append("line")
	    .attr("x1", width - 16)
		.attr("y1", 45) 
		.attr("x2", width + 10) 
		.attr("y2", 45)
	    .attr("stroke", (d, i) => colors(5 - i))
	    .attr("stroke-width", 2)
	
	legend.append("circle")
	    .attr("cx", width - 3)
		.attr("cy", 45)
		.attr("r", 3)
		.attr('fill', 'white')
	    .attr("stroke", (d, i) => colors(5 - i))
	    .attr("stroke-width", 1.5)
	
	legend.append("text")
	    .attr("x", width + 15)
	    .attr("y", 50)
	    .style("text-anchor", "start")
		.style("font-weight", "600")
	    .text((d) => d);
	
	let button1 = svg.append("g")
		.attr("class", "button1")
	
	button1.append("rect")
		.attr("x", svgWidth - 70)
		.attr("y", 220)
		.attr("width", 65)
		.attr("height", 20)
		.style("fill", "RoyalBlue")
		.attr("stroke", "white")
		
	button1.append("text")
		.attr("x", svgWidth - 70)
		.attr("y", 235)
		.attr('fill', 'white')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.style("text-anchor", "start")
		.text("重置戶籍")
		
	let button2 = svg.append("g")
		.attr("class", "button2")
		
	button2.append("rect")
		.attr("x", svgWidth - 70)
		.attr("y", 250)
		.attr("width", 65)
		.attr("height", 20)
		.style("fill", "Tomato")
		.attr("stroke", "white")
		
	button2.append("text")
		.attr("x", svgWidth - 70)
		.attr("y", 265)
		.attr('fill', 'white')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.style("text-anchor", "start")
		.text("重置年份")
		
	svg.selectAll("path.area")
		.on("mouseover", function(d) {
			d3
				.select(this)
				.style("fill-opacity", 0.8)
		})
		.on("mouseout", function(d) {
			d3
				.select(this)
				.style("fill-opacity", 0.2)
		})
		.on("click", function(d) {
			option.census = d.key;
			redrawStackedBarChart(option);
			showOption();
		})
		
	svg.selectAll(".point")
		.on("mouseover", function(d) {
			d3
				.selectAll('.year'+d.data['年份'])
				.style("fill", 'red')
			showData(d, 1);
		})
		.on("mouseout", function(d) {
			d3
				.selectAll('.year'+d.data['年份'])
				.style("fill", 'white')
			hideData();
		})
		.on("click", function(d) {
			option.year = d.data["年份"];
			redrawStackedBarChart(option);
			showOption();
		})
	
	svg.select(".button1")
		.on("mouseover", function(d) {
			d3
				.select(this)
				.style("fill-opacity", 0.6)
		})
		.on("mouseout", function(d) {
			d3
				.select(this)
				.style("fill-opacity", 1)
		})
		.on("click", function(d) {
			option.census = undefined;
			redrawStackedBarChart(option);
			showOption();
		})
	
	svg.select(".button2")
		.on("mouseover", function(d) {
			d3
				.select(this)
				.style("fill-opacity", 0.6)
		})
		.on("mouseout", function(d) {
			d3
				.select(this)
				.style("fill-opacity", 1)
		})
		.on("click", function(d) {
			option.year = undefined;
			redrawStackedBarChart(option);
			showOption();
		})
}
