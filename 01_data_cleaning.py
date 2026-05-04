import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


print("Libraries loaded successfully!")

star_df = pd.read_excel('data/star-ratings-quarterly-data-extract-february-2026.xlsx', 
                         sheet_name='Star Ratings')

print("Shape:", star_df.shape)
print("\nFirst 5 rows:")
print(star_df.head())

# See all column names
print("Column Names:")
print(star_df.columns.tolist())

# Check missing values in each column
print("\nMissing Values:")
print(star_df.isnull().sum())

# Keep only providers that have a star rating
star_rated = star_df[star_df['Overall Star Rating'].notna()].copy()

print(f"Total providers: {len(star_df)}")
print(f"Providers WITH ratings: {len(star_rated)}")
print(f"Providers WITHOUT ratings: {len(star_df) - len(star_rated)}")

# Clean column names
# Remove spaces, make lowercase, replace / with _
star_rated.columns = (star_rated.columns
                      .str.strip()
                      .str.lower()
                      .str.replace(' ', '_')
                      .str.replace('/', '_')
                      .str.replace("'", ""))

print("Cleaned column names:")
print(star_rated.columns.tolist())

# Check data types of each column
print("\nData types:")
print(star_rated.dtypes)

# Convert star ratings to integer (whole numbers like 1,2,3,4,5 not 1.0,2.0)
star_rated['overall_star_rating'] = star_rated['overall_star_rating'].astype(int)

# Confirm it changed
print("\nOverall Star Rating after fix:")
print(star_rated['overall_star_rating'].value_counts().sort_index())

# Save cleaned data to a new CSV file
star_rated.to_csv('data/cleaned_star_ratings.csv', index=False)

print("Cleaned data saved successfully!")
print(f"Final dataset shape: {star_rated.shape}")