import streamlit
import pandas
import requests
import snowflake.connector



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

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('The user entered ', add_my_fruit)
fruityvice_response2 = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)

# Normalize semi-structured JSON data into a flat table.
fruityvice_normalized2 = pandas.json_normalize(fruityvice_response2.json())
# Outputs table as a dataframe onto streamlit app UI
streamlit.dataframe(fruityvice_normalized2)
