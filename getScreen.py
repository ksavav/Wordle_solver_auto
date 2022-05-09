import pyautogui
import pygetwindow
import os
import json
import io
import requests 
import cv2
from PIL import Image

class getScreen:
    def manager(self):
        text_to_list = self.getScreenshot()

        return self.textToList(text_to_list)

    def getScreenshot(self):
        p = os.path.dirname(os.path.abspath(__file__)) + '/src/result.png'

        window = pygetwindow.getWindowsWithTitle('Chrome')[0]
        x1 = window.left
        y1 = window.top
        height = window.height
        width = window.width

        x2 = x1 + width
        y2 = y1 + height

        pyautogui.screenshot(p)

        im = Image.open(p)
        im = im.crop((x1, y1, x2, y2))
        im.save(p)
        #im.show(p)

        return self.textRecognizer(p)

    def cropImage(self, path):
        img = cv2.imread(path)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        height, width, _ = img.shape

        #(h - 420)/2 (w - 350)/2

        #350/420
        h1 = int((height)/2 - 210 - 20)
        h2 = int((height)/2 + 210 - 20)
        w1 = int((width)/2 - 175)
        w2 = int((width)/2 + 175)

        img = img[h1 : h2, w1 : w2]

        cv2.imwrite('src/colors.png', img)
        cv2.imwrite('src/result.png', img)

    def textRecognizer(self, path):
        self.cropImage(path)
        self.deleteColors(path)
        img = cv2.imread(path)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)       
        

        #o -> 0, b -> 8, i -> |
        url = 'https://api.ocr.space/parse/image'
        _, compressedimage = cv2.imencode(".png", img, [1, 90])
        file_bytes = io.BytesIO(compressedimage)

        result = requests.post(url, 
                    files = {path : file_bytes},
                    data  = {'apikey' : "K82240883388957",
                            'OCREngine' : '3'})

        

        x = result.content.decode()
        x = json.loads(x)
        text_from_image = x.get("ParsedResults")[0].get("ParsedText")
        return text_from_image

    def deleteColors(self, path):
        img = Image.open(path)

        img = img.convert('RGBA')

        pixdata = img.load()

        # Clean the background noises, if color != white, then set to black.

        for y in list(range(img.size[1])):
            for x in list(range(img.size[0])):
                if pixdata[x, y] != (255, 255, 255, 255):
                    pixdata[x, y] = (0, 0, 0, 255)


        img.save('src/result.png')

    def textToList(self, text):
        words_on_board = {
            '1' : [],
            '2' : [],
            '3' : [],
            '4' : [],
            '5' : [],
            '6' : [],
        }

        text = text.lower()
        counter = 0

        for i in text:
            if i != " " and i != '\r' and i != '\n':
                if i == "|" or i == "1": i = 'i' 
                if i == "8": i = 'b'
                if i == "0": i = 'o'

                words_on_board[str(counter + 1)].append(i)

                if len(words_on_board[str(counter + 1)]) == 5: counter += 1

        return words_on_board

"""def textRecognizer(path):
    img = deleteColors(path)
    #img = Image.open(path)
    #img = Image.open(path)

    result = pytesseract.image_to_string(img)

    print(result)
"""