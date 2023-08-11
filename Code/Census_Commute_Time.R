library(tidyverse)
library(dplyr)
library(ggplot2)
library(gcookbook)

commute <- read.csv("C:\\Users\\nisha\\Documents\\DAEN Capstone\\County_Commute.csv")
head(commute)

#MD
ggplot(commute, aes(x = Time_Frame, y = Montgomery_Estimate/10205945)) +
  geom_col(fill = "violet", colour = "black") +
  scale_y_continuous(limits = c(0, .5)) +
  geom_text(aes(label =  round(Montgomery_Estimate/10205945, digits = 3)), vjust = -2, colour = "black") +
  labs(title = "Mongomery County Proportion of Commuters by Commute Time",
       y = "Proportion of Commuters",
       x = "Commute Time Bracket (In Minutes)")


ggplot(commute, aes(x = Time_Frame, y = Prince_Georges_Estimate/12137655)) +
  geom_col(fill = "purple", colour = "black") +
  scale_y_continuous(limits = c(0, .5)) +
  geom_text(aes(label =  round(Prince_Georges_Estimate/12137655, digits = 3)), vjust = -2, colour = "black") +
  labs(title = "Prince George's County Proportion of Commuters by Commute Time",
       y = "Proportion of Commuters",
       x = "Commute Time Bracket")

#VA
ggplot(commute, aes(x = Time_Frame, y = Arlington_Estimate/1625165)) +
  geom_col(fill = "blue", colour = "black") +
  scale_y_continuous(limits = c(0, .5)) +
  geom_text(aes(label =  round(Arlington_Estimate/1625165, digits = 3)), vjust = -2, colour = "black") +
  labs(title = "Arlington County Proportion of Commuters by Commute Time",
       y = "Proportion of Commuters",
       x = "Commute Time Bracket (In Minutes)")


ggplot(commute, aes(x = Time_Frame, y = Fairfax_Estimate/10232140)) +
  geom_col(fill = "darkblue", colour = "black") +
  scale_y_continuous(limits = c(0, .5)) +
  geom_text(aes(label =  round(Fairfax_Estimate/10232140, digits = 3)), vjust = -2, colour = "black") +
  labs(title = "Fairfax County Proportion of Commuters by Commute Time",
       y = "Proportion of Commuters",
       x = "Commute Time Bracket")


ggplot(commute, aes(x = Time_Frame, y = Prince_William_Estimate/6730480)) +
  geom_col(fill = "lightblue", colour = "black") +
  scale_y_continuous(limits = c(0, .5)) +
  geom_text(aes(label =  round(Prince_William_Estimate/6730480, digits = 3)), vjust = -2, colour = "black") +
  labs(title = "Prince William County Proportion of Commuters by Commute Time",
       y = "Proportion of Commuters",
       x = "Commute Time Bracket")
 
#DC
ggplot(commute, aes(x = Time_Frame, y = DC_Estimate/5171695)) +
  geom_col(fill = "darkgreen", colour = "black") +
  scale_y_continuous(limits = c(0, .5)) +
  geom_text(aes(label =  round(Prince_William_Estimate/5171695, digits = 3)), vjust = -2, colour = "black") +
  labs(title = "Washington DC Proportion of Commuters by Commute Time",
       y = "Proportion of Commuters",
       x = "Commute Time Bracket")


#NCR
ggplot(commute, aes(x = Time_Frame, y = NCR_Estimate/46103080)) +
  geom_col(fill = 'gold', color = 'black')+
  scale_y_continuous(limits = c(0, .4)) +
  theme(text = element_text(size = 15)) +
  theme(axis.text = element_text(size = 15)) +
  geom_text(aes(label =  round(NCR_Estimate/46103080, digits = 2)), vjust = -1, colour = "black", size =8) +
  labs(title = "National Capital Region Proportion of Commuters by Commute Time (US Census)",
       y = "Proportion of Commuters",
       x = "Commute Time Bracket")


