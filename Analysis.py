#%%
import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns

#%%
# Load the data
JPMC_data = pd.read_csv("Files/JPMorgan Chase.csv")
GS_data = pd.read_csv("Files/The Goldman Sachs.csv")

# %%
# Display JPMorgan & Chase datagg
JPMC_data
# %%
# Display Goldman Sachs data
GS_data


# QUESTION 1
# Compare which company traded most shares or contracts from 2000 to 2023

#%%
# Create year columns for each dataset
JPMC_data['Year']=pd.DatetimeIndex(JPMC_data['Date']).year
GS_data['Year']=pd.DatetimeIndex(GS_data['Date']).year
#%%
# Total shares traded per year per company
JPMC_data1=JPMC_data.groupby('Year')['Volume'].sum()
JPMC_data1
GS_data1=GS_data.groupby('Year')['Volume'].sum()
# %%
# Plot and Compare shares traded per year per company
alt.data_transformers.enable('default', max_rows=None)
JP_chart1 = alt.Chart(JPMC_data).mark_bar(color='blue').encode(
    alt.X('Year:Q'),
    alt.Y('Volume:Q', title='Shares Traded')
).properties(title='Quantity Share traded JPMC')
GS_chart1 = alt.Chart(GS_data).mark_bar(color='green').encode(
    alt.X('Year:Q'),
    alt.Y('Volume:Q', title='Shares Traded')
).properties(title='Quantity Share traded GS')
chart1 = alt.hconcat(JP_chart1, GS_chart1).resolve_scale(color='independent')
chart1


# QUESTION 2
# Compare the total number of shares traded by firms Since 2000.

# %%
# Calculate the total volume for JPMC and GS
jpmc_volume_sum = JPMC_data['Volume'].sum()
gs_volume_sum = GS_data['Volume'].sum()
# Create a dataframe with the volume and company names
data = pd.DataFrame({
    'Company': ['JPMC', 'GS'],
    'Volume': [jpmc_volume_sum, gs_volume_sum]
})
# Create the bar chart with names on top of the bars
chart = alt.Chart(data).mark_bar().encode(
    alt.X('Company'),
    alt.Y('Volume', title='Shares Traded'),
    text='Volume',
    color=alt.Color('Company', legend=None)
).properties(
    title='Comparison of Total Volume of shares traded: JPMC vs GS'
)
# Add labels on top of the bars
text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-10  # Offset the labels above the bars
).encode(
    text='Volume'
)
# Combine the chart and text layer
chart_with_labels = chart + text
chart_with_labels


# QUESTION 3
# Which Company had the lowest and highest stock market prices in 2023

# %%
# Takes data from 2023
JPMC_2023 = JPMC_data[JPMC_data['Year']==2023]
GS_2023 = GS_data[GS_data['Year']==2023]
# Lowest stock prices
JPMC_2023_Low_chart= alt.Chart(JPMC_2023).mark_line().encode(
    alt.X('Date'),
    alt.Y('Low'),
    alt.Text('label:Q')
).transform_calculate(
    label="'JPMC'"
)
GS_2023_Low_chart= alt.Chart(GS_2023).mark_line().encode(
    alt.X('Date'),
    alt.Y('Low'),
    alt.Text('label:Q')
).transform_calculate(
    label="'GS'"
)
Low_chart=(JPMC_2023_Low_chart + GS_2023_Low_chart).encode(
    color=alt.Color('label:N')).properties(title='2023 Lowest Stock Prices JPMC vs GS')
Low_chart

# %%
# Highest stock prices
JPMC_2023_Low_chart= alt.Chart(JPMC_2023).mark_line().encode(
    alt.X('Date'),
    alt.Y('High'),
    alt.Text('label:Q')
).transform_calculate(
    label="'JPMC'"
)
GS_2023_Low_chart= alt.Chart(GS_2023).mark_line().encode(
    alt.X('Date'),
    alt.Y('High'),
    alt.Text('label:Q')
).transform_calculate(
    label="'GS'"
)
Low_chart=(JPMC_2023_Low_chart + GS_2023_Low_chart).encode(
    color=alt.Color('label:N')).properties(title='2023 Lowest Stock Prices JPMC vs GS')
Low_chart
# %%
