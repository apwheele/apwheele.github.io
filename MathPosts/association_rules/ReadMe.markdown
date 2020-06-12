# Association Rules

This code set conducts some association rules analysis using NIBRS data. The datasets are too large to post to GitHub. Here is a [dropbox link to the datasets](https://www.dropbox.com/sh/zlve3a4ck6jqfv1/AAA9XtFqb2SpTW4BwsAuV7Q4a?dl=0), or you can go to ICPSR and download the NIBRS data directly.

 - `00_AssocRules.py` preps the original NIBRS data, and has some functions to do one-hot encoding of repeated columns
 - `01_AssocRules.py` has a function to find the frequent itemsets (the `apriori` function in mlextend always ran out of memory for me, although my function maybe is slower and I don't know how well it will work with a very large number of columns either.
 
Link to ???blog post for further notes????