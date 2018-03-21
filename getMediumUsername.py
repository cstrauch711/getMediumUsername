import requests
import urllib.parse
from bs4 import BeautifulSoup

def getMediumUsername(contactName):
    #If the contactName field is blank or does not contain a first and last name, it returns false
    if contactName is None or contactName=="" or " " not in contactName:
        return False

    #Creates the Google search query for a medium and the contactName
    query = 'https://www.google.com/search?q=medium+' + urllib.parse.quote( contactName.replace(' ','+') )

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
        #continues to next link if link does not contain a medium website
        if str(s.contents).find('/url?q=https://medium.com/') == -1 or str(s.contents).find('&amp') == -1:
            continue
        #continues to next link if the first AND last name are not within the url as well
        for n in contactName.split(' '):
            if str(s.contents).find(n) == -1:
                continue

        #searching for the right link that contains the correct medium profile
        if( 'https://medium.com/' in str(s.contents) ):
            string = str(s.contents)
            url = string[string.find('https://medium.com/'):string.find('&amp')]#shortening the returned link to a link that will work when used
            #use the url to get the username and return that
            username = url[url.find('%40')+3:len(url)]
            #the three if statements remove the extensions that are sometimes present in the returned username url from the search
            if '/followers' in username:
                username = username.replace('/followers','')
            if '/following' in username:
                username = username.replace('/following','')
            if '/latest' in username:
                username = username.replace('/latest','')
            if '/has-recommended' in username:
                username = username.replace('/has-recommended','')
            return(username)

#Call the function to return a usernamel of the person's medium profile.
print( getMediumUsername( '' ) )
