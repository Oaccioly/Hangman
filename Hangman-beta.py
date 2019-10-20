from tkinter import *


class LetrasORG:
    def __init__(self):
        self.conf = int
        self.letra = str
        # self.descobrir = list
        self.tentativas = 7
        self.verif = []
        self.quant = 0

    def teste(self, letra):
        self.letra = letra
        print(f'\n<letra \033[31m{self.letra.upper()}\033[m recebida>')
        check = False
        mod = 12
        
        
        while check !=True:

            for x in range( 0, len( descobrir ) ):
                if self.letra == descobrir[x]:
                    self.quant = self.quant + 1
                    mod = mod-1
                    check = True



                    if x == 0:
                        print('Label 0 tem que mudar')
                        self.label0['text'] = f'{self.letra.upper()}   '
                        self.label0['font'] = 'Arialblack 30'
                        self.label0['underline'] = 0
                        

                    if x == 1:
                        print('Label 1 tem que mudar')
                        self.label1['text'] = f'{self.letra.upper()}   '
                        self.label1['font'] = 'Arialblack 30'
                        self.label1['underline'] = 0

                    if x == 2:
                        print('Label 2 tem que mudar')
                        self.label2['text'] = f'{self.letra.upper()}   '
                        self.label2['font'] = 'Arialblack 30'
                        self.label2['underline'] = 0

                    if x == 3:
                        print('Label 3 tem que mudar')
                        self.label3['text'] = f'{self.letra.upper()}   '
                        self.label3['font'] = 'Arialblack 30'
                        self.label3['underline'] = 0

                    if x == 4:
                        print('Label 4 tem que mudar')
                        self.label4['text'] = f'{self.letra.upper()}   '
                        self.label4['font'] = 'Arialblack 30'
                        self.label4['underline'] = 0

                    if x == 5:
                        print('Label 5 tem que mudar')
                        self.label5['text'] = f'{self.letra.upper()}   '
                        self.label5['font'] = 'Arialblack 30'
                        self.label5['underline'] = 0

                    if x == 6:
                        print('Label 6 tem que mudar')
                        self.label6['text'] = f'{self.letra.upper()}   '
                        self.label6['font'] = 'Arialblack 30'
                        self.label6['underline'] = 0

                    if x == 7:
                        print('Label 7 tem que mudar')
                        self.label7['text'] = f'{self.letra.upper()}   '
                        self.label7['font'] = 'Arialblack 30'
                        self.label7['underline'] = 0

                    if x == 8:
                        print('Label 8 tem que mudar')
                        self.label8['text'] = f'{self.letra.upper()}   '
                        self.label8['font'] = 'Arialblack 30'
                        self.label8['underline'] = 0

                    if x == 9:
                        print('Label 9 tem que mudar')
                        self.label9['text'] = f'{self.letra.upper()}   '
                        self.label9['font'] = 'Arialblack 30'
                        self.label9['underline'] = 0

                    if x == 10:
                        print('Label 10 tem que mudar')
                        self.label10['text'] = f'{self.letra.upper()}   '
                        self.label10['font'] = 'Arialblack 30'
                        self.label10['underline'] = 0

                    if x == 11:
                        print('Label 11 tem que mudar')
                        self.label11['text'] = f'{self.letra.upper()}   '
                        self.label11['font'] = 'Arialblack 30'
                        self.label11['underline'] = 0

                    if x == 12:
                        print('Label 12 tem que mudar')
                        self.label12['text'] = f'{self.letra.upper()}   '
                        self.label12['font'] = 'Arialblack 30'
                        self.label12['underline'] = 0

                else:

                    check = True

            if mod == 12:
                print('<LINHA 111:>Letra errada')
                self.tentativas -= 1

            else:
                print('<LINHA 114:> ',mod)



        print('<LINHA 118:> While finalizado')
        print('<Mod = ',mod)
        print('<Tentativas = ', Tentativas)
        print('<Quant = ', self.quant)
        print('<len de descobrir = ', len(descobrir))
        Tentativas(tentativas = self.tentativas)
        Fim(quant=self.quant, descobrir=len(self.descobrir) )

    def letras(self, conf, descobrir):
        self.conf = conf
        self.descobrir = descobrir

        if self.conf == 0:
            pass
        if self.conf == 1:
            print('CONF 1')
            self.letrasframe = Frame( frame1, width=700, height=50, bg='white', border='9',relief='groove' )
            self.letrasframe.place( x=270, y=410 )
            labels = len(descobrir)
            tents = 0
            quant = (len(descobrir))
            print(f'<LINHA 126:> a palavra secretra possui {len(descobrir)} letras')
            while True:
                self.label0 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label0.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label1 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label1.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label2 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label2.pack(side=LEFT)

                quant += -1
                if quant == 0:
                    break

                self.label3 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label3.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label4 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label4.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label5 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label5.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label6 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label6.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label7 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label7.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label8 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label8.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label9 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label9.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label10 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label10.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label11 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label11.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label12 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label12.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break

                self.label13 = Label(self.letrasframe, text='__   ', font='arialblack 25')
                self.label13.pack(side=LEFT)

                quant += -1
                tents += 1
                if quant == 0:
                    break


            print(f'<LINHA 258:> While terminou em {tents}')

