# Load necessary libraries
library(tidyverse)

# Read the dataset into a dataframe/tibble
df <- read_csv("dataset.csv")

# View the structure of the dataframe
str(df)

# View the summary statistics of numerical variables
summary(df[, c("numerical_var_1", "numerical_var_2", "numerical_var_3", "numerical_var_4")])

# Identify any missing values in the dataset
sum(is.na(df))

# Compute correlations between numerical variables
cor(df[, c("numerical_var_1", "numerical_var_2", "numerical_var_3", "numerical_var_4")])

# Create a histogram of a numerical variable
ggplot(df, aes(x = numerical_var_1)) + 
  geom_histogram()

# Create a scatterplot of two numerical variables
ggplot(df, aes(x = numerical_var_1, y = numerical_var_2)) + 
  geom_point()

# Create a boxplot of a numerical variable by a categorical variable
ggplot(df, aes(x = categorical_var, y = numerical_var_1)) + 
  geom_boxplot()

# Identify outliers in a numerical variable using a boxplot
boxplot(df$numerical_var_1, main = "Boxplot of numerical_var_1")
