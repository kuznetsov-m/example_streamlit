import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

def page_2():
    st.write('# chart_data')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.area_chart(chart_data)

    st.write('# chart')
    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c']
    )

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    )
    st.write(c)

    
    
    st.write('# Code block')
    with st.echo():
        # Everything inside this block will be both printed to the screen
        # and executed.

        print('my text')

        x = 5 + 4
        print(f'x = {x}')

    # And now we're back to _not_ printing to the screen
    foo = 'bar'

    st.write('# Code')
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')
    
    st.write('# Pandas DataFrame')
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    }))

    st.write('# JSON')
    st.json({
        'foo': 'bar',
        'baz': 'boz',
        'stuff': [
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 5',
        ],
    })

    st.write('# Random Line Chart')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])    
    st.line_chart(chart_data)

    st.write('# Map Chart')
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))