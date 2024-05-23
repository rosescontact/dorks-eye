from __future__ import print_function
try:
    from googlesearch import search
except ImportError:
    print("not found imports!!!")

import sys
import time
import requests
from bs4 import BeautifulSoup

print("Dorks Eye 2.0 - improved by rosescontact.")

try:
    data = input("\n[+] Do You Like To Save The Output In A File? (Y/N) ").strip()
    l0g = ""

except KeyboardInterrupt:
    print("\n")
    print("[!] User Interruption Detected..!")
    time.sleep(0.5)
    print("[!] I like to See Ya")
    time.sleep(0.5)
    sys.exit(1)

def logger(data):
    with open((l0g) + ".txt", "a") as file:
        file.write(str(data))
        file.write("\n")

if data.lower().startswith("y"):
    l0g = input("[~] Give The File a Name: ")
    print("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print("[!] Saving is Skipped...")
    print("\n" + "  " + "»" * 78 + "\n")

def dorks():
    try:
        dork = input("\n[+] Enter The Dork Search Query: ")
        amount = input("[+] Enter The Number Of Websites To Display: ")
        siteicerik = input("[+] Enter what to search for in the content of the site (js/content): ").lower()
        logger(dork + "\n")
        print("\n ")
        
        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            try:
                counter += 1
                icerik = requests.get(results)
                
                soup = BeautifulSoup(icerik.text, 'html.parser')
                links = soup.find_all('a', href=True) + soup.find_all('script', src=True)
                js_links = [link['href'] if link.name == 'a' else link['src'] for link in links if link.name == 'a' and link['href'].endswith('.js') or link.name == 'script' and link['src'].endswith('.js')]
                print("looking: " + str(results) + " | found js links: " + str(len(js_links)))

                for js_link in js_links:
                    if not js_link.startswith('http'):
                        js_link = requests.compat.urljoin(results, js_link)
                    js_response = requests.get(js_link)
                    if siteicerik in js_response.text.lower():
                        print("(FOUND IN JAVASCRIPT) [+] ", counter, results)
                        time.sleep(0.1)
                        requ += 1
                        if requ >= int(amount):
                            break

                        data = (counter, results)
                        logger(data)
                        time.sleep(0.1)
                        break
                else:
                    if siteicerik in icerik.text.lower():
                        print("(FOUND IN CONTENT) [+] ", counter, results)
                        time.sleep(0.1)
                        requ += 1
                        if requ >= int(amount):
                            break

                        data = (counter, results)
                        logger(data)
                        time.sleep(0.1)       
            except Exception as e:
                print(f"Error processing {results}: {e}")
                continue
        else:
            print("change the dork with this dork I did not find results.")        
    except KeyboardInterrupt:
        print("\n")
        print("[!] User Interruption Detected..!")
        time.sleep(0.5)
        print("\n[!] I like to See Ya")
        time.sleep(0.5)
        sys.exit(1)

if __name__ == "__main__":
    dorks()
