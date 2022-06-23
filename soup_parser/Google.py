import re


def Google_urls(soup, debug = False):
    print("\nGoogle URLs")
    re_url = (
        "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )
    urls = []
    for i in soup.find_all(re.compile("^a"), href=True):
        url = re.findall(re_url, i["href"])
        if url:
            urls.append(url[0]) 
            if debug == True:
                print("--" * 20)
                print(url)

    return urls
