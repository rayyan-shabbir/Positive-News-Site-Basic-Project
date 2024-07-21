import requests
from send_email import send_email

topic = "tesla"
api_key = "07a071fd4b394cfca644f81d22ac97c6"
url = f"https://newsapi.org/v2/everything?q={tesla}&from=2024-06-21&sortBy=publishedAt&apiKey=07a071fd4b394cfca644f81d22ac97c6&language=en"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)