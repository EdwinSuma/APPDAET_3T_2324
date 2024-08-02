import csv

browsers = []

with open("browsers.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        browser_name = row["Browser"]
        browser_platforms = row["Platforms"].split(",")
        browser_market_share = float(row["MarketShare"])


        browsers.append({
            "name": browser_name,
            "platforms": browser_platforms,
            "market_share": browser_market_share
        })


        print(f"Browser Name: {browser_name}")
        print(f"Browser Platforms: {browser_platforms}")
        print(f"Browser Market Share: {browser_market_share}")
        print("-" * 50)

        #add code here

        #end add code here

# 1 Print all browsers that run on windows
print("These browsers can be installed on Windows Machines: ")
for browser in browsers:
        if "Windows" in browser["platforms"]:
            print(browser["name"])

#add print statement here
print("-" * 50)
# 2 - Print all browsers that can only be ran on exactly one platform
print("These browsers can only be installed on one platform")
for browser in browsers:
    if len(browser["platforms"]) == 1:
        print(browser["name"])

# add print statement here


print("-" * 50)

# 3 - Print the browser with the highest MarketShare 
max_market_share_browser = max(browsers, key=lambda x: x["market_share"])
print("This browser has the most MarketShare: ")
print(max_market_share_browser["name"])

# add print statement here
print(f"Market Share: {max_market_share_browser['market_share']}%")