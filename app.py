import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers 

# Function to get response from LLM model 

def getLLamaResponse(input_text,no_words,blog_style):

    #model config
    llm=CTransformers(model='project_llm/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})

    #prompt template

    template= """
Write a blog for {blog_style} job profile based on the topic {input_text} within {no_words} words.
"""

    prompt= PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                           template=template)
    
    # Generation of the response from the model 

    response= llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

# Creating two more columns for additional 2 fields

col1,col2=st.columns([5,5])

with col1: 
    no_words = st.text_input("Enter the number of words you want the blog to be created")
with col2: 
    blog_style = st.selectbox("Writing the Blog for ",
                              ("Researchers", "Machine Learning and AI", "Miscellaneous", "MFT Automation"), index=0)
    
submit = st.button("Generate Blog")

## Final response
if submit:
    st.write(getLLamaResponse(input_text,no_words,blog_style))