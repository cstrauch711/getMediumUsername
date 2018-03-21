# getMediumUsername
This program takes in a full name to search the web and return a medium profile username if one exists. The program returns None if it is unable to find a matching Medium profile

The program requiries the following modules:
1) requests (to get the web page using the requested url)
2) BeautifulSoup (to scrape the returned html text and find the correct links)
3) urllib.parse (to format the the parameteters into a query format)

The program requires a full name (sepeated by a space) in the string parameter on line 55 where the function is called. 

