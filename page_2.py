import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

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
    