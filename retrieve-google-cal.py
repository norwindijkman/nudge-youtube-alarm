import os
import requests
from ics import Calendar
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
URL = os.environ.get('ICAL_URL')

def main():
    """Saves Calendar data to file
    """
    c = Calendar(requests.get(URL).text)
    events = [ i for i in c.events if i.name.startswith('@yalarm') ]
    for event in events:
        start = event.begin.datetime
        description = event.description
        try:
            soup = BeautifulSoup(description, parser='html5lib')
            link = soup.find('a').attrs['href']
            channel_id = link.split( 'channel/' )[1].split( '/' )[0].split( '?' )[0]
        except:
            channel_id = 'UCwxgo62w72LxZDA1fTibdYg'
        print( start, channel_id )

if __name__ == '__main__':
    main()
