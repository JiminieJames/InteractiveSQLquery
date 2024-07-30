# conn = sqlite3.connect('../resources/fastfood.db')

import streamlit as st
import pandas as pd
import sqlite3

# Path to your SQLite database
db_path = '../resources/fastfood.db'

# Function to run a query and fetch data
def run_query(query):
    conn = sqlite3.connect(db_path)
    result = pd.read_sql(query, conn)
    conn.close()
    return result

# Streamlit application
st.title("Interactive Query Builder for Fast Food Nutrition Data")

st.write("""
This app allows you to build and run your own SQL queries on the fast food nutrition database.
""")

# Get unique values for dropdown options
conn = sqlite3.connect(db_path)
company_options = pd.read_sql('SELECT DISTINCT Company FROM menu', conn)['Company'].tolist()
conn.close()

# Dropdown menu for selecting company
selected_company = st.selectbox("Select Company", company_options)

# Input fields for specifying ranges
calories_limit = st.number_input("Calories less than or equal to. Enter 9999 if not wanting to limit.", min_value=0, value=500)
sugars_limit = st.number_input("Sugars (g) less than or equal to. Enter 9999 if not wanting to limit.", min_value=0, value=50)
fat_limit = st.number_input("Total Fat (g) less than or equal to. Enter 9999 if not wanting to limit.", min_value=0, value=20)
sodium_limit = st.number_input("Sodium  (mg) less than or equal to. Enter 9999 if not wanting to limit.", min_value=0, value=500)
protein_limit = st.number_input("Protein (g) greater than or equal to. Enter 9999 if not wanting to limit.", min_value=0, value=10)

# Button to run the query
if st.button("Run Query"):
    # Build the query based on user input
    query = f'''
    SELECT Company, Item, Calories, "Sugars (g)", "Total Fat (g)", "Sodium  (mg)", "Protein (g)"
    FROM menu
    WHERE Company = '{selected_company}' 
    AND Calories <= {calories_limit} 
    AND "Sugars (g)" <= {sugars_limit} 
    AND "Total Fat (g)" <= {fat_limit} 
    AND "Sodium  (mg)" <= {sodium_limit} 
    AND "Protein (g)" >= {protein_limit};
    '''
    
    try:
        result = run_query(query)
        st.write("Query Results:")
        st.dataframe(result)
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.write("""
Example Queries:
- SELECT * FROM menu LIMIT 5
- SELECT item_name, calories FROM menu WHERE calories < 500
- SELECT item_name, calories, carbohydrates, protein
  FROM menu
  WHERE restaurant = 'McDonald's' AND calories < 500;
""")
