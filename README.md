# Netflix Movies and TV Shows Clustering & Netflix Recommender System

![](https://media.tenor.com/Rfyx9OkRI38AAAAC/netflix-netflix-startup.gif)

This repository contains the code and resources for analyzing the Netflix dataset of movies and TV shows until 2019. The dataset was sourced from the third-party search engine Flixable and includes information about various attributes of the content available on Netflix. The goal of this project is to uncover insights, trends, and patterns within the dataset and develop a content-based recommender system using natural language processing (NLP) techniques.

## Problem Statement

The problem at hand involves exploring the Netflix dataset to gain insights into the content available on the platform. The dataset provides information about movies and TV shows, their attributes, and their availability in different countries. By integrating this dataset with external sources such as IMDB ratings and Rotten Tomatoes, we can extract further valuable information.

The specific tasks to be performed in this project include:

1. **Exploratory Data Analysis (EDA)**: Cleaned the data, unnested the Netflix content and tackled the null/missing values and conduct a thorough analysis of the dataset to uncover trends, patterns, and correlations among different attributes.
2. **Understanding Content Availability**: Determine the types of content available in different countries and identify any variations or preferences.
3. **Analyzing Netflix's Focus**: Investigate whether Netflix has been increasingly focusing on TV shows rather than movies in recent years.
4. **Clustering Similar Content**: Utilize text-based features to cluster similar content, enabling the development of a content-based recommender system.

## Project Summary

The aim of this project is to analyze the Netflix dataset, which includes information on movies and TV shows available on the platform until 2019. With over 220 million subscribers, Netflix is the world's largest online streaming service provider. By analyzing and clustering the content, we can enhance the user experience through a personalized recommendation system, potentially reducing subscriber churn.

The project follows a step-by-step process, as outlined below:

1. **Handling Missing Values**: Address any null or missing values present in the dataset.
2. **Dealing with Nested Columns**: Process nested columns such as director, cast, listed_in, and country to facilitate clear visualization and analysis.
3. **Rating Binning**: Categorize ratings into appropriate categories, including adult, children's, family-friendly, and not rated content.
4. **Exploratory Data Analysis (EDA)**: Perform in-depth EDA on various attributes, uncovering valuable findings to aid in churn prevention.
5. **Cluster Creation**: Create clusters using attributes such as director, cast, country, genre, rating, and description. Tokenize, preprocess, and vectorize the attribute values using TF-IDF vectorizer.
6. **Dimensionality Reduction**: Reduce the dimensionality of the dataset using Principal Component Analysis (PCA) to improve performance.
7. **Clustering Algorithms**: Employ K-Means Clustering and Agglomerative Hierarchical Clustering algorithms to construct two distinct types of clusters. Determine the optimal number of clusters using methods like the Elbow method, Silhouette score, and Dendrogram.
8. **Content-Based Recommender System**: Develop a content-based recommender system using the cosine similarity matrix. This system analyzes the user's watched shows and generates personalized recommendations to enhance their experience.


## Deployment: Enhancing Your Netflix Experience!

We've taken this project one step further by deploying our Netflix recommendation system for a seamless user experience. With our deployed system, you can now unlock personalized content suggestions right at your fingertips. Here's how it works:

1. **Local Server Deployment**: Using Streamlit, we've built a user-friendly interface that runs on your local server. Simply fire up the application, and you'll find a sleek interface awaiting your input.

2. **Live User Interaction**: Thanks to the power of Hugging Face, our recommendation system is live and ready to interact with you. Discover new shows and movies tailored to your taste, as our cutting-edge algorithm analyzes your watch history to provide spot-on suggestions.

3. **Unleash the Power of Content-Based Recommendations**: Say goodbye to aimlessly scrolling through endless options. Our content-based recommender system harnesses the potential of natural language processing (NLP) to match your preferences with similar shows and movies in the Netflix dataset.

4. **User-Centric Approach**: We've prioritized your satisfaction by designing a system that understands your unique viewing habits. Whether you're a fan of crime dramas, romantic comedies, or mind-bending documentaries, our recommendation engine delivers personalized content just for you.

Don't settle for mediocre suggestions or waste time on subpar shows. Elevate your Netflix experience with our deployed recommendation system. Get ready to embark on a binge-watching journey like no other!

## How to Access the Deployed System?

1. Explore the **Web App**: [Netflix Recommender System](https://huggingface.co/spaces/Shahrukh2016/Netflix_Recommender)
2. Enter the Movie or TV Show of your taste.
3. Sit back, relax, and let our recommendation system curate a tailor-made list of shows and movies based on your preferences.

Start exploring a world of entertainment customized just for you. Uncover hidden gems, rediscover old favorites, and dive into thrilling new series all at the touch of a button. Upgrade your Netflix journey today with our cutting-edge recommendation system!

Note: We had the data till 2019 only. Stay tuned as we expand our data in the near future.

For complete project video explaination and to downoad the dataset: [Click here](https://drive.google.com/drive/folders/1kIA05f82ApuR5rMOH2uNmwmyxT6a3Uww?usp=sharing
)

Happy streaming and enjoy your enhanced Netflix experience!
