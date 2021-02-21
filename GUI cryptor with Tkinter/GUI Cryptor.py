def decodec():
    try:
        decoded.delete('1.0',END)
        decodentryget = decodentry.get("1.0","end-1c")
        a = decodentryget
        b = len(a)
        d = ''
        for j in range(b):
            if j % 3==2:
                d = d + a[j]
                d = d + ':'
            else:
                d = d + a[j]
        e = d.split(':')
        f = ''
        for k in e:
            if k == 'GF#':
                f = f + 'A'
            elif k == 'gf#':
                f = f + 'a'
            elif k == 'KU*':
                f = f + 'B'
            elif k == 'ku*':
                f = f + 'b'
            elif k == 'AN@':
                f = f + 'C'
            elif k == 'an@':
                f = f + 'c'
            elif k == 'LD^':
                f = f + 'D'
            elif k == 'ld^':
                f = f + 'd'
            elif k == 'SS$':
                f = f + 'E'
            elif k == 'ss$':
                f = f + 'e'
            elif k == 'GU*':
                f = f + 'F'
            elif k == 'gu*':
                f = f + 'f'
            elif k == 'KN@':
                f = f + 'G'
            elif k == 'kn@':
                f = f + 'g'
            elif k == 'AD^':
                f = f + 'H'
            elif k == 'ad^':
                f = f + 'h'
            elif k == 'LS$':
                f = f + 'I'
            elif k == 'ls$':
                f = f + 'i'
            elif k == 'SF#':
                f = f + 'J'
            elif k == 'sf#':
                f = f + 'j'
            elif k == 'GN@':
                f = f + 'K'
            elif k == 'gn@':
                f = f + 'k'
            elif k == 'KD^':
                f = f + 'L'
            elif k == 'kd^':
                f = f + 'l'
            elif k == 'AS$':
                f = f + 'M'
            elif k == 'as$':
                f = f + 'm'
            elif k == 'LF#':
                f = f + 'N'
            elif k == 'lf#':
                f = f + 'n'
            elif k == 'SU*':
                f = f + 'O'
            elif k == 'su*':
                f = f + 'o'
            elif k == 'GD^':
                f = f + 'P'
            elif k == 'gd^':
                f = f + 'p'
            elif k == 'KS$':
                f = f + 'Q'
            elif k == 'ks$':
                f = f + 'q'
            elif k == 'AF#':
                f = f + 'R'
            elif k == 'af#':
                f = f + 'r'
            elif k == 'LU*':
                f = f + 'S'
            elif k == 'lu*':
                f = f + 's'
            elif k == 'SN@':
                f = f + 'T'
            elif k == 'sn@':
                f = f + 't'
            elif k == 'GS$':
                f = f + 'U'
            elif k == 'gs$':
                f = f + 'u'
            elif k == 'KF#':
                f = f + 'V'
            elif k == 'kf#':
                f = f + 'v'
            elif k == 'AU*':
                f = f + 'W'
            elif k == 'au*':
                f = f + 'w'
            elif k == 'LN@':
                f = f + 'X'
            elif k == 'ln@':
                f = f + 'x'
            elif k == 'SD^':
                f = f + 'Y'
            elif k == 'sd^':
                f = f + 'y'
            elif k == 'GF$':
                f = f + 'Z'
            elif k == 'gf$':
                f = f + 'z'
            elif k == './;':
                f = f + '1'
            elif k == '/(/':
                f = f + '2'
            elif k == '().':
                f = f + '3'
            elif k == ').;':
                f = f + '4'
            elif k == ';//':
                f = f + '5'
            elif k == '.(.':
                f = f + '6'
            elif k == '/);':
                f = f + '7'
            elif k == '(;/':
                f = f + '8'
            elif k == ')/;':
                f = f + '9'
            elif k == ';./':
                f = f + '0'
            elif k == '(.)':
                f = f + ' '
            elif k == '(()':
                f = f + '\n'
            elif k == '':
                continue
            else:
                raise TypeError
        decoded.insert(END,f)
    except:
        decoded.insert(END,"SORRY, there is a problem in your text.\nPLEASE TRY AGAIN")
    

