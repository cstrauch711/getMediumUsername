# getMediumUsername
This program takes in a full name and an optional company name to search the web and return a medium profile username if one exists. The program returns False if it is unable to find a matching Medium profile

The program requiries the following modules:
1) requests (to get the web page using the requested url)
2) BeautifulSoup (to scrape the returned html text and find the correct links)
3) urllib.parse (to format the the parameteters into a query format)

The program requires a full name (sepeated by a space) in the first string parameter on line 48 where the function is called. The second string paramter on line 48 to call the fucntion is for the company name, but that is optional and must be left as a blank string if not being used.

