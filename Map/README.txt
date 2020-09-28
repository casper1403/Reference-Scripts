
Casper van der Vliet
11052953 

Project data processing: Interactive map Visualization.


Folder description:

This project folder consist of 4 directories and two .txt files. The folder named code consist of two .py files where one handles the processing of the data and the other 
the visualization. The folder named data consist of three .csv files with data. The folder named shapefile consist of data files
used in the project to plot the countries on the map. The folder name text contains the logbook and the pipeline description.


How to run: 

Running the visualization consist of three steps: 

1. The first step is setting up an anaconda virtual environment. This is due to the fact that some dependencies didn't work outside of anaconda. '

2. When in an anaconda virtualenv cd to the folder directory and install the requirements by: 

	pip install -r requirements.txt 

3. when done cd, into the code directory and run: 
	
	bokeh serve --show visualize.py

This will open a browser and show the visualization. 
