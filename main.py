import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
df = pd.read_csv('player_injuries_impact.csv')

# Preprocess dates
df['Date of Injury'] = pd.to_datetime(df['Date of Injury'], errors='coerce')
df['Date of return'] = pd.to_datetime(df['Date of return'], errors='coerce')

# Replace "N.A." with NaN
import numpy as np
df.replace('N.A.', np.nan, inplace=True)

# Convert rating columns to numeric
rating_cols = [col for col in df.columns if 'rating' in col]
for col in rating_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Streamlit app layout
st.title('Player Injuries Impact Dashboard')

# Sidebar filters
team_filter = st.sidebar.multiselect('Select Team(s)', options=df['Team Name'].unique(), default=df['Team Name'].unique())
position_filter = st.sidebar.multiselect('Select Position(s)', options=df['Position'].unique(), default=df['Position'].unique())
season_filter = st.sidebar.multiselect('Select Season(s)', options=df['Season'].unique(), default=df['Season'].unique())
injury_filter = st.sidebar.multiselect('Select Injury Type(s)', options=df['Injury'].dropna().unique(), default=df['Injury'].dropna().unique())

# Filter the dataframe
filtered_df = df[(df['Team Name'].isin(team_filter)) & (df['Position'].isin(position_filter)) & (df['Season'].isin(season_filter)) & (df['Injury'].isin(injury_filter))]

# Generate some summary stats
st.header('Summary Statistics')
total_injuries = filtered_df.shape[0]
st.write(f'Total injuries in selection: {total_injuries}')
avg_age = filtered_df['Age'].mean()
st.write(f'Average age of injured players: {avg_age:.1f}')

# Visualization 1: Top injuries by frequency
st.header('Top Injuries by Frequency')
injury_counts = filtered_df['Injury'].value_counts().nlargest(10)
fig1 = px.bar(injury_counts, x=injury_counts.index, y=injury_counts.values, labels={'x': 'Injury Type', 'y': 'Count'}, title='Top 10 Injuries')
st.plotly_chart(fig1)

# Visualization 2: Average player rating before and after injury
st.header('Player Ratings Before and After Injury')
rating_before = filtered_df[rating_cols].filter(like='before_injury_Player_rating').mean(axis=1)
rating_after = filtered_df[rating_cols].filter(like='after_injury_Player_rating').mean(axis=1)
rating_df = pd.DataFrame({'Before Injury': rating_before, 'After Injury': rating_after})
rating_df = rating_df.dropna()
ratings_melt = rating_df.melt(var_name='Period', value_name='Rating')
fig2 = px.box(ratings_melt, x='Period', y='Rating', points='all', title='Player Ratings Before vs After Injury')
st.plotly_chart(fig2)

# Visualization 3: Impact of age on average player rating post-injury
st.header('Age vs Post-Injury Rating')
fig3 = px.scatter(filtered_df, x='Age', y=filtered_df[rating_cols].filter(like='after_injury_Player_rating').mean(axis=1),
                  trendline='ols', labels={'Age': 'Player Age', 'y': 'Average Player Rating After Injury'}, title='Age and Post-Injury Player Ratings')
st.plotly_chart(fig3)

# Visualization 4: Team performance outcomes during player absence
st.header('Team Performance During Player Absence')
missed_result_cols = ['Match1_missed_match_Result', 'Match2_missed_match_Result', 'Match3_missed_match_Result']
results = filtered_df[missed_result_cols].apply(pd.Series.value_counts).fillna(0)
results = results.T[['win', 'draw', 'lose']]
fig4 = px.bar(results, barmode='group', title='Match Results in Missed Matches')
st.plotly_chart(fig4)

# Visualization 5: Injury counts per season
st.header('Injury Frequency Per Season')
season_counts = filtered_df['Season'].value_counts().sort_index()
fig5 = px.line(season_counts, x=season_counts.index, y=season_counts.values, markers=True, title='Injury Counts Over Seasons')
st.plotly_chart(fig5)

# Footer
st.markdown('---')
st.markdown('Developed for Mathematics for AI II Summative Assessment')
