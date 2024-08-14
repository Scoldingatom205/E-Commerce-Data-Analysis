# Install and Import Dependencies
! pip install pmdarima

import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
import matplotlib.pyplot as plt

# Function to prepare data for forecasting by dimension (continent, segment, category)
def prepare_forecasting_data(data, dimension):
    dimension_data = {} # Initialize a dictionary to hold data for each category or segment
     # Iterate through unique values of the dimension and create a DataFrame for each
    for dim_value in data[dimension].unique():
        dim_df = data[data[dimension] == dim_value]
      # Set order_date as the index and resample to monthly sales
        dim_df.set_index('order_date', inplace=True)
        dim_df = dim_df['sales'].resample('M').sum()
        dimension_data[dim_value] = dim_df
    return dimension_data

def find_best_sarima_params(data_dict):
    best_params = {}
    for dim_value, data in data_dict.items():
        model = auto_arima(data, seasonal=True, m=12, trace=True, error_action='ignore', suppress_warnings=True)
        best_params[dim_value] = (model.order, model.seasonal_order)
        print(f"{dim_value} - Best ARIMA order: {model.order}x{model.seasonal_order}")
    return best_params

# Function to forecast using SARIMA model
def forecast_with_sarima(data_dict, sarima_params, dimension_name):
    forecast_results = {}
    # Iterate over each dimension's data to forecast
    for dim_value, params in sarima_params.items():
        order, seasonal_order = params
        data = data_dict[dim_value]
        
        # Fit the SARIMA model with specified parameters
        model = SARIMAX(data, order=order, seasonal_order=seasonal_order)
        model_fit = model.fit(disp=False)
        
        # Forecast the next 12 months
        forecast = model_fit.get_forecast(steps=12)
        forecast_index = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=12, freq='M')
        forecast_series = pd.Series(forecast.predicted_mean.values, index=forecast_index)

        # Store forecast in dictionary
        forecast_results[dim_value] = forecast_series
    return forecast_results

# Plotting the forecast
def plot_forecast(data_dict, forecast_results, dimension_name):
    for dim_value, forecast_series in forecast_results.items():
        data = data_dict[dim_value]

        plt.figure(figsize=(10, 4))
        plt.plot(data.index, data, label='Actual Sales')
        plt.plot(forecast_series.index, forecast_series, label='Forecast', color='green')
        plt.title(f'Sales Forecast for {dim_value} in {dimension_name}')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.legend()
        plt.grid(True)
        plt.show()
