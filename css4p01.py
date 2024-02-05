# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:19:35 2024

@author: sdmoe
"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")
df.columns = df.columns.str.replace(' ', '_')
print("Columns with missing values:")
print(df.isnull().sum())
df.dropna(subset=['Revenue_(Millions)', 'Metascore'], inplace=True)
print("Updated DataFrame after dropping rows with missing values:")
print(df.head())
print(df.isnull().sum())
highest_rated_index = df['Rating'].idxmax()
highest_rated_movie = df.loc[highest_rated_index]
print("Highest-rated movie:")
print(highest_rated_movie[['Title', 'Rating']])
average_revenue = df['Revenue_(Millions)'].mean()
print("Average revenue of all movies:", average_revenue)
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_2017 = filtered_df['Revenue_(Millions)'].mean()
print("Average revenue of movies from 2015 to 2017:", average_revenue_2015_2017)
movies_2016_count = (df['Year'] == 2016).sum()
print("Number of movies released in 2016:", movies_2016_count)
df.columns = df.columns.str.replace(' ', '_')
nolan_movies_count = (df['Director'] == 'Christopher Nolan').sum()
print("Number of movies directed by Christopher Nolan:", nolan_movies_count)
high_rated_movies_count = (df['Rating'] >= 8.0).sum()
print("Number of movies with a rating of at least 8.0:", high_rated_movies_count)
df.columns = df.columns.str.replace(' ', '_')
nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan_movies = nolan_movies['Rating'].median()
print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan_movies)
average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()
print("Year with the highest average rating:", year_highest_average_rating)
print("Highest average rating:", highest_average_rating)
movies_by_year = df.groupby('Year')['Title'].count()
movies_2006 = movies_by_year.get(2006, 0)
movies_2016 = movies_by_year.get(2016, 0)
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(f"Number of movies in 2006: {movies_2006}")
print(f"Number of movies in 2016: {movies_2016}")
print(f"Percentage increase in the number of movies between 2006 and 2016: {percentage_increase:.2f}%")
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace(' ', '_')
all_actors = ', '.join(df['Actors'])
actor_list = all_actors.split(', ')
actor_counts = pd.Series(actor_list).value_counts()
most_common_actor = actor_counts.idxmax()
count_most_common_actor = actor_counts.max()
print(f"Most common actor: {most_common_actor}")
print(f"Number of occurrences: {count_most_common_actor}")
df.columns = df.columns.str.replace(' ', '_')
all_genres = ', '.join(df['Genre'])
genre_list = all_genres.split(', ')
unique_genres = set(genre_list)
num_unique_genres = len(unique_genres)
print("Number of unique genres:", num_unique_genres)
df.columns = df.columns.str.replace(' ', '_')
numerical_features = df[['Rating', 'Runtime_(Minutes)', 'Votes', 'Revenue_(Millions)', 'Metascore']]
correlation_matrix = numerical_features.corr()
print("Correlation Matrix:")
print(correlation_matrix)


