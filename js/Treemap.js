// var _width = $(window).width();
// var _height = $(window).height();
var _width = $("#bottom_panel").width();
var _height = $("#bottom_panel").height() - $("#neon-btn").height() - 5;
var width = 800;
var height = 441.125;

var fontFamily;

function setUi() {
	// 设置字体
	var ua = navigator.userAgent.toLowerCase();
	fontFamily = "楷体";
	if (/\(i[^;]+;( U;)? CPU.+Mac OS X/gi.test(ua)) {
		fontFamily = "PingFangSC-Regular";
	}
	d3.select("body").style("font-family", fontFamily);
}

function treemap(data, width, height) {
	// Simple Treemap
	// 输入：数据，画布宽高
	// 输出：叶节点的位置及大小

	// 存放叶节点的数组
	var leaves = [];

	function calcPos(node, x, y, width, height, parent) {
		var rects = [];
		var rwidth = width,
			rheight = height;

		function worst(row, w) {
			if (row.length == 0) {
				return Infinity;
			}

			var rmax = 0,
				rmin = Infinity,
				s = 0;
			for (var i in row) {
				var r = row[i].value * 25;
				s += r;
				if (r > rmax) rmax = r;
				if (r < rmin) rmin = r;
			}
			var pw = w * w,
				ps = s * s;
			return Math.max((pw * rmax) / ps, ps / (pw * rmin));
		}

		function layoutrow(row, w) {
			var lx = width - rwidth,
				ly = height - rheight;
			var direction; // 0: horizontal;  1: vertical

			var sum = 0;
			for (var i in row)
				sum += row[i].value * 25;
			var ext = sum / w;
			if (Math.abs(w - rwidth) <= 1e-6) {
				rheight -= ext;
				direction = 0;
			} else {
				rwidth -= ext;
				direction = 1;
			}

			for (var i in row) {
				if (direction == 0) {
					var hh = ext,
						ww = row[i].value * 25 / ext;
					var node = {
						x: lx,
						y: ly,
						width: ww,
						height: hh,
					};
					rects.push(node);
					lx += ww;
				} else {
					var ww = ext,
						hh = row[i].value * 25 / ext;
					var node = {
						x: lx,
						y: ly,
						width: ww,
						height: hh,
					};
					rects.push(node);
					ly += hh;
				}
			}
		}

		function squarify(children, row, w) {
			if (children.length == 0) {
				if (row.length != 0) layoutrow(row, w);
				return;
			}

			var node = children[0];
			var [...newrow] = row;
			newrow.push(node);

			if (worst(row, w) >= worst(newrow, w)) {
				var [...tmp] = children
				tmp.shift();
				squarify(tmp, newrow, w);
			} else {
				layoutrow(row, w);
				squarify(children, [], Math.min(rwidth, rheight));
			}
		}

		var children = node.children;
		squarify(children, [], Math.min(rwidth, rheight));
		for (var i in children) {
			var child_node = children[i];
			if (child_node.children == undefined) {
				var leaf = {
					name: child_node.name,
					value: child_node.value,
					x: x + rects[i].x,
					y: y + rects[i].y,
					width: rects[i].width,
					height: rects[i].height,
					parent: parent == -1 ? child_node.name : parent.name,
				};
				leaves.push(leaf);
			} else {
				calcPos(
					child_node,
					x + rects[i].x,
					y + rects[i].y,
					rects[i].width,
					rects[i].height,
					parent == -1 ? child_node : parent
				)
			}
		}
	}

	calcPos(data, (_width - width) / 2, 0, width, height, -1);

	return leaves;
}

function drawTreemap(data) {
	var svg = d3
		.select('#treemap')
		.append("svg")
		.attr("class", "mainsvg")
		.attr("width", _width)
		.attr("height", _height)
		.attr("background", "white");
	
	// 计算布局
	var leaves = treemap(data, width, height);

	// 绘制
	svg
		.append("rect")
		.attr("x", (_width - width) / 2)
		.attr("stroke", "white")
		.attr("stroke-width", 1)
		.attr("fill", "white")
		.attr("width", width)
		.attr("height", height)

	// 定义颜色比例尺
	let colors_10 = d3.schemeCategory10.slice();
	let color = d3.scaleOrdinal(colors_10.reverse());
	// var color = d3.scaleOrdinal(["dodgerBlue", "orange", "greenyellow", "tomato", "purple", "chocolate", "hotpink",
	// 	"olive", "gold", "gray", "aqua", "violet", "yellow", "dimGray", "green", "indigo", "crimson",
	// 	"royalblue"
	// ]);


	const leaf = svg
		.selectAll("g")
		.data(leaves)
		.join("g")
		.attr("transform", (d) => `translate(${d.x},${d.y})`);

	// 矩形
	leaf
		.append("rect")
		.attr("id", (d) => d.name)
		.attr("class", "rectnode")
		.attr("stroke", "white")
		.attr("stroke-width", 1)
		.attr("fill", (d) => color(d.parent))
		.attr("fill-opacity", (d) => d.value > 400 ? 0.86 : Math.sqrt(d.value) * 0.028 + 0.3)
		.attr("width", (d) => d.width)
		.attr("height", (d) => d.height)

	// 交互
	svg
		.selectAll(".rectnode")
		.on("mouseover", function(d, i) {
			d3
				.select(this)
				.attr("fill-opacity", 0.2)
			showData(d, 3);
		})
		.on("mouseout", function(d, i) {
			d3
				.select(this)
				.transition()
				.duration(0)
				.attr("fill-opacity", (d) => d.value > 400 ? 0.86 : Math.sqrt(d.value) * 0.028 + 0.3)
			hideData();
		})
		.on("click", function(d) {
			d3
				.select(this)
				.attr("class", "clicked")
				.attr("fill-opacity", 0.2)
			var si = document.getElementById('si');
			if (si.classList[0] == "btn-click" || si.classList[1] == "btn-click") {
				option.native_level = 1;
			}
			else {
				option.native_level = 2;
			}
			option.native = d.name;
			redrawStackedAreaChart(option);
			redrawStackedBarChart(option);
			showOption();
		})

	// 文字
	leaf
		.append("text")
		.selectAll("tspan")
		.data((d) => (d.name + d.value.toString()).split(/(?=[A-Z][a-z])|\s+/g))
		.join("tspan")
		.attr("x", 2)
		.attr("y", (d, i, nodes) => `${(i === nodes.length - 1) * 0.3 + 0.6 + i * 0.9}em`)
		.attr("fill-opacity", (d, i, nodes) => i === nodes.length - 1 ? 0.7 : null)
		.attr("font-size",
			function(d) {
				var str = d.slice(2);
				if (str[0] < "0" || str[0] > "9")
					str = str.slice(1);
				var v = parseInt(str);
				v = Math.round(v / 15) + 5;
				if (v > 15)
					v = 15;
				return `${v}px`;
			}
		)
		.text((d) => d)
		
	let button = svg.append("g")
		.attr("class", "big_button")
	
	button.append("rect")
		.attr("x", _width - 215)
		.attr("y", 210)
		.attr("width", 80)
		.attr("height", 27)
		.style("fill", "LightSteelBlue")
		.attr("stroke", "white")
		
	button.append("text")
		.attr("x", _width - 175)
		.attr("y", 230)
		.attr('fill', 'white')
		.attr('font-size', '1.2rem')
		.attr("font-weight", "600")
		.style("text-anchor", "middle")
		.text("全部重置")
		
	svg.select(".big_button")
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
			option.year = undefined;
			option.subject = undefined;
			option.native_level = undefined;
			option.native = undefined;
			redrawStackedAreaChart(option);
			redrawStackedBarChart(option);
			showOption();
		})

	svg
		.append('text')
		.classed('left-above-box', true)
		.attr('x', 15)
		.attr('y', 20)
		.attr('fill', 'black')
		.attr('font-size', '1.5rem')
		.attr("font-weight", "600")
		.text('人有千門萬戶，總出於軍、民、')
		
	svg
		.append('text')
		.classed('left-above-box', true)
		.attr('x', 15)
		.attr('y', 45)
		.attr('fill', 'black')
		.attr('font-size', '1.5rem')
		.attr("font-weight", "600")
		.text('匠、竈之一籍。——《後湖志》')
		
	svg
		.append("line")
		.attr("x1", 15)
		.attr("y1", 50) 
		.attr("x2", 347) 
		.attr("y2", 50)
		.attr("stroke", "black")
		.attr("stroke-width", 2)
		
	svg
		.append('text')
		.classed('right-above-box', true)
		.attr('x', _width - 5)
		.attr('y', 20)
		.attr('fill', 'black')
		.attr('font-size', '1.5rem')
		.attr("font-weight", "600")
		.style("text-anchor", "end")
		.text('說天者莫辯乎易，說事者莫辯乎')
		
	svg
		.append('text')
		.classed('right-above-box', true)
		.attr('x', _width - 5)
		.attr('y', 45)
		.attr('fill', 'black')
		.attr('font-size', '1.5rem')
		.attr("font-weight", "600")
		.style("text-anchor", "end")
		.text('書，說體者莫辯乎禮，說志者莫')
		
	svg
		.append('text')
		.classed('right-above-box', true)
		.attr('x', _width - 5)
		.attr('y', 70)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1.5rem')
		.attr("font-weight", "600")
		.style("text-anchor", "end")
		.text('辯乎詩，說理者莫辯乎春秋。  ')
	
	svg
		.append('text')
		.classed('right-above-box', true)
		.attr('x', _width - 5)
		.attr('y', 95)
		.attr('fill', 'black')
		.attr('font-size', '1.5rem')
		.attr("font-weight", "600")
		.style("text-anchor", "end")
		.text('——《揚子法言》')
		
	svg
		.append("line")
		.attr("x1", _width - 5)
		.attr("y1", 100) 
		.attr("x2", 1153) 
		.attr("y2", 100)
		.attr("stroke", "black")
		.attr("stroke-width", 2)
	
	svg
		.append("rect")
		.attr("x", 10)
		.attr("y", 280)
		.attr("width", 330)
		.attr("height", height - 61 - 220)
		.style("fill", "transparent")
		.attr("stroke", "black")
		
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 175)
		.attr('y', 298)
		.attr('fill', 'black')
		.attr('font-size', '1.2rem')
		.attr("font-weight", "600")
		.style("text-anchor", "middle")
		.text('数据集介绍')
	
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 10)
		.attr('y', 313)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('    本可视化项目选用了CBDB的明进士数据，')
		
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 10)
		.attr('y', 328)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('包括明代52年间共14116名进士的全部资料，')
		
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 10)
		.attr('y', 343)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('分别按照年份(1371-1610)、户籍(民、军、官')
		
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 10)
		.attr('y', 358)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('、匠、灶)、科目(诗、书、礼、易、春秋)、')
		
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 10)
		.attr('y', 373)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('甲次(一甲、二甲、三甲)、籍贯(17司146府)')
		
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 10)
		.attr('y', 388)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('等属性进行了可视化处理。其中户籍-年份以')
		
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 10)
		.attr('y', 403)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('以堆叠面积图的形式呈现，甲次-科目以堆叠')
		
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 10)
		.attr('y', 418)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('柱状图的形式呈现，籍贯则单独以矩形树图的')
		
	svg
		.append('text')
		.classed('left-bottom-box', true)
		.attr('x', 10)
		.attr('y', 433)
		.attr('fill', 'black')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('形式呈现。')
		
	svg
		.append("rect")
		.attr("x", _width - 340)
		.attr("y", 265)
		.attr("width", 330)
		.attr("height", height - 111 - 155)
		.style("fill", "transparent")
		.attr("stroke", "black")
		
	svg
		.append('text')
		.classed('right-bottom-box', true)
		.attr('x', _width - 340 + 165)
		.attr('y', 283)
		.attr('fill', 'black')
		.attr('font-size', '1.2rem')
		.attr("font-weight", "600")
		.style("text-anchor", "middle")
		.text('交互帮助')
	
	svg
		.append('text')
		.classed('right-bottom-box', true)
		.attr('x', _width - 340)
		.attr('y', 298)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('堆叠面积图：')
		
	svg
		.append('text')
		.classed('right-bottom-box', true)
		.attr('x', _width - 340)
		.attr('y', 313)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('    点击小圆圈按照所属年份筛选，点击染色')
	
	svg
		.append('text')
		.classed('right-bottom-box', true)
		.attr('x', _width - 340)
		.attr('y', 328)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('面积区域按照户籍类型筛选。')
		
	svg
		.append('text')
		.classed('right-bottom-box', true)
		.attr('x', _width - 340)
		.attr('y', 358)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('堆叠柱状图：')
		
	svg
		.append('text')
		.classed('right-bottom-box', true)
		.attr('x', _width - 340)
		.attr('y', 373)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('    点击单个立柱按照考试科目筛选。')
		
	svg
		.append('text')
		.classed('right-bottom-box', true)
		.attr('x', _width - 340)
		.attr('y', 403)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('矩形树图：')
		
	svg
		.append('text')
		.classed('right-bottom-box', true)
		.attr('x', _width - 340)
		.attr('y', 418)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('    点击单个矩形按照籍贯所在地筛选，点击')
	
	svg
		.append('text')
		.classed('right-bottom-box', true)
		.attr('x', _width - 340)
		.attr('y', 433)
		.attr('fill', 'black')
		.attr('xml:space', 'preserve')
		.attr('font-size', '1rem')
		.attr("font-weight", "600")
		.text('上方按钮可切换司级粒度或府级粒度。')
		
	showOption();
}
