import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import requests
from io import BytesIO

def main():

    @st.cache_resource
    def profile_icon(github_raw_image_url):

        # Fetch the image from the URL
        response = requests.get(github_raw_image_url)

        # Open the image using PIL
        profile_icon = Image.open(BytesIO(response.content))
        return profile_icon

    # GitHub raw image URL
    github_raw_image_url = "https://raw.githubusercontent.com/sjpradhan/App/master/Data/seo.png"

    # Call the function to fetch and process the image
    profile_icon = profile_icon(github_raw_image_url)

    st.set_page_config(page_title="LGD Search Hierarchy", page_icon=profile_icon,layout = "wide")

    st.markdown("<h1 style='text-align: center;'>LGD Data Details🫡</h1>", unsafe_allow_html=True)

# About States-------------------------------------------------------------------------------------------------|

    # Define Path & read csv file
    path = "https://media.githubusercontent.com/media/sjpradhan/App/master/Data/State%20Details.csv"
    state_data = pd.read_csv(path)

    # Create Search bar
    search_term = st.text_input("Search by State/Code:🔎", "")

    # Filter based on State Name & it's LGD code
    if search_term:
        filtered_records = state_data[
            state_data['State Name (In English)'].str.contains(search_term, case=False) |
            state_data['State LGD Code'].astype(str).str.contains(search_term)
            ]

        # If there is invalid search it will show no matching found
        if not filtered_records.empty:
            st.write("Filtered results:",filtered_records.shape)
            st.write(filtered_records)
        else:
            st.write("Opps! No matching results found.🤦‍♂️")

    # Preview of state data
    st.subheader("State Data Preview🫣")
    st.write(state_data.head(), "Rows & Columns In States:", state_data.shape)

# About Districts ---------------------------------------------------------------------------------------------|

    # Define Path & read csv file
    path = "https://media.githubusercontent.com/media/sjpradhan/App/master/Data/District%20Details.csv"
    district_data = pd.read_csv(path)

    # Create Search bar
    search_term = st.text_input("Search by District/Code:🔎", "")

    # Filter based on District Name & it's LGD code
    if search_term:
        filtered_records = district_data[
            district_data['District Name (In English)'].str.contains(search_term, case=False) |
            district_data['District LGD Code'].astype(str).str.contains(search_term)
            ]

        # If there is invalid search it will show no matching found
        if not filtered_records.empty:
            st.write("Filtered results:",filtered_records.shape)
            st.write(filtered_records)
        else:
            st.write("Opps! No matching results found.🤦‍♂️")

    # Preview of district data
    st.subheader("District Data Preview🫣")
    st.write(district_data.head(),"Rows & Columns In Districts:", district_data.shape)

# About Sub-Districts-------------------------------------------------------------------------------------------|

    # Define Path & read csv file
    path = "https://media.githubusercontent.com/media/sjpradhan/App/master/Data/Sub-districts%20Details.csv"
    sub_district_data = pd.read_csv(path)

    # Create Search bar
    search_term = st.text_input("Search by Sub-District/Code:🔎", "")

    # Filter based on Sub-District Name & it's LGD code
    if search_term:
        filtered_records = sub_district_data[
            sub_district_data['Sub-District Name (In English)'].str.contains(search_term, case=False) |
            sub_district_data['Sub-District LGD Code'].astype(str).str.contains(search_term)
            ]

        # If there is invalid search it will show no matching found
        if not filtered_records.empty:
            st.write("Filtered results:",filtered_records.shape)
            st.write(filtered_records)
        else:
            st.write("Opps! No matching results found.🤦‍♂️")

    # Preview of sub-district data
    st.subheader("Sub-District Data Preview🫣")
    st.write(sub_district_data.head(),"Rows & Columns In Sub-Districts:", sub_district_data.shape)

# About Villages----------------------------------------------------------------------------------------------|

    # Define Path & read csv file
    path = "https://media.githubusercontent.com/media/sjpradhan/App/master/Data/village%20Details.csv"
    village_data = pd.read_csv(path)

    # Create Search bar
    search_term = st.text_input("Search by Village/Code:🔎", "")

    # Filter based on Sub-District Name & it's LGD code
    if search_term:
        filtered_records = village_data[
            village_data['Village Name (In English)'].str.contains(search_term, case=False) |
            village_data['Village Code'].astype(str).str.contains(search_term)
            ]

        # If there is invalid search it will show no matching found
        if not filtered_records.empty:
            st.write("Filtered results:",filtered_records.shape)
            st.write(filtered_records)
        else:
            st.write("Opps! No matching results found.🤦‍♂️")

    # Preview of sub-district data
    st.subheader("Villages Data Preview🫣")
    st.write(village_data.head(),"Rows & Columns In Villages:", village_data.shape)

    st.header("Statistics 📈")
    try:
        # States Stats
        states = state_data['State Name (In English)']
        number_of_states = len(states)
        duplicate_records = state_data.duplicated(subset=['State LGD Code']).sum()
        st.write("States:", number_of_states, '|', "Duplicates", duplicate_records)

        # Districts Stats
        district = district_data['District Name (In English)']
        number_of_district = len(district)
        duplicate_records = district_data.duplicated(subset=['District LGD Code']).sum()
        st.write("Districts:", number_of_district, '|', "Duplicates", duplicate_records)

        # Sub Districts Stats
        sub_district = sub_district_data['Sub-District Name (In English)']
        number_of_sub_district = len(sub_district)
        duplicate_records = sub_district_data.duplicated(subset=['Sub-District LGD Code']).sum()
        st.write("Sub-Districts:", number_of_sub_district, '|', "Duplicates", duplicate_records)

        # Villages Stats
        villages = village_data['Village Name (In English)']
        number_of_villages = len(villages)
        duplicate_records = village_data.duplicated(subset=['Village Code']).sum()
        st.write("Villages:", number_of_villages, '|', "Duplicates", duplicate_records)

        # Rename column name
        village = village_data['State Name (In English)'].value_counts().reset_index().rename(
            columns={'State Name (In English)': 'Custom_Column_Name'})
        village = village.rename(columns={'Custom_Column_Name': 'State', 'count': 'villages'})
        st.write(village)

        #Bar chart
        fig = px.bar(village, x='State', y='villages', title='Number of Villages/State')
        # Update the layout to increase the figure size
        fig.update_layout(
            width=800,  # Set the width of the figure
            height=750,  # Set the height of the figure
        )
        # Display the plot
        st.plotly_chart(fig)
    except Exception:
        st.error(f"Upload all the necessary files to view LGD stats:")
if __name__ == "__main__":
    main()


