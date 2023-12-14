import pandas as pd
import mysql.connector
import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import webbrowser

  
#sql database
mydb= mysql.connector.connect(
    host ='localhost',
    user='root',
    password=''
)
print(mydb)
mycursor=mydb.cursor(buffered=True)

mycursor.execute('''use airbnb''')
mydb.commit()

icon = Image.open(r"E:\streamlit\lgo.png")
st.set_page_config(page_title="Holiday Home & Appartment-Airbnb",
                page_icon= icon, 
                   layout="wide", initial_sidebar_state="auto") 

with st.sidebar:
    st.sidebar.markdown("# :rainbow[Select an option to filter:]")
    selected = st.selectbox("**Menu**", ("Home","analysis","Top Charts","location_download","map_view"))
 
if selected=="Home":
    cluum1,colum2 =st.columns([0.5,0.5])
    with cluum1:
        image =Image.open(r"E:\streamlit\air+_b\fdcb5df5-18bb-4563-aa81-6d1c7e2cbb19.webp")
        st.image(image)
        cluum13,colum20 =st.columns([0.5,0.5]) 
        with cluum13:
            image =Image.open(r"E:\streamlit\air+_b\90701f16-dbe7-4978-ab90-e0a186ec998e.webp")
            st.image(image)
        with colum20:
            image =Image.open(r"E:\streamlit\air+_b\54c30ac7-c07c-4078-96be-aa16c1f50a07.webp")
            st.image(image)
    cluum101,colum122 =st.columns([0.5,0.5])
    with cluum101:
            image=Image.open(r"E:\streamlit\air+_b\54c30ac7-c07c-4078-96be-aa16c1f50a07.webp")
            st.image(image)
            
    with colum122:
            image=Image.open(r"E:\streamlit\air+_b\3c1a5d33-42a7-485e-b885-e8cdc281b5d9.jpg")
            st.image(image)
            cluum10,colum12 =st.columns([0.5,0.5])
    with cluum10:
        image =Image.open(r"E:\streamlit\air+_b\90701f16-dbe7-4978-ab90-e0a186ec998e.webp")
        st.image(image)
    with colum12:
        image =Image.open(r"E:\streamlit\air+_b\54c30ac7-c07c-4078-96be-aa16c1f50a07.webp")
        st.image(image)
        
    with colum2:
        image =Image.open(r"E:\streamlit\air+_b\e7ee3078-43d1-4228-985f-74a62911a98c.webp")
        st.image(image)
    st.markdown('## :red[Project Title:]')
    st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Airbnb Analysis")
    st.markdown('## :red[Skills takes away FRom This project:]')
    st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  Python scarpint, Data Preprocessing, Visualization, EDA ,Streamlit ,Mongodb")
    st.markdown('## :red[Domain:]')
    st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Travel industry, Property Management and Tourism")
    colum3,colum4,colum5= st.columns([0.015,0.020,0.1])
    with colum3:
        if st.button("website"):
            webbrowser.open_new_tab('https://www.airbnb.co.in/')

    with colum4:
        if st.button("show_map"):
            webbrowser.open_new_tab('https://www.airbnb.co.in/sitemaps/v2')
