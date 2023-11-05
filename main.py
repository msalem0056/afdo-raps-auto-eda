import streamlit as st

import pandas as pd
from sklearn.datasets import load_breast_cancer
import streamlit as st
import streamlit.components.v1 as components
import sweetviz as sv
from sklearn.preprocessing import StandardScaler



def app(title=None)-> None:
    """Creates the streamlit app

    Args:
        title (string, optional): The App name. Defaults to None.
    """
    st.title(title)
    st.markdown("### Developer: Mike Salem [Linked In](https://www.linkedin.com/in/mike-salem)")
    st.write("Description: The following app was created to showcase exploratory data analysis using Python. You can upload your own file in .csv format as well. The current example use the breast cancer dataset, but adding your own will utilize the latest.")


    default_data = True
    dataframe = load_breast_cancer(as_frame= True)
    dataframe = dataframe.data

    # Choose your own file
    uploaded_file = st.file_uploader("Upload file", type=['.csv','.tsv'])
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        default_data = False


    with st.spinner('Generating Report...'):
        # Use the analysis function from sweetviz module to create a 'DataframeReport' object.
        if not default_data:
            analysis = sv.analyze(dataframe)
            # Render the output on a web page.
            analysis.show_html(filepath='sweetviz.html', open_browser=False, layout='vertical', scale=1.0)
        render = open("sweetviz.html")
        html_file = open("sweetviz.html")
        components.html(render.read(), width=None, height = 900, scrolling= True)
    st.download_button(label="download report",
                                data=html_file.read(),
                                file_name="test_report.html")

if __name__ == "__main__":
    app(title='Exploratory Data Analysis')