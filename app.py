import streamlit as st
import pandas as pd
import pickle 

data=pickle.load(open('cars_Predictions.sav','rb'))

st.title('Car Price Prediction')

st.sidebar.header('Feature selecting')
st.sidebar.info('Easy Application For Predicting Car Price')

st.image('https://i.pinimg.com/736x/83/7c/0b/837c0b7c751efcf2ff1062db4af33a09.jpg')
#__________________________________________________________________________________

m1=['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA',
       'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN',
       'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA',
       'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI',
       'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ',
       'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR',
       'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC',
       'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION',
       'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH',
       'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE',
       'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']

m2=[16, 12, 17, 43, 27, 45, 35, 31,  6, 41,  9,  3, 21, 30, 40, 26, 14,
       11, 42, 24, 32,  2,  8, 29, 10, 23, 20,  0, 44, 19, 39,  7, 25,  4,
       33, 47, 15,  5, 38, 18, 34, 22, 28, 36, 46,  1, 37, 13]

Manufacturer_mapping = dict(zip(m1, m2))
Manufacturer1=st.selectbox('Manufacturer', m1)
Manufacturer = Manufacturer_mapping[Manufacturer1]
# ...................................................................................
mm1=['RX 450', 'Equinox', 'FIT','E 230 124', 'RX 450 F SPORT',
       'Prius C aqua']
mm2=[890, 458, 477,485, 470, 833]
Model_mapping = dict(zip(mm1, mm2))
Model1=st.selectbox('Model',mm1 )
Model=Model_mapping[Model1]
# ....................................................................................
c1=['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
       'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
       'Pickup']
c2=[ 4,  3,  9,  2, 10,  7,  0,  1,  6,  8,  5]
Category_Mapping=dict(zip(c1,c2))
Category1=st.selectbox('Category', c1)
Category=Category_Mapping[Category1]
# ................................................................................
l1 = ['yes', 'no']
l2 = [1,2]
leather_mapping = dict(zip(l1, l2))
Leather1 = st.selectbox('Leather interior', l1)
Leather = leather_mapping[Leather1]

# .................................................................................    
f1=['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG',
       'Hydrogen']
f2=[2, 5, 1, 6, 4, 0, 3]
Fuel_Mapping=dict(zip(f1,f2))
Fuel1=st.selectbox('Fuel type',f1 )
Fuel=Fuel_Mapping[Fuel1]
# .................................................................................
g1=['Automatic', 'Tiptronic', 'Variator', 'Manual']
g2=[0, 2, 3, 1]
Gear_mapping=dict(zip(g1,g2))
Gear1=st.selectbox('Gear box type', g1)
Gear=Gear_mapping[Gear1]
# ...................................................................................
d1=['4x4', 'Front', 'Rear']
d2=[0,1,2]
Drive_mapping=dict(zip(d1,d2))
Drive1=st.selectbox('Drive wheels', d1)
Drive=Drive_mapping[Drive1]
# ...................................................................................
w1=['Left wheel', 'Right-hand drive']
w2=[0,1]
Wheel_mapping=dict(zip(w1,w2))
Wheel1=st.selectbox('Wheel',w1)
Wheel=Wheel_mapping[Wheel1]
# ....................................................................................
cc1=['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
       'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
       'Carnelian red', 'Purple', 'Pink']
cc2=[12,  1, 14,  7,  2, 13, 11,  8,  6, 15,  3,  5,  0,  4, 10,  9]
color_mapping=dict(zip(cc1,cc2))
Color1=st.selectbox('Color', cc1)
Color=color_mapping[Color1]
# .....................................................................................

Engine=st.selectbox('Engine volume', [3.5, 3. , 1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 3.3, 1.4, 2.3,
       3.2, 1.2, 1.7, 2.9, 1.9, 2.7, 2.8, 2.1, 1. , 0.8, 3.4, 2.6, 1.1])
# ..................................................................................................
Cylinders=st.number_input('Cylinders')
# ..................................................................................................
Airbags=st.selectbox('Airbags', [12,  8,  2,  0,  4,  6, 10,  3,  1, 16,  5,  7,  9, 11, 14, 15, 13])  
# ................................................................................................... 
Age=st.number_input('Age')
# ....................................................................................................
Mileage=st.number_input('Mileage')
# ....................................................................................................
Levy=st.number_input('Levy')
# ..................................................................................................

DF=pd.DataFrame({'Manufacturer':Manufacturer,'Model':Model,'Category':Category,'Leather interior':Leather,'Fuel type':Fuel,
                    'Mileage':Mileage,'Gear box type':Gear,'Drive wheels':Drive,'Wheel':Wheel,'Color':Color,'Levy':Levy,
                    'Engine volume':Engine,'Cylinders':Cylinders,'Airbags':Airbags,'Age':Age },index=[0])

# ================= DF بالقيم الرقمية =================
DF = pd.DataFrame({
    'Manufacturer': Manufacturer,
    'Model': Model,
    'Category': Category,
    'Leather interior': Leather,
    'Fuel type': Fuel,
    'Mileage': Mileage,
    'Gear box type': Gear,
    'Drive wheels': Drive,
    'Wheel': Wheel,
    'Color': Color,
    'Levy': Levy,
    'Engine volume': Engine,
    'Cylinders': Cylinders,
    'Airbags': Airbags,
    'Age': Age
}, index=[0])

# ================= DF_raw بالقيم اللي ظاهر للـ user =================
DF_raw = pd.DataFrame({
    'Manufacturer': Manufacturer1,
    'Model': Model1,
    'Category': Category1,
    'Leather interior': Leather1,
    'Fuel type': Fuel1,
    'Mileage': Mileage,
    'Gear box type': Gear1,
    'Drive wheels': Drive1,
    'Wheel': Wheel1,
    'Color': Color1,
    'Levy': Levy,
    'Engine volume': Engine,
    'Cylinders': Cylinders,
    'Airbags': Airbags,
    'Age': Age
}, index=[0])

# زرار التنبؤ
p = st.sidebar.button('Predict Price')

if p:
    Pre = data.predict(DF)[0]

    st.markdown(
        f"""
        <div style="background-color:#1e1e2f; padding:30px; border-radius:15px; text-align:center; margin-top:20px;">
            <h2 style="color:white;">🚗 Estimated Car Price</h2>
            <h1 style="color:#00ff99;">${Pre:,.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # عرض الـ DF_raw مش الـ DF
    st.subheader("Your Car Details")
    st.dataframe(DF_raw, use_container_width=True)
