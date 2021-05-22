##Contains Python functions for HW08, BDS 311
##These functions will be generated collaboratively and called in each user's separate Jupyter notebook

#import standard packages here

import numpy as np


def make_standard_units(input_array):
    '''Converts input_array to standard_units, where data has mean 0 and standard deviation of 1
        INPUT: data array
        OUTPUT: array in standard units'''
    mean_subtracted_array=input_array-np.mean(input_array)
    normalized_array=mean_subtracted_array/np.std(input_array)
    return normalized_array
    
def calc_corrcoef_from_standardized_input(array1,array2):
    '''Calculates Pearson correlation coefficient from two arrays in standard units
    INPUT: array1, array2: In standard units
    OUTPUT: Pearson correlation coefficient'''
    corr=np.mean(array1*array2)
    return corr

def get_regression_parameters(array1, array2):
    '''Calculates regression parameteres from two input arrays
    INPUT: array1, array2: two data arrays
    OUTPUT: regression_array, length 2: regression_array[0] is slope and regression_array[1] is intercept'''

    #test
    xstd=np.std(array1)
    ystd=np.std(array2)
    slope=calc_corrcoef_from_standardized_input(array1,array2)*(ystd/xstd)

    xmean=np.mean(array1)
    ymean=np.mean(array2)
    intercept=ymean-slope*xmean
    
    regression_array=np.array([slope,intercept])
    return regression_array