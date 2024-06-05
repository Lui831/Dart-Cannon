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
from ssd1306 import *
from math import *


####################################################################################################################################################
# Definição de variáveis globais

# Variáveis relacionadas ao botão
button_pressed = 0
button_timer = machine.Timer(-1)
push_button = Pin(0, mode = Pin.IN, pull = Pin.PULL_UP)

# Variáveis relacionadas ao potenciômetro
pottentiometer = ADC(26)
pottentiometer_timer = machine.Timer(-1)
pottentiometer_values = []

# Variáveis relacionadas aos servo-motores

servo2_timer = machine.Timer(-1)
servo1 = Servo(pin_id = 1)
servo2 = Servo(pin_id = 2)

# Variáveis relacionadas ao display

i2c0_scl_pin = 17
i2c0_sda_pin = 16
i2c0 = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
display = SSD1306_I2C(128, 64, i2c0)
display_timer = machine.Timer(-1)

# Variáveis físicas do teste
Vo = 4.37373
d = 1.9
g = 9.81
deltaH = 0


####################################################################################################################################################
## Definição de funções importantes ao código


# Definição das funções de handler do push_button, timer para a "volta" do servo2 e debounce do push_button

def push_button_handler(pin):
    
    # Definição de variáveis globais
    global servo2
    global servo2_timer
    
    # Ação a ser executada
    servo2.write(110)

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

    # Caso o botão esteja apertado...
    if push_button.value() == 0 and button_pressed == 0:
        
        # Faz a ação e seta botão apertado
        push_button_handler(push_button)
        button_pressed = 1
        
    # Caso não esteja apertado...
    elif push_button.value() == 1:
        
        # Reseta o botão apertado
        button_pressed = 0
        
        
# Definição do handler para a medição do ADC conectado ao potenciômetro
        
def pottentiometer_handler(timer):
    
    global pottentiometer
    global servo1
    global pottentiometer_values
    
    # Insere o valor medido do ADC no início da lista de valores do potenciômetro
    pottentiometer_values.insert(0,pottentiometer.read_u16() * (-90/65535)+90) # pottentiometer.read_u16()*(-90/59500)+90
    print(pottentiometer.read_u16())

    
    # Caso a lista tenha 7 valores, exclui o valor final
    if len(pottentiometer_values) == 7:
        
        del(pottentiometer_values[-1])
        
    # Realiza a média móvel dos últimos valores armazenados na lista    
    pottentiometer_value = sum(pottentiometer_values)/len(pottentiometer_values)
    
    # Aciona o servomotor segundo o valor obtido pela média móvel
    servo1.write(pottentiometer_value)


# Definição do handler relacionado à exibição de deltaH no display

def display_handler(timer):
    
    global pottentiometer
    global deltaH
    global Vo, g, d
    
    # Calculo da variação de altura associada
    pottentiometer_value = sum(pottentiometer_values)/len(pottentiometer_values)
    deltaH = tan(radians(pottentiometer_value)) * d - (g/2) * ((d / (Vo * cos(radians(pottentiometer_value)))))**2
    
    # Caso deltaH seja menor que 0, assume-se variação de 0 metros
    if deltaH < 0:
        
        deltaH = 0
    
    # Reseta o displays
    display.fill(0)
    display.show()
    
    # Escreve o valor calculado de deltaH
    display.text("Angulo: %.1f" % pottentiometer_value, 20, 5)
    display.text("Variacao de", 20, 17)
    display.text("altura calculada:", 8, 29)
    display.text("%.3f" % deltaH, 27, 42)
    display.text("angulo em graus: %.3f" % pottentiometer_value, 20, 5)

    # Atualiza o display
    display.show()
    
        
####################################################################################################################################################
## Código main


# Definição do timer do botão
button_timer.init(period=50, mode=machine.Timer.PERIODIC, callback=push_button_check)

# Definição do timer do potenciômetro
pottentiometer_timer.init(period=200, mode=machine.Timer.PERIODIC, callback=pottentiometer_handler)

# Definição do timer do display
display_timer.init(period=500, mode=machine.Timer.PERIODIC, callback=display_handler)


    