def Tentativas(tentativas):
    print(f'\n<Tentativas iniciado> == {tentativas}\n')
    
    if tentativas == 6:
        photo['file'] = 'Forca-imagens\Camada 2.png'
       # print(f'{} Deve ficar vermelho')
    if tentativas == 5:
        photo['file'] = 'Forca-imagens\Camada 3.png'
       # print( f'{LetrasORG.letra} Deve ficar vermelho' )
    if tentativas == 4:
        photo['file'] = 'Forca-imagens\Camada 4.png'
       # print( f'{LetrasORG.letra} Deve ficar vermelho' )
    if tentativas == 3:
        photo['file'] = 'Forca-imagens\Camada 5.png'
       # print( f'{LetrasORG.letra} Deve ficar vermelho' )
    if tentativas == 2:
        photo['file'] = 'Forca-imagens\Camada 6.png'
        #print( f'{LetrasORG.letra} Deve ficar vermelho' )
    if tentativas == 1:
        photo['file'] = 'Forca-imagens\Camada 7.png'
        #print( f'{LetrasORG.letra} Deve ficar vermelho' )


def Fim(quant, descobrir):

    if quant >= descobrir:
        print('\n\033[32mTodas as letras foram descobertas\033[m')
    if quant <= descobrir:
        print(f'<\033[31mAinda resta {descobrir - quant} letras a descobrir\033[m]> ')








#Command Botoes
def q():
    letra = str('q')
    print('\n<letra \033[31mQ\033[m enviada>')
    label.teste(letra=letra)
    
def w():
    letra = str('w')
    print('\n<letra \033[31mW\033[m enviada>')
    label.teste(letra=letra)
    
def e():
    letra = str('e')
    print('\n<letra \033[31mE\033[m enviada>')
    label.teste(letra=letra)
    
def r():
    letra = str('r')
    print('\n<letra \033[31mR\033[m enviada>')
    label.teste(letra=letra)
    
def t():
    letra = str('t')
    print('\n<letra \033[31mT\033[m enviada>')
    label.teste(letra=letra)
    
def y():
    letra = str('y')
    print('\n<letra \033[31mY\033[m enviada>')
    label.teste(letra=letra)
    
def u():
    letra = str('u')
    print('\n<letra \033[31mU\033[m enviada>')
    label.teste(letra=letra)
    
def i():
    letra = str('i')
    print('\n<letra \033[31mI\033[m enviada>')
    label.teste(letra=letra)
    
def o():
    letra = str('o')
    print('\n<letra \033[31mO\033[m enviada>')
    label.teste(letra=letra)
    
def p():
    letra = str('p')
    print('\n<letra \033[31mP\033[m enviada>')
    label.teste(letra=letra)
    

def a():
    letra = str('a')
    print('\n<letra \033[31mA\033[m enviada>')
    label.teste(letra=letra)
    
def s():
    letra = str('s')
    print('\n<letra \033[31mS\033[m enviada>')
    label.teste(letra=letra)
    
def d():
    letra = str('d')
    print('\n<letra \033[31mD\033[m enviada>')
    label.teste(letra=letra)
    
