import requests
import urllib.parse
from bs4 import BeautifulSoup

def getMediumUsername(contactName, companyName):
    #If the contactName field is blank or does not contain a first and last name, it returns false
    if contactName is None or contactName=="" or " " not in contactName:
        return False

    #Creates the Google search query for a medium and the contactName
    query = 'https://www.google.com/search?q=medium+' + urllib.parse.quote( contactName.replace(' ','+') )
    #This will add the companyName to the search query if given, query will stil be created if no companyName is given
    if companyName != '':
        query += "+" + urllib.parse.quote( companyName.replace(' ','+') )

    #This is the request for the google search query and returns the html text of the requested google search page
    try:
        response = requests.get( query )
        r = response.text
    except:
        return False

    #initializing the BeautifulSoup data scraper to parse through the returned html text
    soup = BeautifulSoup( r, 'html.parser' )
    #Using BeautifulSoup to find the returned web links in the google search page text. Returns false if page contains no web links
    if str(soup).find('<h3 class="r"') == -1:
        return False

    #Parses through all the returned links in soup
    for s in soup.find_all('h3'):
        #returns false if no links contain a medium website
        if s.find('/url?q=https://medium.com/') == -1 or s.find('&amp') == -1:
            return False
        #returns false if the first AND last name are not within the url as well
        for n in contactName.split(' '):
            if s.find(n) == -1:
                return False

        #searching for the right link that contains the correct medium profile
        if( 'https://medium.com/' in str(s.contents) ):
            string = str(s.contents)
            url = string[string.find('https://medium.com/'):string.find('&amp')]#shortening the returned link to a link that will work when used
            #use the url to get the username and return that
            username = url[url.find('%40')+3:len(url)]
            return(username)

#Call the function to return a usernamel of the person's medium profile. Including a company will yield a better chance of finding the correct profile, but it is not necessary
getMediumUsername( '','')
