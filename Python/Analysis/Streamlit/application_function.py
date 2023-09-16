import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

def pca_maker(df):
  numeric_col_lst = []
  categorical_col_lst = []
  
  for col in df.columns:
      if df[col].dtype == np.float64 or df[col].dtype == np.int64:
          numeric_col_lst.append(df[col])
      
      else:
          categorical_col_lst.append(df[col])
  
  numeric_df = pd.concat(numeric_col_lst, axis=1)
  categorical_df = pd.concat(categorical_col_lst, axis=1)
  
  new_numeric_df = numeric_df.fillna(numeric_df.mean())
  
  scaler_obj = StandardScaler()
  scaled_values = scaler_obj.fit_transform(new_numeric_df)
  
  pca_columns = ["PCA_" + str(x+1) for x in range(0, 24)]
  
  pca = PCA()
  pca_data = pca.fit_transform(scaled_values)
  pca_df = pd.DataFrame(pca_data)
  pca_df.rename(columns={x:"PCA_" + str(x+1) for x in range(0, 24)}, inplace=True)
  
  output = pd.concat([df, pca_df], axis=1)
  
  return output, categorical_col_lst, pca_columns