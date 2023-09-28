import streamlit as st
import pandas as pd
import random

shows = pd.read_excel('tvshows.xlsx')
movies = pd.read_excel('movies.xlsx')
re = st.selectbox('Search for any top rated movie', movies['title'])

c, c1, c2 = st.columns([6, 15, 6])
k = list(movies['title']).index(re)
c1.image(movies['posters'][k], movies['title'][k])
original_title = '<span style="font-family:Courier; color:white; font-size: 20px;align:center"></span>'
link = '[Watch](' + movies['Link'][k] + ')'
link1 = 'imdb rating : '+  str(movies['imdb rating'][k])
c1.markdown(original_title + link, unsafe_allow_html=True)
c1.markdown(original_title + link1, unsafe_allow_html=True)

st.header('Random suggestions')
c1, c, c2 = st.columns([9, 2, 9])
k = random.randint(0, len(movies['Link']) - 1)
c1.image(movies['posters'][k], movies['title'][k] + ' ' + str(movies['imdb rating'][k]))
original_title = '<span style="font-family:Courier; color:white; font-size: 20px;">ᅠ ᅠ ᅠ </span>'
link = '[Watch](' + movies['Link'][k] + ')'
c1.markdown(original_title + link, unsafe_allow_html=True)

c2.image(shows['posters'][k], shows['title'][k] + ' ' + str(shows['imdb rating'][k]))
original_title = '<span style="font-family:Courier; color:white; font-size: 20px;">ᅠ ᅠ ᅠ </span>'
link = '[Watch](' + shows['Link'][k] + ')'
c2.markdown(link, unsafe_allow_html=True)

i = 1
st.title('Top 200 IMDB Movies ')
q, s, d, t, ls = st.columns([3,3,3,3,3])

if s.button('Movies'):
    while i in range(1, 190):
        c, c1, c2, c3, c4, c5, c6 = st.columns([4, 4, 5, 6, 5, 4, 4])
        c.image(movies['posters'][i], movies['title'][i] + ' ' + str(movies['imdb rating'][i]))
        original_title = '<span style="font-family:Courier; color:white; font-size: 20px;"></span>'
        link = '[Watch](' + movies['Link'][i] + ')'
        c.markdown(link, unsafe_allow_html=True)
        i += 1;
        c1.image(movies['posters'][i], movies['title'][i] + ' ' + str(movies['imdb rating'][i]))
        link = '[Watch](' + movies['Link'][i] + ')'
        original_title = '<span style="font-family:Courier; color:white; font-size: 20px;"></span>'
        c1.markdown(original_title + link, unsafe_allow_html=True)
        i += 1;
        c2.image(movies['posters'][i], movies['title'][i] + ' ' + str(movies['imdb rating'][i]))

        link = '[Watch](' + movies['Link'][i] + ')'
        c2.markdown(original_title + link, unsafe_allow_html=True)
        i += 1;
        c3.image(movies['posters'][i], movies['title'][i] + ' ' + str(movies['imdb rating'][i]))
        original_title = '<span style="font-family:Courier; color:white; font-size: 20px;"></span>'
        link = '[Watch](' + movies['Link'][i] + ')'
        c3.markdown(original_title + link, unsafe_allow_html=True)
        i += 1;
        c4.image(movies['posters'][i], movies['title'][i] + ' ' + str(movies['imdb rating'][i]))
        original_title = '<span style="font-family:Courier; color:white; font-size: 20px;"></span>'
        link = '[Watch](' + movies['Link'][i] + ')'
        c4.markdown(original_title + link, unsafe_allow_html=True)
        i += 1;
        c5.image(movies['posters'][i], movies['title'][i] + ' ' + str(movies['imdb rating'][i]))
        original_title = '<span style="font-family:Courier; color:white; font-size: 20px;">   </span>'
        link = '[Watch](' + movies['Link'][i] + ')'
        c5.markdown(original_title + link, unsafe_allow_html=True)
        i += 1;
        c6.image(movies['posters'][i], movies['title'][i] + ' ' + str(movies['imdb rating'][i]))
        original_title = '<span style="font-family:Courier; color:white; font-size: 20px;"></span>'
        link = '[Watch](' + movies['Link'][i] + ')'
        c6.markdown(original_title + link, unsafe_allow_html=True)
        i += 1;
