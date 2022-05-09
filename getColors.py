import cv2

class getColors:
    def colorsFromImage(self):
        colors_on_board = {
        '1' : [],
        '2' : [],
        '3' : [],
        '4' : [],
        '5' : [],
        '6' : [],
        }

        img = cv2.imread("src/colors.png")
        h, w, _ = img.shape

        for i in reversed(range(6)):
            for j in reversed(range(5)):
                colors_on_board[str(abs(6 - i))].append(list(img[int(h - (h/6) * i - 25), int(w - (w/5) * j - 15)]))

        return colors_on_board
