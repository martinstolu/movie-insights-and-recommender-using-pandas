import pandas as pd

column_names1 = ['user_id', 'item_id', 'rating', 'timestamp']
df_u_data = pd.read_csv('ml-100k/u.data', sep='\t', names=column_names1)


column_names2 =['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation',
              'Children.s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
              'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
              'Thriller' , 'War', 'Western']
df_u_item = pd.read_csv('ml-100k/u.item', sep='|', names=column_names2, encoding='latin-1')

# Show all columns
pd.set_option('display.max_columns', None)

# Show all rows
pd.set_option('display.max_rows', None)

# Don't truncate column content
pd.set_option('display.max_colwidth', None)

# Make output wider to fit everything
pd.set_option('display.width', None)

column_names3 = ['user id', 'age', 'gender', 'occupation', 'zip code']
df_u_user= pd.read_csv('ml-100k/u.user', sep='|', names=column_names3, encoding='latin-1')

print(f"{df_u_data.head()}\n")
print(f"{df_u_item.head()}\n")
print(f"{df_u_user.head()}\n")

# num = df_u_data.item_id.count()
# num2 = df_u_item['movie title'].count()
# print(num, num2)
#
# """🧠 Advanced Practice Challenges
# 🔹 1. Ratings Analysis
# What’s the average rating per movie?"""
# no_1 = df_u_data.groupby('item_id')['rating'].mean()
# print(f"\n{no_1.round(2).head()}")
#
# # Compute average rating per movie
# avg_ratings = df_u_data.groupby('item_id')['rating'].mean().round(2).reset_index()
# print(f"\n{avg_ratings.head()}")
# # Merge with movie titles
# avg_ratings_with_titles = avg_ratings.merge(df_u_item[['movie id', 'movie title']], left_on='item_id', right_on='movie id')
#
# # Drop redundant 'movie id' column
# avg_ratings_with_titles = avg_ratings_with_titles.drop(columns='movie id')
#
# # Sort by highest rating
# avg_ratings_with_titles = avg_ratings_with_titles.sort_values(by='rating', ascending=False)
#
# print(f"\n{avg_ratings_with_titles.head(10)}")

# """What’s the most-rated movie?"""
# m_rated= df_u_item.loc[df_u_item['movie id']== df_u_data.item_id.value_counts().idxmax(), 'movie title'].iloc[0]
# print(m_rated)

#
# """Which movie has the highest average rating (with at least 50 ratings)?"""
#
# ratings_summary = df_u_data.groupby('item_id')['rating'].agg(['mean', 'count'])
# filtered = ratings_summary[ratings_summary['count'] >= 50]
# get_index = filtered['mean'].idxmax()
# get_amount = filtered['mean'].max()
# get_name= df_u_item.loc[df_u_item['movie id']  == get_index, 'movie title'].values[0]
# # print(f"\n{ratings_summary.head()}")
# # print(f'\n{filtered.hea()}')
# print(get_name)
# print(get_amount)

# """🔹 2. User Behavior
# What’s the average rating per user?"""
# avg_rate = df_u_data.groupby('user_id')['rating'].mean().round(2).sort_values(ascending=False)
# user_counts = df_u_data['user_id'].value_counts()
# avg_rate_filtered = avg_rate[user_counts[avg_rate.index] >= 20]
# print(avg_rate_filtered.head())

"""Do older users tend to rate higher or lower than younger users?"""
# older_user = >=30
# younger_user = <30
# TODO 1. create_a_new_column_in_u.data_with_age
# df_u_data_with_age = df_u_data.merge(df_u_user[['user id', 'age']], left_on='user_id', right_on='user id')
# df_u_data_with_age.drop(columns='user id', inplace=True)
# younger_users = df_u_data_with_age[df_u_data_with_age.age <30]
# older_users = df_u_data_with_age[df_u_data_with_age.age >= 30]
# younger_users_average_rating = younger_users.rating.mean().round(2)
# older_users_with_average_ratings = older_users.rating.mean().round(2)
#
# print(younger_users_average_rating, older_users_with_average_ratings)

# """ 3. Genre Trends
# Which genre has the most movies?"""
# most_movies = df_u_item.iloc[:, 5:].sum()
# name= most_movies.idxmax()
# number = most_movies.max()
#

# """What is the average rating per genre?"""
# genre_columns = df_u_item.columns[5:]
# columns_to_merge = ['movie id'] + list(genre_columns)
# avr_rate = df_u_data.merge(df_u_item[columns_to_merge], left_on='item_id', right_on='movie id')
# avr_rate_per_genre = avr_rate.iloc[:, 5:].mean().round(2)
#
# print(avr_rate.head())
# print(avr_rate_per_genre)

    # """ 4. Occupation & Gender Insights
# What’s the average rating given by each occupation?"""
#
# occ_user = df_u_data.merge(df_u_user[['user id', 'occupation']], left_on= 'user_id', right_on='user id')
# avg_rating= occ_user.groupby('occupation')['rating'].mean().round(2)
# print(avg_rating.sort_values(ascending=False))


#     """Do men and women rate differently on average?"""
# occ_user = df_u_data.merge(df_u_user[['user id', 'gender']], left_on= 'user_id', right_on='user id')
# avg_rating= occ_user.groupby('gender')['rating'].mean().round(2)
# print(avg_rating.sort_values(ascending=False))

# """ 5. Time-based Insights
# Convert the timestamp column into datetime."""
#
# df_u_data.timestamp = pd.to_datetime(df_u_data['timestamp'], unit='s')
# # print(df_u_data.head())
#
# """What are the most popular months or years for rating movies?"""
# # popular = df_u_data.groupby('timestamp')['rating'].count().sort_values(ascending=False)
# # print(popular.head())
# df_u_data['year'] = df_u_data['timestamp'].dt.year
# popular_years = df_u_data.groupby('year')['rating'].count().sort_values(ascending=False)
# print(popular_years.head())
#
#
# df_u_data['month'] = df_u_data['timestamp'].dt.month
# popular_months = df_u_data.groupby('month')['rating'].count().sort_values(ascending=False)
# print(popular_months.head())
#
#
# df_u_data['year_month'] = df_u_data['timestamp'].dt.to_period('M')
# popular_ym = df_u_data.groupby('year_month')['rating'].count().sort_values(ascending=False)
# print(popular_ym.head())

ratings_matrix = df_u_data.pivot(index='user_id', columns='item_id', values='rating')
# # ratings_matrix.fillna('-', inplace=True)
print(ratings_matrix.head())
#
# Example: correlation of user 1 with all others
user_similarities = ratings_matrix.corrwith(ratings_matrix.loc[1], axis=1)
# print(user_similarities.head)

user_similarity_matrix = ratings_matrix.T.corr()
print(user_similarity_matrix.head().round(2))

for user in user_similarity_matrix.index:
    # Get similarity scores for this user, drop self-correlation (=1)
    similar_users = user_similarity_matrix.loc[user].drop(user)

    # Sort by similarity descending
    similar_users = similar_users.sort_values(ascending=False)

    # Print top 3 most similar users and their similarity scores
    print(f"Top similar users to user {user}:")
    print(similar_users.head(3))
    print()


