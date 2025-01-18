import pandas as pd
import numpy as np
from statsmodels.stats.stattools import durbin_watson
import statsmodels.stats.api as sms
import statsmodels.api as sm
import scipy.stats as stats


def check_linear_reg_assumptions(results):
    result_df = pd.DataFrame(
        columns=["Tests", "Statistic", "p-value", "Result", "Assumption passed"]
    )

    hc_stat, hc_pvalue = sm.stats.linear_rainbow(results)
    if hc_pvalue < 0.05:
        hc_rez = "Relationship is non-linear"
        hc_pass = "Fail"
    else:
        hc_rez = "Relationship is linear"
        hc_pass = "Pass"

    result_df.loc[len(result_df.index)] = [
        "Harvey-Collier Test:",
        hc_stat,
        hc_pvalue,
        hc_rez,
        hc_pass,
    ]

    bp_test = sms.het_breuschpagan(results.resid, results.model.exog)
    lm_stat, lm_pvalue, f_stat, f_pvalue = bp_test
    if lm_pvalue > 0.05:
        lm_rez = "Heteroscedasticity not found"
        lm_pass = "Pass"
    else:
        lm_rez = "Heteroscedasticity found"
        lm_pass = "Fail"

    if lm_pvalue > 0.05:
        f_rez = "Heteroscedasticity not found"
        f_pass = "Pass"
    else:
        f_rez = "Heteroscedasticity found"
        f_pass = "Fail"
    result_df.loc[len(result_df.index)] = [
        "Breusch-Pagan Test: LM",
        lm_stat,
        lm_pvalue,
        lm_rez,
        lm_pass,
    ]
    result_df.loc[len(result_df.index)] = [
        "Breusch-Pagan Test: F",
        f_stat,
        f_pvalue,
        f_rez,
        f_pass,
    ]

    dw_stat = durbin_watson(results.resid)
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

    residuals = results.resid
    mean_resid = np.mean(residuals)
    std_resid = np.std(residuals)
    standardized_residuals = (residuals - mean_resid) / std_resid
    ks_stat, ks_pvalue = stats.kstest(standardized_residuals, "norm")
    if ks_pvalue > 0.05:
        ks_rez = "Residuals are normally distributed"
        ks_pass = "Pass"
    else:
        ks_rez = "Residuals are non-normally distributed"
        ks_pass = "Fail"
    result_df.loc[len(result_df.index)] = [
        "Kolmogorov-Smirnov Test:",
        ks_stat,
        ks_pvalue,
        ks_rez,
        ks_pass,
    ]

    result_df.set_index(["Tests"], inplace=True)
    return result_df
