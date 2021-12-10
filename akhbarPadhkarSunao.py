# pip install pywin3e2

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests, json
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=fd3afd807e7745329cb1785e2f360e30"
    r = requests.get(url)
    parsed = json.loads(r.text)
    a = parsed["articles"][:5]
    for i in a:
        print(i["title"].split("-")[0:2])
        speak(i["title"])