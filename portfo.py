import streamlit as st
from PIL import Image

def main():
    """Main function to define the structure of the portfolio."""

    # Set page title and icon
    profile_icon = Image.open("user.png")
    st.set_page_config(page_title="Satyajeet Portfolio", page_icon=profile_icon,layout = "wide")

    # Load Image
    portfolio_icon = "Portfolio logo.png"

    # Display the image at the top left corner
    st.image(portfolio_icon, use_column_width=False, width=370, caption="")

    # Sidebar
    st.sidebar.image(portfolio_icon, use_column_width=False, width=200, caption="")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Projects", "Blogs", "Contact"])

    # Main content based on selected page
    if page == "Home":
        Home()
    elif page == "Dashboard":
        Dashboard()
    elif page == "Projects":
        projects()
    elif page == "Blogs":
        Blogs()
    elif page == "Contact":
        contact()

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
    profile_photo = "Profile picture.jpg"
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
        st.markdown("--------------")
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
    dashboard = "Dashboard.jpg"
    st.image(dashboard,use_column_width=True)
    st.write("write description here.....")

    st.subheader("Customer Retention")
    if st.button("View Customer Retention Dashboard"):
        # Replace the URL with your LinkedIn profile URL
        st.markdown("[Projet1](https://www.linkedin.com/your-profile)")
    dashboard = "Dashboard.jpg"
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
        project1pic = "Project1.jpg"
        if st.button("View Project1"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet1](https://www.linkedin.com/your-profile)")
        st.image(project1pic,use_column_width=True)
        st.write("Write description here....")

    with col2:
        project2pic = "Project2.jpg"
        if st.button("View Project2"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet2](https://www.linkedin.com/your-profile)")
        st.image(project2pic, use_column_width=True)
        st.write("Write description here....")

    with col3:
        project3pic = "Project3.jpg"
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
        blog1 = "blog1.jpg"
        st.image(blog1, use_column_width=True)
        st.write("Write description here....")
        if st.button("Click1"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet2](https://www.linkedin.com/your-profile)")
    with col2:
        blog2 = "blog2.jpg"
        st.image(blog2, use_column_width=True)
        st.write("Write description here....")
        if st.button("Click2"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet2](https://www.linkedin.com/your-profile)")
    with col3:
        blog3 = "blog3.jpg"
        st.image(blog3, use_column_width=True)
        st.write("Write description here....")
        if st.button("Click3"):
            # Replace the URL with your LinkedIn profile URL
            st.markdown("[Projet2](https://www.linkedin.com/your-profile)")
    with col4:
        blog4 = "blog4.jpg"
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

def projects():
    """Projects section."""

    st.title("Projects")

    # Example project 1
    st.subheader("Project 1: Title")
    st.write("""
    Description of the project goes here. 
    Include key points and results achieved.
    """)

    # Example project 2
    st.subheader("Project 2: Title")
    st.write("""
    Description of the project goes here. 
    Include key points and results achieved.
    """)

    # Add more projects as needed


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

def contact():
    """Contact section."""

    st.title("Contact")

    st.write("""
    Feel free to reach out to me for collaboration opportunities or just to say hello!
    """)

    st.write("[Email](mailto:sjpradan@egmail.com)")

    st.write("[LinkedIn](https://www.linkedin.com/in/your-profile)")

    st.write("[Github](https://github.com/sjpradhan)")

if __name__ == "__main__":
    main()