def codec():
    try:
        coded.delete('1.0',END)
        codentryget = codentry.get("1.0","end-1c")
        q = codentryget
        m = ""
        for x in q:
            if x == 'A':
                m = m + 'GF#'
            elif x == 'a':
                m = m + 'gf#'
            elif x == 'B':
                m = m + 'KU*'
            elif x == 'b':
                m = m + 'ku*'
            elif x == 'C':
                m = m + 'AN@'
            elif x == 'c':
                m = m + 'an@'
            elif x == 'D':
                m = m + 'LD^'
            elif x == 'd':
                m = m + 'ld^'
            elif x == 'E':
                m = m + 'SS$'
            elif x == 'e':
                m = m + 'ss$'
            elif x == 'F':
                m = m + 'GU*'
            elif x == 'f':
                m = m + 'gu*'
            elif x == 'G':
                m = m + 'KN@'
            elif x == 'g':
                m = m + 'kn@'
            elif x == 'H':
                m = m + 'AD^'
            elif x == 'h':
                m = m + 'ad^'
            elif x == 'I':
                m = m + 'LS$'
            elif x == 'i':
                m = m + 'ls$'
            elif x == 'J':
                m = m + 'SF#'
            elif x == 'j':
                m = m + 'sf#'
            elif x == 'K':
                m = m + 'GN@'
            elif x == 'k':
                m = m + 'gn@'
            elif x == 'L':
                m = m + 'KD^'
            elif x == 'l':
                m = m + 'kd^'
            elif x == 'M':
                m = m + 'AS$'
            elif x == 'm':
                m = m + 'as$'
            elif x == 'N':
                m = m + 'LF#'
            elif x == 'n':
                m = m + 'lf#'
            elif x == 'O':
                m = m + 'SU*'
            elif x == 'o':
                m = m + 'su*'
            elif x == 'P':
                m = m + 'GD^'
            elif x == 'p':
                m = m + 'gd^'
            elif x == 'Q':
                m = m + 'KS$'
            elif x == 'q':
                m = m + 'ks$'
            elif x == 'R':
                m = m + 'AF#'
            elif x == 'r':
                m = m + 'af#'
            elif x == 'S':
                m = m + 'LU*'
            elif x == 's':
                m = m + 'lu*'
            elif x == 'T':
                m = m + 'SN@'
            elif x == 't':
                m = m + 'sn@'
            elif x == 'U':
                m = m + 'GS$'
            elif x == 'u':
                m = m + 'gs$'
            elif x == 'V':
                m = m + 'KF#'
            elif x == 'v':
                m = m + 'kf#'
            elif x == 'W':
                m = m + 'AU*'
            elif x == 'w':
                m = m + 'au*'
            elif x == 'X':
                m = m + 'LN@'
            elif x == 'x':
                m = m + 'ln@'
            elif x == 'Y':
                m = m + 'SD^'
            elif x == 'y':
                m = m + 'sd^'
            elif x == 'Z':
                m = m + 'GF$'
            elif x == 'z':
                m = m + 'gf$'
            elif x == '1':
                m = m + './;'
            elif x == '2':
                m = m + '/(/'
            elif x == '3':
                m = m + '().'
            elif x == '4':
                m = m + ').;'
            elif x == '5':
                m = m + ';//'
            elif x == '6':
                m   = m + '.(.'
            elif x == '7':
                m = m + '/);'
            elif x == '8':
                m = m + '(;/'
            elif x == '9':
                m = m + ')/;'
            elif x == '0':
                m = m + ';./'
            elif x == ' ':
                m = m + '(.)'
            elif x == '\n':
                m = m + '(()'
            else:
                raise TypeError
        coded.insert(END,m)
    except:
        coded.insert(END,"Please remove special characters in your message")

from tkinter import*

cry = Tk()

cry.geometry('12500x9000')

cry.title('Devil Cryptor')

page = Canvas(cry,width = 1700,height = 1000)
page.pack(expand = True,fill = BOTH)


photo = PhotoImage(file = "kd1.png")
page.create_image(0,0,image=photo,anchor = NW)


page.create_text(680,100,text = "DEVIL CRYPTOR",fill = "white",font = ("Comic Sans MS",80))

page.create_text(110,200,text = "Coder",fill = "skyblue",font = ("Courier New",50))

page.create_text(1220,200,text = "Decoder",fill = "skyblue",font = ("Courier New",50))

page.create_rectangle(240,40,1130,170,outline = "skyblue",width = 2)

page.create_line(685,170,685,10000,fill = "skyblue",width = 2)

page.create_line(0,105,240,105,fill = "skyblue",width = 2)

page.create_line(1130,105,10000,105,fill = "skyblue",width = 2)


codentry = Text(cry,height = 4,width = 35,font = ("Copperplate Gothic Light",16))
codentry.place(x = 110,y = 300)


coded = Text(cry,height = 4,width = 35,font = ("Copperplate Gothic Light",16))
coded.place(x = 110,y = 500)

decodentry = Text(cry,height = 4,width = 35,font = ("Copperplate Gothic Light",16))
decodentry.place(x = 730,y = 300)

decoded = Text(cry,height = 4,width = 35,font =("Copperplate Gothic Light",16))
decoded.place(x = 730,y = 500)

bcoder = Button(cry,text = "CONVERT",font = ("Centaur"),bg = "white",fg = "black",command = codec)
bcoder.place(x = 140,y = 400)

bdecoder = Button(cry,text = "CONVERT",font = ("Centaur"),bg = "white",fg = "black",command = decodec)
bdecoder.place(x = 766,y = 400)


cry.mainloop()
