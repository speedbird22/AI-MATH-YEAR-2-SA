# AI-MATH-YEAR-2-SA


This project is a data analytics dashboard built using Streamlit to analyze and visualize the impact of player injuries on football team and player performance. It leverages a dataset containing detailed player injury records, match outcomes, and player ratings across multiple seasons for various teams.

The dashboard provides interactive visualizations and filtering capabilities aimed at helping technical directors, sports analysts, and team managers gain actionable insights into how injuries influence team success and individual player performance before, during, and after injury periods.

Features
Data preprocessing and cleaning to handle missing and irregular data such as injury dates and player ratings.

Sidebar filters for exploratory analysis by team, player position, season, and injury type.

Visualizations including:

Top injuries by frequency bar chart.

Boxplots comparing player ratings before and after injury.

Scatter plot showing the relationship between player age and post-injury rating.

Team performance analysis during player absence.

Injury frequency trends across seasons.

Built with Python libraries such as Pandas, Plotly, Seaborn, and deployed as an interactive web app via Streamlit.

Installation
Install required Python libraries listed in requirements.txt:

text
pip install -r requirements.txt
Usage
Place the provided player_injuries_impact.csv dataset in the project root directory. Run the app by executing:

text
streamlit run main.py
This will open the interactive dashboard in your web browser where you can filter data and explore the visualizations.

Dependencies
streamlit

pandas

matplotlib

seaborn

plotly

statsmodels (required for trendline in scatter plot)
