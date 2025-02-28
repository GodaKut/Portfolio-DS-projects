"""
Tukey distinguishes between possible and probable outliers.
A possible outlier is located between the inner and the outer fence,
 whereas a probable outlier is located outside the outer fence.

While the inner (often confused with the whiskers) and outer fence 
are usually not shown on the actual box plot, 
they can be calculated using the interquartile range (IQR)

Source:
https://towardsdatascience.com/detecting-and-treating-outliers-in-python-part-1-4ece5098b755

I have modified the method to include percentage of potential data loss if 
probable outlier were to be removed. 

"""
import pandas as pd


def tukey_fences_method(df, variable):
    df[variable] = pd.to_numeric(df[variable], errors="coerce")
    # Takes two parameters: dataframe & variable of interest as string
    q1 = df[variable].quantile(0.25)
    q3 = df[variable].quantile(0.75)
    iqr = q3 - q1
    inner_fence = 1.5 * iqr
    outer_fence = 3 * iqr

    # inner fence lower and upper end
    inner_fence_le = q1 - inner_fence
    inner_fence_ue = q3 + inner_fence

    # outer fence lower and upper end
    outer_fence_le = q1 - outer_fence
    outer_fence_ue = q3 + outer_fence

    outliers_prob = []
    for index, x in enumerate(df[variable]):
        if (x <= outer_fence_le) | (x >= outer_fence_ue):
            outliers_prob.append(index)
    data_loss_proc = str(round(len(outliers_prob) * 100 / len(df[variable]), 2)) + " %"

    return outliers_prob, data_loss_proc
