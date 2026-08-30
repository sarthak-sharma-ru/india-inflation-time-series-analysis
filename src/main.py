import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

#Read the excel file 
df = pd.read_excel("data/cpi_1894.xlsx")

#print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())

print("\nROWS WITH MISSING INFLATION")
print(df[df["inflation"].isnull()])

df["date"] = pd.to_datetime(
    df["year"].astype(str) + "-" +
    df["month_code"].astype(str) + "-01"
)

print(df[["year", "month", "date"]].head())


df = df.sort_values("date")
#Start from 2014 onwards
df = df[df["date"] >= "2014-01-01"]

df = df[["date", "index", "inflation"]]
print(df.head())
print(df.shape)

df = df.dropna(subset=["inflation"])
df = df.reset_index(drop=True)
print("\nFINAL DATASET")
print(df.head(10))
print(df.isnull().sum())

print(df["date"].min())
print(df["date"].max())

print(df["date"].diff().value_counts())

#Statistical Data
print("\nINFLATION SUMMARY")

print("Mean:", df["inflation"].mean())
print("Median:", df["inflation"].median())
print("Standard Deviation:", df["inflation"].std())
print("Minimum:", df["inflation"].min())
print("Maximum:", df["inflation"].max())

#Graph
plt.figure(figsize=(12, 6))

plt.plot(df["date"], df["inflation"])

plt.title("India Consumer Price Inflation, 2014–2025")
plt.xlabel("Year")
plt.ylabel("Inflation (%)")

plt.grid(True, alpha=0.3)

plt.tight_layout()

#plt.show()

# Augmented Dickey-Fuller test
result = adfuller(df["inflation"])

print("\nADF TEST")
print("ADF Statistic:", result[0])
print("p-value:", result[1])

# Rolling statistics
df["rolling_mean"] = df["inflation"].rolling(12).mean()
df["rolling_std"] = df["inflation"].rolling(12).std()

print("\nROLLING STATISTICS")
print(df[["date", "inflation", "rolling_mean", "rolling_std"]].tail(10))

plt.figure(figsize=(12, 6))

plt.plot(df["date"], df["inflation"], label="Inflation")
plt.plot(df["date"], df["rolling_mean"], label="12-Month Rolling Mean")

