import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# streamlit part
st.set_page_config(page_title="Airbnb Data Analysis", page_icon="✈️", layout="wide")
st.title("Airbnb Data Analysis 🏠")
st.write("")

def datafm():
    df = pd.read_csv(r"C:\Users\Manir\Desktop\Airbnb prjct\Airbnb.csv")
    return df
df = datafm()

with st.sidebar:
    select = option_menu("Menu", ["Home", "Data Analysis", "About"])

if select == "Home":
    st.subheader("Welcome to the Airbnb")
    image1= Image.open(r"C:\Users\Manir\Downloads\air.jfif")
    st.image(image1)

    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')

    st.subheader("Reviews")
    
if select == "Data Analysis":
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***","***LOCATION BASED***","***GEOSPATIAL VISUALIZATION***","***TOP CHATRT***"])
    with tab1:
        st.title("***PRICE DIFFERENCE***")
        col1,col2 =st.columns(2)

        with col1:

            country = st.selectbox("Select the Country",df["country"].unique())

            df1 = df[df["country"] == country]
            df1.reset_index(drop=True,inplace=True) 

            room_ty = st.selectbox("Select the Room Type",df1["room_type"].unique())

            df2 = df1[df1["room_type"] == room_ty]
            df2.reset_index(drop=True,inplace=True) 

            df_bar = pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace=True)  
            df_bar = df_bar.sort_values(by='price', ascending=True)

            fig_bar = px.bar(df_bar, x ='property_type',y='price',title = "PRICE FOR PROPERTY_TYPES",hover_data = ["number_of_reviews","review_scores"], color_discrete_sequence = px.colors.qualitative.Alphabet ,width =550,height = 500)
            st.plotly_chart(fig_bar)


        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            proper_ty = st.selectbox("Select property type",df2["property_type"].unique())
            
            df4 = df2[df["property_type"] == proper_ty]
            df4.reset_index(drop =True, inplace = True)

            df_pie = pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace = True)

            fig_pi = px.pie(df_pie, values = "price", names = "host_response_time",
            hover_data = ["bedrooms"],color_discrete_sequence = px.colors.qualitative.Plotly,
            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",width= 600, height= 500)
            st.plotly_chart(fig_pi)

        col1,col2 = st.columns(2)

        with col1:
             
            hostresponsetime= st.selectbox("Select the host_response_time",df4["host_response_time"].unique())

            df5= df4[df4["host_response_time"] == hostresponsetime]

            df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace= True)

            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
            title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data=["price"],
            barmode='group',color_discrete_sequence=px.colors.qualitative.Plotly, width=600, height=500)
            


            st.plotly_chart(fig_do_bar)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")


            df_do_bar_2 = pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_do_bar_2.reset_index(inplace=True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='BEDROOMS AND BEDS ACCOMMODATES',hover_data=["price"],
            barmode='group',color_discrete_sequence=px.colors.qualitative.Plotly, width= 600, height= 500)
           
            st.plotly_chart(fig_do_bar_2)

    with tab2:

        def datafm():
            df_a= pd.read_csv(r"C:\Users\Manir\Desktop\Airbnb prjct\Airbnb.csv")
            return df_a
        
        df_a = datafm()


        st.title("***AVAILABILITY ANALYSIS***")
        col1,col2 = st.columns(2)

        with col1:

            country_a= st.selectbox("Select the Country_a",df_a["country"].unique())

            df1_a= df[df["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique())
            
            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)

            df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30")
            st.plotly_chart(df_a_sunb_30)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")


            df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sunb_60)

        col1,col2 =st.columns(2)

        with col1:

            df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(df_a_sunb_90)

        with col2:

            df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.qualitative.Set3)
            st.plotly_chart(df_a_sunb_365)

        roomtype_a =st.selectbox("Select the Room Type_a",df2_a["room_type"].unique())
        
        df3_a =df2_a[df2_a["room_type"] == roomtype_a]

        df_mul_bar_a  = pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df_mul_bar_a.reset_index(inplace=True)

        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data=["price"],
        barmode='group',color_discrete_sequence=px.colors.qualitative.Plotly,width=1050)

        st.plotly_chart(fig_df_mul_bar_a)
    
    with tab3:
        st.title("**Location Analysis**")
        st.write("")

        def datafr():
            df = pd.read_csv(r"C:\Users\Manir\Desktop\Airbnb prjct\Airbnb.csv")
            return df
        df_1 = datafr()

        country_1 = st.selectbox("Select the Country_1",df_1["country"].unique())

        df1_1 = df_1[df_1["country"] == country_1]
        df1_1.reset_index(drop =True, inplace = True)

        proper_ty_1 = st.selectbox("Select Property Type",df1_1["property_type"].unique())

        df2_1 = df_1[df_1["property_type"] == proper_ty_1]
        df2_1.reset_index(drop = True, inplace = True)

        st.write("")
        
        def select_the_df(sel_val):
            if sel_val == str(df2_1['price'].min())+''+str('to')+' '+str(differ_max_min*0.30 + df2_1["price"].min())+' '+str("(30% of the Value)"):
                df_val_30 = df2_1[df2_1["price"] <= differ_max_min*0.30 + df2_1["price"].min()]
                df_val_30.reset_index(drop = True, inplace = True)
                return df_val_30 
            
            elif sel_val == str(differ_max_min*0.30 + df2_1['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_1['price'].min())+' '+str("(30% to 60% of the Value)"):
                df_val_60= df2_1[df2_1["price"] >= differ_max_min*0.30 + df2_1['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_1['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
                
            elif sel_val == str(differ_max_min*0.60 + df2_1['price'].min())+' '+str('to')+' '+str(df2_1['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df2_1[df2_1["price"] >= differ_max_min*0.60 + df2_1['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min = df2_1['price'].max() - df2_1['price'].min()
        
        val_sel= st.radio("Select the Price Range",[str(df2_1['price'].min())+''+str('to')+' '+str(differ_max_min*0.30 + df2_1["price"].min())+' '+str("(30% of the Value)"), 
                           str(differ_max_min*0.30 + df2_1['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_1['price'].min())+' '+str("(30% to 60% of the Value)"), 
                           str(differ_max_min*0.60 + df2_1['price'].min())+' '+str('to')+' '+str(df2_1['price'].max())+' '+str("(60% to 100% of the Value)")])


        df_val_sel = select_the_df(val_sel)

        st.dataframe(df_val_sel)

        # checking the correlation

        df_val_sel_corr = df_val_sel.drop(columns = ["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()


        st.dataframe(df_val_sel_corr)

        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)
        
        # to get plot in order manner 
        df_val_sel_gr =df_val_sel_gr.sort_values(by='accommodates',ascending=True)

        fig_1 = px.bar(df_val_sel_gr, x = "accommodates", y= ["cleaning_fee","bedrooms","beds"], title ="ACCOMMODIES",
                      hover_data=["extra_people"], barmode= 'group', color_discrete_sequence = px.colors.qualitative.Plotly, width=1000 )

        st.plotly_chart(fig_1)

        room_ty_l= st.selectbox("Select the Room_Type_l", df_val_sel["room_type"].unique())

        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]
        

        # to

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_2)
 
        # to get plot in order manner 
        df_val_sel_rt=df_val_sel_rt.sort_values(by='government_area',ascending=True)

        fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                    hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_3)








    with tab4:
        st.title("GEOSPATIAL VISUALIZATION")
        st.write("")

        fig_4 = px.scatter_mapbox(df,lat ="latitude",lon ="longitude", color ="price",size ='accommodates',
        color_continuous_scale = "rainbow", hover_name = 'name',range_color = (0,49000),mapbox_style = "open-street-map",
        zoom = 1)
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)
    

    with tab5:

        country_t= st.selectbox("Select the Country_t",df["country"].unique())

        df1_t= df[df["country"] == country_t]

        property_ty_t= st.selectbox("Select the Property_type_t",df1_t["property_type"].unique())

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price", ascending = True)
        df2_t_sorted.reset_index(drop= True, inplace= True)

        df_price = pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace = True)
        df_price.columns= ["host_neighbourhood","Total_price","Average_price"]

        col1,col2 = st.columns(2)

        with col1:
            df_price_sort = df_price.sort_values(by = "Total_price", ascending=True)
            df_price_sort.reset_index(drop =True, inplace = True)

            fig_price= px.bar(df_price_sort, x= "Total_price", y="host_neighbourhood", orientation ='h',
            title = "PRICE BASED ON THE HOST_NEIGHBOURHOOD",color_discrete_sequence=px.colors.qualitative.Plotly,
             width=600,height=800)

            st.plotly_chart(fig_price)

        with col2:
             
            df_price_sort1 = df_price.sort_values(by = "Average_price", ascending=True)
            df_price_sort1.reset_index(drop =True, inplace = True)
        
            fig_price_2 = px.bar(df_price_sort1, x="Average_price", y="host_neighbourhood",orientation = 'h',
            title = "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",color_discrete_sequence=px.colors.qualitative.Plotly,width=600, height =800)
            st.plotly_chart(fig_price_2)

        col1,col2 =st.columns(2)

        with col1:

            df_price_1 = pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index( inplace = True)
            df_price_1.columns = ["host_location","Total_price","Average_price"]
            
            df_price_s = df_price_1.sort_values(by = "Total_price", ascending=True)
            df_price_s.reset_index(drop= True, inplace =True )
            
            fig_price_3 =  px.bar(df_price_s, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Sunsetdark,
                                title= "PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            df_price_s1 = df_price_1.sort_values(by = "Average_price", ascending=True)
            df_price_s1.reset_index(drop= True, inplace =True )
            
            fig_price_4 =px.bar(df_price_s1 , x="Average_price", y ="host_location", orientation="h",width =600,
                                 height=800, color_discrete_sequence=px.colors.qualitative.Plotly,
                                 title = "Price Based on the Host Location")
            st.plotly_chart(fig_price_4)

            room_type_t =st.selectbox("Select room type",df2_t_sorted["room_type"].unique())

            df3_t = df2_t_sorted[df2_t_sorted["room_type"]== room_type_t]

            df3_t_sorted_price= df3_t.sort_values(by= "price", ascending=True)

            df3_t_sorted_price.reset_index(drop= True, inplace = True)

            df3_top_50_price= df3_t_sorted_price.head(100)
            
        fig_top_50_price_1 = px.bar(df3_top_50_price,x="name", y ="price",
                                    color = "price", color_continuous_scale= "rainbow",
                                        range_color =(0,df3_top_50_price["price"].max()),
                                        title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                        width=1200, height= 800, hover_data = ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2 = px.bar(df3_top_50_price, x="name", y= "price",color = "price", color_continuous_scale= "greens",
                                    range_color = (0,df3_top_50_price["price"].max()),title =
                                        "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",width=1200, height= 800,
                            hover_data= ["accommodates","bedrooms","beds","bed_type"])
        
        st.plotly_chart(fig_top_50_price_2)
                








if select == "About":
    st.header("ABOUT THIS PROJECT")

    st.subheader(":orange[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')
    
    st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')
    
    st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')
    
    st.subheader(":orange[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
    
    st.subheader(":orange[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')

