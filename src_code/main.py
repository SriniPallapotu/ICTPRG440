#import Geopands library 
import geopandas as gpd

#Set file path to read orginal spatial source data
FILE_PATH = r"C:\Python_Programming_TAFE\ICTPRG440\spatial_data_original\NSW_MyHospitals_Public_SriniP\MyHospital_Sites.shp"

#Set Output File path to export output data
OUTPUT_PATH = r"C:\Python_Programming_TAFE\ICTPRG440\output"

#1.	Define a function to read a vector spatial data and return a geodataframe object

def readSpatialData(filepath):
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

def PrintAttributeTable(gdf):
    try:

        if isinstance(gdf,gpd.geodataframe.GeoDataFrame):
            pass
        else:
            raise ValueError("Input is not a GeoDataFrame")
        for row in gdf.itertuples():
            print(row)
    except Exception as e:
        print(f"[PrintAttributeTable] Errot:",{e})   


    return None

   
#print(type(gdf))

#PrintAttributeTable(gdf)

#Check Coordinate Reference System for Input spatial Source data
#print(gdf.crs)

def trans_From_Web_MTo_Geog_WGS84(inputfilepath,outputpath,EPSG=4326):
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
trans_From_Web_MTo_Geog_WGS84(inputfilepath=FILE_PATH,outputpath=OUTPUT_PATH,EPSG=4326)