if selected== "analysis":
    selected = st.sidebar.selectbox("**Type**", ("price_analysis","review_analysis","review_for_city"))
    # colum1,colum2 = st.columns([2,2])
    # with colum1:
    if selected =="price_analysis":
        mycursor.execute('''select room_type,avg(price) as avg_price from airbnb_data2 group by room_type order by avg_price desc ''')
        mydb.commit()
        df=pd.DataFrame(mycursor,columns=mycursor.column_names)
        # df
        fig = px.bar(df, y='avg_price',
                        x='room_type',
                        title="group by room_type using avg price",
                            color='room_type',
                        color_discrete_sequence=px.colors.sequential.Agsunset) 
        # fig.show()
        st.plotly_chart(fig,use_container_width=True) 

        
        # mycursor.execute('''select room_type,avg(price) as avg_price from airbnb_data2 group by room_type order by avg_price desc ''')
        # mydb.commit()
        # df=pd.DataFrame(mycursor,columns=mycursor.column_names)
        # # df
        # df['room_type']=df['room_type'].astype('str')
        # df['room_type']=df['room_type'].str.replace('Shared room',"1")
        # df['room_type']=df['room_type'].str.replace("Entire home/apt",'2')
        # df['room_type']=df['room_type'].str.replace('Private room','3')
        # df['room_type']=df['room_type'].astype('float')
        # df
        
        # x=df.index
        # y=df['room_type']
        # z=[0]

        # dx=[1]
        # dy=[1]
        # dz=df['avg_price']

        # fig=plt.figure(figsize=(8,4))
        # ax=plt.axes(projection='3d')
        # ax.bar3d(x,y,z,dx,dy,dz)
        # st.pyplot(fig)

        mycursor.execute('''select country, sum(price) as total_price from airbnb_data2 group by country order by total_price desc ''')
        mydb.commit()
        df=pd.DataFrame(mycursor,columns=mycursor.column_names)
        # df
        fig = px.bar(df, y='total_price',
                         x='country',
                        title="group by country using price",
                        color='total_price',
                        color_discrete_sequence=px.colors.sequential.Agsunset)
        # fig.show()
        st.plotly_chart(fig,use_container_width=True) 
    

    if selected=="review_analysis":
        colum1,column2 = st.columns([1,1])
        with colum1:
            selecte_country = st.selectbox(
                "select the country",
                ('United States','Canada','Spain','Australia','Brazil','Hong Kong','Portugal','China'))
    
        colum1,column2 = st.columns([1,1])
        with colum1:
            mycursor.execute(f'''select country ,city,room_type, price ,review_rating,host_name from airbnb_data2 
                                where  country like "{selecte_country}"
                                group by city,review_rating,country  order by review_rating desc , price desc limit 7''')
            mydb.commit()
            df=pd.DataFrame(mycursor,columns=mycursor.column_names)
            # df
            fig=px.sunburst(df,values='review_rating',
                        path=['country',"city",'room_type','review_rating','host_name'],
                            color='city',
                            template="plotly_dark",
                            title="top review_rating show price and city ")
                            # color_discrete_sequence=px.colors.sequential.Agsunset)
                    # fig.show()
            st.plotly_chart(fig,use_container_width=True) 
            
        with column2:
            fig=px.bar(df,x='city',y='price',color_discrete_sequence=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
    ##################################################################################################
        
    if selected=="review_for_city":
        select_country = st.selectbox("select the country",('United States','Canada','Spain','Australia','Brazil','Hong Kong','Portugal','China'))
        colum1,column2 = st.columns([1,1])
        with colum1:
                mycursor.execute(f'''select country,city,review_rating,number_of_reviews,price from airbnb_data2
                                    where country like '{select_country}'
                                    group by number_of_reviews  order by number_of_reviews desc limit 7''')
                mydb.commit()
                df=pd.DataFrame(mycursor,columns=mycursor.column_names)
                # df['review_rating']=df['review_rating'].astype('float')
                
                # x=df.index
                # y=df["number_of_reviews"]
                # z=df['review_rating']
                # dx=[1]
                # dy=[1]
                # dz=df['price']
                # fig=plt.figure(figsize=(8,12))
                # ax=plt.axes(projection='3d')
                # ax.bar3d(x,y,z,dx,dy,dz)
                # ax.set_xlabel('X-axis')
                # ax.set_ylabel('Y-axis')
                # ax.set_zlabel('Z-axis')
                # # ax.set_title('3D Bar Chart')
                # # plt.show()
                # st.pyplot(fig,clear_figure=True)
                
                fig=px.bar(df,x='city',y='number_of_reviews',color="price")
                                # color_discrete_sequence=px.colors.sequential.Agsunset)
                # fig.show()
                st.plotly_chart(fig,use_container_width=True) 
            
        with column2:
            fig=px.sunburst(df,values='number_of_reviews',
                        path=['country','city',"number_of_reviews"],     
                            color='number_of_reviews',
                            template="plotly_dark",
                            title="group by city top 7 number of review ",
                            color_discrete_sequence=px.colors.sequential.Agsunset)
            # fig.show()
            st.plotly_chart(fig,use_container_width=True) 



if selected == "Top Charts":
    selected_country = st.selectbox(
        "select the country",
        ('United States','Canada','Spain','Australia','Brazil','Hong Kong','Portugal','China'))

    mycursor.execute(f"""select city, country,sum(price) as total_price
                    from airbnb_data2 where country like '{selected_country}'
                    group by city  order by total_price desc limit 10 """)
    df = pd.DataFrame(mycursor, columns=mycursor.column_names)
    # df
    
    fig = px.bar(df,
            # st.write('top 10 total_price city ')        
            title=selected_country,
            x="city",
            y="total_price",
            color='total_price',
        color_continuous_scale=px.colors.sequential.Agsunset)
    # fig.show()
    st.plotly_chart(fig,use_container_width=True)

   
if selected == "location_download":
    
    selecte_country = st.selectbox(
        "select the country",
        ('United States','Canada','Spain','Australia','Brazil','Hong Kong','Portugal','China'))
    
    # selecte_city = st.selectbox(
    #     "select the city",
    #     ('Adalar','Agrela','Alexandria','Alfena','Annandale','Arcozelo','ArnavutkÃ¶y','Arouca',
    #     'Artarmon','Ãrvore','Ashfield','Astoria','AtaÅŸehir','AtaÅŸehir merkez','Austin','Avalon',
    #     'Avalon Beach','AvcÄ±lar','Aveiro','BaÄŸcÄ±lar','Bagunte','BahÃ§elievler','BakÄ±rkÃ¶y','Balgowlah','Balmain','Baltar',
    #     'Barcelona','Barcelone','Bardwell Park','Barra da Tijuca','Barra da Tijuca - Ri','Barra de Guaratiba','BaÅŸakÅŸehir',
    #     'Baulkham Hills','Beacon Hill','Beaconsfield','Bella Vista','Bellevue Hill','BeÅŸiktaÅŸ','BeÅŸiktaÅŸ/ bebek','Beverly Hills',
    #     'Beykoz','Beylerbeyi','BeylikdÃ¼zÃ¼','BeylikdÃ¼zÃ¼ Osb'))
    
    select_room_type = st.selectbox(
                    "select the room_type",
                    ('Entire home/apt','Private room','Shared room'))
                
    select_property_type = st.selectbox(
                    "select the property_type",
                    ('Aparthotel','Apartment','Barn','Bed and breakfast','Boat','Boutique hotel','Bungalow',
                    'Cabin','Camper/RV','Campsite','Casa particular (Cub','Castle','Chalet','Condominium',
                    'Cottage','Earth house','Farm stay','Guest suite','Guesthouse','Heritage hotel (Indi','Hostel','Hotel','House',
                    'Houseboat','Hut','Loft','Nature lodge','Other','Pension (South Korea','Resort',
                    'Serviced apartment','Tiny house','Townhouse','Train','Treehouse','Villa'))
    
    mycursor.execute(f"""select country,city,property_type,room_type, price, host_name
                from airbnb_data2 
                where country like '{selecte_country}' and room_type like '{select_room_type}' and property_type like '{select_property_type}'
                group by country,city,room_type order by host_name,price desc""")
    df = pd.DataFrame(mycursor, columns=mycursor.column_names)
    # st.write(df)
    # def color_survived(val):
    #     color = 'green' if val>200 else 'red'
    #     return f'background-color: {color}'
    # st.dataframe(df.style.applymap(color_survived, subset=['price']))
    st.expander("",expanded=False)
    st.dataframe(df.style.background_gradient(cmap='Greens'),use_container_width=True)
    
    
    # a=st.dataframe(df.style.applymap(color_survived, subset=['price']))
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(df)

    st.download_button(
    "Press to Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv')
    # st.button(df)
    # fig = px.sunburst(df, values='price', 
    #             path=['country',"city",'property_type','room_type','price','host_name'],
    #                 color='property_type',
    # #                 title=selected_state,
    #                 color_discrete_sequence=px.colors.sequential.Agsunset)
    # # fig.show()
    # st.plotly_chart(fig,use_container_width=True)
    
    
    
if selected == "map_view":
    selected_country = st.selectbox(
                            "select the country",
                            ('United States','Canada','Spain','Australia','Brazil','Hong Kong','Portugal','China'))
    
    mycursor.execute(f'''select country,city,longitude ,latitude,price, host_name 
                 from airbnb_data2  where country like '{selected_country}' group by country,city order by price  desc''')
    mydb.commit()
    df=pd.DataFrame(mycursor,columns=mycursor.column_names)
    # df
    # st.write(df.info())
    # st.map(df,size='price',color="host_name")

    
    import plotly.express as px
    import pandas as pd
    color_scale = [(0, 'orange'), (1,'red')]

    fig = px.scatter_mapbox(df, 
                            lat=df["latitude"], 
                            lon=df["longitude"], 
                            zoom=3,
                            color=df['price'],
                            hover_data=['host_name','city'],
                            color_continuous_scale=color_scale,
                            size=df['price'])

    fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            # "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
    # mapbox_layers=[
    #     {
    #         "below": 'traces',
    #         "sourcetype": "raster",
    #         "sourceattribution": "United States Geological Survey",
    #         "source": [
    #             "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
    #         ]
    #     },
    #     {
    #         "sourcetype": "raster",
    #         "sourceattribution": "Government of Canada",
    #         "source": ["https://geo.weather.gc.ca/geomet/?"
    #                    "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
    #                    "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
    #     }
    #           ])
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":10})
    # fig.show()
    st.plotly_chart(fig,use_container_width=True)
# hide = """
#     <style>
#     # footer {visibility: hidden;}
#     # header {visibility: hidden;}
#     </style>
#     """ 
# st.markdown(hide,unsafe_allow_html = True)   