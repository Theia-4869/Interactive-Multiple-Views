# Interactive Multiple Views
This code base uses interactive multiple views to visualize the Ming Jinshi List from China Biographical Database Project(CBDB). Here are five folders and three files in this code base: Data, Figure, js, Report, Script and index.html, README.md, style.css.

## Data
This folder contains the data used in the visualization process.

Xlsx file: ming_jinshilu_52y_release.xlsx (raw data)

JSON file: ming_jinshilu_52y_release.json, mingjinshi_processed.json, processed_data.json,year_and_census_data.json, subject_and_rank_data.json, si_data.json, fu_data.json (processed data)

## Figure
This folder contains figures used in html(background), report and README.

## js
This folder contains javascript files used in html: d3.min.js, jquery.min.js and other files are listed below.

- DataProcess.js (preprocess data before drawing and dynamically brush data)
- StackedAreachart.js (draw the census-year Stacked Areachart)
- StackedBarchart.js (draw the rank-subject Stacked Barchart)
- Treemap.js (draw the native Squarified Treemap)
- Selecting.js (provide brushpick interaction)

## Report
This folder contains the course report (written in Latex).

## Script
This folder contains scripts for processing raw data.

- data_sort.py (sort JSON data using the value attribute)
- item_native_process.py (divide the native place data organized in JSON format according to administrative division level for each data item)
- item_process.py (read data items organized in JSON format and pick out some properties)
- native_process.py (divide the native place data organized in JSON format according to administrative division level)
- subject_and_rank_process.py (process the subject and rank properties of data items)
- xlsx_process.py (read raw data and store data items in JSON format)
- year_and_census_process.py (process the year and census properties of data items)

## index.html
The index.html file is the web page rendered for the final interactive multiple views visualization.

## style.css
The style.css file is the css style used in the html.

## Visualization
![](./Figure/figure.png)