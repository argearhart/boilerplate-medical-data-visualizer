import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2)

# Add 'overweight' column (1 if BMI >= 25, else 0)
df['overweight'] = df['overweight'].apply(lambda x: 1 if x >= 25 else 0)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using
    # `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=[
                     'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(x='variable', hue='value',
                col='cardio', kind='count', data=df_cat)
    plt.ylabel('total')

    # Get the figure for the output
    fig = plt.gcf()

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(
        0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f",
                cmap='coolwarm', cbar=True, ax=ax)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
