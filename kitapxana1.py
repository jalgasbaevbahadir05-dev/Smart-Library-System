# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 01:12:35 2026

@author: Bahadir
"""
kitoblar = {"O'tkan kunlar": "mavjud", "Hamsa": "mavjud", "Sariq devni minib": "mavjud"}
while True:
    try:
        amal=int(input("Qaysi amalni bajarmoqchisiz?\n1-kitobni olish,\n2-kitobni qaytarish,\n3-hamma kitoblar,\n4-chiqish\n"))
        if amal==1:
            nom=input("Qaysi kitobni olmoqchisiz?\n")
            nom=nom.title()
            if nom in kitoblar:
                if kitoblar[nom]=="mavjud":
                    kitoblar[nom]="olingan"
                    print(f"Marhamat {nom} kitobini olishingiz mumkin")
                else:
                    print(f"Kechirasiz {nom} kitobi mavjud emas")
            else:
                print(f"Kechirasiz bizda {nom} kitobi sotilmaydi")
        elif amal==2:
            if nom in kitoblar:
                nom=input("Qaysi kitobni javonga qaytarmoqchisiz?\n")
                kitoblar[nom]="mavjud"
                print(f"Rahmat, {nom} kitobi javonga qo'yildi")
            else:
                print("Kitobxonamizda bunday nomdagi kitob sotilmaydi.")
        elif amal==3:
            print(f"Quyida kitobxonamizdagi kitoblar haqida ma'lumotlar:\n{kitoblar}")
        elif amal==4:
            print("Tashrifingizdan mamnunmiz, xayr")
            break
    except ValueError:
        print("Iltimos, faqat mavjud xizmat sonlaridan biri va kitob nomi to'g'ri yozilganligiga e'tibor bering!")
        
    