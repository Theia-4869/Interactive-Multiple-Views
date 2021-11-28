function drawStackedBarChart(data) {
	data = data.dataitem;

	let div = d3.select('#right_panel')
	let svgWidth = $('#right_panel').width()
	let svgHeight = $('#right_panel').height()
	let padding = {
		'left': 0.175 * svgWidth,
		'right': 0.025 * svgWidth,
		'top': 0.1 * svgHeight,
		'bottom': 0.15 * svgHeight
	}
	let svg = div.append('svg')
		.attr('id', 'stackedBarChartSvg')
		.attr('width', svgWidth)
		.attr('height', svgHeight)
		
	svg.append('text')
		.classed('title', true)
		.attr('x', (svgWidth + padding.left - padding.right) / 2 - 125)
		.attr('y', 20)
		.attr('fill', 'black')
		.attr('font-size', '1.2rem')
		.attr("font-weight", "600")
		.text('明進士甲次-科目堆疊柱狀圖')

	let x_array = [];
	data.forEach(d => {
		x_array.push(d['科目']);
	})
	// console.log(x_array);
	let y_array = ['未知', '第三甲', '第二甲', '第一甲'];
	
	let stack = d3.stack()
		.keys(y_array)
		.offset(d3.stackOffsetNone);
	let series = stack(data);
	// console.log(series);
	
	let y_max = [];
	series[series.length-1].forEach(d => {
		y_max.push(d[1]);
	})
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

	let axes = svg.append('g')
		.classed('axes', true)

	axes.append('g')
		.classed('x-axis', true)
		.attr('transform', `translate(${0}, ${svgHeight-padding.bottom})`)
		.call(axis_x)
		.selectAll("text")
		.style("font-size", "1rem")
		.style("font-weight", "600")
		.style("font-family", "楷体")

	// axes.selectAll('g.x-axis g.tick')
	// 	.append('line')
	// 	.classed('grid-line', true)
	// 	.attr('x1', 0)
	// 	.attr('y1', 0)
	// 	.attr('x2', 0)
	// 	.attr('y2', -(svgHeight - padding.top - padding.bottom))

	axes.append('g')
		.classed('y-axis', true)
		.attr('transform', `translate(${padding.left}, ${0})`)
		.call(axis_y)
		.style('font-size', '0.8rem')
		.style("font-weight", "600")

	// axes.selectAll('g.y-axis g.tick')
	// 	.append('line')
	// 	.classed('grid-line', true)
	// 	.attr('x1', 0)
	// 	.attr('y1', 0)
	// 	.attr('x2', svgWidth - padding.left - padding.right)
	// 	.attr('y2', 0)
	
	axes.select('.x-axis')
		.append('text')
		.attr('class', 'axisText')
		.attr('x', (svgWidth  + padding.left - padding.right) / 2)
		.attr('y', 40)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.attr('font-family', '楷体')
		.text('科目');
	
	axes.select('.y-axis')
		.append('text')
		.attr('class', 'axisText')
		.attr('x', - (svgHeight + padding.top - padding.bottom) / 2)
		.attr('y', -45)
		.attr('text-anchor','middle')
		.attr('transform', 'rotate(-90)')
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.attr('font-family', '楷体')
		.text('進士人數');

	let body = svg.append('g')
		.classed('body', true)
		.attr('transform', `translate(${padding.left}, ${padding.top})`)

	let colors = d3.scaleOrdinal(d3.schemeCategory10);
	const interval = x(x_array[1]) - x(x_array[0]);

	let groups = body.selectAll('.g')
		.data(series);

	let bars = groups.enter()
		.append('g')
		.merge(groups)
		.attr('class', (d) => 'g ' + d.key)
		.attr('fill', (d, i) => colors(i))
		.selectAll('.bar')
		.data((d) => {
			return d.map((item) => {
				item.index = d.index;
				item.name = d.key;
				return item;
			});
		});

	let y_scale = d3.scaleLinear()
		.domain([0, y_max])
		.range([svgHeight - padding.bottom - padding.top, 0]);

	bars.enter()
		.append('rect')
		.attr('class', (d) => 'bar ' + d.data['科目'])
		.merge(bars)
		.attr('x', (d) => x(d.data['科目']) - interval / 2 - 0.075 * svgWidth)
		.attr('y', (d) => y_scale(d[1]))
		.attr('width', interval / 2)
		.attr('height', (d) => y_scale(d[0]) - y_scale(d[1]))
		.attr("fill-opacity", 0.7)
		
	let legend = svg.selectAll(".legend")
	    .data(y_array.slice().reverse())
	    .enter()
		.append("g")
	    .attr("class", "legend")
	    .attr("transform", (d, i) => "translate(-100," + (i * 20) + ")");
	
	legend.append("rect")
	    .attr("x", width - 50)
	    .attr("y", 30)
	    .attr("width", 20)
	    .attr("height", 10)
	    .style("fill", (d, i) => colors(3 - i));
	
	legend.append("text")
	    .attr("x", width - 20)
	    .attr("y", 40)
	    .style("text-anchor", "start")
		.style("font-weight", "600")
	    .text((d) => d);
		
	let button1 = svg.append("g")
		.attr("class", "button1")
		
	button1.append("rect")
		.attr("x", 10)
		.attr("y", 220)
		.attr("width", 65)
		.attr("height", 20)
		.style("fill", "YellowGreen")
		.attr("stroke", "white")
		
	button1.append("text")
		.attr("x", 10)
		.attr("y", 235)
		.attr('fill', 'white')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.style("text-anchor", "start")
		.text("重置科目")
		
	let button2 = svg.append("g")
		.attr("class", "button2")
	
	button2.append("rect")
		.attr("x", 10)
		.attr("y", 250)
		.attr("width", 65)
		.attr("height", 20)
		.style("fill", "MediumOrchid")
		.attr("stroke", "white")
		
	button2.append("text")
		.attr("x", 10)
		.attr("y", 265)
		.attr('fill', 'white')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.style("text-anchor", "start")
		.text("重置籍貫")

	svg.selectAll(".bar")
		.on("mouseover", function(d) {
			d3
				.selectAll('.'+d.data["科目"])
				.attr("fill-opacity", 1)
			showData(d, 2);
		})
		.on("mouseout", function(d) {
			d3
				.selectAll('.'+d.data["科目"])
				.attr("fill-opacity", 0.7)
			hideData();
		})
		.on("click", function(d) {
			option.subject = d.data["科目"];
			redrawStackedAreaChart(option);
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
			option.subject = undefined;
			redrawStackedAreaChart(option);
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
			option.native_level = undefined;
			option.native = undefined;
			redrawStackedAreaChart(option);
			redrawStackedBarChart(option);
			showOption();
		})
}
