#This program uses the Parking.csv file, with nyc parking ticket information, in order to find different statistics of parking tickets


#import pandas in order to create a DataFrame
import pandas as pd

#Store the data frame into a variable, index the DataFrame by 'Plate'
#Parking.csv from website did not include '$' in front of 'Amount Due'
tickets=pd.read_csv('Parking.csv', index_col='Plate')

'''
Amount_owed takes as input a DataFrame containing all of the ticket information 
  and a plate string and returns a tuple containing the following information: 
  (number of open violations, total dollar amount due of all open violations)
'''
def amount_owed(tickets, plate):
    #creates new data frame 'total'
    #'total' indexes the data frame by plate number
    #'total' has one column, being 'Amount Due', 
    #representing the Total Amount Due for each corresponding plate
    
    total=tickets.groupby(tickets.index).agg({'Amount Due':sum})
    
    #Rename the column 'Amount Due' to 'Total Amount Due'--
    #store in new DataFrame 'final'
    total.rename(columns = {'Amount Due':'Total Amount Due'}, inplace = True) 
    
    #Create new DataFrame that sorts the 'total' Data frame so --
    #the 'Total Amount Due' is ordered from greatest to least 
    final=total.sort_values(by = 'Total Amount Due', ascending = False) 
    
    #add a new column to the tickets DataFrame that contains every plate
    tickets['Plate']=tickets.index
    
    #Create a series that displays the amount of times a plate shows up in 
    #the 'tickets' DataFrame
    series=tickets['Plate'].value_counts()
    
    #Turn this series into its own DataFrame--
    #DataFrame 'series' is indexed by plate, --
    #with one column with the values how many--
    #violations that plate has
    series=series.to_frame()   
    
    #add a new column to 'final' called 'Number of Violations' 
    #that consists of the values from the column in the 'series' DataFrame
    final['Number of Violations']=series['Plate']
    
    #locate and store the value from 'Number of Violations' --
    #associated with plate input
    Number_of_violations=final.loc[plate]['Number of Violations']
    
    #locate and store the value from 'Total Amount Due' associated --
    #with plate input
    Total_amt_due=final.loc[plate]['Total Amount Due']
    
    ##return tuple with 'Number_of_violations' and 'Total_amount_due'
    return Number_of_violations, Total_amt_due
'''
Most_owed takes a DataFrame containing the parking ticket information as input 
  and returns a tuple containing the following information (plate number, total amount due) 
  associated with whichever car owes the most money.
'''
def most_owed(tickets):
    
    #creates new data frame 'Total'
    #'total' indexes the data frame by plate number
    #'total' has one column, being 'Amount Due',--
    #representing the Total Amount Due for each corresponding plate
    total=tickets.groupby(tickets.index).agg({'Amount Due':sum})
    
    #Rename the column 'Amount Due' to 'Total Amount Due'
    total.rename(columns = {'Amount Due':'Total Amount Due'}, inplace = True) 
    
    #Create new DataFrame that sorts the 'total' Data frame so --
    #the 'Total Amount Due' is ordered from greatest to least
    final=total.sort_values(by = 'Total Amount Due', ascending = False) 
    
    #store the 0th index: the plate number with the greatest 'Total Amount Due'
    plate_number=final.index[0]
    
    #store the 0th element of the 'Total Amount Due' column:--
    #the Total Amount Due for the plate
    total_amount_due=final.iloc[0]['Total Amount Due']
    
    #return tuple with 'plate_number' and 'total_amount_due'
    return (plate_number,total_amount_due)
  
  #****Filter tickets for prefix CTH plates

#Preceding code is used to determine how much money diplomatic cars from Egypt owe in total.
'''
#Make a new 'tickets' DataFrame, indexed by 'Plate'
tickets=pd.read_csv('Parking.csv', index_col='Plate')

#Create new DataFrame using DataFrame 'tickets'
tickets_cth=tickets

#Create new column in 'tickets_cth' of every plate
tickets_cth['Plate']=tickets_cth.index

#Create a new column 'Bool'
#The column will have value 'True' if the plate in the row--
#starts with the prefix 'CTH', Egyptian Foreign Consul plate
tickets_cth['Bool']=tickets_cth['Plate'].str.startswith('CTH')

#Only include rows where the column 'Bool' has True values
#DataFrame now only has plates starting with 'CTH'
tickets_cth=tickets_cth[tickets_cth['Bool']>0]

#****Filter tickets for prefix DTH plates

#Make a new 'tickets' DataFrame, indexed by 'Plate'
tickets=pd.read_csv('Parking.csv', index_col='Plate')

#Create new DataFrame using DataFrame 'tickets'
tickets_dth=tickets

#Create new column in 'tickets_dth' of every plate
tickets_dth['Plate']=tickets_dth.index

#Create a new column 'Bool'
#The column will have value 'True' if the plate in the row--
#starts with the prefix 'DTH', Egyptian Foreign Diplomat plate
tickets_dth['Bool']=tickets_dth['Plate'].str.startswith('DTH')

#Only include rows where the column 'Bool' has True values
#DataFrame now only has plates starting with 'DTH'
tickets_dth=tickets_dth[tickets_dth['Bool']>0]

#****Combine Prefix plates into single DataFrame

#combine the 'tickets_cth' and 'tickets_dth' dfs
#to make a new dataframe that only has 
#plates that start with 'CTH' or 'DTH'
prefix_plates= tickets_cth.append(tickets_dth)

#****Filter tickets for suffix THA plates

#Make a new 'tickets' DataFrame, indexed by 'Plate'
tickets=pd.read_csv('Parking.csv', index_col='Plate')

#Create new DataFrame using DataFrame 'tickets'
tickets_tha=tickets

#Create new column in 'tickets_tha' of every plate
tickets_tha['Plate']=tickets_tha.index

#Create a new column 'Bool'
#The column will have value 'True' if the plate in the row--
#ends with the suffix 'tha', Egyptian Foreign Diplomat plate
tickets_tha['Bool']=tickets_tha['Plate'].str.endswith('THA')

#Only include rows where the column 'Bool' has True values
#DataFrame now only has plates ending with 'THA'
tickets_tha=tickets_tha[tickets_tha['Bool']>0]

#****Filter tickets for suffix THD plates

#Make a new 'tickets' DataFrame, indexed by 'Plate'
tickets=pd.read_csv('Parking.csv', index_col='Plate')
'''
#Create new DataFrame using DataFrame 'tickets'
tickets_thd=tickets

