import pickle
import streamlit as st
import requests

st.header("Game Recommendation System")

with open('artifacts/game_list.pkl', 'rb') as f:
    game = pickle.load(f)

with open('artifacts/similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

game_list = game['Name'].values
selected_game = st.selectbox('Game Name', game_list)

def fetch_poster(game_name):
    url = "https://api.igdb.com/v4/games"
    client_id = 'fqngs0404rx4qj9ske9nrjeb4pgpu3'  
    access_token = '3i5r0a4w54egai6y15f43flhkyi2py' 
    
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}',
    }
    
    body = f'fields cover.url; search "{game_name}"; limit 1;'
    
    response = requests.post(url, headers=headers, data=body)
    
    if response.status_code == 200:
        game_data = response.json()
        if game_data:
            cover_url = game_data[0].get('cover', {}).get('url', '')
            if cover_url:
                if cover_url.startswith('//'):
                    cover_url = 'https:' + cover_url
                return cover_url
            else:
                return "https://via.placeholder.com/150"
        else:
            return "https://via.placeholder.com/150"
    else:
        return "https://via.placeholder.com/150"

def recommend(selected_game):
    index = game[game['Name'] == selected_game].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_game_name = []
    recommended_game_poster = []
    for i in distances[1:6]:
        game_name = game.iloc[i[0]].Name
        recommended_game_poster.append(fetch_poster(game_name))
        recommended_game_name.append(game.iloc[i[0]].Name)
    return recommended_game_name, recommended_game_poster

if st.button('Show Recommendation'):
    recommended_game_name, recommended_game_poster = recommend(selected_game)
    cols = st.columns(len(recommended_game_name))
    for col, name, poster_url in zip(cols, recommended_game_name, recommended_game_poster):
         with col:
            st.markdown(
                f'<img src="{poster_url}" alt="{name}" style="height:180px;">',
                unsafe_allow_html=True
            )
            st.caption(name)