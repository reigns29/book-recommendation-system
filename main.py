import pickle
popular_df = pickle.load(open('popular.pkl','rb'))

book_name = list(popular_df['Book-Title'].values),
author=list(popular_df['Book-Author'].values),
image=list(popular_df['Image-URL-M'].values),
votes=list(popular_df['num_ratings'].values),
rating=list(popular_df['avg_rating'].values)

print(book_name , author , image , votes , rating)