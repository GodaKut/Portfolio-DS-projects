import pandas as pd
import numpy as np
from statsmodels.stats.stattools import durbin_watson
import statsmodels.api as sm


def check_logistic_reg_assumptions(results, data, feature):
    result_df = pd.DataFrame(
        columns=["Tests", "Statistic", "p-value", "Result", "Assumption pass"]
    )

    X_data = data[feature].values.reshape(-1, 1)
    x_data_with_const = sm.add_constant(X_data)
    predicted_probs = results.predict(x_data_with_const)
    residuals = data["quality_binary"].values - predicted_probs
    dw_stat = durbin_watson(residuals)

    if dw_stat > 1.5 and dw_stat < 2.5:
        dw_rez = "Autocorrelation not found"
        dw_pass = "Pass"
    else:
        dw_rez = "Autocorrelation found"
        dw_pass = "Fail"
    result_df.loc[len(result_df.index)] = [
        "Durbin-Watson Test:",
        dw_stat,
        "",
        dw_rez,
        dw_pass,
    ]

    if np.any(np.isinf(results.params)):
        ps_rez = "Perfect separation detected!"
        ps_pass = "Fail"
    else:
        ps_rez = "Perfect separation NOT detected."
        ps_pass = "Pass"
    result_df.loc[len(result_df.index)] = [
        "Perfect separation Test:",
        "",
        "",
        ps_rez,
        ps_pass,
    ]
    Test_data = data.copy()
    Test_data["log_X"] = np.log(Test_data[feature] + 1e-5)
    Test_data["interaction"] = Test_data[feature] * Test_data["log_X"]
    X = sm.add_constant(Test_data[[feature, "interaction"]])
    y = Test_data["quality_binary"]
    model = sm.Logit(y, X)
    result = model.fit()
    variable_names = result.model.exog_names
    p_values_with_names = dict(zip(variable_names, result.pvalues))
    if p_values_with_names["interaction"] < 0.05:
        bt_rez = "Relationship is non-linear"
        bt_pass = "Fail"
    else:
        bt_rez = "Relationship is linear"
        bt_pass = "Pass"
    result_df.loc[len(result_df.index)] = [
        "Box-Tidwell Test:",
        "",
        p_values_with_names["interaction"],
        bt_rez,
        bt_pass,
    ]

    result_df.set_index(["Tests"], inplace=True)
    return result_df
