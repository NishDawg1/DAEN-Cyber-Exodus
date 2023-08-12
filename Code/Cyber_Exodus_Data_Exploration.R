library(dplyr)
library(ggplot2)
library(ggthemes)
library(corrplot)

cyber <- read.csv('\\Users\\nisha\\Documents\\DAEN Capstone\\DAEN690_Final_Cyber_Exodus_Dataset.csv')
head(cyber)

#Candidate by Experience
ggplot(cyber, aes(x = Candidate)) + geom_bar(fill = 'gold', col = 'black') +
  geom_text(stat='count', aes(label=..count..), vjust= -.3, size= 6) +
  theme(text = element_text(size = 15)) +
  theme(axis.text = element_text(size = 15)) +
  facet_wrap(~ reorder(EXP_lev, Experience_level)) +
  scale_x_continuous(breaks = seq(from = 0, to = 1, by = 1)) +
  scale_y_continuous(limits = c(0, 500)) +
  labs(title = "Stress Candidate by Experience Level",
       y = 'Frequency',
       x = 'Candidacy')

(26/192)*100
(194/(311+194))*100
(29/(382+29))*100
(2/60)*100

#Candidate by Work Environment
ggplot(cyber, aes(x = Candidate)) + geom_bar(fill = 'gold', colour = 'black') +
  facet_wrap(~ reorder(Work_environment, Work_env)) +
  geom_text(stat='count', aes(label=..count..), vjust= -.3, size= 6) +
  theme(text = element_text(size = 15)) +
  theme(axis.text = element_text(size = 15)) +
  scale_x_continuous(breaks = seq(from = 0, to = 1, by = 1)) +
  labs(title = 'Frequency of Stress Candidates by Work Environment',
       y = 'Frequency',
       x = 'Candidacy')


(3/229)*100
(0/98)*100
(248/(593+248))*100

#Work Environment by Experience
ggplot(cyber, aes(x = reorder(EXP_lev, Experience_level), fill = Work_environment)) + geom_bar(fill = 'gold', colour = 'black') +
  geom_text(stat='count', aes(label=..count..), vjust= -.3, size = 7) +
  facet_wrap(~reorder(Work_environment, Work_env)) +
  theme(text = element_text(size = 15)) +
  theme(axis.text = element_text(size = 15)) +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1)) +
  labs(y = 'Frequency',
       x = 'Experience Level')


#Commute Time and Experience
ggplot(cyber, aes(x = W_com)) + 
  geom_bar(fill = 'gold', col = 'black') +
  facet_wrap(~ reorder(EXP_lev, Experience_level)) +
  geom_text(stat='count', aes(label=..count..), vjust= -.1, size= 6) +
  theme(text = element_text(size = 15)) +
  theme(axis.text = element_text(size = 15)) +
  labs( y = 'Frequency',
       x = 'Commute Time')

#Crime
#Property
ggplot(cyber, aes(x = Prop_Crime_S)) + geom_bar(fill = 'gold', colour = 'black') +
  facet_wrap(~ reorder(EXP_lev, Experience_level)) +
  geom_text(stat='count', aes(label=..count..), vjust= -.1, size= 6) +
  theme(text = element_text(size = 15)) +
  theme(axis.text = element_text(size = 15)) +
  scale_x_continuous(breaks = seq(from = 0, to = 1, by = 1)) +
  labs(y = 'Frequency',
       x = 'Candidacy') 

#Person
ggplot(cyber, aes(x = Per_Crime_S)) + geom_bar(fill = 'gold', colour = 'black') +
  facet_wrap(~ reorder(EXP_lev, Experience_level)) +
  geom_text(stat='count', aes(label=..count..), vjust= -.1, size= 6) +
  theme(text = element_text(size = 15)) +
  theme(axis.text = element_text(size = 15)) +
  scale_x_continuous(breaks = seq(from = 0, to = 1, by = 1)) +
  labs(y = 'Frequency',
       x = 'Candidacy') 


cyber%>%
  group_by(EXP_lev) %>%
  summarize(min = min(Weekly_commute),
            q1 = quantile(Weekly_commute, 0.25),
            median = median(Weekly_commute),
            mean = mean(Weekly_commute),
            q3 = quantile(Weekly_commute, 0.75),
            max = max(Weekly_commute))


 
