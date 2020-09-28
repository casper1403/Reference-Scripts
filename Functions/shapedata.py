import geopandas as gpd
import pandas as pd
import shapely

""" Function that takes a Geodataframe as an input and returns two columns with the coordinates of that shapefile """

def returncoordinates(dataframe):

    dataframe.columns = ['NAME','geometry']
    motherFrame = []

    for NAME, polygon in zip(dataframe['NAME'], dataframe['geometry']):
        if isinstance(polygon, shapely.geometry.polygon.Polygon):
            motherFrame.append([NAME,polygon])
        if isinstance(polygon, shapely.geometry.multipolygon.MultiPolygon):
            polygonList = list(polygon.geoms)
            for poly in polygonList:
                motherFrame.append([NAME,poly])

    gdf = pd.DataFrame(motherFrame, columns=['Name','geometry'])

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

    gdf = gdf.drop('geometry', axis=1)

    return gdf
