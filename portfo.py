import streamlit as st
from PIL import Image
import base64
import pandas as pd
import pycountry
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

def main():
    """Main function to define the structure of the portfolio."""

    # Set page title and icon
    profile_icon = Image.open(r"C:\Users\satya\PycharmProjects\portflios\Icons\user.png")
    st.set_page_config(page_title="Satyajeet Portfolio", page_icon=profile_icon,layout = "wide")

    # Load Image
    portfolio_icon = r"C:\Users\satya\PycharmProjects\portflios\Profile\Portfolio logo.png"

    # Display the image at the top left corner
    st.image(portfolio_icon, use_column_width=False, width=370, caption="")

    # Sub Page For Dashboard
    def retail_performance_dashboard():
        # Read Dataset
        order_details = pd.read_excel(
            r"C:\Users\satya\PycharmProjects\portflios\Data\raw_data_orders_100.xlsx")
        supplier_details = pd.read_excel(
            r"C:\Users\satya\PycharmProjects\portflios\Data\raw_data_product_supplier.xlsx")

        replace_dict = {'SILVER': 'Silver', 'GOLD': 'Gold', 'PLATINUM': 'Platinum'}
        order_details['Customer Status'] = order_details['Customer Status'].replace(replace_dict)

        order_details["Profits"] = (
                order_details["Total Retail Price for This Order"] - order_details["Cost Price Per Unit"])

        merge_data = pd.merge(order_details, supplier_details, on="Product ID", how="inner")

        int_to_convert_text = ['Customer ID', 'Order ID', 'Product ID', 'Supplier ID']
        merge_data[int_to_convert_text] = merge_data[int_to_convert_text].astype(str)

        date_format = ['Date Order was placed', 'Delivery Date']
        merge_data[date_format] = merge_data[date_format].apply(pd.to_datetime)
        merge_data[date_format] = merge_data[date_format].apply(lambda x: x.dt.strftime('%d-%m-%Y'))

        # Setting up the Streamlit dashboard
        st.title("Retail Performance Dashboard🛒")

        st.subheader("KPIs")
        col1, col2, col3, col4 = st.columns(4, gap="small")

        # Customers metric
        with col1:
            total_customers = order_details["Customer ID"].nunique()
            def create_card(title, value, color):
                fig = go.Figure(go.Indicator(
                    mode="number",
                    value=value,
                    title={"text": f"<b>{title}</b>"},
                    number={"font": {"size": 45, "color": color,"family": "Arial, sans-serif"}},
                    domain={'x': [0, 1], 'y': [0, 1]}
                ))
                fig.update_layout(
                    margin=dict(l=20, r=20, t=40, b=20),
                    height=200,
                )
                return fig
            # Create the KPI card figure
            fig = create_card("Total Customers", total_customers, "coral")
            # Display the figure in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        # Sales metric
        with col2:
            total_sales = order_details["Quantity Ordered"].sum()
            def create_card(title, value, color):
                fig = go.Figure(go.Indicator(
                    mode="number",
                    value=value,
                    title={"text": f"<b>{title}</b>"},
                    number={"font": {"size": 45, "color": color}},
                    domain={'x': [0, 1], 'y': [0, 1]}
                ))
                fig.update_layout(
                    margin=dict(l=20, r=20, t=40, b=20),
                    height=200,
                )
                return fig
            # Create the KPI card figure
            fig = create_card("Sales", total_sales, "coral")
            # Display the figure in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        # Profits metric
        with col3:
            total_profits = order_details['Profits'].sum()
            def create_card(title, value, color):
                fig = go.Figure(go.Indicator(
                    mode="number",
                    value=value,
                    title={"text": f"<b>{title}</b>"},
                    number={"font": {"size": 45, "color": color}},
                    domain={'x': [0, 1], 'y': [0, 1]}
                ))
                fig.update_layout(
                    margin=dict(l=20, r=20, t=40, b=20),
                    height=200,
                )
                return fig
            # Create the KPI card figure
            fig = create_card("Profits", total_profits, "coral")

            # Display the figure in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        # Revenue metric
        with col4:
            total_revenue = order_details["Total Retail Price for This Order"].sum().round()
            def create_card(title, value, color):
                fig = go.Figure(go.Indicator(
                    mode="number",
                    value=value,
                    title={"text": f"<b>{title}</b>"},
                    number={"font": {"size": 45, "color": color}},
                    domain={'x': [0, 1], 'y': [0, 1]}
                ))
                fig.update_layout(
                    margin=dict(l=20, r=20, t=40, b=20),
                    height=200,
                )
                return fig
            # Create the KPI card figure
            fig = create_card("Revenue", total_revenue, "coral")
            # Display the figure in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("YOY Growth")
        st.markdown("___")
        col1, col2 = st.columns([1, 2], gap="small")

        order_details["year"] = order_details["Date Order was placed"].dt.year
        yoy_sales = order_details.groupby('year')['Quantity Ordered'].sum().reset_index()
        yoy_sales['Sales YOY'] = yoy_sales['Quantity Ordered'].pct_change() * 100
        yoy_sales['Sales YOY'] = yoy_sales['Sales YOY'].fillna(0).round(2).map(lambda x: f'{x:.2f}%')
        yoy_sales = yoy_sales[["year", "Sales YOY"]]

        yoy_profits = order_details.groupby('year')['Profits'].sum().reset_index()
        yoy_profits["Profits YOY"] = yoy_profits['Profits'].pct_change() * 100
        yoy_profits["Profits YOY"] = yoy_profits["Profits YOY"].fillna(0).round(2).map(lambda x: f'{x:.2f}%')
        yoy_profits = yoy_profits[["year", "Profits YOY"]]

        yoy_revenue = order_details.groupby('year')['Total Retail Price for This Order'].sum().reset_index()
        yoy_revenue["Revenue YOY"] = yoy_revenue["Total Retail Price for This Order"].pct_change() * 100
        yoy_revenue["Revenue YOY"] = yoy_revenue["Revenue YOY"].fillna(0).round(2).map(lambda x: f'{x:.2f}%')
        yoy_revenue = yoy_revenue[["year", "Revenue YOY"]]

        yoy_df = pd.merge(yoy_sales, yoy_profits, how='left', on='year')
        yoy_df = pd.merge(yoy_df, yoy_revenue, how='left', on='year')
        yoy_df.rename(columns={'year': 'Years'}, inplace=True)

        with col1:
            st.table(yoy_df)
            st.write("We can see here year over year growth & loss in sales, profits, revenue & then we can "
                     "visulize this in the plot")

        with col2:
            # Convert YoY columns to numeric values for plotting
            yoy_df['Sales YOY'] = yoy_df['Sales YOY'].str.rstrip('%').astype(float)
            yoy_df['Profits YOY'] = yoy_df['Profits YOY'].str.rstrip('%').astype(float)
            yoy_df['Revenue YOY'] = yoy_df['Revenue YOY'].str.rstrip('%').astype(float)

            # Create a line chart with Plotly
            fig = px.line(yoy_df, x='Years', y=['Sales YOY', 'Profits YOY', 'Revenue YOY'],
                          # title='Year-over-Year Growth',
                          labels={'value': 'YoY Growth (%)', 'variable': 'Metric'},
                          markers=True)

            # # Update the layout for better readability
            fig.update_layout(
                xaxis_title='Year',
                yaxis_title='YoY Growth (%)',
                legend_title='Metrics'
            )
            st.plotly_chart(fig, use_container_width=False)

        st.subheader("Monthly Growth")
        st.markdown("___")
        order_details["Months"] = order_details["Date Order was placed"].dt.month

        monthly_data = order_details.groupby("Months")[
            ["Quantity Ordered", "Total Retail Price for This Order", "Profits"]].sum().reset_index()

        fig = px.line(monthly_data, x='Months', y=['Quantity Ordered', 'Total Retail Price for This Order', 'Profits'],
                      # title='Monthly Growth',
                      labels={'value': 'Values', 'Months': 'Months'},
                      markers=True,
                      height=250)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Customer Relation")
        st.markdown("___")
        col1, col2, col3 = st.columns(3, gap="small")

        with col1:
            customer_distribution = order_details["Customer Status"].value_counts().reset_index()
            fig = px.pie(customer_distribution, values="count", names='Customer Status', title='Customers distribution')
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            order_details['Delivery Time (Days)'] = (
                    order_details['Delivery Date'] - order_details['Date Order was placed']).dt.days
            replace_dict = {'SILVER': 'Silver', 'GOLD': 'Gold', 'PLATINUM': 'Platinum'}
            order_details['Customer Status'] = order_details['Customer Status'].replace(replace_dict)
            average_time_to_deliver = order_details.groupby("Customer Status")[
                "Delivery Time (Days)"].mean().reset_index()
            fig = px.bar(average_time_to_deliver,
                         x='Customer Status',
                         y='Delivery Time (Days)',
                         title='Average Day to Deliver by Customer Status',
                         width=100,  # Set figure width
                         height=350,  # Set figure height
                         )
            fig.update_traces(marker=dict(line=dict(width=2)),  # Customize bar width
                              selector=dict(type='bar')
                              )
            st.plotly_chart(fig, use_container_width=True)

        with col3:
            top_suppliers = order_details.groupby("Customer ID")["Quantity Ordered"].sum().reset_index() \
                .sort_values(by="Quantity Ordered", ascending=False).head(10)

            fig = px.pie(top_suppliers, values="Quantity Ordered", names='Customer ID', title='Top 10 Customers')

            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Product & Supplier Value")
        st.markdown("___")
        col1, col2, col3 = st.columns([1, 1, 2], gap="small")

        with col1:
            revenue_products = merge_data.groupby("Product Category")[
                "Total Retail Price for This Order"].sum().reset_index()
            # Create bar chart using Plotly
            fig = px.bar(revenue_products, x='Product Category', y='Total Retail Price for This Order',
                         title='Revenue by products',
                         labels={'x': 'Product Category', 'y': 'Total Retail Price for This Order'})
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            def get_country_name(country_code):
                try:
                    country = pycountry.countries.get(alpha_2=country_code)
                    if country:
                        return country.name
                    else:
                        return "Unknown"
                except:
                    return "Unknown"

            merge_data['CountryName'] = merge_data['Supplier Country'].apply(get_country_name)
            supplier_country = merge_data["CountryName"].value_counts().reset_index()
            # Assuming you have already created the 'supplier_country' DataFrame with columns 'index' and 'CountryName'
            fig = px.bar(supplier_country, x='CountryName', y='count', labels={'CountryName', 'count'},
                         title='Supplier Countries')
            st.plotly_chart(fig, use_container_width=True)
        with col3:
            top_suppliers = merge_data["Supplier Name"].value_counts().reset_index() \
                                .sort_values(by='count', ascending=False)[0:10]
            fig = go.Figure(
                data=[go.Pie(labels=top_suppliers['Supplier Name'], values=top_suppliers['count'], hole=0.5)])

            # Update layout for title and others
            fig.update_layout(title='Top 10 Suppliers Distribution')
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("___")

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
            .up-arrow {
                position: absolute;
                top: 10px;
                right: 10px;
                cursor: pointer;
            }
            </style>
            """
            , unsafe_allow_html=True
        )

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
                <a href="https://github.com/yourusername"><img src="github-logo.png" width="30" height="30"></a>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <a href="mailto:sjpradan@gmail.com"><img src="gmail.png" width="30" height="30"></a>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <a href="https://linkedin.com/yourusername"><img src="linkedin.png" width="30" height="30"></a>
                <div class="up-arrow" onclick="scrollToTop()">
                    <img src="uparrow.png" width="30" height="30">
                </div>
            </div>
            """
            , unsafe_allow_html=True
        )

    def unknown_dashboard():
        st.title("Projects - Page 1")

    def Project1():
        st.title("Projects - Page 1")

    def Project2():
        st.title("Projects - Page 1")
        # Add content for the first page of projects

    def Project3():
        st.title("Projects - Page 2")
        # Add content for the second page of projects

    # Sidebar and navigation
    st.sidebar.image(portfolio_icon, use_column_width=False, width=200, caption="")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Projects", "Blogs", "Dataset"])

    # Main content based on selected page
    if page == "Home":
        Home()

    elif page == "Dashboard":
        subpage = st.sidebar.radio("View Dashboards", ["Retail Performance Dashboard", "Unknown Dashboard"])
        if subpage == "Retail Performance Dashboard":
            retail_performance_dashboard()
        elif subpage == "Unknown Dashboard":
            unknown_dashboard()

    elif page == "Projects":
        subpage = st.sidebar.radio("View All Projects", ["Project1", "Project2", "Project3"])
        if subpage == "Project1":
            Project1()
        elif subpage == "Project2":
            Project2()
        elif subpage == "Project3":
            Project3()

    elif page == "Blogs":
        Blogs()
    elif page == "Dataset":
        Dataset()

