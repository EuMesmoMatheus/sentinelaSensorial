# Sentinela Sensorial

## Instituição

Catolica SC

## Integrantes

- Anna Beatriz Loz
- Cristian Domingues
- Lucas Gadonski
- Matheus Lofy
- Pablo Lopes

## Introdução

O projeto "Sentinela Sensorial" visa criar um sistema de segurança inteligente para salas de aula, utilizando tecnologias de IoT e inteligência artificial (IA). O objetivo é automatizar o monitoramento e a identificação dos alunos, melhorando a segurança e o registro de presença.

## Equipamentos Utilizados

- **Webcam do Notebook**: Captura imagens dos alunos ao detectar movimento.
- **Notebook/Computador com Acesso à Internet**: Utilizado para processamento das imagens e envio de notificações via e-mail.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para desenvolvimento do sistema.
- **Biblioteca `face_recognition`**: Responsável pelo reconhecimento facial dos alunos com base nas imagens capturadas.
- **Biblioteca `yagmail`**: Utilizada para envio de e-mails automáticos de notificações.
- **OpenCV**: Usada para captura de imagem e processamento adicional.

## Como o Projeto Funciona

### Componentes Utilizados

- **Webcam do Notebook**: Para capturar imagens de alunos ao detectar movimento.
- **Computador com Internet**: Para processamento de imagens e envio de notificações via e-mail.
- **Biblioteca de IA**: `face_recognition` para reconhecimento facial.

### Algoritmos de IA

- **Reconhecimento Facial**: A IA compara as imagens capturadas com as imagens dos alunos (armazenadas em uma pasta), reconhecendo quem está na sala.

### Fluxo de Informações

1. **Captura de Dados**:
   - A webcam do notebook detecta movimento e captura uma imagem, armazenando-a em uma pasta X.
2. **Processamento**:
   - O algoritmo de reconhecimento facial compara a imagem da pasta X com as imagens armazenadas na pasta Y (fotos dos alunos).
3. **Entrega de Resultados**:
   - Caso o rosto seja reconhecido, o sistema envia um e-mail ao professor com o nome do arquivo.
   - Caso o rosto não seja reconhecido, o sistema envia uma notificação de "pessoa não identificada" com a imagem capturada.

## Requisitos do Sistema

### Requisitos Funcionais

1. **Captura de Imagens**:<br> 
   1.1 O reconhecimento da FACE humana deverá ser feito com Biblioteca `face_recognition`.<br>
   1.2 A captura da imagem deverá ocorrer após o reconhecimento da FACE, através da biblioteca `OpenCV`.<br>
2. **Armazenamento de Imagens**:<br>
   2.1 A imagem capturada deverá ser armazenada em uma pasta "pasta x" local.<br>
3. **Identificação Facial**:<br>
   3.1 O sistema deverá comparar a face capturada, com todas as faces dos estudantes armazenadas em uma pasta local “Pasta Y”, utilizando a biblioteca `face_recognition`. <br>
3.2 O sistema deverá encontrar a imagem mais semelhante.<br>
4. **Envio de E-mails**:<br>
   4.1 Se o rosto for reconhecido, deverá enviar um e-mail para o responsável contendo: Dados da Imagem no Database (Pasta Y) + dia/mês/ano, hora:minutos + Foto Capturada. (Pasta X).<br>
   4.2 Se o rosto não for reconhecido, deverá enviar um e-mail para o responsável contendo: Mensagem de estudante não identificado + dia/mês/ano, hora:minutos + Foto Capturada. (Pasta X).<br>
4.3 Para o envio de e-mails, deverá ser utilizada a biblioteca `yagmail`<br>
5. **Armazenamento de Segurança**:<br>
   5.1 Ao fim do turno, as imagens armazenadas na pasta X deverão ser compactadas em um arquivo .zip para backup, após, a pasta X deverá ser limpa.<br>

### Requisitos Não Funcionais

1. **Precisão de Reconhecimento**:
   - O sistema deve garantir alta precisão no reconhecimento facial, com ajustes para qualidade de imagem e iluminação (Biblioteca `OpenCV`para pós processamento). 
2. **Capacidade de Processamento**:
   - O notebook/computador deve ter uma webcam com qualidade mínima de 720p.
3. **Segurança e Privacidade de Dados**:
   - As imagens e dados dos alunos devem ser protegidos durante o armazenamento e a transmissão de informações (via e-mail).
4. **Escalabilidade**:
   - O sistema deve ser escalável para lidar com um número crescente de alunos e imagens.
5. **Facilidade de Uso**:
   - O sistema deve ser simples de usar, com um fluxo de trabalho eficiente para professores e administradores.
6. **Disponibilidade**:
   - O sistema deve estar disponível durante todo o horário escolar, sem interrupções. (Backup de imagens apenas após as 23:00)
7. **Custo e Acessibilidade**:
   - O projeto deve ser acessível, utilizando interface simples e de fácil instalação.
8. **Tempo de Resposta**:
   - O sistema deve processar e enviar notificações em tempo hábil (preferencialmente em segundos).

## Benefícios do Projeto

- **Segurança Aumentada**: O sistema ajuda a identificar automaticamente alunos e alertar sobre a presença de indivíduos não identificados.
- **Automação**: O registro de presença é feito de forma automática, economizando o tempo dos professores.
- **Acessibilidade**: Utilização de equipamentos comuns, como webcams e notebooks, tornando a solução acessível.
  
## Desafios e Limitações

- **Precisão**: A precisão do reconhecimento facial pode ser afetada por iluminação e qualidade das imagens capturadas.
- **Capacidade de Processamento**: É necessário um hardware com capacidade suficiente para lidar com a IA.
- **Privacidade**: Garantir que os dados dos alunos sejam protegidos durante o processo de captura e envio.

## Como Executar o Projeto

### Pré-requisitos

Instale as dependências:

```bash
pip install -r requirements.txt
