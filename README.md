# Web_Scraping_mars_data
**MODULE 10**

**Web Scraping Mars data**

**Overview**

In this challenge, we are trying to scrap the web page:

https://marshemispheres.com/

1. Using Splinter and Beautiful soup we are scraping the web page to retrieve the image URLs and image title.
2. Using python, we created the functions for different websites from where we are scrapping the data using Splinter and Beautiful soup. And encapsulate them into one function scrape\_all().
3. Then, we used Flask to create connection with Mongodb. And created the routes for home page and /scrape page.

We have two methods here:

- find\_one() which will retrieve data from Mongodb and display on our index.html page. This will work for Home page. So Home page will always show what we already have in the Mongodb collection.
- Update\_One=True, if we have new data after scraping it will modify the MongoDB and our index.html will also modified with most updated information.

4. In the index.html page, we created a button to trigger the scrape route(/scrape), which will scrape the data and provide us the most updated information in the data in Mongodb and index.html page.

![MongoDB data](https://github.com/AditiOracle/Web_Scraping_mars_data/blob/main/Resources/Mongo_db_image.PNG)
![Responsive Webpage](https://github.com/AditiOracle/Web_Scraping_mars_data/blob/main/Resources/Responsive_web_page.PNG)
