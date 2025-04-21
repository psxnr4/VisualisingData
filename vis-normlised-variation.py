import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px


# loading dataset
raw_df = pd.read_csv("../normalised.csv")

# define dataset column names to use at metrics
metrics = [
    "mean_ghgs", "mean_land", "mean_watscar", "mean_eut",
    "mean_ghgs_ch4", "mean_ghgs_n2o", "mean_bio",
    "mean_watuse", "mean_acid"
]

# dictionary keys: ['fish', 'meat', 'meat100', 'meat50', 'vegan', 'veggie']
current_group = 'vegan'

# group dataframe by diet_group
# store in dictionary # and index each group individually
diet_dfs = dict(tuple(raw_df.groupby('diet_group')))
df = diet_dfs[current_group]


# define new labels to display
diet_labels = {
    "vegan": "Vegans",       
    "veggie": "Vegetarians",      
    "fish": "Fish-Eaters",        
    "meat50": "Low Meat-Eaters",      
    "meat": "Medium Meat-Eaters",        
    "meat100": "High Meat-Eaters"      
}
dietLabel = diet_labels[current_group]

metric_labels = {
    "mean_ghgs": "GHGs",
    "mean_land": "Land Use",
    "mean_watscar": "Water Scarcity",
    "mean_eut": "Eutrophication",
    "mean_ghgs_ch4": "CH4 Emissions",
    "mean_ghgs_n2o": "N2O Emissions",
    "mean_bio": "Biodiversity",
    "mean_watuse": "Water Use",
    "mean_acid": "Acidification"
}


# Create the parallel coordinates plot
fig = px.parallel_coordinates(
    df,
    dimensions=metrics,
    color='distance_from_mean',  # Color by the distance from average record
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=0, # Set the average record to the centre of colour spectrum
    labels=metric_labels,
)
# Position figure
fig.update_layout(
    title={
        'text': f"Environmental Impacts for Dietary Group: {dietLabel}",
        'y':0.98,  
        'x':0.2,   
        'xanchor': 'center',
        'yanchor': 'top'
    },
    margin=dict(l=40, r=40, t=80, b=40),  
    font=dict(
        size=12
    )
)
fig.show()
