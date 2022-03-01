# Week 22 Homework

## Work to be completed
1. Create a python function to scrape Yelp data for 50 restaurants close to you OR Craigslist for the top 50 items of any topic interesting to you. Think about what data you want to scrape aside from the name and location. You must pick at least three other fields. You can use beautiful soup, selenium, scrapy, and/or splinter as possible.
    - I chose Craigslist, then programmatically selected my area (Columbia/Jeff City), followed by selecting Antiques. 
    - Once there, I grabbed the top 50 listings, pulling out the id, name, price, location and date added to Craigslist. 
    - I set this up in a jupyter notebook first, then used VSCode (function is called read_site).

2. Create a local API that calls your scrape function and stores the data when you call /scrape endpoint. The data you scrape should be viewable when you go to /all .
    - I created local API scrape_craigslist.py that has 2 endpoints - /all and /scrape. 
    - I also included instructions that tell you to use /scrape first. 
    - I kept getting a type error returning from my function when trying to pass back a DataFrame. I ended up writing to a csv file in the function and then reading it in during the /all endpoint.

3. What is web scraping? Web scraping is technique used for retrieving and parsing information stored on the internet. Why is it helpful? It is used in research, marketing, redirecting customers, among other things. It allows companies to be more efficient, target clients with items/ads for items that searching history indicates they are interested in. What does it mean for your online presence? Personally, I think you should be careful with what you do online if you don't want these ads directed at you. Reference the readings and DataCamp.

### Notebook
I created a notebook as well to try out logic from before setting it up in VSCode. 

### DataCamp
![image](https://user-images.githubusercontent.com/49694526/155915932-cb361ba1-cb64-4a51-9565-6d5fccd1c6a4.PNG)

![mongo-first](https://user-images.githubusercontent.com/49694526/156098245-d636da63-bd82-4094-826f-1e49c319b13a.PNG)
