# Visual Best Practices Fallback
import numpy as np

print("--- Visualization Best Practices Fallback ---")
# If matplotlib is missing, save numerical values to file
with open("sales_trends_data.txt", "w") as f:
    f.write("Month,Sales\n")
    for m in range(1, 13):
        f.write(f"{m},{10000 + 500 * m}\n")
print("Saved raw sales data in sales_trends_data.txt")
