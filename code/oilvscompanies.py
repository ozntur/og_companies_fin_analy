import datetime
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl

mpl.rc('figure', figsize=(10,10))
mpl.__version__

style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end   = datetime.datetime(2020, 1, 1)

mygroup = ['CL=F','DVN', 'APA', 'EOG', 'COP', 'MRO', 'NBL', 'PXD', 'COG', 'PXD','EQT','DNR','FANG','XOM','CVX', 'OXY','CXO']

df = web.DataReader(mygroup ,'yahoo',start=start,end=end)['Adj Close']

print(df.columns)

for a in mygroup[1:]:
    xs = df['CL=F']
    ys = df[a]
    plt.scatter(xs,ys, label = a)
    

#plt.scatter(x, y, label = 'DEVON')

plt.xlabel('Crude Oil')
plt.ylabel('O&G Companies')
plt.legend()
plt.show()

from sklearn.metrics import r2_score
from scipy.stats import pearsonr

for b in mygroup[1:]:
    x = df['CL=F'][df['CL=F'].notna() & df[b].notna()].values
    y = df[b][df['CL=F'].notna() & df[b].notna()].values
    print(b, 'r2', r2_score(x, y, multioutput='uniform_average'))
    print(b, 'pearsonsr', pearsonr(x,y))




corr = df.corr()

plt.imshow(corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)
plt.show()


import seaborn as sns; sns.set(style = "ticks", color_codes = True)
g = sns.pairplot(df)