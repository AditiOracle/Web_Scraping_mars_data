# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    # Set up Splinter 
    # Initiate headless driver for deployment
    executable_path = {'executable_path': "chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=True)
    
    
    #Next, we're going to set our news title and paragraph variables (remember, this function will return two values).
    #This line of code tells Python that we'll be using our mars_news function to pull this data.
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data={
        "news_title":news_title,
        "news_paragraph":news_paragraph,
        "featured_image":featured_image(browser),
        "facts":mars_facts(),
        "last_modified":dt.datetime.now(),
        "hemispheres":img_title(browser)
    }
    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
   
   # Scrape Mars News
   # Visit the mars nasa news site
   url = 'https://redplanetscience.com/'
   browser.visit(url)

   # Optional delay for loading the page
   browser.is_element_present_by_css('div.list_text', wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')
   try: 
    slide_elem = news_soup.select_one('div.list_text')
    #slide_elem.find('div', class_='content_title')

    # Use the parent element to find the first <a> tag and save it as  `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()
   

    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
   except AttributeError:
    return None, None

   return news_title, news_p 


#JPL Space Images Featured Image
def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    try:
        # find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

#Mars Facts

def mars_facts():

    try:
        # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
        #print(df)
    except BaseException:
        return None

    # Assign columns and set index of dataframe    
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstap
    return df.to_html(classes="table table-striped")
    #return df.to_html()

def img_title(browser):

    #Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    

    html=browser.html
    soup_img=soup(html,"html.parser")

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.

    results=browser.find_by_css("a.product-item img")
    for i in range(len(results)):
        hemisphere={}
        browser.find_by_css("a.product-item img")[i].click()
        hemisphere["img_url"]=browser.find_by_text("Sample")["href"]
        hemisphere["title"]=browser.find_by_css("h2.title").text
        hemisphere_image_urls.append(hemisphere)
        browser.back()

    return hemisphere_image_urls
    
        
    

if __name__=="__main__":
    # If running as script, print scraped data
    print(scrape_all())
