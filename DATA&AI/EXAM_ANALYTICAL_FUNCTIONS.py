#!/usr/bin/env python
# coding: utf-8

# # <font color='red'>Exam Function Finder:</font>
# 
# ## <font color='yellow'>This Document has:</font>
# + Statistical Functions
# + Date Manipulation Fucntions
# + and more

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math

# for testing purposes
# students = pd.read_csv('resources/Questionnaire 21-22.csv', sep=';')


# ### <font color='red'>Frequencies function, returns:</font>
# <ol>
#     <li>Absolute Frequency</li>
#     <li>Relative Frequency</li>
#     <li>Absolute Cumulative Frequency</li>
#     <li>Absolute Relative Frequency</li>
#                     </ul>
# 

# In[2]:


def all_frequencies(series: pd.Series | list) -> pd.DataFrame:
    if type(series) == list:
        series = pd.Series(series)
    t_abs = series.value_counts(dropna=False).sort_index()
    t_rel = (series.value_counts(dropna=False, normalize=True).sort_index() * 100).round(1)
    t_abs_cum = series.value_counts(dropna=False).sort_index().cumsum()
    t_rel_cum = (series.value_counts(dropna=False, normalize=True).sort_index().cumsum() * 100).round(1)
    return pd.DataFrame({'absolute freq': t_abs, 'relative freq': t_rel, 'absolute cumulative freq': t_abs_cum,
                         'relative cumulative freq': t_rel_cum})


# #### <font color='red'>Merge Method:</font>
# ##### Example
# ```python
# airports = pd.merge(airports,right,on='airport',how='inner')
# ```

# In[4]:


def merge(left: pd.DataFrame(), right: pd.DataFrame(), on: str, how: str) -> pd.DataFrame:
    return pd.merge(left, right, on, how)


# #### <font color='red'>List of outliers</font>
# ##### Example
# ```python
# outlier(mylist, "high") # for upper boundaries only
# outlier(mylist, "low") # for lower boundaries only
# outlier(mylist, "both") # for all boundaries
# ```

# In[5]:


def outlier_boundaries(series: pd.Series, extreme: bool = False) -> list:
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    if extreme:
        iqr *= 3
    else:
        iqr *= 1.5
    return [q1 - iqr, q3 + iqr]


# In[6]:


def get_outliers(series: pd.Series, extreme: bool = False, inner: bool = True) -> pd.Series:
    """
    Used to get a new series of either outliers or the opposite, depending on inner(True by default).
    Get extreme outliers with the boolean extreme (False by default).

    :return: A new Series including or excluding outliers depending on inner.
    :rtype: Series
    :type inner: bool = True
    :type extreme: bool = False
    :type series: Series
    """
    l, h = outlier_boundaries(series, extreme)
    if inner:
        return series[series.between(l, h)]
    return series[~series.between(l, h)]


# In[7]:


def get_outliers2(data: pd.Series, boundary="both") -> list:
    data = pd.Series(data)
    list_to_return = []
    for value in data:
        assert boundary in ['low', 'high', 'both']
        if "low" in boundary:

            if value < (data.quantile(q=0.25) - stats.iqr(data) * 1.5):
                list_to_return.append(value)

        elif "high" in boundary:

            if value > (data.quantile(q=0.75) + stats.iqr(data) * 1.5):
                list_to_return.append(value)
        else:
            if value < (data.quantile(q=0.25) - stats.iqr(data) * 1.5) or value > (
                    data.quantile(q=0.75) + stats.iqr(data) * 1.5):
                list_to_return.append(value)
    return list_to_return


# Variance Calculator

# In[8]:


def variance_calculator(data):
    data = np.array(data)
    total = 0
    for d in data:
        total = total + ((d - np.mean(data)) ** 2)
    return total / len(data)


# Range calculator

# In[9]:


def get_range(data: list | pd.Series(dtype=float) | np.array) -> float:
    data = np.array(data)
    return data.max() - data.min()


# sample standard deviation calculator

# In[10]:


#sample standard deviation with delta degree of freedom------
def sample_standard_deviation(data):
    data = np.array(data)
    total = 0
    for d in data:
        total = total + ((d - np.mean(data)) ** 2)
    return np.sqrt(total / (len(data) - 1))


# population_standard deviation

# In[11]:


#population standard deviation
def population_standard_deviation(data):
    data = np.array(data)
    total = 0
    for d in data:
        total = total + ((d - np.mean(data)) ** 2)
    return np.sqrt(total / len(data))


# Harmonic mean

# In[12]:


def h_mean(series: pd.Series(dtype=float)):
    return stats.hmean(series)


# In[13]:


def harmonic_mean_calc(data, from_this_point, to_this_point):
    if from_this_point >= 0 and to_this_point <= len(data):
        return np.mean(data[from_this_point:to_this_point])
    else:
        return "YOUR INDEX OR DATA-TYPE IS INVALID"


# Geometric mean

# In[14]:


def g_mean(series: pd.Series(dtype=float)):
    return stats.gmean(series)


# In[15]:


def geometric_mean_calc(nums):
    length = len(nums)
    nums = nums / 100
    nums = np.product(nums)
    gm = nums ** (1 / length)
    return gm * 100


# Percentile finder

# In[16]:


def quant_perc_quart_finder(array: list, percentile: int):
    array = pd.Series(array).dropna()
    array = array.sort_values()
    tempo_position: float = (percentile / 100) * (len(array) + 1)
    floor_value = np.floor(tempo_position)
    ceiling_val = np.ceil(tempo_position)
    value = ((array[floor_value - 1]) + (array[ceiling_val - 1])) / 2
    return value


# Create a list of values with amount of frequencies

# In[17]:


