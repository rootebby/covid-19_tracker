import time
from covid import Covid



print("""
**********************
Ülkeler : 
**********************
1. Türkiye
**********************
2. Amerika
**********************
3. Almanya 
**********************
4. İtalya
**********************
5. Çin
**********************
6. Brezilya
**********************
7. Hindistan
**********************
8. İngiltere
**********************
9. Fransa
**********************
10.İspanya  
**********************
98.Ülkeleri Tekrar Gör
**********************
99.Yapımcı ve İletişim
**********************
""")


covid = Covid()

while True:
    ülke = int(input("Seçenek : "))

    if ülke == 1:

        cases = covid.get_status_by_country_name("turkey")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 2:

        cases = covid.get_status_by_country_name("us")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 3:

        cases = covid.get_status_by_country_name("germany")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 4:

        cases = covid.get_status_by_country_name("italy")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 5:

        cases = covid.get_status_by_country_name("china")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 6:

        cases = covid.get_status_by_country_name("brazil")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 7:

        cases = covid.get_status_by_country_name("india")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 8:

        cases = covid.get_status_by_country_name("UNITED KINGDOM")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 9:

        cases = covid.get_status_by_country_name("france")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 10:

        cases = covid.get_status_by_country_name("spain")
        for x in cases:
            print(x,":",cases[x])

    elif ülke == 98:

        print("""
**********************
Ülkeler : 
**********************
1. Türkiye
**********************
2. Amerika
**********************
3. Almanya 
**********************
4. İtalya
**********************
5. Çin
**********************
6. Brezilya
**********************
7. Hindistan
**********************
8. İngiltere
**********************
9. Fransa
**********************
10.İspanya  
**********************
98.Ülkeleri Tekrar Gör
**********************
99.Yapımcı ve İletişim
**********************
""")

    elif ülke == 99:
        time.sleep(1)
        print("Bilgiler Derleniyor .")
        time.sleep(1)
        print("Bilgiler Derleniyor ..")
        time.sleep(1)
        print("Bilgiler Derleniyor ...")
        time.sleep(1)
        print("""
   ▄████████  ▄██████▄   ▄██████▄      ███             ▄████████ ▀█████████▄  ▀█████████▄  ▄██   ▄   
  ███    ███ ███    ███ ███    ███ ▀█████████▄        ███    ███   ███    ███   ███    ███ ███   ██▄ 
  ███    ███ ███    ███ ███    ███    ▀███▀▀██        ███    █▀    ███    ███   ███    ███ ███▄▄▄███ 
 ▄███▄▄▄▄██▀ ███    ███ ███    ███     ███   ▀       ▄███▄▄▄      ▄███▄▄▄██▀   ▄███▄▄▄██▀  ▀▀▀▀▀▀███ 
▀▀███▀▀▀▀▀   ███    ███ ███    ███     ███          ▀▀███▀▀▀     ▀▀███▀▀▀██▄  ▀▀███▀▀▀██▄  ▄██   ███ 
▀███████████ ███    ███ ███    ███     ███            ███    █▄    ███    ██▄   ███    ██▄ ███   ███ 
  ███    ███ ███    ███ ███    ███     ███            ███    ███   ███    ███   ███    ███ ███   ███ 
  ███    ███  ▀██████▀   ▀██████▀     ▄████▀          ██████████ ▄█████████▀  ▄█████████▀   ▀█████▀  
  ███    ███                                                                                                """)
        time.sleep(2)
        print("coded by root@ebby:~#")
        time.sleep(1)
        print("İnstagram : emirkan_esme")
        time.sleep(1)
        print("Mail : 2003emirkanesme@gmail.com")
        time.sleep(1)

    else:

        print("Geçersiz Seçenek !!!")