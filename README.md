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

## Como o Projeto Funciona

### Componentes Utilizados
- **Webcam do Notebook**: Para capturar imagens de alunos ao detectar movimento.
- **Computador com Internet**: Para processamento de imagens e envio de notificações via e-mail.
- **Biblioteca de IA**: `face_recognition` para reconhecimento facial.

### Algoritmos de IA:
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
1. **Captura de Imagens**: <br> 
   1.1 *Reconhecimento de FACE feito com Biblioteca `face_recognition`.*
   1.2 *Captura da Imagem deve ocorrer após reconhecimento de FACE.*
2. **Armazenamento de Imagens**:
   2.2 *Armazenamento de Imagem em repositorio no ambiente local "pasta x"*
3. **Identificação Facial**:
   3.1 *Utilizar imagem armazenada para validação facial com database.*
   3.2 *Consulta em database local, com imagens dos estudantes "pasta y".*
   3.3 *Utilização da biblioteca `face_recognition` para percorrer todas as imagens cadastradas no database e encontrar a mais semelhante.*
4. **Envio de E-mails**:
   4.1 *Quando rosto é reconhecido, enviar e-mail para responsavel contento: Dados da Imagem no Database (Pasta Y) + dia/mês/ano, hora:minutos + Foto Capturada. (Pasta X).*
   4.2  *Quando rosto não é reconhecido, enviar e-mail para responsavel contento: Mensagem de estudante não identificado + dia/mês/ano, hora:minutos + Foto Capturada. (Pasta X).*
5. **Armazenamento de Segurança**:
   5.1 *TODO fim de turno, os arquivos armazenados na pasta X, será feito um backup das imagens do dia é criado uma pasta de backup (.zip), após armazenamento pasta X é limpa.*

### Requisitos Não Funcionais
1. **Precisão de Reconhecimento**:
   - O sistema deve garantir alta precisão no reconhecimento facial, com ajustes para qualidade de imagem e iluminação (Implementação em PYTHON).
2. **Capacidade de Processamento**:
   - O notebook/computador deve ter uma webcam com qualidade semelhante a 720p.
3. **Segurança e Privacidade de Dados**:
   - As imagens e dados dos alunos devem ser protegidos durante o armazenamento e a transmissão de informações (via e-mail).
4. **Escalabilidade**:
   - O sistema deve ser escalável para lidar com um número crescente de alunos e imagens.
5. **Facilidade de Uso**:
   - O sistema deve ser simples de usar, com um fluxo de trabalho eficiente para professores e administradores.
6. **Disponibilidade**:
   - O sistema deve estar disponível durante todo o horário escolar, sem interrupções. (Backup de Imagens apenas após as 23:00)
7. **Custo e Acessibilidade**:
   - O projeto deve ser acessível, utilizando interface simples e facil instalação.
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

### Pré-requisitos:

Instale as dependências:

```bash
