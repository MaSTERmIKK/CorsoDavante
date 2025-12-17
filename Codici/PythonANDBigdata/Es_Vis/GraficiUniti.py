import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from math import pi

# Generazione di dati casuali
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(scale=0.5, size=100)
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(10, 100, size=len(categories))
values1 = np.random.randint(10, 50, size=len(categories))
values2 = np.random.randint(10, 50, size=len(categories))
data = np.random.normal(size=100)
matrix_data = np.random.rand(5, 5)

# Radar chart values
radar_values = np.random.randint(1, 10, size=len(categories)).tolist()
radar_values += radar_values[:1]
angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
angles += angles[:1]

# Creazione della figura e dei subplot
fig, axs = plt.subplots(4, 3, figsize=(15, 20))

# Line Plot
axs[0, 0].plot(x, y)
axs[0, 0].set_title("Line Plot")

# Bar Plot
axs[0, 1].bar(categories, values)
axs[0, 1].set_title("Bar Plot")

# Scatter Plot
axs[0, 2].scatter(x, y)
axs[0, 2].set_title("Scatter Plot")

# Histogram
axs[1, 0].hist(data, bins=10)
axs[1, 0].set_title("Histogram")

# Pie Chart
axs[1, 1].pie(values, labels=categories, autopct='%1.1f%%')
axs[1, 1].set_title("Pie Chart")

# Box Plot
axs[1, 2].boxplot(data)
axs[1, 2].set_title("Box Plot")

# Violin Plot
axs[2, 0].violinplot(data)
axs[2, 0].set_title("Violin Plot")

# Density Plot
sns.kdeplot(data, ax=axs[2, 1])
axs[2, 1].set_title("Density Plot")

# Regression Plot
sns.regplot(x=x, y=y, ax=axs[2, 2])
axs[2, 2].set_title("Regression Plot")

# Heatmap
sns.heatmap(matrix_data, annot=True, ax=axs[3, 0], cmap="YlGnBu")
axs[3, 0].set_title("Heatmap")

# Stacked Bar Plot
axs[3, 1].bar(categories, values1, label='Series 1')
axs[3, 1].bar(categories, values2, bottom=values1, label='Series 2')
axs[3, 1].legend()
axs[3, 1].set_title("Stacked Bar Plot")

# Radar (Spider) Chart
ax_radar = plt.subplot(4, 3, 12, polar=True)
ax_radar.plot(angles, radar_values)
ax_radar.fill(angles, radar_values, alpha=0.3)
ax_radar.set_xticks(angles[:-1])
ax_radar.set_xticklabels(categories)
ax_radar.set_title("Radar Chart")

plt.tight_layout()
plt.show()
