function redrawStackedAreaChart (option) {
	d3.json("Data/processed_data.json").then(function(data){
		document.getElementById('left_panel').innerHTML = "";
		year_data = processYear(data, option);
		drawStackedAreaChart(year_data, option);
	});
}


function redrawStackedBarChart (option) {
	d3.json("Data/processed_data.json").then(function(data){
		document.getElementById('right_panel').innerHTML = "";
		subject_data = processSubject(data, option);
		drawStackedBarChart(subject_data, option);
	});
}


function showOption () {
	var svg = d3.select('.mainsvg');
	
	svg.selectAll('.option-text')
		.remove()
		
	svg.append('text')
		.classed('option-text', true)
		.attr('x', _width - 175)
		.attr('y', 150)
		.attr('fill', 'black')
		.attr('font-size', '1.2rem')
		.attr("font-weight", "600")
		.style("text-anchor", "middle")
		.text('當前選擇')
	
	svg.append('text')
		.classed('option-text', true)
		.attr('x', _width - 300)
		.attr('y', 175)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.style("text-anchor", "start")
		.text(option.census?'戶籍：'+option.census:'戶籍：无')
		
	svg.append('text')
		.classed('option-text', true)
		.attr('x', _width - 125)
		.attr('y', 175)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.style("text-anchor", "start")
		.text(option.subject?'科目：'+option.subject:'科目：无')
		
	svg.append('text')
		.classed('option-text', true)
		.attr('x', _width - 300)
		.attr('y', 200)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.style("text-anchor", "start")
		.text(option.year?'年份：'+option.year:'年份：无')
		
	svg.append('text')
		.classed('option-text', true)
		.attr('x', _width - 125)
		.attr('y', 200)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.style("text-anchor", "start")
		.text(option.native?'籍贯：'+option.native:'籍贯：无')
}

function showData (d, type) {
	var svg = d3.select('.mainsvg');
	
	svg.selectAll('.data-text')
		.remove()
		
	svg.append('text')
		.classed('data-text', true)
		.attr('x', 175)
		.attr('y', 115)
		.attr('fill', 'black')
		.attr('font-size', '1.2rem')
		.attr("font-weight", "600")
		.style("text-anchor", "middle")
		.text('當前數據')
		
	if (type == 1) {
		svg.append('text')
			.classed('data-text', true)
			.attr('x', 120)
			.attr('y', 150)
			.attr('fill', 'black')
			.attr('font-size', '1rem')
			.attr("font-weight", "600")
			.style("text-anchor", "start")
			.text('年份：'+d.data['年份'])
			
		svg.append('text')
			.classed('data-text', true)
			.attr('x', 120)
			.attr('y', 175)
			.attr('fill', 'black')
			.attr('font-size', '1rem')
			.attr("font-weight", "600")
			.style("text-anchor", "start")
			.text('戶籍：'+d.name)
			
		svg.append('text')
			.classed('data-text', true)
			.attr('x', 120)
			.attr('y', 200)
			.attr('fill', 'black')
			.attr('font-size', '1rem')
			.attr("font-weight", "600")
			.style("text-anchor", "start")
			.text('進士人數：'+(d[1]-d[0]))
	}
	
	else if (type == 2) {
		svg.append('text')
			.classed('data-text', true)
			.attr('x', 120)
			.attr('y', 150)
			.attr('fill', 'black')
			.attr('font-size', '1rem')
			.attr("font-weight", "600")
			.style("text-anchor", "start")
			.text('科目：'+d.data['科目'])
			
		svg.append('text')
			.classed('data-text', true)
			.attr('x', 120)
			.attr('y', 175)
			.attr('fill', 'black')
			.attr('font-size', '1rem')
			.attr("font-weight", "600")
			.style("text-anchor", "start")
			.text('甲次：'+d.name)
			
		svg.append('text')
			.classed('data-text', true)
			.attr('x', 120)
			.attr('y', 200)
			.attr('fill', 'black')
			.attr('font-size', '1rem')
			.attr("font-weight", "600")
			.style("text-anchor", "start")
			.text('進士人數：'+(d[1]-d[0]))
	}
	
	else if (type == 3) {
		var si = document.getElementById('si');
		var native_level = "府级";
		if (si.classList[0] == "btn-click" || si.classList[1] == "btn-click") {
			native_level = "司级";
		}
		svg.append('text')
			.classed('data-text', true)
			.attr('x', 120)
			.attr('y', 150)
			.attr('fill', 'black')
			.attr('font-size', '1rem')
			.attr("font-weight", "600")
			.style("text-anchor", "start")
			.text('行政级别：'+native_level)
			
		svg.append('text')
			.classed('data-text', true)
			.attr('x', 120)
			.attr('y', 175)
			.attr('fill', 'black')
			.attr('font-size', '1rem')
			.attr("font-weight", "600")
			.style("text-anchor", "start")
			.text('行政區劃：'+d.name)
			
		svg.append('text')
			.classed('data-text', true)
			.attr('x', 120)
			.attr('y', 200)
			.attr('fill', 'black')
			.attr('font-size', '1rem')
			.attr("font-weight", "600")
			.style("text-anchor", "start")
			.text('進士人數：'+d.value)
	}
}


function hideData () {
	var svg = d3.select('.mainsvg');
	
	svg.selectAll('.data-text')
		.remove()
}