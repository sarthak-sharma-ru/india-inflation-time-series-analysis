# India Inflation Time Series Analysis and Forecasting

## Project Overview

This project analyses historical consumer price inflation in India and develops a time-series forecasting model using the ARIMA methodology.

The analysis examines monthly inflation data from **2014 to 2025**, investigates the statistical properties of the series, compares forecasting performance with a naïve benchmark, and generates a **12-month inflation forecast for 2026**.

The project was developed using Python as an independent research project.

---

## Objectives

The main objectives of this project are to:

- Analyse historical trends in India's consumer price inflation.
- Perform exploratory and descriptive analysis of the inflation time series.
- Test the series for stationarity using the Augmented Dickey-Fuller (ADF) test.
- Apply differencing to transform the data into a stationary series.
- Use Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) analysis to guide ARIMA model specification.
- Compare ARIMA models using information criteria.
- Evaluate out-of-sample forecasting performance using MAE and RMSE.
- Compare the ARIMA model with a naïve forecasting benchmark.
- Generate a 12-month forecast for India's inflation in 2026.

---

## Dataset

The project uses monthly Consumer Price Index (CPI) data for India.

**Time Period:** 2014–2025  
**Frequency:** Monthly

The dataset used in this project is available in:

```text
cpi_1894.xlsx
