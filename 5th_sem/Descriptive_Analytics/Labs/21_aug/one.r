data <- read.csv("C:/Soham/Repositories/BT24DS_TY/5th_sem/Descriptive_Analytics/Labs/21_aug/iris.csv")
#print(data)

#head(data)

#str(data)

#summary(data)

#colSums(is.na(data))

groupby('SepalLengthCm')['PetalLengthCm'].mean()