######################################################
# Importing necessary libraries
import streamlit as st
import pickle
import pandas as pd

#######################################################
# Loading the pickle file
content_dict= pickle.load(open('content_dict.pkl','rb'))

# Converting dictionary into pandas DataFrame
content= pd.DataFrame(content_dict)

# Loding the pickle file
similarity= pickle.load(open('cosine_similarity.pkl','rb'))

#######################################################
# Defining a function for recommendation system
def recommend(title, cosine_sim=similarity, data=content):
    recommended_content=[]
    # Get the index of the input title in the programme_list
    programme_list = data['title'].to_list()
    index = programme_list.index(title)

    # Create a list of tuples containing the similarity score and index 
    # between the input title and all other programmes in the dataset
    sim_scores = list(enumerate(cosine_sim[index]))

    # Sort the list of tuples by similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]

    # Get the recommended movie titles and their similarity scores
    recommend_index = [i[0] for i in sim_scores]
    rec_movie = data['title'].iloc[recommend_index]
    rec_score = [round(i[1], 4) for i in sim_scores]

    # Create a pandas DataFrame to display the recommendations
    rec_table = pd.DataFrame(list(zip(rec_movie, rec_score)), columns=['Recommendation', 'Similarity_score(0-1)'])
    # recommended_content.append(rec_table['Recommendation'].values)

    return rec_table['Recommendation'].values

#######################################################
# # Loading the pickle file
# content_dict= pickle.load(open('content_dict.pkl','rb'))

# # Converting dictionary into pandas DataFrame
# content= pd.DataFrame(content_dict)

# # Loding the pickle file
# similarity= pickle.load(open('cosine_similarity.pkl','rb'))

########################################################
# Displaying title
st.title("Netflix Recommender System")

# Display dialogue box that contains content
selected_content_name = st.selectbox(
    'Which Movie/TV Show are you watching?',
    content['title'].values)
st.write('**Note**: We have the data till 2019 only.')
#########################################################

# Setting a button
if st.button('Recommend'):
    recommendations= recommend(title=selected_content_name)
    st.write('**_You are watching:_**', selected_content_name)
    st.write('**_Your top 10 recommendations:_**')
    for num,i in enumerate(recommendations):
        st.write(num+1,':', i)

    # Last note
    st.write('_Lights out, popcorn in hand, and let the movies begin! We hope our recommendations hit the spot._:smile:')
