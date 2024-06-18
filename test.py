import requests
import time
import pandas as pd
from PIL import Image
import streamlit as st
from io import BytesIO
import plotly.express as px

def main():

    st.title(":rainbow[LGD Hierarchy Data]🗺️")

    st.divider()

    st.markdown(
        """
        <style>
        .spacer {
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Add a spacer div to create space
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        # Create Search bar
        search_term = st.text_input(":blue[Search by :green[State]/:orange[Code:]]🔎", "")

    # About States-------------------------------------------------------------------------------------------------|

    @st.cache_data
    def load_state_data():
        state_df = pd.read_csv(r"C:\Users\satya\PycharmProjects\lgd_app\Data\State Details.csv")

        state_df = state_df[["State LGD Code", "State Name (In English)", "State Name (In Local language)", "State or UT",
        "Census2011 Code"]]

        return state_df

    state_df = load_state_data()

    # Filter based on State Name & it's LGD code
    if search_term:
        filtered_records = state_df[
            state_df['State Name (In English)'].str.contains(search_term, case=False) |
            state_df['State LGD Code'].astype(str).str.contains(search_term)
            ]

        # If there is invalid search it will show no matching found
        if not filtered_records.empty:
            st.write(":blue[Filtered results:]", filtered_records.shape)
            st.write(filtered_records)
        else:
            st.write(":red[Opps! No matching results found.]🤦‍♂️")

    # Preview of state data
    st.subheader(":orange[State Data Preview]🫣",divider='rainbow')
    ":green[Rows & Columns In States]➡️", state_df.shape
    st.write(state_df.head())

# About Districts ---------------------------------------------------------------------------------------------|
    @st.cache_data
    def load_district_data():
        district_df = pd.read_csv(r"C:\Users\satya\PycharmProjects\lgd_app\Data\District Details.csv")

        district_df = district_df[
            ["District LGD Code", "District Name (In English)", "District Name (In Local language)",
             "Hierarchy", "Short Name of District", "Census2011 Code", "Pesa Status"]]

        return district_df

    district_df = load_district_data()



    col1, col2, col3 = st.columns(3)

    with col1:
        # Create Search bar
        search_term = st.text_input(":blue[Search by :green[District]/:orange[Code:]]🔎", "")

    # Filter based on District Name & it's LGD code
    if search_term:
        filtered_records = district_df[
            district_df['District Name (In English)'].str.contains(search_term, case=False) |
            district_df['District LGD Code'].astype(str).str.contains(search_term)
            ]

        # If there is invalid search it will show no matching found
        if not filtered_records.empty:
            st.write(":blue[Filtered results:]",filtered_records.shape)
            st.write(filtered_records)
        else:
            st.write(":red[Opps! No matching results found.]🤦‍♂️")

    # Preview of district data
    st.subheader(":orange[District Data Preview]🫣",divider='rainbow')
    ":green[Rows & Columns In Districts]➡️", district_df.shape
    st.write(district_df.head())

# About Sub-Districts-------------------------------------------------------------------------------------------|
    @st.cache_data
    def load_sub_district_data():
        sub_district_df = pd.read_csv(r"C:\Users\satya\PycharmProjects\lgd_app\Data\Sub-districts Details.csv")

        sub_district_df = sub_district_df[["Sub-District LGD Code","Sub-District Name (In English)",
        "Sub-District Name (In Local language)","Hierarchy","Census2011 Code", "Pesa Status"]]

        sub_district_df["Sub-District LGD Code"] = sub_district_df["Sub-District LGD Code"].astype(str)
        sub_district_df["Census2011 Code"].fillna(0, inplace=True)
        sub_district_df["Census2011 Code"] = sub_district_df["Census2011 Code"].astype(int).astype(str)

        return sub_district_df

    sub_district_df = load_sub_district_data()

    col1, col2, col3 = st.columns(3)

    with col1:
        # Create Search bar
        search_term = st.text_input(":blue[Search by :green[Sub-District]/:orange[Code:]]🔎", "")

    # Filter based on Sub-District Name & it's LGD code
    if search_term:
        filtered_records = sub_district_df[
            sub_district_df['Sub-District Name (In English)'].str.contains(search_term, case=False) |
            sub_district_df['Sub-District LGD Code'].astype(str).str.contains(search_term)
            ]

        # If there is invalid search it will show no matching found
        if not filtered_records.empty:
            st.write(":blue[Filtered results:]",filtered_records.shape)
            st.write(filtered_records)
        else:
            st.write(":red[Opps! No matching results found.]🤦‍♂️")

    # Preview of sub-district data
    st.subheader(":orange[Sub-District Data Preview]🫣",divider = "rainbow")
    ":green[Rows & Columns In Sub-Districts➡️]", sub_district_df.shape
    st.write(sub_district_df.head())


# About Villages----------------------------------------------------------------------------------------------|

    @st.cache_data
    def load_village_data():
        village_df = pd.read_csv(r"C:\Users\satya\PycharmProjects\lgd_app\Data\Village Details.csv")
        village_df = village_df[["State Code","State Name (In English)","District Code","District Name (In English)",
                    "Sub-District Code","Sub-District Name (In English)","Village Code","Village Version",
                    "Village Name (In English)","Village Name (In Local)","Village Status","Census 2011 Code"]]
        village_df["Village Code"] = village_df["Village Code"].astype(str)
        village_df["Census 2011 Code"].fillna(0, inplace=True)
        village_df["Census 2011 Code"] = village_df["Census 2011 Code"].astype(int).astype(str)

        return village_df
    village_df = load_village_data()

    col1, col2, col3 = st.columns(3)

    with col1:
        # Create Search bar
        search_term = st.text_input(":blue[Search by :green[Village]/:orange[Code:]]🔎", "")

    # Filter based on Sub-District Name & it's LGD code
    if search_term:
        filtered_records = village_df[
            village_df['Village Name (In English)'].str.contains(search_term, case=False) |
            village_df['Village Code'].astype(str).str.contains(search_term)
            ]

        # If there is invalid search it will show no matching found
        if not filtered_records.empty:
            st.write(":blue[Filtered results:]",filtered_records.shape)
            st.write(filtered_records)
        else:
            st.write(":red[Opps! No matching results found.]🤦‍♂️")

    # Preview of sub-district data
    st.subheader(":orange[Villages Data Preview]🫣",divider="rainbow")
    ":green[Rows & Columns In Villages]", village_df.shape
    st.write(village_df.head())
    st.caption("Update till June 2024, To get latest LGD Data Please visit LGD Official site.")

    st.markdown("---")

# Footer
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f4f4f4;
            padding: 10px 0;
            text-align: center;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    # Icons
    st.markdown(
        """
        <script>
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
        </script>
        <div class="footer">
            <a href="https://github.com/sjpradhan"><img src=https://raw.githubusercontent.com/sjpradhan/repo/master/Icons/github-logo.png width="30" height="30"></a>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <a href="mailto:sjpradan@gmail.com"><img src=https://raw.githubusercontent.com/sjpradhan/repo/master/Icons/gmail.png width="30" height="30"></a>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://www.linkedin.com/in/sjpradhan"><img src=https://raw.githubusercontent.com/sjpradhan/repo/master/Icons/linkedin.png width="30" height="30"></a>
        </div>
        """
        , unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()