plt.title("Inflation and 12-Month Rolling Mean")
plt.xlabel("Year")
plt.ylabel("Inflation (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

#plt.show()
# ACF
plt.figure(figsize=(12, 5))
plot_acf(df["inflation"], lags=24)
plt.title("Autocorrelation of Inflation")
plt.tight_layout()
#plt.show()

# PACF
plt.figure(figsize=(12, 5))
plot_pacf(df["inflation"], lags=24)
plt.title("Partial Autocorrelation of Inflation")
plt.tight_layout()
#plt.show()

# First difference of inflation
df["inflation_diff"] = df["inflation"].diff()

print("\nFIRST DIFFERENCE")
print(df[["date", "inflation", "inflation_diff"]].head(10))

df["inflation_diff"].dropna()

# ADF test on differenced inflation

diff_result = adfuller(df["inflation_diff"].dropna())
diff_data = df["inflation_diff"].dropna()

print("\nADF TEST - DIFFERENCED INFLATION")
print("ADF Statistic:", diff_result[0])
print("p-value:", diff_result[1])

# ACF plot
plot_acf(diff_data, lags=24)
plt.title("ACF of Differenced Inflation")
#plt.show()

#PACF plot
plot_pacf(diff_data, lags=24)
plt.title("PACF of Differenced Inflation")
#plt.show()

# Fit ARIMA(1,1,1)
model_111 = ARIMA(df["inflation"], order=(1, 1, 1))
result_111 = model_111.fit()

print("\nARIMA(1,1,1) RESULTS")
print(result_111.summary())

from statsmodels.tsa.arima.model import ARIMA

# Candidate ARIMA models
models = {
    "ARIMA(1,1,0)": (1, 1, 0),
    "ARIMA(0,1,1)": (0, 1, 1),
    "ARIMA(1,1,1)": (1, 1, 1),
    "ARIMA(1,1,2)": (1, 1, 2),
    "ARIMA(2,1,1)": (2, 1, 1),
    "ARIMA(2,1,2)": (2, 1, 2)
}

print("\nMODEL COMPARISON")

for name, order in models.items():

    model = ARIMA(df["inflation"], order=order)
    result = model.fit()

    print(
        name,
        "| AIC:", round(result.aic, 2),
        "| BIC:", round(result.bic, 2)
    )

    # FINAL CANDIDATE MODEL

final_model = ARIMA(df["inflation"], order=(2, 1, 1))

final_result = final_model.fit()

print("\nFINAL MODEL: ARIMA(2,1,1)")

print(final_result.summary())

# TRAIN-TEST SPLIT

train = df.iloc[:-12]
test = df.iloc[-12:]

print("\nTRAINING DATA")
print(train.shape)

print("\nTESTING DATA")
print(test.shape)

print("\nTEST DATA")
print(test)

# FIT FINAL ARIMA MODEL

final_model = ARIMA(
    train["inflation"],
    order=(2, 1, 1)
)

final_model_fit = final_model.fit()

print("\nFINAL MODEL SUMMARY")
print(final_model_fit.summary())

# FORECAST THE TEST PERIOD


forecast = final_model_fit.forecast(
    steps=len(test)
)

print("\nFORECASTED INFLATION")
print(forecast)

#Compare Actual and Predicted
comparison = pd.DataFrame({
    "date": test["date"].values,
    "actual_inflation": test["inflation"].values,
    "forecasted_inflation": forecast.values
})

print("\nACTUAL VS FORECAST")
print(comparison)

mae = mean_absolute_error(
    test["inflation"],
    forecast
)

mse = mean_squared_error(
    test["inflation"],
    forecast
)

rmse = mse ** 0.5

print("\nFORECAST ACCURACY")
print("MAE:", mae)
print("RMSE:", rmse)

# ACTUAL VS FORECAST GRAPH

plt.figure(figsize=(12, 6))

plt.plot(
    test["date"],
    test["inflation"],
    label="Actual Inflation",
    marker="o"
)

plt.plot(
    test["date"],
    forecast.values,
    label="Forecasted Inflation",
    marker="o"
)

plt.title("Actual vs Forecasted Inflation (2025)")
plt.xlabel("Date")
plt.ylabel("Inflation (%)")

plt.legend()
plt.grid(True)

plt.show()

# NAIVE FORECAST BASELINE

last_train_value = train["inflation"].iloc[-1]

naive_forecast = [last_train_value] * len(test)

print("\nNAIVE FORECAST")
print(naive_forecast)

# NAIVE FORECAST ACCURACY

naive_mae = mean_absolute_error(
    test["inflation"],
    naive_forecast
)

naive_mse = mean_squared_error(
    test["inflation"],
    naive_forecast
)

naive_rmse = naive_mse ** 0.5

print("\nNAIVE FORECAST ACCURACY")
print("MAE:", naive_mae)
print("RMSE:", naive_rmse)

#FINAL MODEL COMPARISON

model_comparison = pd.DataFrame({
    "Model": [
        "ARIMA(2,1,1)",
        "Naive Forecast"
    ],
    
    "MAE": [
        mae,
        naive_mae
    ],
    
    "RMSE": [
        rmse,
        naive_rmse
    ]
})

print("\nFINAL MODEL COMPARISON")
print(model_comparison)

# FINAL ARIMA MODEL USING FULL DATA

final_full_model = ARIMA(
    df["inflation"],
    order=(2, 1, 1)
)

final_full_model_fit = final_full_model.fit()

print("\nFINAL ARIMA MODEL FITTED ON FULL DATA")
print(final_full_model_fit.summary())

# FORECAST NEXT 12 MONTHS

future_forecast = final_full_model_fit.forecast(steps=12)

print("\nFORECAST FOR NEXT 12 MONTHS")
print(future_forecast)

# CREATE DATES FOR NEXT 12 MONTHS

forecast_dates = pd.date_range(
    start="2026-01-01",
    periods=12,
    freq="MS"
)

# CREATE FORECAST DATAFRAME

forecast_df = pd.DataFrame({
    "date": forecast_dates,
    "forecasted_inflation": forecast
})

print("\nFORECAST FOR 2026")

print(forecast_df)

#FINAL PREDCITED GRAPH

plt.figure(figsize=(12, 6))

# Historical inflation
plt.plot(
    df["date"],
    df["inflation"],
    label="Historical Inflation"
)

# Forecasted inflation
plt.plot(
    forecast_df["date"],
    forecast_df["forecasted_inflation"],
    label="Forecasted Inflation",
    linestyle="--"
)

# Mark where forecasting begins
plt.axvline(
    x=pd.Timestamp("2026-01-01"),
    linestyle=":"
)

plt.title("India Inflation: Historical Data and 2026 Forecast")
plt.xlabel("Year")
plt.ylabel("Inflation (%)")

plt.legend()
plt.grid(True)

plt.show()

#Saving Data

# SAVE 2026 FORECAST

forecast_df.to_csv(
    "data/forecast_2026.csv",
    index=False
)

print("\n2026 forecast saved successfully!")
