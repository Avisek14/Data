import pandas as pd
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import numpy as np

# Load the Excel file
file_path = "C://Users//sahoo//Alcohol_consumption_Indian_State_2021_.xlsx"
data = pd.ExcelFile(file_path)

# Parse the sheet
df = data.parse('Alcohol_consumption_India_2021')

# Filter for "Total" area to avoid duplicating Urban/Rural
df_total = df[df['Area'] == 'Total']

# Extract relevant columns
states = df_total['States/UTs']
women_consumption = df_total['Women age 15 years and above who consume alcohol (%)']
men_consumption = df_total['Men age 15 years and above who consume alcohol (%)']

# Visualization 1: Bar Chart - Alcohol Consumption (Women vs. Men)
x = np.arange(len(states))  # Positions for the bars
width = 0.4  # Width of the bars

plt.figure(figsize=(14, 8))
plt.bar(x - width/2, women_consumption, width, label='Women', color='lightblue', edgecolor='black')
plt.bar(x + width/2, men_consumption, width, label='Men', color='salmon', edgecolor='black')

# Customize the plot
plt.xlabel('States/UTs', fontsize=12)
plt.ylabel('Alcohol Consumption (%)', fontsize=12)
plt.title('Comparison of Alcohol Consumption (Men vs. Women)', fontsize=16)
plt.xticks(x, states, rotation=90, fontsize=10)
plt.legend(fontsize=12)

# Adjust layout for better visibility
plt.tight_layout()
plt.show()

# Visualization 2: Horizontal Bar Chart - Top 10 States (Men Alcohol Consumption)
top_men = df_total.sort_values('Men age 15 years and above who consume alcohol (%)', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y='States/UTs', x='Men age 15 years and above who consume alcohol (%)', data=top_men, palette='Reds_r')
plt.title('Top 10 States by Alcohol Consumption (Men)', fontsize=14)
plt.xlabel('Alcohol Consumption (%)')
plt.ylabel('States/UTs')
plt.tight_layout()
plt.show()

# Visualization 3: Horizontal Bar Chart - Top 10 States (Women Alcohol Consumption)
top_women = df_total.sort_values('Women age 15 years and above who consume alcohol (%)', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y='States/UTs', x='Women age 15 years and above who consume alcohol (%)', data=top_women, palette='Blues_r')
plt.title('Top 10 States by Alcohol Consumption (Women)', fontsize=14)
plt.xlabel('Alcohol Consumption (%)')
plt.ylabel('States/UTs')
plt.tight_layout()
plt.show()

# Visualization 4: Scatter Plot - Women vs. Men Alcohol Consumption
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x='Women age 15 years and above who consume alcohol (%)',
    y='Men age 15 years and above who consume alcohol (%)',
    hue='States/UTs',
    data=df_total,
    palette='tab20',
    legend=False
)
plt.title('Scatter Plot: Women vs. Men Alcohol Consumption', fontsize=14)
plt.xlabel('Women Alcohol Consumption (%)')
plt.ylabel('Men Alcohol Consumption (%)')
plt.tight_layout()
plt.show()

# Visualization 5: Pie Chart - Rural vs Urban (Men Alcohol Consumption for India)

# Filter the data for India and men's alcohol consumption
df_india = df[df['States/UTs'] == 'India']
consumption_by_area = df_india.groupby('Area')['Men age 15 years and above who consume alcohol (%)'].sum()
plt.figure(figsize=(8, 8))
consumption_by_area.plot.pie(autopct='%1.1f%%', colors=['skyblue', 'lightgreen'], startangle=140)
plt.title('Men Alcohol Consumption (Urban vs. Rural)', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.show()

# Visualization 6: Pie Chart - Rural vs Urban (Women Alcohol Consumption for India)

# Filter the data for India and women's alcohol consumption
df_india = df[df['States/UTs'] == 'India']
women_consumption = df_india.groupby('Area')['Women age 15 years and above who consume alcohol (%)'].sum()

plt.figure(figsize=(8, 8))
colors = ['skyblue', 'lightgreen']
women_consumption.plot.pie(
    autopct='%1.1f%%',
    colors=colors,
    startangle=140,
    labels=women_consumption.index,
    fontsize=12
)
plt.title('Women Alcohol Consumption in India (Urban vs. Rural)', fontsize=14)
plt.ylabel('')  # Remove y-axis label for better appearance
plt.tight_layout()
plt.show()

# Visualization 7: grouped bar chart - Comparison of Alcohol Consumption Among Men and Women in Odisha with there nearest States

# Filter for "Total" area and the specified states
states_to_compare = ['Odisha', 'Andhra Pradesh', 'West Bengal', 'Chhattisgarh', 'Jharkhand']
df_filtered = df[(df['Area'] == 'Total') & (df['States/UTs'].isin(states_to_compare))]

# Extract data for plotting
states = df_filtered['States/UTs']
women_consumption = df_filtered['Women age 15 years and above who consume alcohol (%)']
men_consumption = df_filtered['Men age 15 years and above who consume alcohol (%)']

# Create the grouped bar chart
x = np.arange(len(states))  # Positions for the bars
width = 0.4  # Width of the bars

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, women_consumption, width, label='Women', color='lightblue', edgecolor='black')
plt.bar(x + width/2, men_consumption, width, label='Men', color='salmon', edgecolor='black')

# Customize the plot
plt.xlabel('States/UTs', fontsize=12)
plt.ylabel('Alcohol Consumption (%)', fontsize=12)
plt.title('Comparison of Alcohol Consumption Among Men and Women in Odisha with there nearest States', fontsize=16)
plt.xticks(x, states, rotation=0, fontsize=12)
plt.legend(fontsize=12)

# Adjust layout for better visibility
plt.tight_layout()
plt.show()