def create_vector(x: list, f: list) -> pd.Series:
    l = []
    for index, s in enumerate(x):
        for x in range(f[index]):
            l.append(s)
    return pd.Series(l)


# In[18]:


def all_tendencies_series(series: pd.Series) -> pd.DataFrame:
    return pd.DataFrame(
        {'mean': series.mean(), 'mode': series.mode(),
         'median': series.median(), 'harmonic mean': stats.hmean(series), 'geometric mean': stats.gmean(series)})


# In[19]:


def all_tendencies(list1: list, list2: list) -> pd.DataFrame:
    vec = create_vector(list1, list2)
    return all_tendencies_series(vec)


# All dispersion factors

# In[20]:


def all_dispersion(series: pd.Series) -> pd.DataFrame:
    series.dropna(inplace=True)
    return pd.DataFrame({'min': series.min(), 'max': series.max(), 'interquartile range': stats.iqr(series),
                         'range': np.ptp(series), 'variance': series.var(),
                         'mean absolute deviation': series.mad(), '1st quantile': series.quantile(0.25),
                         '3rd quantile': series.quantile(.75)}, index=[0])


# In[21]:


def draw_boxplot(df: pd.DataFrame) -> plt.boxplot:
    """
    Normalizes the data in the DataFrame so the columns can be better compared in the boxplot. DataFrame columns passed into this function need to be numerical dtypes.
    :rtype: plt.boxplot
    :param df: DataFrame or part of one to be displayed in a boxplot.
    :return: boxplot instance
    """
    new_df: pd.DataFrame = pd.DataFrame()
    plt.figure()
    for column in df.columns.tolist():
        new_df[column] = stats.zscore(df[column])
    new_df.boxplot(new_df.columns.tolist())
    return plt.show()


# In[22]:


def general_regression(x: pd.Series, y: pd.Series, degree: int = 1, exp: bool = False, log: bool = False) -> pd.Series:
    if exp and log:
        raise Exception("Both exponential and logarithmic flags can't be set at the same time")
    if (exp or log) and degree > 1:
        raise Exception("")
    data = pd.DataFrame({'x': x, 'y': y})
    data.reset_index(drop=True, inplace=True)
    func = lambda x: x  # def func(x): return[x]
    inv_func = lambda x: x
    if log:
        func = np.log
        inv_func = np.exp
    if exp:
        func = np.exp
        inv_func = np.log
    sy = data.y.std()
    model = np.polyfit(x, inv_func(y), degree)
    line = np.poly1d(model)
    predict = lambda x: func(line(x))
    data['y_pred'] = pd.Series(predict(x))
    se = math.sqrt(((data.y_pred - data.y) ** 2).mean())
    r2 = 1 - (se ** 2) / (sy ** 2)
    result = [se, r2, predict]
    index = ['se', 'R2', 'predict']
    for i in range(1, len(model) + 1):
        result = np.append(result, model[-i])
        index += chr(i + 96)  # to obtain the characters a,b,...
    result = pd.Series(result)
    result.index = index
    return result


# In[24]:


def linear_regression(x: pd.Series, y: pd.Series) -> list:
    model = np.polyfit(x, y, 1)
    predict = np.poly1d(model)
    xx = np.arange(x.min(), x.max(), (x.max() - x.min()) / 100)
    yy = predict(xx)
    y_pred = predict(x)
    se = math.sqrt(((y_pred - y) ** 2).mean())
    sy = y.std()
    r2 = 1 - (se ** 2) / (sy ** 2)
    return [xx, yy, se, r2]


# In[25]:


def draw_linear_regression_scatter_plot(x: pd.Series, y: pd.Series, x_label: str, y_label: str, title: str) -> None:
    xx, yy, se, r2 = linear_regression(x, y)
    plt.scatter(x, y, alpha=0.2)
    plt.plot(xx, yy, color='red')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.fill_between(xx, yy - 2 * se, yy + 2 * se, color='#FFFF0020')
    plt.show()


# In[26]:


def draw_histogram(series: pd.Series, title: str = 'Title', xlabel: str = 'xLabel', bin_width: int = 0) -> None:
    plt.figure()
    plt.title(title)
    plt.xlabel(xlabel)
    if bin_width is 0:
        series.plot.hist()
    else:
        classes = create_classes_and_cut(series, bin_width)[0]
        series.plot.hist(bins=classes)
    plt.show()


# In[27]:


def all_quartiles(series: pd.Series) -> pd.DataFrame:
    return pd.DataFrame({'25%': series.quantile(0.25), '50%': series.quantile(0.5), '75%': series.quantile(0.75)},
                        index=[0])


# In[28]:


def all_deciles(series: pd.Series) -> pd.DataFrame:
    return pd.DataFrame({'10%': series.quantile(0.1), '20%': series.quantile(0.2), '30%': series.quantile(0.3),
                         '40%': series.quantile(0.4), '50%': series.quantile(0.5), '60%': series.quantile(0.6),
                         '70%': series.quantile(0.7), '80%': series.quantile(0.8), '90%': series.quantile(0.9)},
                        index=[0])


# In[29]:


def draw_single_boxplot(series: pd.Series, title: str, include_outliers: bool = True) -> None:
    df = pd.DataFrame({title: series})
    plt.figure()
    df.boxplot(title, showfliers=include_outliers)
    plt.show()


# In[ ]:


def create_classes_and_cut(series: pd.Series, increment: int) -> list:
    m = series.max().astype(int)
    classes = range(0, m + increment, increment)
    byte_classes = pd.cut(series, classes)
    return [classes, byte_classes]


# #### Converting jupyter notebooks to python scripts
# 
# `jupyter nbconvert --to script EXAM_ANALYTICAL_FUNCTIONS.ipynb`

