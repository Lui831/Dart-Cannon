####################################################################################################################################################
# Título: código main para Dart Cannon (versão mola)
# Descrição: contém manipulação de display I²C, interrupção de botão, manipulação de 2 servo-motores e leitura de potenciômetro
# Autores: João V. C. Branco, Luiz H. A. Santos, Pedro A. W. Dian, Vitor G. Soller
# Data: -
####################################################################################################################################################
# Inclusão de bibliotecas necessárias

from machine import *
from time import *
from servo import *



####################################################################################################################################################
# Definição de variáveis globais

button_pressed = 0
button_timer = machine.Timer(-1)
push_button = Pin(0, mode = Pin.IN, pull = Pin.PULL_UP)

pottentiometer = ADC(26)
pottentiometer_timer = machine.Timer(-1)
pottentiometer_values = []

servo1 = Servo(pin_id = 1)
servo2 = Servo(pin_id = 2)



####################################################################################################################################################
## Definição de funções importantes ao código


# Definição das funções de handler do push_button e timer para debounce

def push_button_handler(pin):
    
        # Ação a ser executada
        print("BOTÃO APERTADO!!!")
        servo2.write(180)
        sleep(1)
        servo2.write(0)
        
def push_button_check(timer):

    # Definição das variáveis globais
    global push_button
    global button_pressed

    # Caso o botão esteja apertado...
    if push_button.value() == 0 and button_pressed == 0:
        
        # Faz a ação e seta botão apertado
        push_button_handler(push_button)
        button_pressed = 1
        
    # Caso não esteja apertado...
    elif push_button.value() == 1:
        
        # Reseta o botão apertado
        button_pressed = 0
        
def pottentiometer_handler(timer):
    
    global pottentiometer
    global servo
    global pottentiometer_values
    
    # Realiza a média móvel dos valores de potenciômetro medidos
    pottentiometer_values.insert(0,pottentiometer.read_u16() * (180/59500))
    pottentiometer_value = (pottentiometer_values[0] + pottentiometer_values[1] + pottentiometer_values[2] + pottentiometer_values[3] + pottentiometer_values[4] + pottentiometer_values[5])/6
    
    # Aciona o servomotor
    print(pottentiometer_value)
    servo1.write(pottentiometer_value)
    
        

        
####################################################################################################################################################
## Código main


# Definição do timer do botão
button_timer.init(period=50, mode=machine.Timer.PERIODIC, callback=push_button_check)

# Definição do timer do potenciômetro
pottentiometer_timer.init(period=200, mode=machine.Timer.PERIODIC, callback=pottentiometer_handler)



