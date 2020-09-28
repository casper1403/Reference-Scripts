"""
Casper van der Vliet
11052953
"""
import geopandas as gpd
import pandas as pd
import shapely

def get_data():

    """ Fuction that is used to fetch the data for the visualization and provide the geoDataframe, It requires a folder with the data in csv format to run and due to the
    usage of geopandas it is best used through an anaconda environement.

    The script consist of three sub parts; the first takes the csv data and turns it into a dataframe, the second performs some operations on the data and the third
    prepares the shapefile data to be used with bokeh. The merge of the (selected) data with the shapefile happens in the visualize.py script  """

    # Load the csv files into the dataframe and delete data before 1990 with the sharemoileusers as it only shows irrelevant values
    dfShareInternetUsers = pd.read_csv(r"..\data\share-of-individuals-using-the-internet.csv")
    dfShareMobileUsers = pd.read_csv(r"..\data\mobile-cellular-subscriptions-per-100-people.csv")
    dfShareBroadband = pd.read_csv(r"..\data\broadband-penetration-by-country.csv")
    dfShareMobileUsers = dfShareMobileUsers[dfShareMobileUsers['Year'] > 1990]

    def flatten_df(df):

        """
        The data was ordered that the years were rows, but to reduce the amount of rows for later merging it would be better to have the year data as column values
        Function that takes dataframe as input and outputs a dictionary ordered {Country name : {year:data}.....}
        Dataframe should be ordered: country,alpha-3 code,year,value
        alpha-3 column in dataframe should be named 'Code'  """

        countryDict = {}
        checkList = list()
        df = df.dropna(subset=['Code'])

        # loop over all the rows of the dataframe and add the values to a dictionary
        for country,code,year,value in zip(df.iloc[:,0],df.iloc[:,1],df.iloc[:,2],df.iloc[:,3]):
            if country in countryDict:
                countryDict[country][1][year] = value
            else:
                countryDict[country] = code , dict()
                countryDict[country][1][year] = value

                checkList.append(code)

        # Return dictionary with country name as key and the data as key:value pairs
        return countryDict

    def transform(df, flatten_df, dataType=None):

        """ Function that performs operation on the data. The data is taken from the dictionaries and put in a single data frame. """

        # Create a frame and add the data the that was flattened in the dictionary
        frame = pd.DataFrame()
        frame = frame.from_dict(flatten_df(df), orient='index').reset_index()
        # Create a new dataframe that contains all the data and transform it so that every year has a single column
        dfcolumns = pd.json_normalize(frame[1])
        # sort the columns so that the years ascending
        dfcolumns = dfcolumns.reindex(columns=sorted(list(dfcolumns.columns)))
        # add missing countries so their polygons get shown in the map
        frame = frame.append({'index':'North Korea', 0:'PRK'}, ignore_index=True)
        frame = frame.append({'index':'French Guiana',0:'GUF'}, ignore_index=True)
        frame = frame.append({'index':'Western Sahara',0:'ESH'}, ignore_index=True)
        frame = frame.append({'index':'Taiwan',0:'TWN'}, ignore_index=True)
        frame = frame.append({'index':'Syria',0:'SYR'}, ignore_index=True)
        frame = frame.append({'index':'Sierra Leone',0:'SLE'}, ignore_index=True)
        # Merge the countries with the data
        frame =  frame.merge(dfcolumns,how='outer',left_index=True,right_index=True).rename(columns={0:'ISO3','index':'NAME'})
        # add a row that keeps track of the type of data
        frame.insert(2,'data', dataType)
        # Drop the column that contained all the data from the dictionaries,
        frame = frame.drop(columns=1)
        return frame


    # perform the operations on all the dataframes and concat them into a single frame
    gdfFileShareBroadband = transform(dfShareBroadband, flatten_df, "Broadband subscriptions per 100 people")
    gdfFileShareMobileUsers = transform(dfShareMobileUsers, flatten_df, "Mobile subscriptions per 100 people")
    gdfShareInternetUsers = transform(dfShareInternetUsers, flatten_df, "Share of the population using the Internet")
    masterFrame = pd.concat([gdfFileShareBroadband,gdfFileShareMobileUsers])
    masterFrame = pd.concat([masterFrame, gdfShareInternetUsers])

    # Read the shapefile and create geopandas object
    geoFrame = gpd.read_file(r"..\shapefile\TM_WORLD_BORDERS-0.3.shp")
    geoFrame = geoFrame.drop(columns=['FIPS','ISO2','UN',"AREA",'REGION','SUBREGION','LON','LAT','POP2005','NAME']).rename(columns={'geometry':'type'})
    geoFrame = geoFrame.drop(index=[144]).reset_index()

    # extract the individual polygons from the multipolygon objects and save them in a datafrme,then concat the new frame to the old frame
    newFrame = []
    index = 0
    for code, polygon in zip(geoFrame['ISO3'],geoFrame['type']):
        if isinstance(polygon, shapely.geometry.polygon.Polygon):
            geoFrame.at[index,'geometry'] = polygon
        if isinstance(polygon, shapely.geometry.multipolygon.MultiPolygon):
            polygonList = list(polygon.geoms)
            for poly in polygonList:
                newFrame.append([code,poly])
        index+=1
    geoFrame = geoFrame.drop(columns=['type'])
    newFrame = pd.DataFrame(newFrame,columns=['ISO3','geometry'])
    geoFrame = geoFrame.dropna()
    gdf = pd.concat([geoFrame,newFrame])


    def getPolyCoords(row, geom, coord_type):

        """ Function that extracts the x and y coordinates from the polygon objects and returns a list of the x or y coordinates """

        if isinstance(row[geom], shapely.geometry.polygon.Polygon):
            if coord_type == 'x':
                return list(row[geom].exterior.coords.xy[0])
            elif coord_type == 'y':
                return list(row[geom].exterior.coords.xy[1])

    # apply the function to the dataframe row with the polygons and create a new row storing the x and y coordinate values.
    gdf['xs'] = gdf.apply(getPolyCoords, geom = 'geometry', coord_type = 'x', axis = 1)
    gdf['ys'] = gdf.apply(getPolyCoords, geom = 'geometry', coord_type = 'y', axis = 1)
    gdf = gdf.drop(columns=['index'])

    #merge the dataframe with the data and the frame with the coordinates so that every row has a polygon and the country data for that polygon
    Merge = pd.merge(masterFrame ,gdf, on='ISO3')

    # Rename the columns to str() so it can be parsed into a datacolumnsource.
    for i in list(Merge.columns):
        if isinstance(i, int):
            Merge = Merge.rename(columns={i:str(i)})

    # Drop some unneeded columsn
    masterFrame = Merge.drop(columns=['geometry','ISO3','2017'])

    return masterFrame
