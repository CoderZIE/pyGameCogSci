import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
file_path = 'scores.csv'  
data = pd.read_csv(file_path, header=None, names=['Score', 'Lives'])

# Process data
data['Lives'] = 9 - data['Lives']

average_scores = data.groupby('Lives')['Score'].mean().reset_index()


plt.figure(figsize=(10, 5))

plt.step(average_scores['Lives'], average_scores['Score'], where='mid', 
         color='orange', label='Average Score (Step)', linewidth=2)

plt.plot(average_scores['Lives'], average_scores['Score'], 
         marker='o', linestyle='-', color='red', markersize=8, label='Average Score (Line)')

plt.scatter(data['Lives'], data['Score'], color='blue', alpha=0.6, label='Individual Scores')

plt.title('Average Score vs Lives (With Steps)')
plt.xlabel('Lives')
plt.ylabel('Average Score')
plt.grid(True)
plt.legend()
plt.show()
