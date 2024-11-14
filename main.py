for i in range(5):
    meme_dict = {
                "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
                "LOL": "Una risposta comune a qualcosa di divertente",
                "SHEESH": "Leggera disapprovazione",
                "CREEPY": "Spaventoso, Inquietante",
                "PARA": "Preoccuparsi per qualcosa, paranoiarsi"
                }
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
    if parola in meme_dict.keys():
        print(meme_dict.keys())
    else:
        print("Mi dispiace ma la parola non è presente sul dizionario.")
