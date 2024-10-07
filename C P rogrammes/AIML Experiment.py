Experiment-5
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Ames_Housing_Data.csv')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Checking for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Data types and non-null counts
print("\nData types and non-null counts:")
print(df.info())

# Summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Summary statistics for categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
print("\nSummary statistics for categorical columns:")
print(df[categorical_cols].describe())

# Check unique values in categorical columns
print("\nUnique values in categorical columns:")
for col in categorical_cols:
    print(f"{col}: {df[col].nunique()} unique values")

# Check for duplicates
print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")

# Dropping duplicates (if needed)
df = df.drop_duplicates()

# Correlation matrix for numerical columns
print("\nCorrelation matrix:")
corr = df.corr()
print(corr)

# 1. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# 2. Histogram for Numerical Features
numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], kde=True, bins=30, color='blue')
    plt.title(f'Distribution of {col}')
    plt.show()

# 3. Box Plot for Numerical Features (Detecting Outliers)
for col in numerical_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df[col], color='green')
    plt.title(f'Box Plot of {col}')
    plt.show()

# 4. Count Plot for Categorical Features
for col in categorical_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=col, palette='Set2')
    plt.title(f'Count Plot of {col}')
    plt.xticks(rotation=45)
    plt.show()

# 5. Pairplot to visualize pairwise relationships (Numerical data)
plt.figure(figsize=(10, 8))
sns.pairplot(df, diag_kind='kde', corner=True)
plt.title("Pairplot of Numerical Features")
plt.show()

# 6. Scatter plot for relationships between selected numerical variables
# Example: Scatter plot between two variables, replace 'var1' and 'var2' with actual column names
plt.figure(figsize=(8, 6))
plt.scatter(df['var1'], df['var2'], color='purple')
plt.title('Scatter Plot of var1 vs var2')
plt.xlabel('var1')
plt.ylabel('var2')
plt.show()

# 7. Heatmap of missing values to visualize gaps in the dataset
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title("Missing Values Heatmap")
plt.show()

# 8. Bar Plot to show mean values of a numerical variable grouped by a categorical variable
# Replace 'categorical_col' and 'numerical_col' with actual column names
plt.figure(figsize=(8, 6))
sns.barplot(x='categorical_col', y='numerical_col', data=df, estimator=np.mean, ci=None, palette='Blues_d')
plt.title('Mean of Numerical Feature Grouped by Categorical Feature')
plt.xticks(rotation=45)
plt.show()

# 9. Violin Plot to visualize distribution and frequency of a numerical variable grouped by a categorical variable
plt.figure(figsize=(8, 6))
sns.violinplot(x='categorical_col', y='numerical_col', data=df, palette='coolwarm')
plt.title('Violin Plot: Categorical vs Numerical Feature')
plt.xticks(rotation=45)
plt.show()

# 10. Line Plot for time series data (if applicable)
# Replace 'date_col' and 'value_col' with actual column names
if 'date_col' in df.columns:
    df['date_col'] = pd.to_datetime(df['date_col'])
    df.set_index('date_col', inplace=True)
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=df.index, y='value_col', data=df, color='red')
    plt.title('Time Series Analysis')
    plt.show()