# *Dart Cannon v0.1*

### **Descrição Geral**

Repositório para o armazenamento de arquivos, *datasheets*, esquemáticos e códigos referentes ao primeiro projeto semestral da disciplina Microcontroladores e Sistemas Embarcados.

### **Integrantes da Equipe**

- João Vitor Choueri Branco;
- Luiz Henrique Antoniassi Santos;
- Pedro Afonso Wirthmann Dian;
- Vitor Guirão Soller;

---

### **Descrição do Projeto**

O projeto visa a criação de um canhão lançador de projéteis leves, o *`Dart Cannon`*, o qual teria somente **um** grau de liberdade (atira projéteis somente em um plano pré-determinado) e **calcularia** a trajetória do projeto a ser atirado segundo uma referência específica.

### **Lista de Componentes**

- *Raspberry* PI Pico;
- 2 x Servo Motor MG996;
- Display OLED I²C 128x32 Pixels;
- Potenciômetro de 10k ohms;
- *Push-button*;
- Fonte de alimentação 5V/2A;

### **Diagrama de Blocos Lógicos**

Com base nas proposições realizadas, pode-se estruturar o seguinte diagrama que representa a estrutura lógica do *`Dart Cannon`*:

![Imagem1](./Images/DartCannon.png)

### **Esquema Elétrico**

![Imagem2](./Images/Esquemático-Completo.png)

### **Organização das Tarefas**

- <u>Organização e implementação do *hardware*</u>: término do esquemático e teste do hardware físico implementado (sem o Raspberry Pi Pico);
- <u>Idealização da arquitetura de *software* e teste</u>: criação de um código em *MicroPython* que garanta o funcionamento integral do canhão. Em primeira instância, os *inputs* seriam compostos principalmente pelo teclado e os *outputs* por *prints*.
- <u>Teste integral de *software* e *hardware*</u>: readaptação do *software* criado para *inputs* e *outputs* do Raspberry Pi Pico, aplicação neste e implementação junto ao *hardware*. Poderão ser testados alguns casos específicos de manuseio do canhão.
- <u>Implementação com parte mecânica e teste final</u>: junção da parte mecânica do projeto com sua parte eletrônica, realizando os testes finais de validação e verificando se a adição de inércia mecânica não interfere no funcionamento dos servo-motores.

## Imagem do Grupo

![Imagem3](./Images/Grupo.png)

## Vídeo Explicativo


https://github.com/Lui831/Dart-Cannon/assets/81604963/2cd243e0-ed82-4f9d-b0a3-4bb92a8a0a49


