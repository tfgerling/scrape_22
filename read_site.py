#!/usr/bin/env python

def antiques_scrape():
    import pandas as pd
    import requests
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    url = 'https://www.craigslist.org/about/sites'

    # get page response
    response = requests.get(url)

    browser.visit(url)
    browser.links.find_by_partial_href('//columbiamo').click()
    browser.links.find_by_partial_href('/search/ata').click()

    antiques_results = []
    for i in range(1, 51):

        try:
            item_name = browser.find_by_xpath(
                f'/html/body/section/form/div[4]/ul/li[{i}]/div/h3/a').text
            item_price = browser.find_by_xpath(
                f'/html/body/section/form/div[4]/ul/li[{i}]/a').text
            location = browser.find_by_xpath(
                f'//*[@id="search-results"]/li[{i}]/div/span[2]/span[2]').text.replace('(', '').replace(')', '')
            date_added = browser.find_by_xpath(
                f'/html/body/section/form/div[4]/ul/li[{i}]/div/time')['datetime']
            data_id = browser.find_by_xpath(
                f'/html/body/section/form/div[4]/ul/li[{i}]/div/h3/a')['data-id']
            antique_dict = {'id': data_id,
                            'name': item_name,
                            'price': item_price,
                            'loc': location,
                            'date_add': date_added}
            antiques_results.append(antique_dict)

        except AttributeError as e:
            print(e)

    df = pd.DataFrame(antiques_results)
    df.to_csv('antiques_cl.csv', index=False)
    # return df
    return antique_dict
