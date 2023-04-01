# Load required libraries
library(tidyverse)
library(babynames)

# Filter the names that were not used prior to 2010
new_names <- babynames %>%
  filter(year >= 2010) %>%
  group_by(name) %>%
  summarise(total = sum(n)) %>%
  filter(total == max(total)) %>%
  select(name)

# Filter babynames data for new_names only
new_names_data <- babynames %>%
  filter(name %in% new_names$name)

# Create a boxplot to summarize the distribution of the number of uses in each year
ggplot(new_names_data, aes(x=year, y=n)) +
  geom_boxplot() +
  labs(title = "Distribution of number of uses of new names",
       x = "Year", y = "Number of uses")

# Which of those names were used most and least during this period?
new_names_data %>%
  group_by(name) %>%
  summarise(total = sum(n)) %>%
  arrange(desc(total)) %>%
  slice_head(n = 1) %>%
  select(name, total)

new_names_data %>%
  group_by(name) %>%
  summarise(total = sum(n)) %>%
  arrange(total) %>%
  slice_head(n = 1) %>%
  select(name, total)
