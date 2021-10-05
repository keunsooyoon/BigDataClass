

카페 매출 데이터 분석

install.packages("readxl")
library(readxl)


sales = read_xlsx("Cafe_Sales.xlsx")
head(sales)
tail(sales)
dim(sales)
str(sales)
summary(sales)
View(sales)


# 결측치 확인...NA 확인

is.na(sales)


table(is.na(sales))

FALSE   TRUE 
312734    171 


table(is.na(sales$order_id))
table(is.na(sales$order_date))


# 결측치 제거


sales <- na.omit(sales)
table(is.na(sales))





head(sales,20)



# 중복 확인...

unique(sales$order_date)

날짜 와 시간까지 order_date 열에 함께 들어 가있다. 


unique(sales$category)

unique(sales$item)

unique(sales$price)

# 매장에서 팔린 제품의 총 판매 금액이 얼나 될까..

table(sales$item)

sort(table(sales$item))

sort(table(sales$item), decreasing = TRUE)

# 매출액 계산

sales_tr <- data.frame(table(sales$item))
sales_tr


sales_item <-  subset.data.frame(sales, select = c("item", "price"))
sales_item

sales_item <- unique(sales_item)
sales_item



# 제품별 판매 개수와 제품별 가격을 계산
item_list = merge(sales_tr, sales_item, by.x="Var1", by.y = "item")
item_list

item_list$amount = item_list$Freq * item_list$price
item_list


sum(item_list$amount)


# 요일별 판매 분석


sales$weekday <-  weekdays(sales$order_date)

table(sales$weekday)



date_info <-  data.frame(weekday = c("월요일","화요일","수요일",
                                   "목요일","금요일","토요일","일요일"),
                       day=c("평일","평일","평일","평일","평일",
                             "주말","주말"))

sales <- merge(sales, date_info)

head(sales)

table(sales$day)


# 계절별 판매 분석

sales$month <- months(sales$order_date)
head(sales)




# Quiz.season 열을 만들어 12월~2월은 "겨울" 3-5 "봄" 6-8"여름 "9-11 "겨울"

# by신동희

sales$month <- months(sales$order_date)
sales$month<- as.integer(gsub('월', '', sales$month))

sales$season <- ifelse(sales$month >=12,"겨울",
                       ifelse(sales$month>=9, '가을',
                       ifelse(sales$month >=6,'여름',
                       ifelse(sales$month>=3,'봄',
                       ifelse(sales$month>=1,'겨울')))))

head(sales)

table(sales$season)



# 시각화 

cate <- data.frame(table(sales$category))
cate

library(ggplot2)

ggplot(cate, aes(Var1, Freq)) + 
  geom_col() +
  geom_text(label = cate$Freq)




요일별 판매건수 시각화.


days <- data.frame(table(sales$weekday))
days

ggplot(days,aes(Var1,Freq)) +geom_col()+geom_text(label=cate$Freq)


days$por = days$Freq / sum(days$Freq) * 100
days


ggplot(days, aes(x="", y = por, fill=Var1)) + geom_col()