#Create new column in 'tickets_thd' of every plate
tickets_thd['Plate']=tickets_thd.index

#Create a new column 'Bool'
#The column will have value 'True' if the plate in the row--
#ends with the suffix 'thd', Egyptian Foreign Diplomat plate
tickets_thd['Bool']=tickets_thd['Plate'].str.endswith('THD')

#Only include rows where the column 'Bool' has True values
#DataFrame now only has plates ending with 'THD'
tickets_thd=tickets_thd[tickets_thd['Bool']>0]

#****Combine Suffix plates into single DataFrame

#combine the 'tickets_tha' and 'tickets_thd' dfs
#to make a new dataframe that only has 
#plates that end with 'THA' or 'THD'
suffix_plates= tickets_tha.append(tickets_thd)

#****Combine Prefix plates and Suffix plates into single DataFrame

#combine prefix and suffix DataFrames into one new--
#DataFrame 'Egypt_tickets'
Egypt_tickets=prefix_plates.append(suffix_plates)

#****Total amount Egypt owes:
#****Sum is from every Egyptian plate in Problem 1 DataFrame, regardless of Year
#****Sum includes Years (2020,2097,2098,2099) as Prompt did not say to exclude Total Amount Due from such years

#create series from values in column 'Amount Due' --
#in DataFrame of Egyptian plates
total_due=Egypt_tickets['Amount Due']

#Find sum of series to get total amount Egypt owes
#display/return total amount Egypt owes
total_due.sum()

#****License plate number of worst offender: 
#****Amount owed by worst offender:

#found by running 'Most owed' function from problem 3 --
#using DataFrame of Egyptian plates
#display tuple with 'plate_number' and 'total_amount_due'
most_owed(Egypt_tickets)

#****Worst year for parking tickets from Egyption diplomats:
#****Total Amount Egypt Owed during Worst Year

#Create column in 'Egypt_tickets' df displays the year of each violation
Egypt_tickets['Year'] = pd.DatetimeIndex(Egypt_tickets['Issue Date']).year

#Renamed this new DataFrame as 'Year'
Year=Egypt_tickets
Year

#Create new DataFrame that is indexed by the 'Year' --
#and the total amount due for that year
Year_sort=Year.groupby(Year['Year']).agg({'Amount Due':sum})

#Rename the column 'Amount Due' to 'Total Amount Due'
Year_sort.rename(columns = {'Amount Due':'Total Amount Due'}, inplace = True) 

#Add new column to 'Year_sort' of with value of each Year
Year_sort['Year']=Year_sort.index

#Create new column 'Bool' in 'Year_sort' that have value--
#as 'True' if year is greater than 1994
Year_sort['Bool']=Year_sort['Year']>1994

#values in 'Bool' column have value--
#as 'True' if year is greater than 1994 and also less than 2020
Year_sort['Bool']=Year_sort['Year']<2020

#'Year_sort' DataFrame only contains--
#Years where 'Bool' column has value True--
#Therefore only rows from year 1995-2019--
#are in 'Year_sort' DataFrame
Year_sort=Year_sort[Year_sort['Bool']>0]

#Sort 'Year_sort' DataFrame in descending value in --
#column 'Total Amount Due'
Year_descend=Year_sort.sort_values(by = 'Total Amount Due', ascending = False) 

#Store 0th index (first year) in 'Worst_year'
#This row has the year with the most larget value in 'Total Amount Due'
Worst_year=Year_descend.index[0]

#store the 0th element of the 'Total Amount Due' column:--
#value of the Total Amount Due for year with most 'Total Amount Due'
Worst_total=Year_descend.iloc[0]['Total Amount Due']

#return/display the worst year and total amount due in that year
Worst_year, Worst_total