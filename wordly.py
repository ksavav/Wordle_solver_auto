from words import words
from getColors import getColors
from getScreen import getScreen
import keyboard
import time

yellow_list = []
yellow = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": []
}
green = ['-', '-', '-', '-', '-']
used_letters = []

def word_creator():
    for item in words:
        i = 0
        counter = 0

        for letter in item[0]:
            if letter in used_letters:
                if (letter in yellow_list and counter == 0) or (letter in green and counter == 0): counter = 1
                else: break

            if green[i] != '-' and letter != green[i]: break
            
            if letter in yellow[str(i+1)]: break
            i += 1

        if i == 5:
            temp_y = yellow_list.copy()

            for l in yellow_list:
                for x in item[0]:
                    if x == l: 
                        try:
                            temp_y.remove(l)
                        except:
                            True
            
            if len(temp_y) == 0:
                print(f"Try this: {item}")
                break

def main():
    print("Welcome to 'Wordly solver'! The program will automatically check the word you typed on the Wordly website.\nAfter a few seconds in the terminal output, you will see the next best word to type.\n\n")

    counter = 0

    text_from_image = getScreen()
    colors_from_image = getColors()

    while 1:
        keyboard.wait('enter')
        time.sleep(2)

        text = text_from_image.manager()
        colors = colors_from_image.colorsFromImage()

        current_word = text[str(counter + 1)]
        

        j = 0
        for letter in current_word:
            if(green[j] == '-'):
                temp_color = colors[str(counter + 1)][j]
                
                if temp_color == [83, 141, 78]: green[j] = letter

                elif temp_color == [181, 159, 59]:
                    yellow_list.append(letter)
                    yellow[str(j+1)].append(letter)

                else: used_letters.append(letter)
                
            j += 1

        counter += 1

        word_creator()

    


if __name__ == "__main__":
    main()