def f():
    letra = str('f')
    print('\n<letra \033[31mF\033[m enviada>')
    label.teste(letra=letra)
    
def g():
    letra = str('g')
    print('\n<letra \033[31mG\033[m enviada>')
    label.teste(letra=letra)
    
def h():
    letra = str('h')
    print('\n<letra \033[31mH\033[m enviada>')
    label.teste(letra=letra)
    
def j():
    letra = str('j')
    print('\n<letra \033[31mJ\033[m enviada>')
    label.teste(letra=letra)
    
def k():
    letra = str('k')
    print('\n<letra \033[31mK\033[m enviada>')
    label.teste(letra=letra)
    
def l():
    letra = str('l')
    print('\n<letra \033[31mL\033[m enviada>')
    label.teste(letra=letra)
    

def z():
    letra = str('z')
    print('\n<letra \033[31mZ\033[m enviada>')
    label.teste(letra=letra)
    
def x():
    letra = str('x')
    print('\n<letra \033[31mX\033[m enviada>')
    label.teste(letra=letra)
    
def c():
    letra = str('c')
    print('\n<letra \033[31mC\033[m enviada>')
    label.teste(letra=letra)
    
def v():
    letra = str('v')
    print('\n<letra \033[31mV\033[m enviada>')
    label.teste(letra=letra)
    
def b():
    letra = str('b')
    print('\n<letra \033[31mB\033[m enviada>')
    label.teste(letra=letra)
    
def n():
    letra = str('n')
    print('\n<letra \033[31mN\033[m enviada>')
    label.teste(letra=letra)
    
def m():
    letra = str('m')
    print('\n<letra \033[31mM\033[m enviada>')
    label.teste(letra=letra)
    
#===============================

janela = Tk()
janela.geometry('1024x768')
janela.title('Jogo da forca')
janela.resizable(width=FALSE, height=FALSE)

frame1 = Frame(janela, width=1024,height=768, bg='Black', relief='raised', border=8)
frame1.pack(side=TOP)

titleframe = Frame(frame1, bg='Red')
titleframe.place(x=700,y=10)

# tema = Label(titleframe, text='Tema', font='Times 25', relief='raised', border='7' )
# tema.pack(side=TOP)

bonecoframe = Frame(frame1, width=300 , height=300, bg='Blue')
bonecoframe.place(x=20, y=0)

photo = PhotoImage(file='Forca-imagens\Camada 1.png')
labelphoto = Label(bonecoframe, image = photo)
labelphoto.pack()


botoesframeQP = Frame(frame1, bg='red')
botoesframeQP.place(x=200, y=520)

botoesframeAL = Frame(frame1, bg='red')
botoesframeAL.place(x=250, y=600)

botoesframeZM = Frame(frame1, bg='Red')
botoesframeZM.place(x=300, y=680)



#conjunto Q-P
btQ = Button(botoesframeQP, text='Q',width=3, font='Times 25', relief='raised', border=8, command=q)
btW = Button(botoesframeQP, text='W',width=3, font='Times 25', relief='raised', border=8, command=w)
btE = Button(botoesframeQP, text='E',width=3, font='Times 25', relief='raised', border=8, command=e)
btR = Button(botoesframeQP, text='R',width=3, font='Times 25', relief='raised', border=8, command=r)
btT = Button(botoesframeQP, text='T',width=3, font='Times 25', relief='raised', border=8, command=t)
btY = Button(botoesframeQP, text='Y',width=3, font='Times 25', relief='raised', border=8, command=y)
btU = Button(botoesframeQP, text='U',width=3, font='Times 25', relief='raised', border=8, command=u)
btI = Button(botoesframeQP, text='I',width=3, font='Times 25', relief='raised', border=8, command=i)
btO = Button(botoesframeQP, text='O',width=3, font='Times 25', relief='raised', border=8, command=o)
btP = Button(botoesframeQP, text='P',width=3, font='Times 25', relief='raised', border=8, command=p)

