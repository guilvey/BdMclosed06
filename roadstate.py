import bs4
import requests



def main():
    urlinforoute06 = "http://www.inforoutes06.fr/fr/"
    r = requests.get(urlinforoute06)

    html_raw = r.text.lower();

    if ("6098" in html_raw) and ("antibes" in html_raw):
        print("route fermee")
    else:
        print("route ouverte")

    


if __name__ == '__main__':
    main()