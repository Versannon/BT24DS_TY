# Topic 3: Descriptive Statistics and Correlation

## What are Descriptive Statistics?
If you have a spreadsheet with 10,000 rows of sales data, you can't possibly understand it by reading every single row. **Descriptive Statistics** are mathematical tools that summarize that massive pile of data into a few simple numbers that describe the whole group.

We generally break these statistics down into three categories: Central Tendency, Dispersion, and Shape.

### 1. Measures of Central Tendency (Finding the Middle)
These numbers try to find the single "typical" or "middle" value that represents the entire dataset.
*   **Mean**: The mathematical average. You add all the numbers up and divide by how many there are. (E.g., The average age in a classroom).
*   **Median**: If you line up all the numbers in order from smallest to largest, the median is the exact middle number. This is very useful when you have crazy outliers. (E.g., If Bill Gates walks into a bar, the *mean* wealth skyrockets, but the *median* wealth stays normal because it just picks the middle person).
*   **Mode**: The number that shows up the most often. (E.g., In a shoe store, the mode is the shoe size that sells the most pairs).

### 2. Measures of Dispersion (Finding the Spread)
These numbers tell you how spread out or scattered your data is. Are all the numbers clustered tightly around the average, or are they all over the place?
*   **Range**: The difference between the biggest number and the smallest number. 
*   **Variance & Standard Deviation**: These measure, on average, how far each individual number is from the mean. A small standard deviation means the data is tightly packed; a large one means it is widely spread.
*   **IQR (Interquartile Range)**: The spread of the middle 50% of the data. It ignores extreme highs and lows.

### 3. Measures of Shape
This describes what the data looks like if you were to draw it on a graph.
*   **Skewness**: Measures if the data is leaning to one side. If most people fail a test but a few get 100%, the graph will look asymmetrical, or "skewed."
*   **Kurtosis**: Measures how "spiky" or "flat" the data is compared to a normal bell curve.

## Correlation: How Things Move Together
**Correlation** is a way to measure if two different variables are related. If one changes, does the other change too?

*   **Positive Correlation**: Both go up together. (E.g., The hotter it gets outside, the more ice cream is sold).
*   **Negative Correlation**: As one goes up, the other goes down. (E.g., The more hours you spend playing video games, the lower your test scores might be).

### Types of Correlation:
*   **Pearson (r)**: The most common. It measures a strict linear relationship (a straight line on a graph).
*   **Spearman**: Measures relationships based on ranks (1st place, 2nd place), rather than raw numbers.
*   **Kendall's Tau**: Another rank-based method used when the dataset is very small.

### The Golden Rule: Correlation does NOT imply Causation
Just because two things move together does not mean one *caused* the other. 
*   **Simple Example**: Ice cream sales and shark attacks both increase during the summer (Positive Correlation). But eating ice cream does *not* cause shark attacks! They both simply increase because of a third factor: the weather is hot, so people eat ice cream and swim in the ocean.

## Summary
Descriptive statistics allow us to summarize thousands of data points into easily digestible summaries. By understanding the center, the spread, and the relationships (correlation) within the data, we gain a clear picture of what has happened.
