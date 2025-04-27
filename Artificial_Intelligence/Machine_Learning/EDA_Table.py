# Goal: Test bivariate relationships between predictors and targets

import pandas as pd
from scipy.stats import fisher_exact, mannwhitneyu, spearmanr

# Merge data
df = pd.merge(X_num_train_full, df_cat, on='id')
df = pd.merge(df, y_train_full, on='id')

# Define outcomes
outcomes = ['Outcome_1', 'Outcome_2']

# Store results
results = []

# Loop
for outcome in outcomes:
    for var in df.columns[1:-2]:  # Assume last 2 columns are outcomes
        if df[var].dtype.kind in 'iufc':  # i: int, u: unsigned int, f: float, c: complex
            # Continuous predictor
            group0 = df[df[outcome] == 0][var]
            group1 = df[df[outcome] == 1][var]
            # Check if both groups have enough observations
            if len(group0) > 0 and len(group1) > 0:
                try:
                    # Mann-Whitney U
                    _, p_mw = mannwhitneyu(group0, group1, alternative='two-sided', nan_policy='omit')
                    # Spearman correlation
                    corr, p_corr = spearmanr(df[var], df[outcome], nan_policy='omit')
                    test_used = "Mann-Whitney U + Spearman"
                    p_value = min(p_mw, p_corr)
                except Exception as e:
                    test_used = "Mann-Whitney U + Spearman (failed)"
                    p_value = np.nan
            else:
                test_used = "Mann-Whitney U + Spearman (insufficient data)"
                p_value = np.nan
        
        else:
            # Categorical predictor
            try:
                contingency_table = pd.crosstab(df[var], df[outcome])
                # Fisher's Exact Test
                _, p_value = fisher_exact(contingency_table)
                test_used = "Fisher's Exact Test"
            except Exception as e:
                test_used = "Categorical Test (failed)"
                p_value = np.nan
        
        results.append({
            'Outcome': outcome,
            'Predictor': var,
            'Test Used': test_used,
            'P-Value': p_value
        })

# Results table
results_df = pd.DataFrame(results)
results_df

from datetime import datetime
time_str = datetime.today().strftime('%Y%m%d')
filename = f"{time_str}_FeatureSelection_Update.csv"
results_df.to_csv(filename, index=False)
