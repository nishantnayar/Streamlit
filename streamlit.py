import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_autorefresh import st_autorefresh
from PIL import Image

# Layout
st.set_page_config(page_title="Project",
                   layout="wide",
                   initial_sidebar_state="expanded")
count = st_autorefresh(interval=60000, limit=100000000, key="fizzbuzzcounter")


# this is where we will create a CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


local_css("config/CustomStyle.css")

# options menu
with st.sidebar:
    selected = option_menu("Main Menu", ['Home', 'LLM', 'About'],
                           icons=['house', 'app', 'info-circle'],
                           menu_icon="list", default_index=1)

# Home Page
if selected == "Home":
    st.write("home is where the heart is")

if selected == 'LLM':
    tab1, tab2 = st.tabs(["RAG", "Others"])

    with tab1:
        st.title('Retrieval-Augmented Generation')
        st.write("This is where we will add the LLM Application")

    with tab2:
        st.title('Others')
        st.write("Work in Progress")

# About Page
if selected == 'About':
    st.title('Author')
    with st.container():
        col1, col2 = st.columns([300, 100])
        col1.write('')
        col1.write('')
        col1.write('')
        col1.write('**Name:**   Nishant Nayar')
        col1.write('**Education:**    M.S. Data Science')
        col1.write('**College:**    Physical Sciences Division, University of Chicago')
        col1.write('**Contact:**    nishant.nayar@hotmail.com  or [linkedin](www.linkedin.com/in/nishantnayar)')
        img = Image.open('fig/IMG_0245.jpg').resize((256, 256))
        col2.image(img)

    st.divider()

    st.title('About Me')
    st.write("Passionate about uncovering the potential within data, I bring over 15 years of experience in data "
             "management and analytics, complemented by an MS in Analytics from The University of Chicago with a "
             "focus on Data Visualization and Explainable AI. Throughout my career, I've successfully led agile "
             "development teams and orchestrated the execution of complex data programs, specializing in enterprise "
             "data management governance, technology, and strategy. With a track record of leading global teams and "
             "delivering business-critical projects, I thrive on the transformative power of data-driven "
             "decision-making. My commitment to optimizing operational efficiency and generating optimal business "
             "value through data analytics drives my professional journey.")
