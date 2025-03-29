# Airbnb Analysis

![image](https://github.com/user-attachments/assets/a326f943-8e9f-4a43-ba59-eb55f872c278)
<br/>
--
## Overview
The Airbnb Data Analysis and Visualization project focuses on exploring and presenting data in a clear way. It includes collecting data, cleaning it, processing it, and building an interactive Streamlit dashboard. The goal is to provide useful insights and make Airbnb data easy to understand
--
## Methods
- Data Collection: Web scraping, API access, database queries.
- Data Preprocessing: Data cleaning, handling missing values, feature engineering.
- ETL Work: MongoDB data extraction, data transformation using Pandas.
- EDA: Visualization with Matplotlib, Seaborn, and Plotly.
- Streamlit UI: Streamlit library for building interactive web applications.
--
## Skills Covered
- Data collection and integration.
- Data cleaning and preprocessing.
- ETL techniques for data transformation.
- Exploratory Data Analysis (EDA).
- Data visualization.
- Web application development with Streamlit.
  
--
## **Getting Started**
1. Clone the repo
   > https://github.com/aboyhere/Airbnb-Analysis 
2. install required packages
   >[pip install -r packages.text]
3. Run streamlit app
   > streamlit run Airbnb.py
4. Access the app in your browser
   <br/>
   **Automatically redirect to your local browser**
--

## Sample streamlit code
```python
st.title("GEOSPATIAL VISUALIZATION")
        st.write("")

        fig_4 = px.scatter_mapbox(df,lat ="latitude",lon ="longitude", color ="price",size ='accommodates',
        color_continuous_scale = "rainbow", hover_name = 'name',range_color = (0,49000),mapbox_style = "open-street-map",
        zoom = 1)
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)
```

## Conclusion

**Using this project to we can able to analysis the huge dataset into Visualization model and make decisions**





