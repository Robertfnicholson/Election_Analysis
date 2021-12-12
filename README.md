# PyPoll Challenge

## Overview of Project

Tom, a Colorado Board of Elections employee, requested my assistance in an election audit of the 
tabulated results of the U.S. Congressional precinct in Colorado. I was tasked with reporting the total 
number of votes cast, the total number of votes for each candidate, the percentage of votes for each 
candidate, the winner of the election based on the popular vote, the voter turnout for each county, the 
percentage of votes from each county of the total count and the county with the highest voter turnout. I 
used Python to automate the process and the resulting code could be used to audit not only other 
congressional districts but also senatorial districts and local elections. </p>

## Election-Audit Results:
The Election-Audit results were generated using Python code. The results are as follows:

* Total votes cast in the election was 369,711.
* The county votes were as follows: 
	* Jefferson, 10.5% (38,855); 
	* Denver: 82.8% (306,055), and 
	* Arapahoe: 6.7% (24,801).
* The largest county turnout was Denver.
* Charles Casper Stockham received 85,213 votes or 23.0%.
* Diana DeGette received 272,892 votes or 73.8%.
* Raymon Anthony Doane received 11,606 votes or 3.1%.
* The election winner was Diana DeGette.
* Her winning vote count was 272,892.
* Her winning vote percentage was 73.8%.

We used a for loop in our code to loop through each row of the election_results.csv file and added a total 
vote counter and variables to count the votes from each county and from each candidate. See screenshot of code 
below.

![Python_code1.png](https://github.com/Robertfnicholson/Election_Analysis/blob/52f527b63c3f00d7483a2d7cccfd31866b084680/Python_code1.png)
</p>

## Challenges
We encountered a series of challenges in developing the code. This included not having the correct conditional 
statement. We found source code in GitHub from an earlier class student who dropped the "and" condition to 
determine the largest county turnout, resulting in the following code:

![Python_code2.png](https://github.com/Robertfnicholson/Election_Analysis/blob/52f527b63c3f00d7483a2d7cccfd31866b084680/Python_code2.png)
</p>

## Election-Audit Summary
Tom and I successfully built and implemented Python code that automated an election audit, converting 
a manual Excel process into a repeatable process. I propose that the Election Commission authorize the 
use of our code to audit other congressional districts and senatorial districts and local elections. The 
code can be modified to be used for other elections. This would include changing the breakdown by 
counties to a breakdown required for senatorial districts and for local elections. This would also include 
changing the code to allow for the opening and reading of csv files that would contain the data for the 
other elections.</p>

