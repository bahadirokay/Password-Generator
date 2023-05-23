import string
import random

language = input(str("Please choose language. 'en' for English or 'tr' for Turkish\n"
                     "Lütfen dil seçiniz. İngilizce için 'en' ya da Türkçe için 'tr' değerlerini "
                     "giriniz.")).lower()

letter_list = string.ascii_letters
low_letter_list = string.ascii_lowercase
upper_letter_list = string.ascii_uppercase
number_list = string.digits
symbol_list = string.punctuation
all_list = low_letter_list + symbol_list + number_list + upper_letter_list

def turkish():
    password_list = []
    new_password_list = ("")
    mix = [random.choice(low_letter_list), random.choice(upper_letter_list), random.choice(symbol_list)]
    ask_char = input("Şifrenizde sayı, sembol, harfleri ayrı ayrı basamakla sayılarını bildirmek"
                     " ister misiniz? 'E' ya da 'H':").lower()
    if ask_char == "e":
        letter = input("Lütfen şifrenizin içerisinde kaç adet harf olmasını istediğinizi giriniz.")
        symbol = input("Lütfen kaç adet sembol olmasını istediğini giriniz.")
        number = input("Lütfen kaç adet rakam olmasını istediğinizi giriniz.")
        for a in range(1, int(letter)+1):
            password_list.append(random.choice(letter_list))
        for b in range(1, int(symbol)+1):
            password_list.append(random.choice(symbol_list))
        for c in range(1, int(number)+1):
            password_list.append(random.choice(number_list))
        for d in range(1, len(password_list)+1):
            len_list = (random.randint(0, len(password_list)-1))
            new_char = password_list.pop(len_list)
            new_password_list += (new_char)
        print(f"Şifreniz oluşturulmuştur: {new_password_list}")
    elif ask_char == "h":
        number_of_char = input("Lütfen şifrenizin kaç karekter olmasını istediğini söyleğiniz.")
        for a in range(1, int(number_of_char)-2):
            new_password_list += (random.choice(all_list))
        for b in range(1, 4):
            len_mix = (random.randint(0, len(mix)-1))
            new_char = mix.pop(len_mix)
            new_password_list += (new_char)
        print(f"Şifreniz oluşturulmuştur: {new_password_list}")

def english():
    password_list = []
    new_password_list = ("")
    mix = [random.choice(low_letter_list), random.choice(upper_letter_list), random.choice(symbol_list)]
    ask_char = input("Would you like to report numbers, symbols, letters separately and digits in "
                     "your password? 'Y' or 'N':").lower()
    if ask_char == "y":
        letter = input("Please enter how many letters you want your password to contain.")
        symbol = input("Please enter how many symbols you want.")
        number = input("Please enter how many digits you want.")
        for a in range(1, int(letter)+1):
            password_list.append(random.choice(letter_list))
        for b in range(1, int(symbol)+1):
            password_list.append(random.choice(symbol_list))
        for c in range(1, int(number)+1):
            password_list.append(random.choice(number_list))
        for d in range(1, len(password_list)+1):
            len_list = (random.randint(0, len(password_list)-1))
            new_char = password_list.pop(len_list)
            new_password_list += (new_char)
        print(f"Your new password is: {new_password_list}")
    elif ask_char == "n":
        number_of_char = input("Please tell how many characters you want your password to be.")
        for a in range(1, int(number_of_char)-2):
            new_password_list += (random.choice(all_list))
        for b in range(1, 4):
            len_mix = (random.randint(0, len(mix)-1))
            new_char = mix.pop(len_mix)
            new_password_list += (new_char)
        print(f"Your new password is: {new_password_list}")

if language == "tr":
    turkish()
elif english() == "en":
    english()
