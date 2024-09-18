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
from math import *


####################################################################################################################################################
# Definição de variáveis globais

# Variáveis relacionadas ao botão - Acionamento Automatico
button_pressed = 0
button_timer = machine.Timer(-1)
push_button = Pin(0, mode = Pin.IN)

# Variáveis relacionadas ao PWM
PWM = Pin(26, Pin.IN)
PWM_timer = machine.Timer(-1)
cont = 0
angle = 0

# Variáveis relacionadas ao botão - Acionamento Manual
button_pressed2 = 0
push_button2 = Pin(16, mode = Pin.IN)


# Variáveis relacionadas aos servo-motores
servo2_timer = machine.Timer(-1)
servo1 = Servo(pin_id = 1)
servo2 = Servo(pin_id = 2)


####################################################################################################################################################
## Definição de funções importantes ao código


# Definição das funções de handler do push_button, timer para a "volta" do servo2 e debounce do push_button

def push_button_handler(pin):
    
    # Definição de variáveis globais
    global servo2
    global servo2_timer
    
    # Ação a ser executada
    servo2.write(110)
    print("BOTÃO APERTADO")

    # Aciona o timer para a voltar para o estado original
    servo2_timer.init(mode=Timer.ONE_SHOT, period=1000, callback=servo2_timer_handler)

def servo2_timer_handler(timer):
    
    # Definição de variáveis globais
    global servo2
    
    # Ação a ser executada
    servo2.write(0)
        
def push_button_check(timer):

    # Definição das variáveis globais
    global push_button
    global button_pressed
    global push_button2
    global button_pressed2

    # Caso o botão esteja apertado...
    if push_button.value() == 1 and button_pressed == 0:
        
        # Faz a ação e seta botão apertado
        push_button_handler(push_button)
        button_pressed = 1
        
    # Caso não esteja apertado...
    elif push_button.value() == 0:
        
        # Reseta o botão apertado
        button_pressed = 0
        
    
    if push_button2.value() == 1 and button_pressed2 == 0:
        
        # Faz a ação e seta botão apertado
        push_button_handler(push_button)
        button_pressed2 = 1
        
    # Caso não esteja apertado...
    elif push_button2.value() == 0:
        
        # Reseta o botão apertado
        button_pressed2 = 0
        
        
# Definição das funções de decodificação do PWM

def inc_counter(timer):
    
    # Definição de variáveis globais
    global cont
    
    # Incrementa o contador com base no valor do pino
    cont += PWM.value()
    
    
def obtain_angle(pin):
    
    # Definição de variáveis globais
    global angle
    global cont
    
    # Calcula o valor do ângulo e insere no motor
    angle = cont * 0.1 * 90
    print(angle)
    servo1.write(angle)
    
    # Reseta o contador
    cont = 0


    
        
####################################################################################################################################################
## Código main


# Definição do timer do botão - Acionamento Automatico e Manual
button_timer.init(period=50, mode=machine.Timer.PERIODIC, callback=push_button_check)

# Definição do timer do PWM
PWM_timer.init(period=100, mode=machine.Timer.PERIODIC, callback=inc_counter)

# Seta a interrupção para reinício da contagem do PWM
PWM.irq(trigger=Pin.IRQ_RISING, handler=obtain_angle)







    


