from tkinter import *
import pandas as pd
from random import randint
from time import sleep


class LetrasORG:
    def __init__(self):
        self.conf = int
        self.letra = str
        self.descobrir = int
        self.tentativas = 7
        self.verif = []
        self.quant = 0
        self.palavraS = str
         
    def teste(self, letra):
        self.letra = letra
        print(f'\n<letra \033[31m{self.letra.upper()}\033[m recebida>')
        check = False
        mod = 12
        
        
        while check !=True:
            

            for x in range( 0, len( self.descobrir ) ):
                if self.letra == self.descobrir[x]:
                    self.quant = self.quant + 1
                    mod = mod-1
                    check = True



                    if x == 0:
                        print('Label 0 tem que mudar')
                        self.label0['text'] = f'{letra.upper()}   '
                        self.label0['font'] = 'Arialblack 30'
                        self.label0['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 1:
                        print('Label 1 tem que mudar')
                        self.label1['text'] = f'{letra.upper()}   '
                        self.label1['font'] = 'Arialblack 30'
                        self.label1['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 2:
                        print('Label 2 tem que mudar')
                        self.label2['text'] = f'{letra.upper()}   '
                        self.label2['font'] = 'Arialblack 30'
                        self.label2['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 3:
                        print('Label 3 tem que mudar')
                        self.label3['text'] = f'{letra.upper()}   '
                        self.label3['font'] = 'Arialblack 30'
                        self.label3['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 4:
                        print('Label 4 tem que mudar')
                        self.label4['text'] = f'{letra.upper()}   '
                        self.label4['font'] = 'Arialblack 30'
                        self.label4['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 5:
                        print('Label 5 tem que mudar')
                        self.label5['text'] = f'{letra.upper()}   '
                        self.label5['font'] = 'Arialblack 30'
                        self.label5['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 6:
                        print('Label 6 tem que mudar')
                        self.label6['text'] = f'{letra.upper()}   '
                        self.label6['font'] = 'Arialblack 30'
                        self.label6['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 7:
                        print('Label 7 tem que mudar')
                        self.label7['text'] = f'{letra.upper()}   '
                        self.label7['font'] = 'Arialblack 30'
                        self.label7['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 8:
                        print('Label 8 tem que mudar')
                        self.label8['text'] = f'{letra.upper()}   '
                        self.label8['font'] = 'Arialblack 30'
                        self.label8['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 9:
                        print('Label 9 tem que mudar')
                        self.label9['text'] = f'{letra.upper()}   '
                        self.label9['font'] = 'Arialblack 30'
                        self.label9['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 10:
                        print('Label 10 tem que mudar')
                        self.label10['text'] = f'{letra.upper()}   '
                        self.label10['font'] = 'Arialblack 30'
                        self.label10['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 11:
                        print('Label 11 tem que mudar')
                        self.label11['text'] = f'{letra.upper()}   '
                        self.label11['font'] = 'Arialblack 30'
                        self.label11['underline'] = 0
                        bt_verde(letra= self.letra)
                    if x == 12:
                        print('Label 12 tem que mudar')
                        self.label12['text'] = f'{letra.upper()}   '
                        self.label12['font'] = 'Arialblack 30'
                        self.label12['underline'] = 0
                        bt_verde(letra= self.letra)
                else:

                    check = True

            if mod == 12:
                print('<LINHA 111:>Letra errada')
                self.tentativas -= 1
                bt_vermelho(letra=label.letra)

            else:
                print('<LINHA 114:> ',mod)



        print('<LINHA 126:> While finalizado')
        print('<Mod = ',mod)
        print('<Tentativas = ', Tentativas)
        print('<Quant = ', self.quant)
        print('<len de descobrir = ', len(self.descobrir))
        Tentativas(tentativas = self.tentativas)
        Fim(quant=self.quant, descobrir=len(self.descobrir) )

    def letras(self, conf, descobrir):
        self.conf = conf
        self.descobrir = descobrir

        if self.conf == 0:
            self.letrasframe.destroy()
            

            
        if self.conf == 1:
            print('CONF 1')
            self.letrasframe = Frame( frame1, width=700, height=50, bg='white', border='9',relief='groove' )
            self.letrasframe.place( x=240, y=410 )
            labels = len(self.descobrir)
            tents = 0
            quant = (len(self.descobrir))
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

def Random_word():
        try:
            planilha = pd.read_excel("Tabela\Palavras.xlsx")
            x = randint(0, planilha.shape[0])
            print('O tema é ',planilha['Tema'] [x])
            print('A palavra secreta é ',planilha['Palavra_secreta'] [x])
            palavraS = str(planilha['Palavra_secreta'] [x]).strip()
            tema['text'] = planilha['Tema'] [x]
            descobrir = []
            for x in range(len(palavraS)):
                descobrir += str(palavraS[x]).lower()
            print(descobrir)
            label.letras(conf=1, descobrir=descobrir)  
            photo['file'] = 'Forca-imagens\Camada 1.png'
            label.palavraS = palavraS
            
            
        except:
            print('Falha em solicitar o arquivo Palavras')
            sleep(5)
            try:
                planilha = pd.read_excel("Tabela\Palavras.xlsx")
                x = randint(0, planilha.shape[0])
                print('O tema é ',planilha['Tema'] [x])
                print('A palavra secreta é ',planilha['Palavra_secreta'] [x])
                palavraS = planilha['Palavra_secreta'] [x]
                tema['text'] = planilha['Tema'] [x]
                descobrir = []
                for x in range(len(palavraS)):
                    descobrir += str(palavraS[x]).lower()
                print(descobrir)
                label.letras(conf=1, descobrir=descobrir)
                photo['file'] = 'Forca-imagens\Camada 1.png'
                label.palavraS = palavraS
                
            except:
                print('Erro critico')
                sleep(3)
                quit()
            
def Tentativas(tentativas):
    print(f'\n<Tentativas iniciado> == {tentativas}\n')
    
    if tentativas == 6:
        photo['file'] = 'Forca-imagens\Camada 2.png'
 
        
    if tentativas == 5:
        photo['file'] = 'Forca-imagens\Camada 3.png'

       
    if tentativas == 4:
        photo['file'] = 'Forca-imagens\Camada 4.png'
      
       
    if tentativas == 3:
        photo['file'] = 'Forca-imagens\Camada 5.png'
       
       
    if tentativas == 2:
        photo['file'] = 'Forca-imagens\Camada 6.png'
        
        
    if tentativas == 1:
        photo['file'] = 'Forca-imagens\Camada 7.png'
        


def Fim(quant, descobrir):

    if quant >= descobrir:
        print('\n\033[32mTodas as letras foram descobertas\033[m')
        label.letras(conf= 0 , descobrir='Passou')
        label.tentativas = 7
        label.quant = 0
        descobrir = -1
        bt_reset()
        Random_word()
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
def bt_skip():
    print('\nbt_skip\n')
    label.letrasframe.destroy()
    bt_reset()
    Random_word()

def bt_verde(letra):
    print('\n\033[33m<Bt_verde>\033[m]\n')
    if letra == 'q':
        btQ['command'] = ''
        btQ['bg'] = 'Green'
        print('btQ[bg]')
    if letra == 'w':
        btW['command'] = ''
        btW['bg'] = 'Green'
        print('btW[bg]')
    if letra == 'e':
        btE['command'] = ''
        btE['bg'] = 'Green'
        print('btE[bg]')
    if letra == 'r':
        btR['command'] = ''
        btR['bg'] = 'Green'
    if letra == 't':
        btT['command'] = ''
        btT['bg'] = 'Green'
        print('btT[bg]')
    if letra == 'y':
        btY['command'] = ''
        btY['bg'] = 'Green'
        print('btY[bg]')
    if letra == 'u':
        btU['command'] = ''
        btU['bg'] = 'Green'
        print('btU[bg]')
    if letra == 'i':
        btI['command'] = ''
        btI['bg'] = 'Green'
        print('btI[bg]')
    if letra == 'o':
        btO['command'] = ''
        btO['bg'] = 'Green'
        print('btO[bg]')
    if letra ==  'p':
        btP['command'] = ''
        btP['bg'] = 'Green'
        print('btP[bg]')
    
    if letra == 'a':
        btA['command'] = ''
        btA['bg'] = 'Green'
        print('btA[bg]')
    if letra == 's':
        btS['command'] = ''
        btS['bg'] = 'Green'
        print('btS[bg]')
    if letra == 'd':
        btD['command'] = ''
        btD['bg'] = 'Green'
        print('btD[bg]')
    if letra == 'f':
        btF['command'] = ''
        btF['bg'] = 'Green'
        print('btF[bg]')
    if letra == 'g':
        btG['command'] = ''
        btG['bg'] = 'Green'
        print('btG[bg]')
    if letra == 'h':
        btH['command'] = ''
        btH['bg'] = 'Green'
        print('btH[bg]')
    if letra == 'j':
        btJ['command'] = ''
        btJ['bg'] = 'Green'
        print('btJ[bg]')
    if letra == 'k':
        btK['command'] = ''
        btK['bg'] = 'Green'
        print('btK[bg]')
    if letra == 'l':
        btL['command'] = ''
        btL['bg'] = 'Green'
        print('btL[bg]')
    
    if letra == 'z':
        btZ['command'] = ''
        btZ['bg'] = 'Green'
        print('btZ[bg]')
    if letra == 'x':
        btX['command'] = ''
        btX['bg'] = 'Green'
        print('btX[bg]')
    if letra == 'c':
        btC['command'] = ''
        btC['bg'] = 'Green'
        print('btC[bg]')
    if letra == 'v':
        btV['command'] = ''
        btV['bg'] = 'Green'
        print('btV[bg]')
    if letra == 'b':
        btB['command'] = ''
        btB['bg'] = 'Green'
        print('btB[bg]')
    if letra == 'n':
        btN['command'] = ''
        btN['bg'] = 'Green'
        print('btN[bg]')
    if letra == 'm':
        btM['command'] = ''
        btM['bg'] = 'Green'
        print('btM[bg]')

def bt_vermelho(letra):
    print('\n\033[31m<Bt_vermelho>\033[m]\n')
    if letra == 'q':
        btQ['command'] = ''
        btQ['bg'] = 'red'
        print('btQ[bg]')
    if letra == 'w':
        btW['command'] = ''
        btW['bg'] = 'red'
        print('btW[bg]')
    if letra == 'e':
        btE['command'] = ''
        btE['bg'] = 'red'
        print('btE[bg]')
    if letra == 'r':
        btR['command'] = ''
        btR['bg'] = 'red'
    if letra == 't':
        btT['command'] = ''
        btT['bg'] = 'red'
        print('btT[bg]')
    if letra == 'y':
        btY['command'] = ''
        btY['bg'] = 'red'
        print('btY[bg]')
    if letra == 'u':
        btU['command'] = ''
        btU['bg'] = 'red'
        print('btU[bg]')
    if letra == 'i':
        btI['command'] = ''
        btI['bg'] = 'red'
        print('btI[bg]')
    if letra == 'o':
        btO['command'] = ''
        btO['bg'] = 'red'
        print('btO[bg]')
    if letra ==  'p':
        btP['command'] = ''
        btP['bg'] = 'red'
        print('btP[bg]')
    
    if letra == 'a':
        btA['command'] = ''
        btA['bg'] = 'red'
        print('btA[bg]')
    if letra == 's':
        btS['command'] = ''
        btS['bg'] = 'red'
        print('btS[bg]')
    if letra == 'd':
        btD['command'] = ''
        btD['bg'] = 'red'
        print('btD[bg]')
    if letra == 'f':
        btF['command'] = ''
        btF['bg'] = 'red'
        print('btF[bg]')
    if letra == 'g':
        btG['command'] = ''
        btG['bg'] = 'red'
        print('btG[bg]')
    if letra == 'h':
        btH['command'] = ''
        btH['bg'] = 'red'
        print('btH[bg]')
    if letra == 'j':
        btJ['command'] = ''
        btJ['bg'] = 'red'
        print('btJ[bg]')
    if letra == 'k':
        btK['command'] = ''
        btK['bg'] = 'red'
        print('btK[bg]')
    if letra == 'l':
        btL['command'] = ''
        btL['bg'] = 'red'
        print('btL[bg]')
    
    if letra == 'z':
        btZ['command'] = ''
        btZ['bg'] = 'red'
        print('btZ[bg]')
    if letra == 'x':
        btX['command'] = ''
        btX['bg'] = 'red'
        print('btX[bg]')
    if letra == 'c':
        btC['command'] = ''
        btC['bg'] = 'red'
        print('btC[bg]')
    if letra == 'v':
        btV['command'] = ''
        btV['bg'] = 'red'
        print('btV[bg]')
    if letra == 'b':
        btB['command'] = ''
        btB['bg'] = 'red'
        print('btB[bg]')
    if letra == 'n':
        btN['command'] = ''
        btN['bg'] = 'red'
        print('btN[bg]')
    if letra == 'm':
        btM['command'] = ''
        btM['bg'] = 'red'
        print('btM[bg]')

def bt_reset(rst=1):
    print('\nBt reset iniciado\n')
    if rst == 1:
        btQ['command'] = q
        btQ['bg'] = 'white'
        

        btW['command'] = w
        btW['bg'] = 'white'
        

        btE['command'] = e
        btE['bg'] = 'white'
        

        btR['command'] = r
        btR['bg'] = 'white'

        btT['command'] = t
        btT['bg'] = 'white'
        

        btY['command'] = y
        btY['bg'] = 'white'
        

        btU['command'] = u
        btU['bg'] = 'white'
        

        btI['command'] = i
        btI['bg'] = 'white'
        

        btO['command'] = o
        btO['bg'] = 'white'
        

        btP['command'] = p
        btP['bg'] = 'white'
        


        btA['command'] = a
        btA['bg'] = 'white'
        
        
        btS['command'] = s
        btS['bg'] = 'white'
        

        btD['command'] = d
        btD['bg'] = 'white'
        

        btF['command'] = f
        btF['bg'] = 'white'
        

        btG['command'] = g
        btG['bg'] = 'white'
        

        btH['command'] = h
        btH['bg'] = 'white'
        

        btJ['command'] = j
        btJ['bg'] = 'white'
        

        btK['command'] = k
        btK['bg'] = 'white'
        

        btL['command'] = l
        btL['bg'] = 'white'
        


        btZ['command'] = z
        btZ['bg'] = 'white'
        

        btX['command'] = x
        btX['bg'] = 'white'
        

        btC['command'] = c
        btC['bg'] = 'white'
        

        btV['command'] = v
        btV['bg'] = 'white'
        

        btB['command'] = b
        btB['bg'] = 'white'
        

        btN['command'] = n
        btN['bg'] = 'white'
        

        btM['command'] = m
        btM['bg'] = 'white'
     
    
#===============================
janela = Tk()
janela.geometry('1024x768')
janela.title('Jogo da forca')
janela.resizable(width=FALSE, height=FALSE)

frame1 = Frame(janela, width=1024,height=768, bg='Black', relief='raised', border=8)
frame1.pack(side=TOP)

titleframe = Frame(frame1, bg='Red')
titleframe.place(x=650,y=10)

tema = Label(titleframe, text='Tema', font='Times 25', relief='raised', border='7' )
tema.pack(side=LEFT)

bonecoframe = Frame(frame1, width=300 , height=300, bg='Blue')
bonecoframe.place(x=0, y=0)

photo = PhotoImage(file='Forca-imagens\Camada 1.png')
labelphoto = Label(bonecoframe, image = photo)
labelphoto.pack()


botoesframeQP = Frame(frame1, bg='red')
botoesframeQP.place(x=180, y=500)

botoesframeAL = Frame(frame1, bg='red')
botoesframeAL.place(x=200, y=580)

botoesframeZM = Frame(frame1, bg='Red')
botoesframeZM.place(x=220, y=660)

bt_skip = Button(janela, text='Skip', font='times 25', relief='raised', border=8, command=bt_skip)
bt_skip.place(x=765, y=668)


#conjunto Q-P
btQ = Button(botoesframeQP, text='Q', width=3, bg='white', font='Times 25', relief='raised', border=8, command=q)
btW = Button(botoesframeQP, text='W', width=3, bg='white', font='Times 25', relief='raised', border=8, command=w)
btE = Button(botoesframeQP, text='E', width=3, bg='white', font='Times 25', relief='raised', border=8, command=e)
btR = Button(botoesframeQP, text='R', width=3, bg='white', font='Times 25', relief='raised', border=8, command=r)
btT = Button(botoesframeQP, text='T', width=3, bg='white', font='Times 25', relief='raised', border=8, command=t)
btY = Button(botoesframeQP, text='Y', width=3, bg='white', font='Times 25', relief='raised', border=8, command=y)
btU = Button(botoesframeQP, text='U', width=3, bg='white', font='Times 25', relief='raised', border=8, command=u)
btI = Button(botoesframeQP, text='I', width=3, bg='white', font='Times 25', relief='raised', border=8, command=i)
btO = Button(botoesframeQP, text='O', width=3, bg='white', font='Times 25', relief='raised', border=8, command=o)
btP = Button(botoesframeQP, text='P', width=3, bg='white', font='Times 25', relief='raised', border=8, command=p)

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

#conjunto A-L
btA = Button(botoesframeAL, text='A', width=3, bg='white', font='Times 25', relief='raised', border=8, command=a)
btS = Button(botoesframeAL, text='S', width=3, bg='white', font='Times 25', relief='raised', border=8, command=s)
btD = Button(botoesframeAL, text='D', width=3, bg='white', font='Times 25', relief='raised', border=8, command=d)
btF = Button(botoesframeAL, text='F', width=3, bg='white', font='Times 25', relief='raised', border=8, command=f)
btG = Button(botoesframeAL, text='G', width=3, bg='white', font='Times 25', relief='raised', border=8, command=g)
btH = Button(botoesframeAL, text='H', width=3, bg='white', font='Times 25', relief='raised', border=8, command=h)
btJ = Button(botoesframeAL, text='J', width=3, bg='white', font='Times 25', relief='raised', border=8, command=j)
btK = Button(botoesframeAL, text='K', width=3, bg='white', font='Times 25', relief='raised', border=8, command=k)
btL = Button(botoesframeAL, text='L', width=3, bg='white', font='Times 25', relief='raised', border=8, command=l)

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
btZ = Button(botoesframeZM, text='Z', width=3, bg='white', font='Times 25', relief='raised', border=8, command=z)
btX = Button(botoesframeZM, text='X', width=3, bg='white', font='Times 25', relief='raised', border=8, command=x)
btC = Button(botoesframeZM, text='C', width=3, bg='white', font='Times 25', relief='raised', border=8, command=c)
btV = Button(botoesframeZM, text='V', width=3, bg='white', font='Times 25', relief='raised', border=8, command=v)
btB = Button(botoesframeZM, text='B', width=3, bg='white', font='Times 25', relief='raised', border=8, command=b)
btN = Button(botoesframeZM, text='N', width=3, bg='white', font='Times 25', relief='raised', border=8, command=n)
btM = Button(botoesframeZM, text='M', width=3, bg='white', font='Times 25', relief='raised', border=8, command=m)

btZ.grid(column=1,row=3)
btX.grid(column=2,row=3)
btC.grid(column=3,row=3)
btV.grid(column=4,row=3)
btB.grid(column=5,row=3)
btN.grid(column=6,row=3)
btM.grid(column=7,row=3)
#=======================


label = LetrasORG()
Random_word()


# palavraS = input('Palavra secreta: ').strip().lower()
# palavraS = '123'
# descobrir = []
# for x in range(len(palavraS)):
#     descobrir += palavraS[x]
# print(descobrir)
# label = LetrasORG()
# label.letras(conf=1, descobrir=descobrir)


mainloop()











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

