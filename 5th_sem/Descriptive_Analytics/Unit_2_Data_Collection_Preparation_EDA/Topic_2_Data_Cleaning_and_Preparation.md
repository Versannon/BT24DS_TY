# Topic 2: Data Cleaning and Preparation

## The Importance of Data Cleaning
Imagine you want to bake a cake, but your flour is full of pebbles, and you are missing sugar. If you try to bake with these ingredients, your cake will be ruined. 

The same is true for data analytics. Real-world data is almost never perfect. It has missing pieces, typos, and weird anomalies. **Data Cleaning** is the process of finding and fixing these errors before you analyze the data. If you skip this step, your final conclusions will be wrong.

## Handling Missing Data
It is very common for datasets to have blank spaces. A customer might skip a question on a survey, or a sensor might lose power for a minute. Before fixing it, analysts look at *why* it is missing. We categorize missing data into three types:

### 1. MCAR (Missing Completely at Random)
There is absolutely no pattern to why the data is missing. It happened purely by chance.
*   **Simple Example**: You drop a stack of paper surveys, and one page blows away in the wind. The data on that page is lost completely by random chance.

### 2. MAR (Missing at Random)
The fact that data is missing is related to *other* information you have, but not the missing value itself.
*   **Simple Example**: Let's say men are less likely to answer a survey question about "feelings of sadness." The missing data (sadness) is related to another variable we know (gender).

### 3. MNAR (Missing Not at Random)
This is the worst kind. The data is missing *because* of the value it would have been. 
*   **Simple Example**: In a survey asking people about their salary, people who earn very low wages might intentionally skip the question because they are embarrassed. The missing data is directly related to the value that should be there.

### How do we fix missing data? (Imputation)
Instead of throwing away a whole row of data just because one box is empty, we try to guess (impute) the missing value:
*   **Mean/Median/Mode**: Replacing the blank with the average (mean), middle (median), or most common (mode) value of that column.
*   **Advanced Methods**: Using algorithms like Regression or K-Nearest Neighbors (KNN) to look at other data points and make an educated guess about what the missing value should be.

## Dealing with Outliers
An **Outlier** is a data point that is wildly different from the rest. Sometimes it's a real, but rare, event. Other times, it's a mistake.

*   **Simple Example**: In a class of 20 students, most are between 18 and 22 years old. If your dataset says one student is 150 years old, that is an outlier (and definitely a typo).

### How to detect Outliers:
*   **Z-Score**: This measures how far a number is from the average. Generally, if a Z-score is greater than 3 (or less than -3), the number is so far away from the average that it is considered an outlier.
*   **IQR (Interquartile Range)**: This looks at the middle 50% of your data. If a number is far below or far above this middle chunk (specifically, outside the range of $Q_1 - 1.5 \times IQR$ and $Q_3 + 1.5 \times IQR$), it is flagged as an outlier.

## Summary
Data Cleaning is often the most time-consuming part of an analyst's job, but it is the most important. By properly handling missing values and identifying strange outliers, you ensure that the insights you generate later are actually trustworthy.
