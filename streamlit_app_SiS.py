
import streamlit as st
from snowflake.snowpark.context import get_active_session


st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """
)

from snowflake.snowpark.functions import col 

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))


ingredients_list=st.multiselect (
    'Choose up to 5 ingredients:'
    ,my_dataframe
)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    ingredients_string=''
    for fruit_chosen in ingredients_list: 
        ingredients_string += fruit_chosen+' '
    st.write(ingredients_string)
    my_insert_stmt="""insert into smoothies.public.orders(ingredients)
              values('"""+ ingredients_string + """')"""
    time_to_insert=st.button('Submit Order')
    if time_to_insert: 
        session.sql(my_insert_stmt).collect()
        
        st.success('Your Smoothie is ordered!', icon="✅")
   
