'''
Created on July 8, 2016

This is an example script for accessing spatial data from the 
Reynold Creek Critical Zone Observatory (WY1984 - WY2014)

@author: pkormos
'''
import netCDF4 as nc
import numpy as np

url = 'http://data.boisestate.edu/opendap/CZO/'  # Data location

########################################################################################
# uncomment the variable that you want to access #######################################
########################################################################################

# variable names for air temperature
dir_name = 'air_temperature'
dir_name2 = 'ta'
var_name = 'surface_temperature'

# # variable names for relative humidity
# dir_name = 'relative_humidity'
# dir_name2 = 'rh'
# var_name = 'relative_humidity'

# # variable names for dew point temperature
# dir_name = 'dew_point_temperature'
# dir_name2 = 'dp'
# var_name = 'dew_point_temperature'

# # variable names for percent snow
# dir_name = 'percent_snow'
# dir_name2 = 'pcts'
# var_name = 'pct_snow'

# # variable names for precipitation amount
# dir_name = 'precipitation_depth'
# dir_name2 = 'precip'
# var_name = 'precipitation_amount'

########################################################################################
# define the spatial extent of interest ################################################
########################################################################################

########################################################################################
# use the following code if you will define a lat lon extent ###########################
latn =   43.1782   # north most latitude                                             ###
lats =   43.1738   # south most latitude                                             ###
lone = -116.73   # east most longitude                                               ###
lonw = -116.74   # west most longitude                                               ###
########################################################################################
# do not modify code below, which gets the extent indices ##############################
fn = url + dir_name + '/' + dir_name2 + '_wy' + str(1984) + '.nc' # build file name ####
dataset = nc.Dataset(fn) # pointer to a netcdf file ###############################
tt_lat = dataset.variables['lat'][:] # pointer to the lat. var #########################
tt_lon = dataset.variables['lon'][:] # pointer to the lat. var ######################### 
msk = (tt_lat >= lats) & (tt_lat <= latn) & (tt_lon >= lonw) & (tt_lon <= lone) # mask #
yi1 = np.min(np.where(msk)[0]) # get y index 1 #########################################
yi2 = np.max(np.where(msk)[0]) # get y index 2 #########################################
xi1 = np.min(np.where(msk)[1]) # get x index 1 #########################################
xi2 = np.max(np.where(msk)[1]) # get x index 2 #########################################
dataset.close()
########################################################################################

# ########################################################################################
# # use the following code if you will define a northing easting extent ##################
# norn = 4780634   # north most latitude                                               ###
# nors = 4780144   # south most latitude                                               ###
# ease =  521895   # east most longitude                                               ###
# easw =  521405   # west most longitude                                               ###
# ########################################################################################
# # do not modify code below, which gets the extent indices ##############################
# fn = url + dir_name + '/' + dir_name2 + '_wy' + str(1984) + '.nc' # build file name ####
# dataset = nc.Dataset(fn) # pointer to a netcdf file ####################################
# tt_eas = dataset.variables['x'][:] # pointer to the lat. var ###########################
# tt_nor = dataset.variables['y'][:] # pointer to the lat. var ########################### 
# yi1 = np.max(np.where(tt_nor>norn)) # get y index 1 ####################################
# yi2 = np.min(np.where(tt_nor<nors)) # get y index 2 ####################################
# xi1 = np.max(np.where(tt_eas<easw)) # get x index 1 ####################################
# xi2 = np.min(np.where(tt_eas>ease)) # get x index 2 ####################################
# dataset.close()                                     ####################################
# ########################################################################################

# ## print some data from those data sets (here is where you would use this data in your code.
# wyoi = np.arange(1984,2015)                      # make vector of water years of interest (1984 to 2014)
# for y in wyoi:
#     fn = url + dir_name + '/' + dir_name2 + '_wy' + str(y) + '.nc' # build file name ####
#     dataset = nc.Dataset(fn)      # create a dataset object
#     variable = dataset.variables[var_name]
#     print('WY'+str(y))
#     print(variable[0,yi1:yi2,xi1:xi2])  # 0 is first time step in the water year.
#  
## plot up some data 
import matplotlib.pyplot as plt
fn = url + dir_name + '/' + dir_name2 + '_wy' + str(1984) + '.nc' # build file name ####
dataset = nc.Dataset(fn)      # create a dataset object
variable = dataset.variables[var_name]
plt.imshow(variable[0,yi1:yi2,xi1:xi2])
dataset.close()
