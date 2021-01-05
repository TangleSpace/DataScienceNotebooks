# Some imports to get us active
from datetime import datetime, timedelta
from pandas.plotting import table
from datetime import datetime, timedelta
from pandas.plotting import autocorrelation_plot,lag_plot
from statsmodels.tsa.seasonal import STL
from scipy.spatial.distance import pdist, squareform
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from hurst import compute_Hc,random_walk
from statsmodels.tsa.stattools import kpss
from statsmodels.tsa.stattools import adfuller
from gatspy.periodic import LombScargleFast
from scipy.stats import *
from sklearn.preprocessing import *
from matplotlib.patches import Rectangle, FancyArrowPatch
from sklearn.linear_model import LinearRegression

import pandas_ta as ta
import staircase as sc
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
sns.set(style="whitegrid")



def compute_hurst(ts,lags=[2,100]):
    ts = np.asarray(ts)
    lag_range = range(lags[0], lags[1])
    tau = [np.sqrt(np.std(np.subtract(ts[lag:], ts[:-lag]))) for lag in lag_range]
    m = np.polyfit(np.log(lag_range), np.log(tau), 1)
    return m[0]*2