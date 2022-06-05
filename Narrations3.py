MostCommonDescription = """In this table, you can see the most prominent client attributes, the amount of times they appear in the dataset, 
the proportion of their amount compared to all others in the dataset (For age, 69 clients are 18, 69/1350 total clients is 0.05 of the total), 
and the proportion.

The most significant discoveries from this would most likely be smoker, age, BMI and children. 
I say this because Sex is 50/50, so for male to be 0.1% ,dominant isnt significant whatsover. 
There are 4 regions so each should have 25% ,or so clients, so 27% ,isnt too out of the curve, 
and charges has thousands of different values so you cant say one value is significant.

In terms of the more statistically significant ones, the fact that 80% ,of people are non smokers is interesting 
because there are two options, Yes/No making it 50/50 assuming nothing, so a 30%, deviation from this shows that in fact 
people who are clients here are prone to not smoke.

The children data is interesting as well because with the max age being 4 in the dataset, all children should be about 20% ,each assuming nothing, 
therefore for 0 to have 42% ,of the total clients in terms of children amount it is significant. 
This could imply the people who are clients to this service tend to not have children, but this may also 
be explained by the fact that most clients are 18, so many others could be very young as well and not have children yet which would explain this.

_____________________________________________________________________________"""

Proportions_Description = """The benefit of the following tables is not only that it gives a better picture of the
overall data instead of the only the highest occuring point, but also it divides the data into ranges, making for a better representation
of which group is more prominent. 

For instance, the Charges and BMI columns had thousands of different numbers, unique to the decimal! So to find the most occuring number wont show much
as all values are mostly unique. Having said this, by dividing our values into ranges as we have, we are able to have a more accurite picture of the data!

So what have we found here? Aside from the Categorical Values we already mentioned in the previous table (Smoker, Sex, Region), some other columns really 
shine hear such as the aforementioned Charges column. Now that we seperated it into ranges, and how many clients are inside each range, we are able to accurately
tell that almost 40%, of the clients pay the least amount of insurance, almost another 30%, pay for the second cheapest range, and the rest of the ranges pay less 
than 10%, decreasing the number each time more and more the more expensive the insurance is.

This might be because people cant afford higher and higher fees, or it might be because, most of them are healthy enough to pay cheaper fees, this is further 
illustrated by the fact that in the Age proportions, where almost all age ranges are about 10%, except for 18-23 which are the only ones above 10%, at 16%! This 
larger group of younger people would definitely drive some of the Charges to be cheaper for the younger Clients

The BMI on the other hand seems to be the only one who doesnt have a decreasing range scale, where instead it looks more like a normal curve, with little people
having the lowest BMI, then steadily increasing until it reaches its peak at BMI 28-32 with 26%, then a steady decrease again towards the end.

And lastly, for Children over 42%, dont have children with 25%, having 1 child. And like many other data tables, this one also has a rapid decline
with fewer and fewer clients having more children. This could be because of economic development, or for economic reasons in general. 

___________________________________________________________________________________________________________________________"""

Correlations_Description = """So here we have two types of correlation analysis. The first is a correlation between each possible
combination of columns. Is there a correlation between Age and BMI? Age and Number of Children? So on. The second is a correlation 
of a column with its own count, for instance, as the values of age increase, does the number of clients increase as well? And so on.

For the first correlation, perhaps the most significant observations are the following:
- The strongest postitive correlation is between Smoking and Charges, which is fairly obvious and doesnt require much explanation
- The second strongest correlation is a positive one which shows how Age is one of the (although weak) strongest correlations with 
how much someone is charged after smoking or not
- The last, and arguably relevant observation is the third strongest yet very weak correlation which shows how BMI plays a role but not
even close to the biggest role in how much someone is charged

For the Second and final correlation, here is what was found:
- According to this table and the previosly mentioned findings, people are likely to have no children in this clientel dataset, if they do, it
will most likely be one child, and every increase of another child is exponentially more unlikely than the previous one.
- Charges have a very strong negative correlation, indicating that the more expensive insurance is the less people have it. Again, this may be
because most people in this dataset are young, dont smoke, and are generally healthy so they pay less, but it could also be as simple as less people
are able to afford more expensive insurances, and oftentime extremelly expensive insurances are due to costly diseases that dont happen to every client
very often
-For Age as mentioned most clients are younger, and there is a small decrease in clients the older they are
-For BMI, as we saw, it is one of the only ones with a seemingly normal curve, and therefore has less of a linear and strong correlation than the rest.

___________________________________________________________________________________________________________________________"""

Regions_Categorical_Description = """For these more categorical attributes, we can see that even by separating them by their
respective regions, they all seem to have a highly similar value showing no statistically significant impact on the clients depending
on their region in terms of these categorical attributes.

___________________________________________________________________________________________________________________________"""

Regions_Numerical_Description = """Here we have an analysis of the nominal attributes in the dataset, but by seperating it into
the clients from each region. The reason this was made was because one of my goals was calculating correlation between attributes. 
And when doing that, I realized that with nominal and categorical dichotomous variables this is fairly simple to do. However, Categorical 
values that are not dichotomous are a bit more complicated to perform this calculation and could give very skewed projections and calculations.

It is for this reason that this entire section was created, it was a way to see if regions have an impact on all the other attributes.
Now that his was made, that can be answered, and here is what was found:

- Most Attributes seem to remain relatively constant and not change in between regions
- Two Attributes that seem to stand out a bit more than the others is Charges and Age
- It seems as if Easter regions have a large number of 18 year olds, then smaller, yet still large, ages after that, such as 7 20 year olds,
and 6 21 year olds compared to the 34 18 year olds. The same applies to Western regions but with 19 years olds, they have no 18 year olds but
have the same cluster of age group that Easter has with 18 year olds, but with 19 year olds having about 30 clients, and the following ages having
on average 7 - 6 per age following that.
- Also for Charges, Eastern Charges seem to be on average a slight bit more than Western Charges, almost $1000 more on average.

___________________________________________________________________________________________________________________________"""