def Home():
    """Home section."""

    # Add custom space from the top
    st.markdown(
        """
        <style>
        .spacer {
            margin-top: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Add a spacer div to create space
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    # Define Image
    profile_photo = r"C:\Users\satya\PycharmProjects\portflios\Profile\Profile picture.jpg"
    # Create two columns
    col1, col2 = st.columns(2)

    # Add content to the first column
    with col1:
        st.title("My Name")
        st.subheader("Software Engineer")
        st.write("""
    Hi, I'm [Your Name], a data scientist passionate about solving real-world problems using data. 
    I have experience in machine learning, data analysis, and visualization. 
    This is my portfolio showcasing some of my projects and skills.
    """)

    # Add content to the second column
    with col2:
        st.image(profile_photo, use_column_width=True)


    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Soft Skills")
        st.markdown("---")
        st.write("""
            - Data Analysis ⭐⭐⭐⭐⭐
            - Machine Learning ⭐⭐⭐⭐⭐
            - Data Visualization ⭐⭐⭐⭐⭐
            - Python Programming ⭐⭐⭐⭐⭐
            """)

    with col2:
        st.subheader("Technical Skills")
        st.markdown("--------------")
        st.write("""
                    - Data Analysis ⭐⭐⭐⭐⭐
                    - Machine Learning ⭐⭐⭐⭐⭐
                    - Data Visualization ⭐⭐⭐⭐⭐
                    - Python Programming ⭐⭐⭐⭐⭐
                    """)

# Dashboard in home section-------------------------------------------------------------------------
    st.markdown(
        """
        <style>
        .spacer {
            margin-top: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Add a spacer div to create space
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.header("Dashboard")
    st.markdown("--------------")
    st.subheader("Sales & Profit Dashboard")
    if st.button("View Sales & Profit Dashboard"):
        # Replace the URL with your LinkedIn profile URL
        st.markdown("[Projet1](https://www.linkedin.com/your-profile)")
    dashboard = r"C:\Users\satya\PycharmProjects\portflios\Dashboard\Dashboard.jpg"
    st.image(dashboard,use_column_width=True)
    st.write("write description here.....")

    st.subheader("Customer Retention")
    if st.button("View Customer Retention Dashboard"):
        # Replace the URL with your LinkedIn profile URL
        st.markdown("[Projet1](https://www.linkedin.com/your-profile)")
    dashboard = r"C:\Users\satya\PycharmProjects\portflios\Dashboard\Dashboard.jpg"
    st.image(dashboard,use_column_width=True)
    st.write("write description here.....")

# Projects in home section--------------------------------------------------------------------------
    st.markdown(
        """
        <style>
        .spacer {
            margin-top: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Add a spacer div to create space
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.header("Projects")
    st.markdown("--------------")
    col1, col2,col3 = st.columns(3)
    with col1:
        project1pic = r"C:\Users\satya\PycharmProjects\portflios\Projects\Project1.jpg"
        if st.button("View Project1"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet1](https://www.linkedin.com/your-profile)")
        st.image(project1pic,use_column_width=True)
        st.write("Write description here....")

    with col2:
        project2pic = r"C:\Users\satya\PycharmProjects\portflios\Projects\Project2.jpg"
        if st.button("View Project2"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet2](https://www.linkedin.com/your-profile)")
        st.image(project2pic, use_column_width=True)
        st.write("Write description here....")

    with col3:
        project3pic = r"C:\Users\satya\PycharmProjects\portflios\Projects\Project3.jpg"
        if st.button("View Project3"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet3](https://www.linkedin.com/your-profile)")
        st.image(project3pic, use_column_width=True)
        st.write("Write description here....")

# Blogs in home section--------------------------------------------------------------------------
    st.markdown(
        """
        <style>
        .spacer {
            margin-top: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Add a spacer div to create space
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.subheader("Blogs")
    st.markdown("--------------")
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        blog1 = r"C:\Users\satya\PycharmProjects\portflios\Blogs\blog1.jpg"
        st.image(blog1, use_column_width=True)
        st.write("Write description here....")
        if st.button("Click1"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet2](https://www.linkedin.com/your-profile)")
    with col2:
        blog2 = r"C:\Users\satya\PycharmProjects\portflios\Blogs\blog2.jpg"
        st.image(blog2, use_column_width=True)
        st.write("Write description here....")
        if st.button("Click2"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet2](https://www.linkedin.com/your-profile)")
    with col3:
        blog3 = r"C:\Users\satya\PycharmProjects\portflios\Blogs\blog3.jpg"
        st.image(blog3, use_column_width=True)
        st.write("Write description here....")
        if st.button("Click3"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet2](https://www.linkedin.com/your-profile)")
    with col4:
        blog4 = r"C:\Users\satya\PycharmProjects\portflios\Blogs\blog4.jpg"
        st.image(blog4, use_column_width=True)
        st.write("Write description here....")
        if st.button("Click4"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet2](https://www.linkedin.com/your-profile)")
    st.markdown("--------------")

# Add footer------------------------------------------------------------------------------------------------
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
        .up-arrow {
            position: absolute;
            top: 10px;
            right: 10px;
            cursor: pointer;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

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
            <a href="https://github.com/yourusername"><img src="github-logo.png" width="30" height="30"></a>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <a href="mailto:sjpradan@gmail.com"><img src="gmail.png" width="30" height="30"></a>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://linkedin.com/yourusername"><img src="linkedin.png" width="30" height="30"></a>
            <div class="up-arrow" onclick="scrollToTop()">
                <img src="uparrow.png" width="30" height="30">
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )

def Dashboard():
    st.subheader("Dashboard1")
    dashboard = "Dashboard.jpg"
    st.image(dashboard, use_column_width=True)
    st.write("write description here.....")

    st.subheader("Dashboard2")
    dashboard = "Dashboard.jpg"
    st.image(dashboard, use_column_width=True)
    st.write("write description here.....")


def Blogs():

    st.title("About Me")
    st.write("""
    Hi, I'm [Your Name], a data scientist passionate about solving real-world problems using data. 
    I have experience in machine learning, data analysis, and visualization. 
    This is my portfolio showcasing some of my projects and skills.
    """)

    st.subheader("Skills")
    st.write("""
    - Data Analysis
    - Machine Learning
    - Data Visualization
    - Python Programming
    """)

def Dataset():
    """Dataset Section."""

    col1, col2, col3 , col4 = st.columns([0.7,1,0.2,1])
    with col2:
        st.title("Datasets")
    with col3:
        st.image(r"C:\Users\satya\PycharmProjects\portflios\Icons\dataset_6802146.png", width=100)

    st.markdown("___")
    st.subheader("Retail Performance Analysis Data")
    col1, col2 = st.columns(2)
    with col1:
        # Read Dataset
        order_details = pd.read_excel(
            r"C:\Users\satya\PycharmProjects\portflios\Data\raw_data_orders_100.xlsx")

        int_to_convert_text = ['Customer ID', 'Order ID', 'Product ID']
        order_details[int_to_convert_text] = order_details[int_to_convert_text].astype(str)

        date_format = ['Date Order was placed', 'Delivery Date']
        order_details[date_format] = order_details[date_format].apply(pd.to_datetime)
        order_details[date_format] = order_details[date_format].apply(lambda x: x.dt.strftime('%d-%m-%Y'))

        st.write("Order's Data Preview:")
        st.download_button(label="⬇️", data=order_details.to_csv(), file_name="order_details.csv",
                           mime="text/csv")

        st.write(order_details.head())

    with col2:
        # Read Dataset
        supplier_details = pd.read_excel(
            r"C:\Users\satya\PycharmProjects\portflios\Data\raw_data_product_supplier.xlsx")

        int_to_convert_text = ['Product ID','Supplier ID']
        supplier_details[int_to_convert_text] = supplier_details[int_to_convert_text].astype(str)

        st.write("Supplier's Data Preview:")
        st.download_button(label="⬇️", data=supplier_details.to_csv(),
                           file_name="supplier_details.csv", mime="text/csv")

        st.write(supplier_details.head())

if __name__ == "__main__":
    main()
