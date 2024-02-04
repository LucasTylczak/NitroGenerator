import requests
import time

print("""

     

     

      

 ██████   █████  ███   █████                         █████████                                                    █████                      
░░██████ ░░███  ░░░   ░░███                         ███░░░░░███                                                  ░░███                       
 ░███░███ ░███  ████  ███████   ████████   ██████  ███     ░░░   ██████  ████████    ██████  ████████   ██████   ███████    ██████  ████████ 
 ░███░░███░███ ░░███ ░░░███░   ░░███░░███ ███░░███░███          ███░░███░░███░░███  ███░░███░░███░░███ ░░░░░███ ░░░███░    ███░░███░░███░░███
 ░███ ░░██████  ░███   ░███     ░███ ░░░ ░███ ░███░███    █████░███████  ░███ ░███ ░███████  ░███ ░░░   ███████   ░███    ░███ ░███ ░███ ░░░ 
 ░███  ░░█████  ░███   ░███ ███ ░███     ░███ ░███░░███  ░░███ ░███░░░   ░███ ░███ ░███░░░   ░███      ███░░███   ░███ ███░███ ░███ ░███     
 █████  ░░█████ █████  ░░█████  █████    ░░██████  ░░█████████ ░░██████  ████ █████░░██████  █████    ░░████████  ░░█████ ░░██████  █████    
░░░░░    ░░░░░ ░░░░░    ░░░░░  ░░░░░      ░░░░░░    ░░░░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░      ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░     

                                                                                                                                             

                                                                                                                                             

                                                                                                                                             

╔═══════════════════════╦══════════════════════════╦═══════════════════════╗
║  Dev : LucasTylczak   ║  Info  : NitroGenerator  ║  Programm  : Python   ║
╚═══════════════════════╩══════════════════════════╩═══════════════════════╝







""")

time.sleep(0.1)

url = "https://api.discord.gx.games/v1/direct-fulfillment"

# Demander à l'utilisateur d'entrer la valeur

partner_user_id = input("Entrez la valeur de partnerUserId : ")

headers = {

    "authority": "api.discord.gx.games",
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "origin": "https://www.opera.com",
    "referer": "https://www.opera.com/",
    "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
}

data = {"partnerUserId": partner_user_id}

response = requests.post(url, headers=headers, json=data)

# Extraire le jeton de la réponse

token = response.json().get("token")

if token:

    # Ajouter le jeton à l'URL
    url_avec_token = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"

    print("")
    print(f"Token: {token}")
    print("")
    print(f"URL avec Token: {url_avec_token}")

    # Vous pouvez ouvrir l'URL dans un navigateur ou l'utiliser selon vos besoins
else:
    print("Erreur : Impossible d'extraire le jeton de la réponse.")