btQ.grid(column=1,row=1)
btW.grid(column=2,row=1)
btE.grid(column=3,row=1)
btR.grid(column=4,row=1)
btT.grid(column=5,row=1)
btY.grid(column=6,row=1)
btU.grid(column=7,row=1)
btI.grid(column=8,row=1)
btO.grid(column=9,row=1)
btP.grid(column=10,row=1)
#========================
#ppp
#conjunto A-L
btA = Button(botoesframeAL, text='A',width=3, font='Times 25', relief='raised', border=8, command=a)
btS = Button(botoesframeAL, text='S',width=3, font='Times 25', relief='raised', border=8, command=s)
btD = Button(botoesframeAL, text='D',width=3, font='Times 25', relief='raised', border=8, command=d)
btF = Button(botoesframeAL, text='F',width=3, font='Times 25', relief='raised', border=8, command=f)
btG = Button(botoesframeAL, text='G',width=3, font='Times 25', relief='raised', border=8, command=g)
btH = Button(botoesframeAL, text='H',width=3, font='Times 25', relief='raised', border=8, command=h)
btJ = Button(botoesframeAL, text='J',width=3, font='Times 25', relief='raised', border=8, command=j)
btK = Button(botoesframeAL, text='K',width=3, font='Times 25', relief='raised', border=8, command=k)
btL = Button(botoesframeAL, text='L',width=3, font='Times 25', relief='raised', border=8, command=l)

btA.grid(column=1,row=2)
btS.grid(column=2,row=2)
btD.grid(column=3,row=2)
btF.grid(column=4,row=2)
btG.grid(column=5,row=2)
btH.grid(column=6,row=2)
btJ.grid(column=7,row=2)
btK.grid(column=8,row=2)
btL.grid(column=9,row=2)
#=======================

#conjunto Z-M
btZ = Button(botoesframeZM, text='Z',width=3, font='Times 25', relief='raised', border=8, command=z)
btX = Button(botoesframeZM, text='X',width=3, font='Times 25', relief='raised', border=8, command=x)
btC = Button(botoesframeZM, text='C',width=3, font='Times 25', relief='raised', border=8, command=c)
btV = Button(botoesframeZM, text='V',width=3, font='Times 25', relief='raised', border=8, command=v)
btB = Button(botoesframeZM, text='B',width=3, font='Times 25', relief='raised', border=8, command=b)
btN = Button(botoesframeZM, text='N',width=3, font='Times 25', relief='raised', border=8, command=n)
btM = Button(botoesframeZM, text='M',width=3, font='Times 25', relief='raised', border=8, command=m)

btZ.grid(column=1,row=3)
btX.grid(column=2,row=3)
btC.grid(column=3,row=3)
btV.grid(column=4,row=3)
btB.grid(column=5,row=3)
btN.grid(column=6,row=3)
btM.grid(column=7,row=3)
#=======================
    
# def Autentificador():
#     dados = Toplevel(janela, )

        



palavraS = input('Palavra secreta: ').strip().lower()
# palavraS = '123'
descobrir = []
for x in range(len(palavraS)):
    descobrir += palavraS[x]
print(descobrir)
label = LetrasORG()
label.letras(conf=1, descobrir=descobrir)

dados = Toplevel()
mainloop()

#
#
#
#
#
#
#
#
#
#
# print('===' * 20)
# print('Jogo da velha \n')
# print('===' * 20)
#
# descobrir = ['p', 'a','s','s','i','v','a']
# letrasd = []
# tentativas = int(len(descobrir))
# erros = []
# verif = True
# for x in range(0, len(descobrir)):
#     letrasd.append(" _")
# print(descobrir)
# print(letrasd)
# acetou = False
#
# while acetou == False or tentativas > 0:
#     print('\nErros =', erros)
#     letra = str(input('Enter a letter: ')).strip().lower()
#     print(type(letra), 'letra ==',letra.isidentifier(), end='\n')
#
#     try:
#         for x in range(0, len(letrasd)):
#             if letra == erros[x]:
#                 print(f'Voce ja falou {letra}')
#                 break
#     except:
#         for x in range(0, len(descobrir)):
#             if letra == descobrir[x]:
#                 letrasd[x] = letra
#                 print(letrasd)
#                 verif = True
#                 break
#             else:
#                 verif = False
#         if verif == False:
#             print(f'\n{letra.upper()} There is no secret word \n')
#             erros += letra
#             print(letrasd)

