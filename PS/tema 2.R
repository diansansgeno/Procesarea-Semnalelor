#Ciobanescu Diana-Nicoleta, gr 244 (via 243)

#tema lab 2

#exerc 1
d <- expand.grid(d1=1:6, d2=1:6)
p1a <- mean(d$d2 < d$d1)
p1b <- mean(abs(d$d1 - d$d2) == 1)
p1c <- mean(d$d2 < d$d1 & d$d1 != d$d2) / mean(d$d1 != d$d2)

#exerc 2
p2a <- (14 * 13 * 12) / 14^3
p2b <- (choose(14, 2) * choose(3, 2) * 2) / 14^3

#exerc 3
p3a <- function(n) prod((365 - 0:(n-1)) / 365)
n3b <- 1
while(p3a(n3b) > 0.5) n3b <- n3b + 1

#exerc 4
p4a <- choose(13, 5) * 4^5 / choose(52, 5)
p4b <- 4 * choose(13, 2) * 13^3 / choose(52, 5)
p4c <- 0

#exerc 5
mod5a_nume <- choose(10, 5)
mod5a_fara <- choose(10, 5) / 2
p5b <- (2 * choose(8, 3)) / choose(10, 5)

#exerc 6
p6a <- choose(6,3)*choose(6,3)/choose(12,6)
p6b <- (choose(6,3)*choose(6,3)/2)/(choose(12,6)/2)

#exerc 7
p7a <- 1-(5/6)^7
p7b <- choose(7,2)*(1/6)^2*(5/6)^5
p7c <- p7b/p7a

#exerc 8
p8a <- choose(5,4)*0.8^4*0.2
p8b <- choose(5,4)*0.8^4*0.2 + 0.8^5
n8c <- ceiling(log(0.001)/log(0.2))
p8c <- 1-0.2^n8c

#exerc 9
p9a <- choose(6,2)*(1/4)^2*(3/4)^4
p9b <- 1-(3/4)^6-choose(6,1)*(1/4)*(3/4)^5
p9c <- (1/4)^2*(3/4)^4

#exerc 10
p10a0 <- (35/36)^15
p10a1 <- choose(15,1)*(1/36)*(35/36)^14
n10b <- ceiling(log(0.5)/log(35/36))
p10b <- 1-(35/36)^n10b

#exerc 11
p11a <- 0.6*0.7*0.2 + 0.6*0.3*0.8 + 0.4*0.7*0.8
p11b <- c(0.4*0.3*0.2, 0.6*0.3*0.2 + 0.4*0.7*0.2 + 0.4*0.3*0.8, 0.6*0.7*0.2 + 0.6*0.3*0.8 + 0.4*0.7*0.8, 0.6*0.7*0.8)
p11c <- choose(3,2)*(0.7)^2*(0.3)

#exerc 12
p12a <- (choose(4,1)*0.3*0.7^3)/(1-0.7^4)
p12b <- (0.3^2*0.7^2)/(choose(4,2)*0.3^2*0.7^2)

#exerc 13
p13a <- choose(14,3)*choose(6,2)/choose(20,5)
p13b <- choose(14,4)*choose(6,1)/choose(20,5)+choose(14,5)*choose(6,0)/choose(20,5)
p13c <- choose(5,3)*(14/20)^3*(6/20)^2

#exerc 14
p14a <- choose(6,2)*choose(24,3)/choose(30,5)
p14b <- 1-choose(24,5)/choose(30,5)
p14c <- choose(5,2)*(6/30)^2*(24/30)^3

#exerc 15
p15a <- choose(4,2)*choose(48,3)/choose(52,5)
p15b <- choose(48,5)/choose(52,5)
p15c <- choose(5,2)*(4/52)^2*(48/52)^3

#exerc 16
p16a <- choose(7,2)*choose(5,2)/choose(12,4)
p16b <- (7/12)*(6/11)*(5/10)*(4/9)
p16c <- ((7/12)*choose(6,1)*choose(5,2)/choose(11,3))/p16a

#exerc 17
p17a <- choose(10,8)*2^8/choose(20,8)
p17b <- 10*choose(9,6)*2^6/choose(20,8)

#exerc 18
p18a <- choose(5,2)*choose(15,2)/choose(20,4)
p18b <- 1-choose(15,4)/choose(20,4)

#exerc 19
p19a <- factorial(4)/(factorial(2)*factorial(1)*factorial(1))*(5/12)^2*(4/12)*(3/12)
p19b <- choose(5,2)*choose(4,1)*choose(3,1)/choose(12,4)
p19c_cu <- (5/12)*(4/12)*(5/12)*(3/12)
p19c_fara <- (5/12)*(4/11)*(4/10)*(3/9)

