import streamlit
import pandas
import requests

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Breakfast oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

############################# API tutorial on streamlit##################################
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Normalize semi-structured JSON data into a flat table.
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Outputs table as a dataframe onto streamlit app UI
streamlit.dataframe(fruityvice_normalized)

use role pc_rivery_role;
use warehouse pc_rivery_wh;

create or replace TABLE PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST (
	FRUIT_NAME VARCHAR(25)
);

insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST
values ('banana')
, ('cherry')
, ('strawberry')
, ('pineapple')
, ('apple')
, ('mango')
, ('coconut')
, ('plum')
, ('avocado')
, ('starfruit');
