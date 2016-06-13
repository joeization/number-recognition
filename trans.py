import Image


class Trans:
    def __init__(self, path, num):
        self.ans = num
        jpgfile = Image.open(path)
        width, height = jpgfile.size
        im = jpgfile.load()
        self.form = [0]*256
        cnt = 0
        for x in range(0, width):
            for y in range(0, height):
                t = im[x, y]
                gry = 0.299*t[0] + 0.587*t[1] + 0.114*t[2]
                if gry >= 125:
                    self.form[cnt] = 1
                else:
                    self.form[cnt] = 0
                cnt += 1
