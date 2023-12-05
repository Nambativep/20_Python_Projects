# site connectivity check up
# we give it a URL and the URL check the status of that site
# to know if the site or is up and if we can access the site

# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url
# return a response

import urllib.request as urllib


def main(url):
    print("checking connecting ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("the response code was: ", response.getcode())


print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)




