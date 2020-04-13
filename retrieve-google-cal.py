import os
import requests
import icalendar
from datetime import datetime, timedelta, timezone
from dateutil.rrule import *
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
URL = os.environ.get('ICAL_URL')

def parse_recurrences(recur_rule, start, exclusions):
    """ Find all reoccuring events """
    rules = rruleset()
    first_rule = rrulestr(recur_rule, dtstart=start)
    rules.rrule(first_rule)
    if not isinstance(exclusions, list):
        exclusions = [exclusions]
        for xdate in exclusions:
            try:
                rules.exdate(xdate.dts[0].dt)
            except AttributeError:
                pass
    now = datetime.now(timezone.utc)
    this_year = now + timedelta(days=60)
    dates = []
    for rule in rules.between(now, this_year):
        dates.append(rule)
    return dates

def parse_channel_id(description):
    try:
        soup = BeautifulSoup(description, 'html.parser')
        print(soup)
        link = soup.find('a').attrs['href']
        channel_id = link.split( 'channel/' )[1].split( '/' )[0].split( '?' )[0]
    except:
        channel_id = 'UCwxgo62w72LxZDA1fTibdYg'
    return channel_id



def main():
    """Saves Calendar data to file
    """
    c = requests.get(URL).text
    gcal = icalendar.Calendar.from_ical(c)
    for component in gcal.walk():
        if component.name == "VEVENT":
            summary = component.get('summary')
            if summary.startswith('@yalarm'):
                description = component.get('description')
                location = component.get('location')
                startdt = component.get('dtstart').dt
                enddt = component.get('dtend').dt
                exdate = component.get('exdate')
                channel_id = parse_channel_id(description)
                if component.get('rrule'):
                    reoccur = component.get('rrule').to_ical().decode('utf-8')
                    for start in parse_recurrences(reoccur, startdt, exdate):
                        utc = (start - start.utcoffset()).replace(tzinfo=timezone.utc)
                        print( utc, channel_id )
                else:
                    utc = (startdt - startdt.utcoffset()).replace(tzinfo=timezone.utc)
                    print( utc, channel_id )

if __name__ == '__main__':
    main()
