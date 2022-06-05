Intro = """INTRODUCTION
________________________________________________________________________________________________________________________________________
This insurance csv file contains a list of approximately 1350 clients, with the following attributes:  
    Age, Sex, BMI, Children, Smoker, Region and Charges.
To analyze this dataset, I first extracted all of the data from the file, and separated each column into a separate variable with lists. 

I decided to analyze the dataset and extract information in the following ways using this data: 
1) Find the most common client, aka the most common value in each column
2) Seperate each column into more digestible blocks, with their proportion to the whole
   (How many clients are between 18 - 23? What percentage of clients is that of the total?)
3) Calculate which two collumns have the highest correlation with each other (does an increase in age show a correlation with increase in BMI?)
4) Calculate a correlation between an Attribute and the Number of Clients (As age increases, are there more or less clients?)
5) Calculate the Mean, Mode, Median, Max, Min, and 3 most common Ranges for 
each attribute/collumn in each region(What is the most common age range in SouthWest area?)

Given that, heres what I was able to calculate:
_________________________________________________________________________________________________________________________________________"""

MostCommonDescription = """In this table, you can see the most prominent client attributes, the amount of times they appear in the dataset, the proportion of their amount compared to all others in the dataset (For age, 69 clients are 18, 69/1350 total clients is 0.05 of the total), and the proportion.

The most significant discoveries from this would most likely be smoker, age, BMI and children. I say this because Sex is 50/50, so for male to be 0.1% dominant isnt significant whatsover. There are 4 regions so each should have 25% or so clients, so 27% isnt too out of the curve, and charges has thousands of different values so you cant say one value is significant.

In terms of the more statistically significant ones, the fact that 80% of people are non smokers is interesting because there are two options, Yes/No making it 50/50 assuming nothing, so a 30% deviation from this shows that in fact people who are clients here are prone to not smoke.

The children data is interesting as well because with the max age being 4 in the dataset, all children should be about 20% each assuming nothing, therefore for 0 to have 42% of the total clients in terms of children amount it is significant. This could imply the people who are clients to this service tend to not have children, but this may also be explained by the fact that most clients are 18, so many others could be very young as well and not have children yet which would explain this.

_____________________________________________________________________________"""