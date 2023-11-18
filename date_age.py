import plotly.express as px
import pandas as pd

# Load your dataset
file_path = 'wing_tree.csv'  # Replace with your file path
family_tree_df = pd.read_csv(file_path)

# Process names to show only the first initial and last name
family_tree_df['Shortened_Name'] = family_tree_df['Name'].apply(
    lambda name: name.split()[0][0] + '.' + ' ' + name.split()[-1] if len(name.split()) > 1 else name
)

# Create an interactive scatter plot using Plotly
fig = px.scatter(family_tree_df, x='Birth_Year', y='Age',
                 color='Group', hover_name='Shortened_Name',
                 labels={'Group': 'Gender', 'Birth_Year': 'Birth Year', 'Age': 'Age at Death'},
                 title='Age at Death Over Birth Year (Interactive)')

fig.update_traces(marker=dict(size=7), 
                  selector=dict(mode='markers'), 
                  textfont=dict(size=6))

fig.show()

# save the figure
fig.write_html('age_at_death.html')
