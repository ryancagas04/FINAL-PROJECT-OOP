"""A short demonstration of the Cleanalyze package."""
import pandas as pd
from cleanalyze import DataCleaner, DataAnalyzer, DataVisualizer, validate_dataset

sample = pd.DataFrame({
    "student": ["Ana", "Ben", "Cara", "Ben"],
    "score": [88, None, 95, None],
    "hours_studied": [3, 2, 5, 2]
})

print("BEFORE CLEANING")
print(sample)
print("\nVALIDATION")
print(validate_dataset(sample))

cleaner = DataCleaner(sample)
cleaned = cleaner.process()
print("\nAFTER CLEANING")
print(cleaned)

analyzer = DataAnalyzer(cleaned)
print("\nSUMMARY")
print(analyzer.process())
print("Average score:", analyzer.get_mean("score"))
print("Median score:", analyzer.get_median("score"))

# Uncomment to display a chart in a local Python environment:
# visualizer = DataVisualizer(cleaned)
# visualizer.create_histogram("score")
# import matplotlib.pyplot as plt
# plt.show()
