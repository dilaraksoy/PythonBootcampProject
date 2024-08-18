import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_joker(player_wins, opponent_wins, jokers_used, player_num):
    if opponent_wins > 0 and not jokers_used:
        joker_choice = input(f"{player_num}. Oyuncu, bir joker kullanmak ister misiniz? (1. Geçmişe Dön / 2. Hayır): ").strip()
        return joker_choice
    else:
        return "2"  # Joker kullanımı mümkün değilse "Hayır" seçeneğini döndür

def tas_kagit_makas_DILARA_AKSOY():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Kurallar basit: Taş makası yener, Makas kağıdı yener, Kağıt taşı yener.")
    print("Oyunu kazanmak için ilk iki turu kazanın. İyi şanslar!")
    print("\nJokerler:")
    print("1. Geçmişe Dön: Bu joker, bir önceki turun sonucunu geçersiz kılar ve rakibin bir puanını siler.")
    print("2. Hayır: Joker kullanmak istemiyorum.")

    mode = input("Oyun modunu seçin:\n1. İki kişi\n2. Tek kişi\nSeçiminizi yapın (1 veya 2): ")

    if mode not in ["1", "2"]:
        print("Geçersiz seçim! Oyun sonlandırılıyor.")
        return

    choices = ["taş", "kağıt", "makas"]

    while True:
        player1_wins = 0
        player2_wins = 0
        jokers_used = {"player1": False, "player2": False}

        while player1_wins < 2 and player2_wins < 2:
            print("\n1. Taş\n2. Kağıt\n3. Makas")

            # 1. oyuncunun joker seçimi
            joker_choice = choose_joker(player1_wins, player2_wins, jokers_used["player1"], 1)
            if joker_choice == "1":
                jokers_used["player1"] = True
                player2_wins = max(0, player2_wins - 1)
                print("Geçmişe Dön jokeri kullanıldı. Rakibin bir puanı silindi!")
                clear_screen()
                continue

            player1_choice = input("1. Oyuncu - Seçiminizi yapın (1, 2, 3): ")
            if player1_choice not in ["1", "2", "3"]:
                print("Geçersiz seçim, lütfen tekrar deneyin.")
                continue
            player1_choice = choices[int(player1_choice) - 1]

            clear_screen()

            if mode == "2":
                player2_choice = random.choice(choices)
                print(f"Bilgisayarın seçimi: {player2_choice}")
            else:
                # 2. oyuncunun joker seçimi
                joker_choice = choose_joker(player2_wins, player1_wins, jokers_used["player2"], 2)
                if joker_choice == "1":
                    jokers_used["player2"] = True
                    player1_wins = max(0, player1_wins - 1)
                    print("Geçmişe Dön jokeri kullanıldı. Rakibin bir puanı silindi!")
                    clear_screen()
                    continue

                player2_choice = input("2. Oyuncu - Seçiminizi yapın (1, 2, 3): ")
                if player2_choice not in ["1", "2", "3"]:
                    print("Geçersiz seçim, lütfen tekrar deneyin.")
                    continue
                player2_choice = choices[int(player2_choice) - 1]

            print(f"1. Oyuncunun seçimi: {player1_choice}")
            print(f"2. Oyuncunun seçimi: {player2_choice}" if mode == "1" else f"Bilgisayarın seçimi: {player2_choice}")

            if (player1_choice == "taş" and player2_choice == "makas") or \
               (player1_choice == "kağıt" and player2_choice == "taş") or \
               (player1_choice == "makas" and player2_choice == "kağıt"):
                print("1. Oyuncu bu turu kazandı!")
                player1_wins += 1
            elif player1_choice == player2_choice:
                print("Berabere!")
            else:
                print("2. Oyuncu bu turu kazandı!" if mode == "1" else "Bilgisayar bu turu kazandı!")
                player2_wins += 1

            print(f"Skor: 1. Oyuncu {player1_wins} - {'2. Oyuncu' if mode == '1' else 'Bilgisayar'} {player2_wins}")

        if player1_wins == 2:
            print("Tebrikler, 1. Oyuncu oyunu kazandı!")
        else:
            print("2. Oyuncu oyunu kazandı!" if mode == "1" else "Bilgisayar oyunu kazandı!")

        play_again = input("Başka bir oyun oynamak ister misiniz? (1. Evet / 2. Hayır): ").lower()
        if play_again != "1":
            print("Oyun sona erdi. Teşekkürler!")
            break

tas_kagit_makas_DILARA_AKSOY()
