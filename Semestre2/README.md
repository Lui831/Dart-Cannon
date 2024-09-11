# Tamakabin

**Tamakabin** é o projeto do 2° semestre da disciplina **Microcontroladores e Sistemas Embarcados** (EEN251) do **Instituto Mauá de Tecnologia** (IMT), ministrada pelos professores [Sergio Ribeiro Augusto](https://www.linkedin.com/in/sergio-ribeiro-augusto-258a9ba0/?originalSubdomain=br) e [Rodrigo França](https://www.linkedin.com/in/rodrigo-fran%C3%A7a-847872b1/).<BR>
Este repositório é responsável pela parte de IoT da aplicação. O front-end está [neste repositório](https://github.com/enzosakamoto/tamakabin-front).

<p align="center">
  <img width="910" alt="planta" src="https://github.com/user-attachments/assets/808cb715-9244-4dbf-bf49-f9812f788d3e">
</p>

## Sumário

- [Requisitos](#requisitos)
- [Escopo](#escopo)
  - [Diagrama de blocos](#diagrama-de-blocos)
  - [Tecnologias](#tecnologias-e-conceitos)
  - [Materiais](#materiais)
  - [Modelagem eletrônica](#modelagem-eletrônica)
  - [Modelagem financeira](#modelamento-financeiro)
- [Funcionamento](#funcionamento)
- [Testes](#testes)
- [Vídeo de funcionamento](#vídeo-de-funcionamento)
  - [Funcioamento simples](#seguidor-básico)
- [Foto da equipe](#foto-da-equipe)
- [Autores](#autores)

# Requisitos

| id  | requisito                                                                   | tipo      |
| --- | --------------------------------------------------------------------------- | --------- |
| 1   | Utilizar sensores digitais                                                  | Técnico   |
| 2   | Verificar a umidade da planta                                               | Funcional |
| 3   | Verificar a luminosidade incidida na planta                                 | Funcional |
| 4   | Verificar a temperatura                                                     | Técnico   |
| 5   | Utilizar padrões de comunicação HTTP ou MQTT                                | Técnico   |
| 6   | Comunicar-se com outro dispositivo                                          | Técnico   |

# Escopo

O projeto consiste em uma Raspberry Pi conectada à um vaso de planta que envia requisições com as informações que coleta dos sensores conectados aos pinos de GPIO.

## Diagrama de blocos

![diagrama_blocos_tamakabin drawio](https://github.com/user-attachments/assets/0b7b289f-1450-4077-9225-5b2d5da3ec60)


## Tecnologias e conceitos

- I2C (Comunicação com os displays e sensores)
- Transistores (MOSFET/Ponte H)
- PWM (Controle do motor)
- Requisições HTTP
- Banco de dados não relacional
- PIO (Entrada e saída do microprocessador)
- APIs
- Redes

## Materiais

O sistema é montado com os seguintes componentes:

- 1 microcomputador **Raspberry Pi 3 Model B+**
- 1 sensor de **umidade e temperatura** DHT22
- 1 Módulo **Sensor de Luminosidade** Luz LDR
- 1 Bomba d'água
- 1 MOSFETs IRLZ44N

## Modelagem eletrônica

O circuito utiliza diversos conceitos eletrícos e eletrônicos desenvolvidos durante o curso e em entidades acâdemicas relacionadas, como:

- MOSFETs para ativação das bombas
- Displays e sensores com comunicação I2C
- Conversão de sinais
- Regulação de tensão

<p align="center">
  <img width="910" alt="diagrama eletronico" src="https://github.com/user-attachments/assets/72ba51d3-3a49-4561-89fa-2963866ee962">
</p>


## Modelamento financeiro

Os componentes do projeto foram fornecidos pelo Instituto Mauá de Tecnologia. Para fins de teste, os equipamentos do Instituto Mauá de Tecnologia como multímetro, fonte e protoboard foram utilizados.<br>
| Componente         | Preço Estimado (BRL) |
|--------------------|----------------------|
| Raspberry Pi 3     | R$ 250,00 - R$ 350,00 |
| Sensor DHT22       | R$ 20,00 - R$ 40,00   |
| Módulo LDR         | R$ 5,00 - R$ 15,00    |

# Funcionamento

## Funcionamento da Aplicação

1. **Coleta de Dados pelos Sensores**
   - **DHT22**: Mede temperatura e umidade.
   - **LDR**: Mede a intensidade da luz.

2. **Processamento dos Dados na Raspberry Pi**
   - A Raspberry Pi lê os dados dos sensores e os processa (e.g., conversão de unidades).

3. **Envio de Dados via HTTP**
   - A Raspberry Pi envia os dados em formato JSON para uma API via requisição HTTP (`POST`).

4. **Tratamento e Uso dos Dados pela API**
   - A API armazena, processa ou aciona alertas com base nos dados recebidos.

5. **Possíveis Extensões**
   - Automação de ações (e.g., ligar ventilador, acender luzes) baseada nos dados dos sensores.

## Depuração

No projeto, a linguagem Python foi utilizada para a aplicação tanto por sua eficiência nesse tipo de caso de uso e também na variedade de bibliotecas que a linguagem oferece.

O `cmd` e as seguintes bibliotecas foram utilizadas para depurar o código:
- Adafruit_Python
- requests
- pymongo
  
## Diagrama de funcionamento

# Testes

## Dia 19/08/2024

- **Teste de funcionamento do sensor DHT22**

<p align="center">
  <img height="600" alt="testedht" src="https://github.com/user-attachments/assets/7335f450-3d8d-40ff-b1c1-6864b62ef15f">
</p>

## Dia 29/08/2024

- **Teste de funcionamento do Display e bomba**

https://github.com/user-attachments/assets/4b965cbf-abdd-4a26-8b6d-a66f4481a4f5

## Dia 04/09/2024 - Apresentação final
<p align="center">
   <img height="600" alt="testedht" src="https://img.youtube.com/vi/6dndOLTqGWo/0.jpg" href="https://youtu.be/6dndOLTqGWo">
</p>

## Foto da equipe

<p align="center">
  <img width="800" alt="kirby" src="https://github.com/user-attachments/assets/b4e1d8fe-257f-430c-bb13-04429a5ec331">
</p>

# Autores

- [Antonio Ferrite 21.00663-6](https://github.com/tom-ferrite) 
- [Enzo Sakamoto 21.00210-0](https://github.com/enzosakamoto) 
- [Flavio Murata 21.01192-3](https://github.com/flaviomurata)
- [Maria Fernanda Pinho 21.00256-8](https://github.com/mafepinho)
- [Pedro Matumoto 21.00784-5](https://github.com/pedromatumoto)
