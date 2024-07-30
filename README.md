# Project for Interactive Data Visualization

## Description

This project focuses on various data visualization techniques and tools to analyze and represent data effectively.

## Repository Structure

- `data/`: Contains the datasets used for analysis.
- `notebooks/`: Jupyter notebooks for data visualization and analysis.
- `scripts/`: Python scripts for data processing and visualization.
- `results/`: Output files and visualizations generated from the analysis.

------------------------------------------------------------------------

For this project I worked with a nutritional Kaggle dataset covering the Nutritional values, including Calories and Micro-nutrients, from six of the largest and most popular fast food restaurants: McDonald's, Burger King, Wendy's, Kentucky Fried Chicken (KFC), Taco Bell, and Pizza Hut.
It provides data on their food item offerings including Calories, Calories from Fat, Total Fat, Saturated Fat, Trans Fat, Cholesterol, Sodium, Carbs, Fiber, Sugars, Protein, and Weight Watchers Points (where available).
We plan to look at the dataset in various ways including:
1.      Whether one restaurant has higher volume of high caloric foods than others
2.      Which food items have the highest/lowest caloric values
3.      Using scatterplots to compare different categories (grams of sugar > calories) (cholesterol > calories) (grams of protein > grams of sugar) etc.
Ultimately our interactive visualizations hope to build a tool for users to make better decisions for themselves on which food items to select if they patronize any of these establishments.

--------------------------------------------------------------------------

Data Preparation
Download the Kaggle dataset and load it into a SQLite database.
Clean and preprocess the data for analysis.
Backend Setup
Set up a Flask backend to serve the data and handle API requests.
Write routes to fetch data based on user inputs.
Visualization Creation
Use Plotly (Python) or D3.js (JavaScript) to create the visualizations.
Incorporate AOS to animate the visualizations as users scroll through the page.
Frontend Development
Create an HTML page with sections for each visualization.
Add dropdowns, textboxes, or other interactive elements to filter the data.
Integrate AOS animations for a dynamic user experience.
Testing and Deployment
Test the project to ensure all components work seamlessly.
Deploy the project on GitHub Pages or another web hosting service.

Used Jinja2 template Rending
