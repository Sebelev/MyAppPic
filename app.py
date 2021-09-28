import streamlit as st
from fn import load_image, image_pixel




st.title ("Black or White")

image_file = st.file_uploader("Загрузите изображение:", ["jpg", "jpeg"])

if image_file != None:

    pixel_tuple = image_pixel(image_file)
    st.image(load_image(image_file), image_file.name)

    if pixel_tuple.count('#000000') > pixel_tuple.count('#ffffff'):
        st.write('Черных пикселей больше, чем белых')
        color = '#000000'
    elif pixel_tuple.count('#000000') < pixel_tuple.count('#ffffff'):
        st.write('Белых пикселей больше, чем черных')
        color = '#ffffff'
    elif pixel_tuple.count('#000000')  == 0 and pixel_tuple.count('#ffffff') == 0:
        st.write('Нет белых и черных пикселей')
        color = '#808080'
    elif pixel_tuple.count('#000000') == pixel_tuple.count('#ffffff'):
        st.write('Равное количество белых и черных пикселей')
        color = '#808080'

    st.write("Всего таких пикселей", pixel_tuple.count(st.color_picker('Выбрать цвет', color)))







