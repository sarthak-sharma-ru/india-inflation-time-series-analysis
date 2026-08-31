# India Inflation Time Series Analysis and Forecasting

## Project Overview

This project analyses historical consumer price inflation in India and develops a time-series forecasting model using the ARIMA methodology.

The analysis examines monthly inflation data from **2014 to 2025**, investigates the statistical properties of the series, compares forecasting performance with a naïve benchmark, and generates a **12-month inflation forecast for 2026**.

The project was developed using Python as an independent research project.

---

## Objectives

The main objectives of this project are to:

* Analyse historical trends in India's consumer price inflation.
* Perform exploratory and descriptive analysis of the inflation time series.
* Test the series for stationarity using the Augmented Dickey-Fuller (ADF) test.
* Apply differencing to transform the data into a stationary series.
* Use Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) analysis to guide ARIMA model specification.
* Compare ARIMA models using information criteria.
* Evaluate out-of-sample forecasting performance using MAE and RMSE.
* Compare the ARIMA model with a naïve forecasting benchmark.
* Generate a 12-month forecast for India's inflation in 2026.

---

## Dataset

The project uses monthly Consumer Price Index (CPI) data for India.

**Time Period:** 2014–2025
**Frequency:** Monthly

The dataset used in this project is available in:

`cpi_1894.xlsx`

---

## Methodology

### 1. Data Preparation

The CPI dataset was loaded and processed using Python libraries for data analysis.

The data was cleaned and transformed into a time-series format suitable for forecasting analysis.

### 2. Exploratory Data Analysis

Historical inflation trends were examined to understand:

* Changes in inflation over time.
* Periods of high and low inflation.
* Volatility and fluctuations in the inflation series.
* General patterns in India's historical inflation.

### 3. Stationarity Testing

The Augmented Dickey-Fuller (ADF) test was used to evaluate whether the inflation series was stationary.

Where necessary, first-order differencing was applied before ARIMA modelling.

### 4. ARIMA Model Development

Multiple ARIMA specifications were considered and compared using:

* Akaike Information Criterion (AIC)
* Bayesian Information Criterion (BIC)

The final selected model was:

`ARIMA(2,1,1)`

### 5. Model Evaluation

Forecasting performance was evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

The ARIMA model was also compared with a naïve forecasting benchmark.

---

## Model Comparison

| Model          |  MAE | RMSE |
| -------------- | ---: | ---: |
| ARIMA(2,1,1)   | 3.24 | 3.45 |
| Naïve Forecast | 2.99 | 3.12 |

The results show that the naïve forecasting benchmark achieved lower MAE and RMSE than the evaluated ARIMA model during the out-of-sample testing period.

This highlights the importance of comparing statistical forecasting models with simple benchmark methods rather than assuming that a more complex model will necessarily produce better forecasts.

---

## Forecast for 2026

The final ARIMA model was used to generate a 12-month forecast for India's inflation.

| Date           | Forecasted Inflation (%) |
| -------------- | -----------------------: |
| January 2026   |                     5.38 |
| February 2026  |                     5.53 |
| March 2026     |                     5.14 |
| April 2026     |                     5.46 |
| May 2026       |                     5.45 |
| June 2026      |                     5.46 |
| July 2026      |                     5.47 |
| August 2026    |                     5.47 |
| September 2026 |                     5.47 |
| October 2026   |                     5.47 |
| November 2026  |                     5.47 |
| December 2026  |                     5.47 |

The model forecasts inflation remaining relatively stable at approximately **5.4%–5.5%** during most of 2026.

---

## Results and Key Findings

The analysis produced the following key findings:

* India's inflation rate experienced significant fluctuations during the 2014–2025 period.
* The time series was examined for stationarity before ARIMA modelling.
* First-order differencing was applied as part of the ARIMA modelling process.
* An ARIMA(2,1,1) model was selected as the preferred model among the evaluated ARIMA specifications.
* Forecast accuracy was evaluated using MAE and RMSE.
* The naïve forecasting benchmark achieved lower forecast errors than the ARIMA model during the evaluation period.
* The results demonstrate the importance of benchmarking advanced forecasting models against simpler alternatives.
* The ARIMA model generated a relatively stable 12-month forecast for India's inflation in 2026.

---

## Visualisation

The project includes a visual comparison of historical inflation data and the forecast.

![India Inflation Historical Data and Forecast](Inflation%20vs%20Time%20Graph.png)

---

## Project Structure

```text
india-inflation-time-series-analysis/
│
├── src/
│   └── main.py
│
├── cpi_1894.xlsx
│
├── Inflation vs Time Graph.png
│
├── README.md
│
├── LICENSE
│
└── .gitignore
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Statsmodels
* OpenPyXL

---

## Time-Series Techniques Used

* Exploratory Data Analysis
* Augmented Dickey-Fuller (ADF) Test
* First-Order Differencing
* Autocorrelation Function (ACF)
* Partial Autocorrelation Function (PACF)
* ARIMA Modelling
* AIC and BIC Model Comparison
* Naïve Forecast Benchmarking
* MAE and RMSE Forecast Evaluation

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/india-inflation-time-series-analysis.git
```

### 2. Navigate to the project directory

```bash
cd india-inflation-time-series-analysis
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib statsmodels openpyxl
```

### 4. Run the analysis

```bash
python src/main.py
```

---

## Future Improvements

Possible extensions of this project include:

* Testing SARIMA models to account for seasonality.
* Comparing ARIMA models with machine learning and deep learning forecasting models.
* Incorporating macroeconomic variables as exogenous predictors.
* Using multivariate time-series models.
* Performing rolling-window forecast evaluation.
* Developing prediction intervals for future forecasts.
* Comparing the forecasts with actual inflation data as new observations become available.

---

## Author

**Sarthak Sharma**

BTech Computer Science & Engineering (Artificial Intelligence and Machine Learning)
Vellore Institute of Technology – Andhra Pradesh

**Interests:** Economics, Econometrics, Financial Markets, Quantitative Analysis, Machine Learning, and Investment Research.

