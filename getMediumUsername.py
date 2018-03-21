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

    #Parses through all the returned links in soup and search for the right link that contains the correct medium profile
    for s in soup.find_all('h3'):
        string = str(s.contents)
        #if the link is not a medium webiste, skip to next link
        if 'https://medium.com/' not in string or '&amp' not in string:
            continue
        else:
            #Checks to see if string contains the first and last name of the person in. Returns None if all are not present
            for n in contactName.split(' '):
                if string.find(n) == -1:
                    print(string)
                    return None
                else:
                    continue
            url = string[string.find('https://medium.com/'):string.find('&amp')]#shortening the returned link to a link that will work when used
            username = url[url.find('%40')+3:len(url)]#use the url to get the username and return that
            #the following if statements remove the extensions that are sometimes present in the returned username url from the search
            if '/followers' in username:
                username = username.replace('/followers','')
            if '/following' in username:
                username = username.replace('/following','')
            if '/latest' in username:
                username = username.replace('/latest','')
            if '/has-recommended' in username:
                username = username.replace('/has-recommended','')
            if '/highlight' in username:
                username = username.replace('/highlights','')
            return(username)

#Call the function to return a usernamel of the person's medium profile.
print( getMediumUsername( '' ) )


