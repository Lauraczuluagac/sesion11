import pandas as pd
import streamlit as st
import numpy as np

# Crear datos de ejemplo
marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai']
modelos = ['Camry', 'Civic', 'F-150', 'Silverado', 'Altima', 'X5', 'C-Class', 'A4', 'Jetta', 'Elantra']
anios = [2018, 2020, 2019, 2017, 2016, 2021, 2018, 2020, 2019, 2017]
precios = np.random.randint(15000, 50000, 10)

# Crear DataFrame con los datos
df_autos = pd.DataFrame({'marca': marcas, 'modelo': modelos, 'anio': anios, 'precio': precios})

# Mostrar el DataFrame
print(df_autos)

#1
st.header( "Ejercicios 1 loc")
st.write( "Seleccionar todas las filas de la columna marca")
df_autos.loc[:,'marca']

#2

st.header( "Ejercicios 2 loc")
st.write( "Seleccionar las filas de los autos cuyo precio es mayor a $40,000.")
filtro2=df_autos.loc[df_autos['precio']>40000] 

st.dataframe(filtro2)

#3
st.header( "Ejercicios 3 loc")
st.write( "Seleccionar las filas de los autos que son de la marca BMW")
filtro3=df_autos.loc[df_autos["marca"]=="BMW"]

st.dataframe(filtro3)

#4
st.header( "Ejercicios 4 loc")
st.write( "Seleccionar las filas de los autos que son de la marca Toyota y tienen un precio menor a $20,000.")
filtro4=df_autos.loc[(df_autos["marca"]=="Toyota") & (df_autos["precio"]<20000)]

st.dataframe(filtro4)

#5
st.header( "Ejercicios 5 loc")
st.write( "Seleccionar las filas de los autos que son del año 2019.")
filtro5=df_autos[df_autos.loc[:,"anio"]==2019]

st.dataframe(filtro5)

#6
st.header( "Ejercicios 6 loc")
st.write( "Seleccionar las filas de los autos que son del año 2016 o anteriores.")
filtro6=df_autos[df_autos.loc[:,"anio"]<=2016]

st.dataframe(filtro6)

#7
st.header( "Ejercicios 7 loc")
st.write( "Seleccionar las filas de los autos que son de la marca Honda y el modelo es Civic")
filtro7=df_autos.loc[(df_autos["marca"]=="Honda") & (df_autos["modelo"]=="Civic")]

st.dataframe(filtro7)

#8
st.header( "Ejercicios 8 loc")
st.write( "Seleccionar las filas de los autos que tienen un precio entre $25,000 y $30,000.")
filtro8=df_autos.loc[(df_autos["precio"]>=25000) & (df_autos["precio"]<=30000)]

st.dataframe(filtro8)

#9
st.header( "Ejercicios 9 loc")
st.write( "Seleccionar las filas de los autos que tienen un precio mayor a $30,000 y el modelo es C-Class")
filtro9=df_autos.loc[(df_autos["precio"]>30000) & (df_autos["modelo"]=="C-Class")]

st.dataframe(filtro9)

#10
st.header( "Ejercicios 10 loc")
st.write( "Seleccionar las filas de los autos que son de la marca Volkswagen y el modelo no es Jetta")
filtro10=df_autos.loc[(df_autos["marca"]=="Volkswagen") & (df_autos["modelo"]!="Jetta")]

st.dataframe(filtro10)

#iloc
#1
st.header( "Ejercicios 1 iloc")
st.write( "Seleccionar las filas de los autos de los primeros 5 fabricantes en el DataFrame.")
f1=df_autos.iloc[0:5]

st.dataframe(f1)

#2
st.header( "Ejercicios 2 iloc")
st.write( "Seleccionar las filas de los autos de los últimos 5 fabricantes en el DataFrame.")
f2=df_autos.iloc[5:10]

st.dataframe(f2)

#3
st.header( "Ejercicios 3 iloc")
st.write( "Seleccionar la primera columna de todas las filas del DataFrame.")
f3=df_autos.iloc[0,:]

st.dataframe(f3)

#4
st.header( "Ejercicios 4 iloc")
st.write( "Seleccionar las celdas de la primera fila y primera columna del DataFrame.")
f4=df_autos.iloc[0:1,0:1]

st.dataframe(f4)

#5
st.header( "Ejercicios 5 iloc")
st.write( "Seleccionar las filas pares del DataFrame.")
f5=df_autos.iloc[0::2]

st.dataframe(f5)

#6
st.header( "Ejercicios 6 iloc")
st.write( "Seleccionar las filas impares del DataFrame que tienen un precio mayor a $25,000.")
f6=df_autos.iloc[1::2][df_autos["precio"]>25000]

st.dataframe(f6)

#7
st.header( "Ejercicios 7 iloc")
st.write( "Seleccionar las filas de los autos que son de la marca Ford y el modelo es F-150")
f7=df_autos.iloc[:][(df_autos["marca"]=="Ford") & (df_autos["modelo"]=="F-150")]

st.dataframe(f7)

#8
st.header( "Ejercicios 8 iloc")
st.write( "Seleccionar las filas de los autos que son del año 2018 y tienen un precio mayor a $20,000.")
f8=df_autos.iloc[:][(df_autos["anio"]==2018) & (df_autos["precio"]>20000)]

st.dataframe(f8)

#9
st.header( "Ejercicios 9 iloc")
st.write( "Seleccionar las filas de los autos que tienen un precio mayor a $30,000 y la marca es Toyota")
f9=df_autos.iloc[:][  (df_autos["precio"]>30000)&(df_autos["marca"]=="Toyota")]

st.dataframe(f9)

#10
st.header( "Ejercicios 10 iloc")
st.write( "Seleccionar las filas de los autos que son de la marca Honda y el modelo no es Civic")
f10=df_autos.iloc[:][ (df_autos["marca"]=="Honda")& (df_autos["modelo"]!="Civic")]

st.dataframe(f10)