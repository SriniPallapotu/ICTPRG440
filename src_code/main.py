#import Geopands library 
import geopandas as gpd

""" 
The Objective of this Python program is to 
    1. Read Vector Spatial Data file (Eg:NSW state Public Hospitals Information) into GeoDataFrame
    2. Reproject the Dataset from its Original Coordinate Reference System (CRS) to specified EPSG code
       and export the resulting new Shapefile to output folder.
    3. Print the Attribute Table of Original GeoDataFrame
This script performs error handling with Try / Except and Basic GeoPandas operations
"""

#Set file path to read orginal spatial source data
FILE_PATH = r"C:\Python_Programming_TAFE\ICTPRG440\spatial_data_original\NSW_MyHospitals_Public_SriniP\MyHospital_Sites.shp"

#Set Output File path to export output data
OUTPUT_PATH = r"C:\Python_Programming_TAFE\ICTPRG440\output"

#1.	Define a function to read a vector spatial data and return a geodataframe object

def readSpatialData(filepath):
    """ 
    This function reads spatial data from input shapefile and returns the GeoDataFrame

    Parameters: 

        Paramaeter:Datatype
        filepath : str
            input fullpath to read source spatial data file (Eg: .shp)

    Returns GeoDataFrame: gpd.GeoDataFrame
    """
    try:
        if isinstance(filepath,str):
            pass
        else :
            raise ValueError("Provided File path is Not a String")
        gdf=gpd.read_file(filepath)
    except Exception as e:
        print(f"[readSpatialData] Errot:",{e})
    return gdf

gdf=readSpatialData(FILE_PATH)

#print(gdf.head())

#2. Print Attribute Table of GeoDataFrame

def PrintAttributeTable(input_gdf):
    """
    This funtion prints attribute table (all rows and all Coloumns) of input GeoDataFrame

    Parameters:
        input_gdf:gpd.GeoDataFrame

    Returs None
    
    """
    try:

        if isinstance(input_gdf,gpd.geodataframe.GeoDataFrame):
            pass
        else:
            raise ValueError("Input is not a GeoDataFrame")
        for row in input_gdf.itertuples():
            print(row)
    except Exception as e:
        print(f"[PrintAttributeTable] Error:",{e})   


    return None

   
#print(type(gdf))

#PrintAttributeTable(gdf)

#Check Coordinate Reference System for Input spatial Source data
#print(gdf.crs)

#3. Transform (Reproject) original CRS into Targeted CRS

def trans_From_Web_MTo_Geog_WGS84(inputfilepath,outputpath,EPSG=4326):
    """
    This funtion reprojects the origianl spatial dataset CRS to target CRS and export it to new shapefile.

    parameters:
        inputfilepath:str
            fullpath to input spatialfile to be reprojected
        outputpath:str
            fullpath to directory where reprojected file will be saved
        EPSG:int
             EPSG code of target CRS
    Returns None

    """
    try:
        if isinstance(EPSG,int):
            pass
        else:
            raise ValueError("Provided EPSG is not an Integer")
        
        if isinstance(inputfilepath,str):
            pass
        else:
            raise ValueError("Provided Input Filepath is not a string")
        
        if isinstance(outputpath,str):
            pass
        else:
            raise ValueError("Provided Output Path is not a string")
        outputfile=outputpath+"\\"+str(EPSG)+"Hospitals_sites.shp"
        gdf=readSpatialData(inputfilepath)
        print("Original_CRS",gdf.crs)
        gdf=gdf.to_crs(EPSG)
        print("ReProjected_CRS",gdf.crs)
        gdf.to_file(outputfile)
    except Exception as e:
        print(f"[trans_From_Web_MTo_Geog_WGS84] Errot:",{e})
    return None
#trans_From_Web_MTo_Geog_WGS84(inputfilepath=FILE_PATH,outputpath=OUTPUT_PATH,EPSG=4326)

if __name__=="__main__":
    trans_From_Web_MTo_Geog_WGS84(inputfilepath=FILE_PATH,outputpath=OUTPUT_PATH,EPSG=4326)
