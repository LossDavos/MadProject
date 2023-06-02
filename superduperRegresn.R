students <- read.csv("https://raw.githubusercontent.com/LossDavos/MadProject/main/student-mat.csv", sep=",", header=TRUE, encoding="UTF-8")
summary(students)


for (i in colnames(students)){
  if (all(students[[i]] %in% c("yes", "no"))){
    students[[i]] <- ifelse(students[[i]] == "yes", 1, 0)
  }
}
# students[['Walc']] = 5 - students[['Walc']] 
# students[['Dalc']] = 5 - students[['Dalc']] 
# students[['goout']] = 5 - students[['goout']] 

fit2 <- lm(students$G3 ~ students$absences, data=students)
t <- fit2$coef
plot(students$G3, students$absences, pch=20)
abline(coef=t, col="blue", lwd=2)

# david_is_dummy <- dummy_cols(students, select_columns = c('Medu', 'Fedu'))
# 
# #fit <- lm(david_is_dummy$G3 ~ david_is_dummy$Medu_1 + david_is_dummy$Medu_2 + david_is_dummy$Medu_3+ david_is_dummy$Medu_4 +
# #            david_is_dummy$Fedu_1 + david_is_dummy$Fedu_2 + david_is_dummy$Fedu_3 + david_is_dummy$Fedu_4
# #            , data=david_is_dummy)
# fit <- lm(david_is_dummy$G3 ~ david_is_dummy$absences
#             , data=david_is_dummy)
t_test_results <- list()
cols_binary <-c("sex", "famsize",     "schoolsup",  "famsup",     "paid",       "activities", "nursery",    "higher",     "internet",   "romantic")
cols_categorical <- c("Medu", "Fedu","studytime",  "failures", "famrel",    
                      "freetime", "goout" ,     "Dalc"  ,     "Walc"      , "health"  ,   "absences")
for (i in 1:10){
  result <- t.test(G3 ~ students[[cols_binary[i]]], data = students)
  t_test_results[[cols_binary[i]]] <- result
  names(t_test_results)[i] <- cols_binary[i]
}
for (i in 1:11){
  result <- t.test(G3 ~ students[[cols_categorical[i]]]>= mean(students[[cols_categorical[i]]]), data = students)
  t_test_results[[cols_categorical[i]]] <- result
  names(t_test_results)[i+10] <- cols_categorical[i]
}
for (i in names(t_test_results)) {
  print(i)  # Print the name of the element
  print(t_test_results[[i]])  # Print the element itself
}
boxplot(foot_length ~ gender, data=foot, col=foot$gender)
max <- 0
fit_lm_model <- function(variables, w){
  composite_variable <- rep(0,395)
  for (i in 1:length(variables)){
    composite_variable <- composite_variable + students[[variables[i]]] * w[i]
  }
  fitted <- lm(G3 ~ composite_variable
              , data=students)
  rsq <- summary(fitted)$r.squared
  if (rsq > max){
    print(rsq)
    max <<- rsq
  }
  if ( rsq > 0.3){
  print(fitted$r.squared)
    print(variables)
    print(weights)
  }

  t <- fitted$coef
  
  # plot(composite_variable, students$G3, pch=20)
  # abline(coef=t, col="blue", lwd=2)
}
possible <-  c( "schoolsup",  "famsup",     "paid",  "higher",   
               "Medu", "Fedu","studytime", "famrel",    
               "freetime", "goout" ,     "Dalc"  ,     "Walc"      , "health")
for (i in 1:100000){
  si <-  sample(5:10, 1)
fit_lm_model(sample(possible,si), sample(1:100, si)/10)
}

library(corrplot)
R <- cor(students[,c(7,8,14:19, 21, 24:33)])
corrplot.mixed(R, lower = "number", lower.col = "black", upper = "ellipse", tl.pos="lt")



# Load the required library for logistic regression
library(glmnet)

# Create a subset of the relevant variables from the 'students' dataset
subset_data <- students[, c( "sex", "Medu", "Fedu",
                             "studytime", "failures",
                            "schoolsup", "famsup", "paid", "higher",
                            "romantic", "famrel", "goout", "Dalc", "Walc", "absences","G3")]

# Fit a logistic regression model
logistic_model <- glm(G3>=mean(G3) ~ ., data = subset_data, family = "binomial")

# Print the summary of the logistic regression model
summary(logistic_model)



result <- t.test(students$G3 ~ students[['Medu']]>= mean(students[['Medu']]), data = students['sex'=='F'])
print(result)
result <- t.test(students$G3 ~ students[['Fedu']]>= mean(students[['Fedu']]), data = students['sex'=='F'])
print(result)
result <- t.test(students$G3 ~ students[['Medu']]>= mean(students[['Medu']]), data = students['sex'=='M'])
print(result)
result <- t.test(students$G3 ~ students[['Fedu']]>= mean(students[['Fedu']]), data = students['sex'=='M'])
print(result)


##TOP 10 BEST
subs <- head(students[order(students$G3, decreasing=TRUE),],10)
summary_all <- colMeans(students[c(7,8,13:30)])
summary_top <- colMeans(subs[c(7,8,13:30)])

# worst_0 <- head(students[order(students$G3),],10)
worst_0 <- students[students$G3==0,]
summary_worst <- colMeans(worst_0[c(7,8,13:30)])

subsetik <- students[students$G3>0,][]
worst_non_0 <- head(subsetik[order(subsetik$G3),],10)
summary_worst_non_0 <- colMeans(worst_non_0[c(7,8,13:30)])

print(summary_top > summary_all)
