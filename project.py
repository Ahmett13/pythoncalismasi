print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔════════════════════════╗")
print("║       MAIN MENU        ║")
print("║1-CALCULATOR            ║")
print("║2-GAMES                 ║")
print("║3-ŞEKİL ÇİZDİRME        ║")
print("║4-TAKVİM                ║")
print("║5-RİTMİK SAYMA          ║")
print("║6-NOT HESAPLAMA         ║")
print("║7-ÇARPIM TABLOSU        ║")
print("║8-BMI HESAPLAMA         ║")
print("║9-DÖVİZ DURUMU          ║")
print("║10-ŞEKİL ALAN HESAPLAMA ║")
print("║11-EXIT (e)            ║")
print("║  Seçiminizi Yapınız    ║")
print("╚════════════════════════╝")
import calculator
import games.GamesMainMenu as ggm
choose = int(input("What is your choose?"))
if choose == 1:
    calculator.incalculator()
elif choose == 2:
    ggm.inGameMainMenu()
    