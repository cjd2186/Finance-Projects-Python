#Take Monte Carlo Simulation equation and translate into code
#The Monte Carlo Simulation estimates an average probability over n trials
#The output should approximately be the p probablity value inputted
import random

#Pass the variables as follows:
#n represents the number of trials
#p represents the probability to be used when calculating a Bernoulli random variable

#p_hat represents the avaerage probability from the inputted probability over n trials
def p_hat(n, p):
    
#Initialize Sum equal to zero, Sum to be used later
    Sum=0
       
#create loop for trial i in n+1 trials, making a range from 1 to n
    for i in range (1, n+1):

#create a bernoulli randomly generated between 0 and 1
        bernoulli= random.random()

#if bernoulli <= p --> bernoulli # is 1    
        if bernoulli <=p:
            bernoulli=1

#if bernoulli is not <= p --> bernoulli # is 0
        else:
            bernoulli=0 

#Sum bernoullis  
        Sum+=bernoulli

#Divide Sum by n trials to get Average
    Average=Sum/n

#Return Average, which is the average probability p_hat
    return Average

#Output becomes closer to actual probablity over more trials
#Run function for p value .5 over n trials 100, 1000 and 10000 trials
print (p_hat(100, .5))
print (p_hat(1000, .5))
print (p_hat(10000, .5))

#Run function for p value .75 over n trials 100, 1000 and 10000 trials
print (p_hat(100, .75))
print (p_hat(1000, .75))
print (p_hat(10000, .75))

#Function to calculate European Call Option price using Black Scholes Merton Formula
#The Black Scholes Merton Fomrula is used to price a European Call Option over T days

#Pass the variables as follows:
#r represents the interest rate
#T represents the number of days until the option can be exercised
#u represents the up factor
#d represents the down factor
#S_0 represents the initial stock price
#K represents the strike price
def black_scholes(r, T, u, d, S_0, K):
    import math

#calculate p*, risk neutral probability
    p_star= (1+ (r-d))/(u-d)

#Initialize Sum to zero    
    Sum=0

#loop day k over T+1 days to get range from 0 to T
    for k in range(0,T+1):

#calculate each part of the formula being iterated in loop (under the summation sigma)
#each term separated by paratheses to the right of summation sign is assigned a variable: 'Binomial_coefficient', 'x', 'y', 'z'

#calculate Binomial coefficient (T K)
        binomial_coefficient= math.factorial(T)/ (math.factorial(k)*math.factorial(T-k))
#calculate x y and z
        x=p_star**k
        y=(1-p_star)**(T-k)
        z=((u**k)*(d**(T-k))*S_0)-K
        
#if z term is negative, then z term becomes 0
        if (z<0):
            z=0
#multiply terms and add to sum, sum will increase each loop
        Sum+= binomial_coefficient*x*y*z

#calculate rate
    rate=1/((1+r)**T)

#Call option price equals sum multiplied by rate
    C_0=Sum*rate

#return call option price
    return (C_0)

print(black_scholes(.05, 10, 1.15, 1.01, 50, 70))


###Calculate European Call Option Price using Monte Carlo Simulation
#Monte Carlo Simulation estimates the price of stock over T days
#Different paths of increased or decreased stocks are estimated, and averaged out over n trials
#The average call price over n trials is outputted to yield a European call option price

#Function to output either a 'u' or 'd' stored in a variable
#Pass the variables as follows:
#u up factor
#d down factor
#p_star risk neutral probability
def up_or_down(u, d, p_star):
    import random

#generate random Bernoulli between 0 and 1
    bernoulli= random.random()

#if bernoulli <= p* --> bernoulli # is u
#if bernoulli is not <= p* --> bernoulli # is d
    if bernoulli <=p_star:
            bernoulli=u
    else:
            bernoulli=d
#return bernoulli, with value 'u' or 'd'
    return bernoulli


#Function to output an estimated list of stock prices over T days (Binomial Lattice Model)
#Pass the variables as follows: 
#r represents the interest rate
#T represents the number of days until the option can be exercised
#u represents the up factor
#d represents the down factor
#S_0 represents the initial stock price
#K represents the strike price
def calculate_path(r, T, u, d, S_0):

#Create list of stock prices with only initial price
    Stock_prices=[S_0]

#Calculate p* risk neutral probability
    p_star= (1+ (r-d))/(u-d)

#Create loop for day k over T+1 days to get range from 0 to T
    for k in range (0,T+1):

#Use function up_or_down to assign 'u' or 'd' to bernoullli variable
        bernoulli=up_or_down(u, d, p_star)

#new stock value equals to day before value times bernoulli
#k to index stock price list
        S_T=bernoulli*Stock_prices[k]

#add stock price at day k to list
        Stock_prices.append(S_T)

#return list of estimated stock prices
    return (Stock_prices)



#Function for Monte Carlo Simulation for European Call Option Pricing
#Pass the variables as follows:
#r represents the interest rate
#T represents the number of days until the option can be exercised
#u represents the up factor
#d represents the down factor
#S_0 represents the initial stock price
#K represents the strike price
#n represents the number of trials
def mont_carlo(r, T, u, d, S_0, K, n):

