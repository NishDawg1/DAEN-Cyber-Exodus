library(tidyverse)
library(dplyr)
library(ggplot2)
library(gcookbook)

#Cyber Salaries

sal <- read.csv("C:\\Users\\nisha\\Documents\\DAEN Capstone\\Cyber_salaries.csv")
head(sal)

#Salary and Experience
ggplot(sal, aes(x =reorder(experience_level,salary), y = salary)) + 
  geom_boxplot(fill = "gold", colour = "black") +
  coord_flip() +
  theme(text = element_text(size = 15)) +
  theme(axis.text = element_text(size = 15)) +
  scale_y_continuous(labels = scales:: comma, breaks = seq(0, 400000, 50000), limits = c(0, 400000)) +       
  labs(title = "Salary by Experience Level",
       y = "Salary (USD)",
       x = "Experience Level")


sal%>%
  group_by(experience_level) %>%
  summarize(min = min(salary),
            q1 = quantile(salary, 0.25),
            median = median(salary),
            mean = mean(salary),
            q3 = quantile(salary, 0.75),
            max = max(salary))


# Work environment and Experience
ggplot(sal, aes(x = experience_level)) + 
  geom_text(stat='count', aes(label=..count..), vjust= -.3) +
  theme(text = element_text(size = 15)) +
  theme(axis.text = element_text(size = 15)) +
  geom_bar(fill = "darkgreen", colour = "black") +
  labs(title = "Experience Level Frequency",
       y = "Frequency",
       x = "Experience Level")

  