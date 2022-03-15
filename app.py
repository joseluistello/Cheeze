import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Recruitment Network", page_icon=":wave:", layout="wide")

# Header ---- 
with st.container():
    st.subheader("Welcomeeee :wave:")
    st.title("Recruitment Network")
    st.write("")


from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
nodes.append( Node(id="javascript", 
                   label="", 
                   size=800, 
                   svg="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1024px-Unofficial_JavaScript_logo_2.svg.png") 
            ) 
            
nodes.append( Node(id="react",
                   label="",
                   size=800, 
                   svg="https://cdn.worldvectorlogo.com/logos/react-1.svg") 
            )

edges.append( Edge(source="javascript", 
                   label="framework_of", 
                   target="react", 
                   type="CURVE_SMOOTH") 
            )

config = Config(width=1400, 
                height=500, 
                directed=True,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", # or "blue"
                collapsible=True,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True}
                # **kwargs e.g. node_size=1000 or node_color="blue"
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)




