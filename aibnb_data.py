import pandas as pd
import mysql.connector
import streamlit as st
import plotly.express as px
import numpy as np

  
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


with st.sidebar:
    selected = st.selectbox("**Menu**", ("Home","Top Charts","Explore Data","Explore Data1"))
    
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

   
if selected == "Explore Data":
    
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
    def color_survived(val):
        color = 'green' if val>200 else 'red'
        return f'background-color: {color}'
    st.dataframe(df.style.applymap(color_survived, subset=['price']))
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
    
    
    
if selected == "Explore Data1":
    selected_country = st.selectbox(
                            "select the country",
                            ('United States','Canada','Spain','Australia','Brazil','Hong Kong','Portugal','China'))
    
    mycursor.execute(f'''select country,city,longitude ,latitude,price, host_name 
                 from airbnb_data2  where country like '{selected_country}' group by country,city order by price  desc''')
    mydb.commit()
    df=pd.DataFrame(mycursor,columns=mycursor.column_names)
    # # df
    # st.map(df)


    import plotly.express as px
    import pandas as pd
    color_scale = [(0, 'orange'), (1,'red')]

    fig = px.scatter_mapbox(df, 
                            lat=df["latitude"], 
                            lon=df["longitude"], 
                            zoom=3,
                            color=df['price'],
                            color_continuous_scale=color_scale,
                            size=df['price'])

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":10})
    # fig.show()
    st.plotly_chart(fig,use_container_width=True)
