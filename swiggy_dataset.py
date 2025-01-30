# -*- coding: utf-8 -*-
"""swiggy_dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1As5px7NOGqzEM68BG7954aGEXF0qI1tE
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re

# Load the dataset
df = pd.read_csv('swiggy_file.csv')

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Convert 'Rating', 'Number of Ratings', 'Average Price' to numeric
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Number of Ratings'] = pd.to_numeric(df['Number of Ratings'], errors='coerce')
df['Average Price'] = pd.to_numeric(df['Average Price'], errors='coerce')

# Replace 'Pure Veg' values (Yes/No) with binary (1 for Yes, 0 for No)
df['Pure Veg'] = df['Pure Veg'].apply(lambda x: 1 if isinstance(x, str) and x.strip().lower() == 'yes' else 0)

# Extract each offer as a separate entry
df['Offer Name'] = df['Offer Name'].fillna('No Offers')
df['Extracted Offers'] = df['Offer Name'].apply(lambda x: re.findall(r'\bFLAT \d+ OFF\b', x))

# Display summary statistics
print(df.describe())

# Count of restaurants per Cuisine
cuisine_counts = df['Cuisine'].value_counts()
print("\nCuisine Counts:\n", cuisine_counts)

# Count of restaurants per Area
area_counts = df['Area'].value_counts()
print("\nArea Counts:\n", area_counts)

# Distribution of Ratings
sns.histplot(df['Rating'], kde=True, color='blue')
plt.title('Distribution of Ratings')
plt.show()

# Distribution of Number of Ratings
sns.histplot(df['Number of Ratings'], kde=True, color='green')
plt.title('Distribution of Number of Ratings')
plt.show()

# Count most frequent offers
offer_counts = df['Extracted Offers'].explode().value_counts()
print("\nMost Common Offers:\n", offer_counts)

# Word Cloud for Offers
offer_text = ' '.join(df['Offer Name'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(offer_text)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Offers')
plt.show()

# Average rating for each Cuisine
cuisine_ratings = df.groupby('Cuisine')['Rating'].mean().sort_values(ascending=False)
print("\nCuisine Ratings:\n", cuisine_ratings)

# Average Price distribution for each Cuisine
sns.boxplot(y='Cuisine', x='Average Price', data=df)
plt.title('Average Price Distribution by Cuisine')
plt.show()

# 4️⃣ Plot 1: Average Price Distribution for each Cuisine
plt.figure(figsize=(12, 6))  # Bigger plot for better visibility
avg_price_cuisine = df.groupby('Cuisine')['Average Price'].mean().sort_values(ascending=False)
sns.barplot(x=avg_price_cuisine.index, y=avg_price_cuisine.values, palette='coolwarm')
plt.xticks(rotation=45, ha='right', fontsize=12)  # Rotate for better readability
plt.title('Average Price Distribution for Each Cuisine', fontsize=16, fontweight='bold')
plt.xlabel('Cuisine', fontsize=14)
plt.ylabel('Average Price (in INR)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Light grid for better readability
plt.show()

# Count of restaurants in each area
area_counts = df['Area'].value_counts()
area_counts.plot(kind='bar', figsize=(10, 5), color='purple')
plt.title('Number of Restaurants by Area')
plt.show()

# 5️⃣ Plot 2: Count of Restaurants in Each Area
plt.figure(figsize=(12, 6))  # Bigger plot for better visibility
restaurant_count_by_area = df['Area'].value_counts().sort_values(ascending=False)
sns.barplot(x=restaurant_count_by_area.index, y=restaurant_count_by_area.values, palette='viridis')
plt.xticks(rotation=45, ha='right', fontsize=12)  # Rotate for better readability
plt.title('Count of Restaurants in Each Area', fontsize=16, fontweight='bold')
plt.xlabel('Area', fontsize=14)
plt.ylabel('Number of Restaurants', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Light grid for better readability
plt.show()

# Area with highest rating
best_areas = df.groupby('Area')['Rating'].mean().sort_values(ascending=False).head(10)
print("\nTop 10 Areas by Rating:\n", best_areas)

# Correlation heatmap
corr = df[['Rating', 'Number of Ratings', 'Average Price']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Price vs Rating Scatter Plot
sns.scatterplot(x='Average Price', y='Rating', data=df)
plt.title('Price vs Rating')
plt.show()

# Top 10 cuisines with the most restaurants
top_cuisines = cuisine_counts.head(10)
sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette='viridis')
plt.title('Top 10 Cuisines with Most Restaurants')
plt.show()

# Box plot for Price by Cuisine
sns.boxplot(y='Cuisine', x='Average Price', data=df)
plt.title('Box Plot of Prices for Each Cuisine')
plt.show()

# Top 10 Areas with the most restaurants
top_areas = area_counts.head(10)
sns.barplot(x=top_areas.values, y=top_areas.index, palette='magma')
plt.title('Top 10 Areas with Most Restaurants')
plt.show()

# Plot the areas with the highest rated restaurants
area_ratings = df.groupby('Area')['Rating'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=area_ratings.index[:10], y=area_ratings.values[:10], palette='Set3')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Areas with the Highest Rated Restaurants', fontsize=16, fontweight='bold')
plt.xlabel('Area', fontsize=14)
plt.ylabel('Average Rating', fontsize=14)
plt.show()

# 7️⃣ **Correlation Analysis**
print("\n🔍 Correlation Analysis")
# Correlation heatmap
correlation = df[['Rating', 'Number of Ratings', 'Average Price', 'Number of Offers']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='Blues', fmt='.2f', linewidths=0.5)
plt.title('Correlation Between Numeric Features', fontsize=16, fontweight='bold')
plt.show()

# ✅ **Summary**
print("\n🔍 Analysis Summary")

# Plot the average rating for each cuisine
cuisine_ratings = df.groupby('Cuisine')['Rating'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=cuisine_ratings.index[:10], y=cuisine_ratings.values[:10], palette='coolwarm')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Highest Rated Cuisines', fontsize=16, fontweight='bold')
plt.xlabel('Cuisine', fontsize=14)
plt.ylabel('Average Rating', fontsize=14)
plt.show()

# 3️⃣ **Filter by Location**
def filter_by_location(location_name):
    """Filters data for a specific location and returns key insights and visualizations."""
    location_data = df[df['Location'].str.contains(location_name, case=False, na=False)]
    print(f"\n🔍 Insights for Location: {location_name}")
    print(f"Number of Restaurants: {location_data.shape[0]}")
    print(f"Top 5 Cuisines:\n{location_data['Cuisine'].value_counts().head(5)}")
    print(f"Average Rating for {location_name}: {location_data['Rating'].mean():.2f}")
    # Plot cuisine popularity
    plt.figure(figsize=(10, 6)) # Fixed: Removed extra indentation
    sns.countplot(y=location_data['Cuisine'], order=location_data['Cuisine'].value_counts().index[:10], palette='coolwarm')
    plt.title(f'Top 10 Cuisines in {location_name}', fontsize=16, fontweight='bold')
    plt.xlabel('Number of Restaurants', fontsize=14)
    plt.ylabel('Cuisine', fontsize=14)
    plt.show()

# Filter data for a location
filter_by_location('Kharagpur')

# 4️⃣ **Custom Plots**
def custom_plots():
    """Generate custom plots for customer satisfaction and demand forecasting."""
    print("\n🔍 Custom Plots for Customer Satisfaction and Demand Forecasting")

# 4️⃣ **Custom Plots**
def custom_plots():
    """Generate custom plots for customer satisfaction and demand forecasting."""
    print("\n🔍 Custom Plots for Customer Satisfaction and Demand Forecasting")
    # **Customer Satisfaction**: Distribution of Ratings
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Rating'], bins=20, kde=True, color='green')
    plt.title('Distribution of Restaurant Ratings', fontsize=16, fontweight='bold')
    plt.xlabel('Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.show()

# 5️⃣ **Advanced Analysis (ML Models)**
def machine_learning_models():
    """Run machine learning models to predict Rating and Average Price."""
    print("\n🔍 Running ML Models for Predicting Ratings and Prices")

    # **Predict Rating**
    # Prepare X and y for the regression model
    X = df[['Number of Ratings', 'Average Price', 'Number of Offers', 'Pure Veg']]
    y_rating = df['Rating']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y_rating, test_size=0.2, random_state=42)

    # Regression model for predicting Rating
    reg_rating = RandomForestRegressor(random_state=42)
    reg_rating.fit(X_train, y_train)

    # Predict and evaluate
    y_pred_rating = reg_rating.predict(X_test)
    print("\n📈 Rating Prediction Results")
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred_rating):.2f}")
    print(f"R2 Score: {r2_score(y_test, y_pred_rating):.2f}")
    # **Predict Average Price**
    y_price = df['Average Price']

# Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y_price, test_size=0.2, random_state=42)

    # Regression model for predicting Average Price
    reg_price = RandomForestRegressor(random_state=42)
    reg_price.fit(X_train, y_train)

    # Predict and evaluate
    y_pred_price = reg_price.predict(X_test)
    print("\n📈 Price Prediction Results")
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred_price):.2f}")
    print(f"R2 Score: {r2_score(y_test, y_pred_price):.2f}")

machine_learning_models()

# Combine all offer descriptions from the 'Offer Name' column
offer_text = ' '.join(df['Offer Name'].dropna().astype(str))

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='coolwarm').generate(offer_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Attractive Offer Phrases', fontsize=16, fontweight='bold')
plt.show()

# Prepare data for heatmap
area_ratings = df.pivot_table(index='Area', columns='Cuisine', values='Rating', aggfunc='mean')

plt.figure(figsize=(12, 8))
sns.heatmap(area_ratings, annot=True, fmt=".2f", cmap='YlGnBu', linewidths=0.1)
plt.title('Average Ratings for Cuisines in Different Areas', fontsize=16, fontweight='bold')
plt.xlabel('Cuisine', fontsize=14)
plt.ylabel('Area', fontsize=14)
plt.show()