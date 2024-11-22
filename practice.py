import streamlit as st
import nbformat

# Load the notebook
file_path = "HW3.ipynb"  # Replace with your file path

with open(file_path, 'r', encoding='utf-8') as f:
    notebook_content = nbformat.read(f, as_version=4)

# Title of the blog
st.title("HW3 - Technical Blog")

# Introductory text
st.markdown("""
### Welcome to the HW3 Technical Blog
This blog walks you through the code and outputs of the HW3 Jupyter Notebook, now transformed into an interactive Streamlit app. 
Enjoy exploring the analysis and insights!
""")

# Function to process and display each cell from the notebook
def display_notebook_content(cells):
    for cell in cells:
        if cell['cell_type'] == 'markdown':
            # Display markdown content
            st.markdown(cell['source'])
        elif cell['cell_type'] == 'code':
            # Display code content
            st.markdown("#### Code:")
            st.code(cell['source'])
            # Placeholder for outputs (if any)
            if 'outputs' in cell:
                for output in cell['outputs']:
                    if output['output_type'] == 'stream':
                        st.write(output['text'])
                    elif output['output_type'] == 'execute_result' and 'text/plain' in output['data']:
                        st.write(output['data']['text/plain'])
                    elif output['output_type'] == 'error':
                        st.error("Error: " + "\n".join(output['traceback']))

# Display content of the notebook
st.markdown("## Notebook Content")
display_notebook_content(notebook_content['cells'])