#Initialize sum to be 0
    Sum=0

#Calculate rate
    rate=1/((1+r)**T)

#Create loop for trial k in n+1 trials to get range from 0 to n
    for k in range (0, n+1):

#run calculate_path to get stock price at day T
#subtract strike price K from stock price to get option price
        Final_option=calculate_path(r, T, u, d, S_0)[T]-K

#if option price is negative, option price is 0
#I.e. if option price is negative, there is no payoff or profit
        if (Final_option>0):
            Sum+=Final_option
        else:
            Sum+=0
#Average sum of call prices by dividing by n trials
    Average=Sum/n

#Multiply average by interest rate in order to get call option price
    Price= Average*rate
    
#return European call option price
    return (Price)

#Run with desired variables over 100, 1000, 10000 trials to get closer to actual European Call Option price
#Actual European Call Option Price calculated using Black Scholes Merton Formula
print(mont_carlo(.05, 10, 1.15, 1.01, 50, 70, 100))
print(mont_carlo(.05, 10, 1.15, 1.01, 50, 70, 1000))
print(mont_carlo(.05, 10, 1.15, 1.01, 50, 70, 10000))

###Calculate Asian Call Option Price using Monte Carlo Simulation
#Monte Carlo Simulation estimates the price of stock over T days
#Different paths of increased or decreased stocks are estimated, and averaged out over n trials
#The average call price over n trials is outputted to yield an Asian call option price

#Function to output either a 'u' or 'd' stored in a variable
#Pass the variables as follows:
#u up factor
#d down factor
#p_star risk neutral probability
def up_or_down(u, d, p_star):
    import random
    
#generate random Bernoulli between 0 and 1
    bernoulli= random.random()

#if bernoulli <= p --> bernoulli # is u
#if bernoulli is not <= p --> bernoulli # is d
    if bernoulli <=p_star:
            bernoulli=u
    else:
            bernoulli=d
#return bernoulli, with value 'u' or 'd'
    return bernoulli


#Function to output an estimated list of stock prices over T days (Binomial Lattice Model)
#Pass the variables as follows: 
#r represents the interest rate
#T represents the number of days until the option can be exercised
#u represents the up factor
#d represents the down factor
#S_0 represents the initial stock price
#K represents the strike price
def calculate_path(r, T, u, d, S_0):
    
#Create list of stock prices with only initial price
    Stock_prices=[S_0]

#Calculate p* risk neutral probability
    p_star= (1+ (r-d))/(u-d)

#Create loop for day k over T+1 days
    for k in range (0,T+1):

#Use function up_or_down to assign 'u' or 'd' to bernoullli variable
        bernoulli=up_or_down(u, d, p_star)

#new stock value equals to day before value times bernoulli
#k to index stock price list
        S_T=bernoulli*Stock_prices[k]

#add stock price at day k to list
        Stock_prices.append(S_T)

#return list of estimated stock prices
    return (Stock_prices)


#Function to price Asian Call option
#Pass the variables as follows:
#r represents the interest rate
#T represents the number of days until the option can be exercised
#u represents the up factor
#d represents the down factor
#S_0 represents the initial stock price
#K represents the strike price
def Asian_Call_price(r, T, u, d, S_0, K):

#Initialize sum to be 0
    Sum=0

#Run calculate_path to get list of stock prices, store into variable
    path=calculate_path(r, T, u, d, S_0)

#create loop for day i over 1 to T+1 days
    for i in range (1,T+1):

#Add stock price at day i to sum
        Sum+=path[i]

#Average sum of stock prices by dividing by T days
    Average=Sum/T

#Payoff equals the Average of the Stock prices minus the Strike price
    Payoff=Average-K

#If Payoff is negative, the call option price is 0
#If Payoff is postive, the call option price equals the Payoff
#I.e. if payoff is negative, there is no payoff or profit in the stock option
    if (Payoff<0):
        C_T=0
    else:
        C_T=Payoff

#Return Asian call option price for one Binomial Lattice Model Path
    return (C_T)


#Function for Monte Carlo Simulation to Price Asian Call Option
#Pass the variables as follows:
#r represents the interest rate
#T represents the number of days until the option can be exercised
#u represents the up factor
#d represents the down factor
#S_0 represents the initial stock price
#K represents the strike price
#n represents the number of trials
def mont_carlo(r, T, u, d, S_0, K, n):

#Initialize sum to be 0
    Sum=0

#Calculate rate
    rate=1/((1+r)**T)

#Create loop for trial k in n+1 trials, to get range from 0 to n
    for k in range (0, n+1):

#run Asian_Call_price to get price of Asian call option
        Sum+=Asian_Call_price(r, T, u, d, S_0, K)

#Average sum of call prices by dividing by n trials
    Average=Sum/n

#Multiply average by interest rate in order to get call option price
    Price= Average*rate

#return Asian call option price
    return (Price)

