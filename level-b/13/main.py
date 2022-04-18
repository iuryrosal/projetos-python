from web_scraping import WebScraping

url = "https://www.airbnb.com.br/s/Fortaleza-~-CE/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Fortaleza%20-%20CE&place_id=ChIJL1zB9iFPxwcRqid5ywZnbf0&checkin=2022-05-09&checkout=2022-05-13&source=structured_search_input_header&search_type=autocomplete_click"
web_scraping = WebScraping(url)
print(web_scraping.pick_all_rooms())