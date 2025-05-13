import numpy as np


def calculate_mean(list):
    matr = np.array(list).reshape(3, 3)
    axis1_mean = np.mean(matr, axis = 0)
    axis2_mean = np.mean(matr, axis = 1)
    flat_mean = np.mean(matr)

    return [axis1_mean.tolist(), axis2_mean.tolist(), flat_mean]
    

def calculate_var(list):
    matr = np.array(list).reshape(3, 3)
    axis1_var = np.var(matr, axis = 0)
    axis2_var = np.var(matr, axis = 1)
    flat_var = np.var(matr)

    return [axis1_var.tolist(), axis2_var.tolist(), flat_var]

def calculate_stddev(list):
    matr = np.array(list).reshape(3, 3)
    axis1_std = np.std(matr, axis = 0)
    axis2_std = np.std(matr, axis = 1)
    flat_std = np.std(matr)

    return [axis1_std.tolist(), axis2_std.tolist(), flat_std]

def calculate_max(list):
    matr = np.array(list).reshape(3, 3)
    axis1_max = np.max(matr, axis = 0)
    axis2_max = np.max(matr, axis = 1)
    flat_max = np.max(matr)

    return [axis1_max.tolist(), axis2_max.tolist(), flat_max]

def calculate_min(list):
    matr = np.array(list).reshape(3, 3)
    axis1_min = np.min(matr, axis = 0)
    axis2_min = np.min(matr, axis = 1)
    flat_min = np.min(matr)

    return [axis1_min.tolist(), axis2_min.tolist(), flat_min]

def calculate_sum(list):
    matr = np.array(list).reshape(3, 3)
    axis1_sum = np.sum(matr, axis = 0)
    axis2_sum = np.sum(matr, axis = 1)
    flat_sum = np.sum(matr)

    return [axis1_sum.tolist(), axis2_sum.tolist(), flat_sum]


def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
        
    calculations = {'mean': calculate_mean(list),
                    'variance': calculate_var(list),
                    'standard deviation': calculate_stddev(list),
                    'max': calculate_max(list),
                    'min': calculate_min(list),
                    'sum': calculate_sum(list)
    }





    return calculations