#Run with desired variables over 100, 1000, 10000 trials to get closer to actual Asian Call Option price
print(mont_carlo(.05, 10, 1.15, 1.01, 50, 70, 100))
print(mont_carlo(.05, 10, 1.15, 1.01, 50, 70, 1000))
print(mont_carlo(.05, 10, 1.15, 1.01, 50, 70, 10000))


###Calculate Barrier Call Option Price using Monte Carlo Simulation
#Monte Carlo Simulation estimates the price of stock over T days
#Different paths of increased or decreased stocks are estimated, and averaged out over n trials
#The average call price over n trials is outputted to yield a Barrier call option price

#Function to output either a 'u' or 'd' stored in a variable
#Pass the variables as follows:
#u up factor
#d down factor
#p_star risk neutral probability
def up_or_down(u, d, p_star):
    import random

#generate random Bernoulli between 0 and 1
    bernoulli= random.random()

#if bernoulli <= p --> bernoulli # is u
#if bernoulli is not <= p --> bernoulli # is d
    if bernoulli <=p_star:
            bernoulli=u
    else:
            bernoulli=d
#return bernoulli, with value 'u' or 'd'
    return bernoulli

#Function to output an estimated list of stock prices over T days (Binomial Lattice Model)
#Pass the variables as follows: 
#r represents the interest rate
#T represents the number of days until the option can be exercised
#u represents the up factor
#d represents the down factor
#S_0 represents the initial stock price
#K represents the strike price
def calculate_path(r, T, u, d, S_0):
    
#Create list of stock prices with only initial price
    Stock_prices=[S_0]

#calculate p* risk neutral probability
    p_star= (1+ (r-d))/(u-d)
    
#Create loop for day k over T+1 days, to get range from 0 to T
    for k in range (0,T+1):

#Use function up_or_down to assign 'u' or 'd' to bernoullli variable
        bernoulli=up_or_down(u, d, p_star)
    
#new stock value equals to day before value times bernoulli
#k to index stock price list
        S_T=bernoulli*Stock_prices[k]

#add stock price at day k to list
        Stock_prices.append(S_T)

#return list of estimated stock prices
    return (Stock_prices)


#Function to price Barrier Call Option
#Pass the variables as follows: 
#r represents the interest rate
#T represents the number of days until the option can be exercised
#u represents the up factor
#d represents the down factor
#S_0 represents the initial stock price
#K represents the strike price
#b represents stock price
#n_1 represents n_1th day (eg 4th, 5th day)
#n_2 represents n_2th day (eg 6th, 7th day)
def Barrier_Call_price(r, T, u, d, S_0, K, b, n_1, n_2):
    
#Run calculate_path to get stock price at day T, store into variable
    S_T=calculate_path(r, T, u, d, S_0)[T]

#Payoff equals Stock Price minus Strike Price
    Payoff=S_T-K

#If Payoff is negative, the call option payoff is 0
#If Payoff is postive, the call option payoff equals the Payoff
#I.e. if payoff is negative, there is no payoff or profit
    if (Payoff<0):
        Payoff=0
    else:
        Payoff=Payoff
    
#Run calculate path to get list of stock prices over T days
    price=calculate_path(r, T, u, d, S_0)

#if stock price at day n_1 and at day n_2 is greater than price b, I=1
#if stock price at day n_1 and at day n_2 is less than price b, I=0
    if (price[n_1] and price[n_2]>= b):
        I=1
    else:
        I=0

#Option price equals Payoff multiplied by I
    C_T=Payoff*I

#Return Barrier call option price for one Binomial Lattice Model Path
    return (C_T)


#Function for Monte Carlo Simulation for Barrier Call Option Pricing
#Pass the variables as follows:
#r represents the interest rate
#T represents the number of days until the option can be exercised
#u represents the up factor
#d represents the down factor
#S_0 represents the initial stock price
#K represents the strike price
#b represents stock price
#n_1 represents n_1th day (eg 4th, 5th day)
#n_2 represents n_2th day (eg 6th, 7th day)
#n represents the number of trials
def mont_carlo(r, T, u, d, S_0, K, b, n_1, n_2, n):

#Initialize sum to be 0
    Sum=0

#Calculate rate
    rate=1/((1+r)**T)

#Create loop for trial k in n+1 trials, to get range from 0 to n
    for k in range (0, n+1):
        
#run Barrier_Call_price to get price of Barrier call option    
        Sum+=Barrier_Call_price(r, T, u, d, S_0, K, b, n_1, n_2)
    
#Average sum of call prices by dividing by n trials
    Average=Sum/n

#Multiply average by interest rate in order to get call option price
    Price= Average*rate

#Return Barrier call option price
    return (Price)

#Run with desired variables over 100, 1000, 10000 trials to get closer to actual Barrier Call Option price
print(mont_carlo(.05, 10, 1.15, 1.01, 50, 70, 66, 4, 6, 100))
print(mont_carlo(.05, 10, 1.15, 1.01, 50, 70, 66, 4, 6, 1000))
print(mont_carlo(.05, 10, 1.15, 1.01, 50, 70, 66, 4, 6, 10000))


