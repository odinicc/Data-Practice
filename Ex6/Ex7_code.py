import pandas as pd
import numpy as np
from sklearn import preprocessing
import os 
import seaborn as sns

df = pd.read_csv ('kc_house_data.csv')
print(df)

#check data types
df.dtypes

#convert values
df['bedrooms'] = df['bedrooms'].astype(np.int64)
df['bathrooms'] = df['bathrooms'].astype(np.int64)
df['floors'] = df['floors'].astype(np.int64)

#convert date to int 
df['date']= pd.to_datetime(df['date'])
df['date'] = pd.to_numeric(df['date'])

#Normalize  dataframe
df = (df - df.mean()) / (df.max() - df.min())

#check data types
df.dtypes

#check correlation matrix
df.corr()

#find columns with max correlation
correlation = df.corr(method='pearson')
columns = correlation.nlargest(12, 'price').index
columns

#place the target data price in a separate dataframe y_data . x_data
y_data = df['price']
x_data = df[columns]  
x_data=df.drop('price',axis=1)

#split the series 
import numpy as np
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)

#import libs
import sklearn
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import sklearn
from scipy import stats
import matplotlib.pyplot as plt



def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
   
    fig, ax = plt.subplots()
    #define first graph style and second graph style
    sns.kdeplot(RedFunction, color='red', ax=ax, label=RedName)
    sns.kdeplot(BlueFunction, color='blue', ax=ax,label=BlueName )
    
    #define titles and axis
    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of flats')
    
    #show plot
    ax.legend()
    plt.show()
    plt.close()

#Run polinomial regression with order = 2
pr1=PolynomialFeatures(degree=2)
x_train_pr1=pr1.fit_transform(x_train)
x_test_pr1=pr1.fit_transform(x_test)
poly1 = LinearRegression()
poly1.fit(x_train_pr1,y_train)
yhat_test = poly1.predict(x_test_pr1)

#Estimate R2 
poly1.score(x_test_pr1, y_test)

#Draw the graph
DistributionPlot(y_test,yhat_test,"Actual Values (Test)","Predicted Values (Test)",'hi')

# Find the best order for model
#POLINOMIAL REGRESSION

Rsqu_test = []
order = [1, 2, 3]
lr = LinearRegression()
for n in order:
    pr = PolynomialFeatures(degree=n)
    
    x_train_pr = pr.fit_transform(x_train)
    x_test_pr = pr.fit_transform(x_test)    
    lr.fit(x_train_pr, y_train)
   
    Rsqu_test.append(lr.score(x_test_pr, y_test))

plt.plot(order, Rsqu_test)
plt.xlabel('order')
plt.ylabel('R^2')
plt.title('R^2 Using Test Data')
# Best order for regression is 2


#Looking for best alpha
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
Ridge(normalize=True)

parameters= [{'alpha': [0.001,0.1,1, 10, 100, 1000,10000,100000,100000],'normalize':[True,False]} ]
Grid2 = GridSearchCV(Ridge(), parameters,cv=4)
Grid2.fit(x_data,y_data)
Grid2.best_estimator_

#Ridge(alpha=1, normalize=True)

pr1=PolynomialFeatures(degree=2)
x_train_pr1=pr1.fit_transform(x_train)
x_test_pr1=pr1.fit_transform(x_test)
RigeModel = Ridge(alpha=0.001, normalize=True)
RigeModel.fit(x_train_pr1,y_train)
yhat_test = RigeModel.predict(x_test_pr1)

#calcaulate R2
RigeModel.score(x_test_pr1, y_test)

#draw the graph with alpha = 1
DistributionPlot(y_test,yhat_test,"Actual Values (Test)","Predicted Values (Test)",'hi')


#TRY RGBOOST
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor

HCBR_Model = HistGradientBoostingRegressor()
HCBR_Model.fit(x_train,y_train)
yhat_test = HCBR_Model.predict(x_test)
HCBR_Model.score(x_test, y_test)

#draw the graph with Gradient Boosting Model
DistributionPlot(y_test,yhat_test,"Actual Values (Test)","Predicted Values (Test)",'hi')

