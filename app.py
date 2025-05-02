import streamlit as st
import pickle
st.title('Movie Recomender by Varun Kumar')


movie_list=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movie_list1=movie_list['title']
Selected_Movie_Name = st.selectbox("Select your movie",movie_list1)

st.write("You selected:", Selected_Movie_Name)


def recomend(movie):
    movie_index=movie_list[movie_list['title']==movie].index[0]
    
    movie_list1=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])[1:6]
    recommended=[]
    for i in movie_list1:

        recommended.append(movie_list.iloc[i[0]].title)

    return recommended

if st.button("Recommend"):
    recomendation=recomend(Selected_Movie_Name)
    for i in recomendation:
       st.write(i)
