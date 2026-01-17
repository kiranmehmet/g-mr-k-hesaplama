import os

def dukkani_tara():
    # Bu nokta (.) botun olduğu her yere bakmasını sağlar
    sayac = 0
    print("\n--- DÜKKANIN HER YERİNE BAKILIYOR ---")
    
    for kok, klasorler, dosyalar in os.walk('.'):
        for dosya in dosyalar:
            if dosya.endswith(('.pdf', '.xlsx', '.xls')):
                sayac += 1
                print(f"{sayac}. Bulundu: {dosya}")
                
    print(f"\nBOT: Abi toplam {sayac} tane kaynak (PDF/Excel) buldum. Hepsine hakimim!")

dukkani_tara()