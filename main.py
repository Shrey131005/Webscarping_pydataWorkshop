from bs4 import BeautifulSoup
with open('index.html','r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content,'lxml' )  #BeautifulSoup(content to be scraped, "lxml"library to easily use html and xml data  )
    #print(soup.prettify())

    event_tags =soup.find_all('h5')
    #print(event_tags)

    # for event in event_tags:
    #     print(event.text)

    event_cards = soup.find_all('div',class_ = 'card')
    for event in event_cards:
        #print(event.a)
        event_name = event.h5.text
        #print(event_name)

        event_prize = event.a.text
        # print(event_prize)

        print(f'{event_name} is worth {event_prize}')