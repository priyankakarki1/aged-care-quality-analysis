import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
star_rated = pd.read_csv('data/cleaned_star_ratings.csv')

# Connect to MySQL using SQLAlchemy
engine = create_engine('mysql+pymysql://root:@localhost/aged_care_analysis')

print("Connected to MySQL successfully!")
print(f"Data has {len(star_rated)} rows ready to load")

# Load dataframe into MySQL as a table
star_rated.to_sql(
    name='star_ratings',
    con=engine,
    if_exists='replace',
    index=False
)

print(" Data loaded into MySQL successfully!")
print("Table 'star_ratings' is ready to query!")