import urllib.request

def fetchincidents(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    print(data)

if __name__ == "__main__":
    fetchincidents("https://www.normanok.gov/sites/default/files/documents/2024-08/2024-08-02_daily_arrest_summary.pdf")