from ucimlrepo import fetch_ucirepo 
import pandas as pd

# fetch dataset 
cdc_diabetes_health_indicators = fetch_ucirepo(id=891) 
  
# data (as pandas dataframes) 
X = cdc_diabetes_health_indicators.data.features 
y = cdc_diabetes_health_indicators.data.targets 
 
# save as csv
X['diabetes'] = y.iloc[:,0]
X.to_csv("data.csv")
