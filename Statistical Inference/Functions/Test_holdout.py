import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import statsmodels.api as sm


def test_holdout_model(feature, results, x_train, y_train, holdout_df):
    X_holdout_alco = sm.add_constant(holdout_df[feature])
    y_pred_holdout_alco = results.predict(X_holdout_alco)
    y_holdout = holdout_df["quality"]

    mae_H = mean_absolute_error(y_holdout, y_pred_holdout_alco)
    mse_H = mean_squared_error(y_holdout, y_pred_holdout_alco)
    rmse_H = np.sqrt(mse_H)
    r2_H = r2_score(y_holdout, y_pred_holdout_alco)

    y_pred_alco = results.predict(x_train)
    mae = mean_absolute_error(y_train, y_pred_alco)
    mse = mean_squared_error(y_train, y_pred_alco)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_train, y_pred_alco)

    stat_rez = pd.DataFrame(
        index=[
            "Mean Absolute Error (MAE)",
            "Mean Squared Error (MSE)",
            "Root Mean Squared Error (RMSE)",
            "R-squared (R²)",
        ],
        columns=["Training data", "Holdout data"],
    )
    stat_rez["Training data"] = [mae, mse, rmse, r2]
    stat_rez["Holdout data"] = [mae_H, mse_H, rmse_H, r2_H]

    return stat_rez
