# Load the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Read the CSV file
df = pd.read_csv('cybersecurity_attacks.csv')


# Convert timestamp to datetime and extract month
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Month'] = df['Timestamp'].dt.strftime('%B')  # This converts to month names

# Count attacks by month and type
monthly_attacks = df.groupby(['Month', 'Attack Type']).size().reset_index(name='Count')

# Create a month order for proper sorting
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Sort the data by the custom month order
monthly_attacks['Month'] = pd.Categorical(monthly_attacks['Month'], categories=month_order, ordered=True)
monthly_attacks = monthly_attacks.sort_values('Month')

# Find the most popular attack type for each month
most_popular_attacks = monthly_attacks.sort_values(['Month', 'Count'], ascending=[True, False])
most_popular_by_month = most_popular_attacks.groupby('Month').first().reset_index()

print("Most popular attack types per month:")
print(most_popular_by_month[['Month', 'Attack Type', 'Count']])


# Create a more detailed visualization with month names
plt.figure(figsize=(15, 7))
sns.barplot(data=monthly_attacks, x='Month', y='Count', hue='Attack Type')
plt.title('Cyber Attack Types by Month')
plt.xlabel('Month')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.legend(title='Attack Type', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()