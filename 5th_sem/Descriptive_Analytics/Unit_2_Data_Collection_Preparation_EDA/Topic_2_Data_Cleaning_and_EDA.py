# Data Preparation, Missing Values, Outliers and EDA in Python
import numpy as np

data = {
    'Age': [25, 30, np.nan, 35, 40, 150, 45, 29, 31, 38],
    'Salary': [50000, 60000, 55000, np.nan, 65000, 70000, 48000, 52000, 61000, 75000]
}

ages = np.array(data['Age'])
salaries = np.array(data['Salary'])

# Impute
ages[np.isnan(ages)] = np.nanmedian(ages)
salaries[np.isnan(salaries)] = np.nanmedian(salaries)

# Outliers
q75, q25 = np.percentile(ages, [75, 25])
iqr = q75 - q25
lower, upper = q25 - 1.5 * iqr, q75 + 1.5 * iqr
ages_capped = np.clip(ages, lower, upper)

print("--- Data Preprocessing ---")
print("Capped Ages:", ages_capped)
