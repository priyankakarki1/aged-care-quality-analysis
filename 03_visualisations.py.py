import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
star_rated = pd.read_csv('data/cleaned_star_ratings.csv')

# Set style
plt.style.use('seaborn-v0_8')

# Chart 1: Average star rating by state
state_avg = star_rated.groupby('state_territory')['overall_star_rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
bars = plt.bar(state_avg.index, state_avg.values, color='#1A6B72')
plt.title('Average Star Rating by State', fontsize=16, fontweight='bold')
plt.xlabel('State')
plt.ylabel('Average Star Rating')
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig('charts/avg_rating_by_state.png', dpi=150)
plt.show()

print(" Chart 1 saved!")
# Chart 2: Provider type comparison (Government vs Not for Profit vs For Profit)
plt.figure(figsize=(8, 5))
purpose_avg = star_rated.groupby('purpose')['overall_star_rating'].mean().sort_values(ascending=False)

sns.barplot(x=purpose_avg.index, y=purpose_avg.values, palette='Blues_d')
plt.title('Average Star Rating by Provider Type', fontsize=16, fontweight='bold')
plt.xlabel('Provider Type')
plt.ylabel('Average Star Rating')
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig('charts/rating_by_purpose.png', dpi=150)
plt.show()

print(" Chart 2 saved!")

# Chart 3: Distribution of star ratings
plt.figure(figsize=(8, 5))
star_counts = star_rated['overall_star_rating'].value_counts().sort_index()

sns.barplot(x=star_counts.index, y=star_counts.values, palette='Blues_d')
plt.title('Distribution of Star Ratings Across All Providers', 
          fontsize=16, fontweight='bold')
plt.xlabel('Star Rating')
plt.ylabel('Number of Providers')
plt.tight_layout()
plt.savefig('charts/rating_distribution.png', dpi=150)
plt.show()

print(" Chart 3 saved!")

# Chart 4: Small vs Medium vs Large facility comparison
plt.figure(figsize=(8, 5))
size_avg = star_rated.groupby('size')['overall_star_rating'].mean().sort_values(ascending=False)

sns.barplot(x=size_avg.index, y=size_avg.values, palette='Blues_d')
plt.title('Average Star Rating by Facility Size', 
          fontsize=16, fontweight='bold')
plt.xlabel('Facility Size')
plt.ylabel('Average Star Rating')
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig('charts/rating_by_size.png', dpi=150)
plt.show()

print(" Chart 4 saved!")

# Chart 5: Metro vs Rural comparison
plt.figure(figsize=(12, 6))
mmm_avg = star_rated.groupby('mmm_region')['overall_star_rating'].mean().sort_values(ascending=False)

sns.barplot(x=mmm_avg.values, y=mmm_avg.index, palette='Blues_d')
plt.title('Average Star Rating: Metro vs Rural', 
          fontsize=16, fontweight='bold')
plt.xlabel('Average Star Rating')
plt.ylabel('Region Type')
plt.tight_layout()
plt.savefig('charts/metro_vs_rural.png', dpi=150)
plt.show()

print("Chart 5 saved!")
print("\n All charts completed and saved!")