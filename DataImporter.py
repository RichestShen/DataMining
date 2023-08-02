import pandas as pd
import numpy as np
import scipy as spy
import matplotlib as mpl
import seaborn as sns
from matplotlib import pyplot as plt
from pandas import DataFrame, Series
# from numpy import *

'''
Import packages used frequently in advance, and customized some settings according
to my demand,
so that we can reduce some repeated routines and make our code more readable.

To use this file to accelerate your data processing, use the command below
at the very beginning of your program:
    from DataImporter import *
author: Qianyi Shen
date: 2022.09.10
'''

# Customize matplotlib. If default settings needed, use command 'mpl.rcdefaults'.
mpl.rcParams.update({
    'font.sans-serif': ['Songti SC'],  # 'Songti SC' also works. 'Arial Unicode MS' in Windows
    # Set a font which supports Zh-CN. This font works well on
    # macOS Monterey 12.5.1,
    # if it doesn't work on your PC, try another instead.
    'savefig.dpi': 600,
    # Set dpi to make the graph more clear, change it if numbers become to large.
    'savefig.transparent': True,
    # Set a transparent background when saving graphs. Set 'False' when unnecessary.
    # Note that this config works only when you're saving graphs.
    'text.usetex': False,
    # Add support for LaTeX, set 'True' if needed.
    # Note that Zh-CN isn't support yet, because it uses pdfLaTeX.
})


# Set some color collections to make the graphs look more professional.
light_color = {
    '#005EAD', '#AF6DE5', '#719FFB', '#1CAC99', '#FE9499', '#4A8FDE', '#F8A13E',
    '#4DE890', '#2178B8', '#77A2E8', '#F86067', '#26C4B8', '#FE8006', '#0094C5',
    '#5AE7E4', '#2E9F79', '#3638AE', '#FF7F00', '#FBBF72', '#FA9B97', '#30A02D',
    '#B0E188', '#2077B5', '#A8CBE4', '#F5FFB3', '#BEECAF', '#61D0BA', '#05B9C7',
}
darker_color = {
    '#2878b5', '#9ac9db', '#f8ac8c', '#c82423', '#ff8884', 
}
blue_color = {
    '#4B59C2', '#5A77BB', '#4A94C5', '#3B2E7E', '#013370', '#1A2946',
}
tech_style_color = {
    '#F53B57', '#3C40C6', '#3C40C6', '#00D8D6', '#05C46B', '#C9C9C9',
}
