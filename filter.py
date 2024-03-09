import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# Load the data into a DataFrame
data = [
    # Your data here
]

df = pd.DataFrame(data)

# Define function to filter by location
def filter_location(df, location):
    if location.lower() == 'india':
        # Show dropdown for Indian states
        states = df[df['location'].str.lower() == 'india']['state'].unique()
        state_dropdown = widgets.Dropdown(options=states, description='State:', disabled=False)
        state_search = widgets.Text(placeholder='Search state...', description='Search:', disabled=False)

        def filter_by_state(state):
            if state == '':
                return df[df['location'].str.lower() == 'india']
            else:
                return df[(df['location'].str.lower() == 'india') & (df['state'] == state)]
        
        def search_state(change):
            filtered_df = filter_by_state(state_dropdown.value)
            display(filtered_df)

        state_dropdown.observe(search_state, names='value')
        state_search.observe(search_state, names='value')

        display(state_dropdown)
        display(state_search)
        display(filter_by_state(''))

    else:
        # Show search bar for other countries
        country_search = widgets.Text(placeholder='Search country...', description='Search:', disabled=False)
        
        def filter_by_country(country):
            if country == '':
                return df[df['location'].str.lower() == location.lower()]
            else:
                return df[df['location'].str.contains(country, case=False, na=False)]
        
        def search_country(change):
            filtered_df = filter_by_country(country_search.value)
            display(filtered_df)

        country_search.observe(search_country, names='value')

        display(country_search)
        display(filter_by_country(''))

# Define function to filter scholarships by keyword search
def filter_by_keyword(df, keyword):
    if keyword == '':
        return df
    else:
        return df[df['scholarship'].str.contains(keyword, case=False, na=False)]

# Define function to filter scholarships by domain
def filter_by_domain(df, domain):
    if domain == 'All':
        return df
    else:
        return df[df['domain'] == domain]

# Define function to filter scholarships by degrees
def filter_by_degrees(df, degrees):
    if not degrees:
        return df
    else:
        return df[df['degrees'].isin(degrees)]

# Define function to filter scholarships by category
def filter_by_category(df, category):
    if category == 'All':
        return df
    else:
        return df[df['category'] == category]

# Create dropdown menu for selecting country
countries = df['location'].unique()
countries.sort()
country_dropdown = widgets.Dropdown(options=countries, description='Country:', disabled=False)

def filter_by_country_dropdown(change):
    filter_location(df, country_dropdown.value)

country_dropdown.observe(filter_by_country_dropdown, names='value')

# Create search bar for keyword search
keyword_search = widgets.Text(placeholder='Search scholarships...', description='Search:', disabled=False)

def filter_by_keyword_search(change):
    filtered_df = filter_by_keyword(df, keyword_search.value)
    display(filtered_df)

keyword_search.observe(filter_by_keyword_search, names='value')

# Create dropdown menu for selecting domain
domains = ['All', 'Engineering', 'Medical', 'Research', 'Arts', 'Others']  # Add more domains as needed
domain_dropdown = widgets.Dropdown(options=domains, description='Domain:', disabled=False)

def filter_by_domain_dropdown(change):
    filtered_df = filter_by_domain(df, domain_dropdown.value)
    display(filtered_df)

domain_dropdown.observe(filter_by_domain_dropdown, names='value')

# Create checkbox options for selecting degrees
degree_checkboxes = []
for degree in df['degrees'].unique():
    checkbox = widgets.Checkbox(
        value=False,
        description=degree,
        disabled=False
    )
    degree_checkboxes.append(checkbox)

def filter_by_degrees_checkboxes(change):
    degrees = [checkbox.description for checkbox in degree_checkboxes if checkbox.value]
    filtered_df = filter_by_degrees(df, degrees)
    display(filtered_df)

for checkbox in degree_checkboxes:
    checkbox.observe(filter_by_degrees_checkboxes, names='value')
    display(checkbox)

# Create dropdown menu for selecting category
categories = ['All', 'OPEN', 'SEBC', 'EWS', 'OBC', 'SC', 'ST', 'OTHER']
category_dropdown = widgets.Dropdown(options=categories, description='Category:', disabled=False)

def filter_by_category_dropdown(change):
    filtered_df = filter_by_category(df, category_dropdown.value)
    display(filtered_df)

category_dropdown.observe(filter_by_category_dropdown, names='value')

display(country_dropdown)
display(keyword_search)
display(domain_dropdown)
display(category_dropdown)