#exerc 20
p20a <- factorial(6)/(factorial(3)*factorial(2)*factorial(1))*(0.5)^3*(0.3)^2*(0.2)^1
p20b <- 0.8^6-0.5^6-0.3^6
p20c <- choose(50,3)*choose(30,2)*choose(20,1)/choose(100,6)

#exerc 21
p21a <- factorial(6)/6^6
p21b <- factorial(6)/(factorial(2)^3)/6^6
p21c <- choose(6,3)*factorial(6)/(factorial(2)^3)/6^6
p21d <- 2^6/choose(12,6)

#exerc 22
p22a <- choose(3,1)*choose(5,2)*choose(7,2)*choose(9,1)/choose(24,6)
p22b <- (choose(3,6)+choose(5,6)+choose(7,6)+choose(9,6))/choose(24,6)
p22c <- choose(9,6)/choose(24,6)

#exerc 23
p23a <- factorial(20)/(factorial(2)^4*factorial(3)^4*12^20)
p23b <- choose(12,4)*choose(8,4)*p23a

#exerc 24
p24a <- 13*choose(4,3)*12*choose(4,2)/choose(52,5)
p24b <- 13*choose(4,2)*choose(12,3)*4^3/choose(52,5)
p24c <- choose(13,2)*choose(4,2)^2*11*4/choose(52,5)

#exerc 25
p25_5 <- 4/36
p25_8 <- 5/36
p25_other <- 1-p25_5-p25_8
P25En <- function(n) p25_other^(n-1)*p25_5
p25b <- p25_5/(p25_5+p25_8)

#exerc 26
p26a <- function(k) (5/6)^(k-1)*(1/6)
p26b <- choose(7,2)*(1/6)^3*(5/6)^5
p26c <- (5/6)^4

#exerc 27
p27a <- function(k,n) 1/n
p27b <- function(k,n) ((n-1)/n)^(k-1)*(1/n)
p27c_fara <- function(k,n) k/n
p27c_cu <- function(k,n) 1-((n-1)/n)^k

#exerc 28
p28a <- choose(4,2)*0.6^3*0.4^2
p28b <- sum(choose(5,3:5)*0.6^(3:5)*0.4^(5-(3:5)))
p28c <- 0.6/(1-0.4^2)

#exerc 29
k29 <- c(1,3,5,7)
p29a_k <- choose(10-k29,2)/choose(10,3)
p29a <- sum(p29a_k)
p29 <- 3/10
p29b <- p29/(1-(1-p29)^2)

#exerc 30
p30a <- 2/16
p30b <- 3/32

#exerc 31
p31a <- function(n) 2/n
p31b <- function(n,r) 2*(n-r-1)/(n*(n-1))
p31c <- function(n) 2/(n-1)

#exerc 32
p32a <- function(n,m) if (m > n-m+1) 0 else choose(n-m+1,m)/choose(n,m)
p32b <- p32a(8,3)
p32c <- 6/choose(8,3)

#exerc 33
p33a <- factorial(4)*factorial(3)/factorial(6)
p33b <- 2*factorial(3)*factorial(3)/factorial(6)
p33c <- 1-factorial(3)*choose(4,3)*factorial(3)/factorial(6)

#exerc 34
p34a <- choose(8,3)/2^8
p34b <- choose(6,3)/2^8
p34c <- choose(6,3)/choose(8,3)

#exerc 35
p35a <- 1/3
p35b <- 2*(6-2)/(6*5)
p35c <- factorial(4)*factorial(3)/factorial(6)

#exerc 36
p36a <- factorial(4)*2^4/factorial(8)
p36b <- factorial(6)*2^2/factorial(8)

#exerc 37
p37a <- 1-3*(2/3)^8+3*(1/3)^8
p37b <- 3*(2^8-2)/3^8

#exerc 38
p38a <- sum((-1)^(0:4)*choose(4,0:4)*factorial(4-0:4))/factorial(4)
p38b <- choose(4,1)*2/factorial(4)

#exerc 39
p39a <- sum((-1)^(0:3)*choose(3,0:3)*factorial(6-0:3)*2^(0:3))/factorial(6)
s39_1 <- 3*(factorial(5)*2/factorial(6))
s39_2 <- choose(3,2)*(factorial(4)*2^2/factorial(6))
s39_3 <- factorial(3)*2^3/factorial(6)
p39b <- s39_1-2*s39_2+3*s39_3

#exerc 40
j40 <- 1:4
p40a <- sum((-1)^(j40+1)*choose(4,j40)*choose(52-13*j40,13)/choose(52,13))
p40b_gresit <- 4*choose(39,13)/choose(52,13)

#exerc 41
j41 <- 1:3
p41a <- sum((-1)^(j41+1)*choose(13,j41)*choose(52-4*j41,13-4*j41)/choose(52,13))

#exerc 42
p42a <- (10^8-3*9^8+3*8^8-7^8)/10^8
p42b <- 3*(9^8-2*8^8+7^8)/10^8