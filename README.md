# Sentinela Sensorial

## Instituição
Catolica SC

## Integrantes
- Anna Beatriz Loz
- Cristian Domingues
- Lucas Gadonski
- Matheus Lofy
- Pablo Lopes

## Introdução ao Projeto
O projeto "Sentinela Sensorial" visa criar um sistema de segurança inteligente para salas de aula, utilizando tecnologias de IoT e inteligência artificial (IA). Ele automatiza o monitoramento de alunos e o registro de presença, oferecendo maior segurança ao ambiente.

## Como o Projeto Funciona

### Componentes IoT:
- **Webcam do Notebook**: Captura imagens quando detecta movimento.
- **Computador com Internet**: Para processamento de imagens e envio de notificações.

### Algoritmos de IA:
- **Reconhecimento Facial**: IA compara imagens capturadas (armazenadas em uma pasta X) com imagens dos alunos (armazenadas na pasta Y), utilizando a biblioteca `face_recognition`.

## Fluxo de Informações

1. **Captura de Dados**: A webcam do notebook captura a imagem e a armazena na pasta X.
2. **Processamento**: O algoritmo de IA compara a imagem da pasta X com as imagens da pasta Y.
3. **Entrega dos Resultados**: O sistema envia um e-mail ao professor:
   - **Se o rosto for reconhecido**: Envia o nome do arquivo da imagem reconhecida.
   - **Se o rosto não for reconhecido**: Envia a imagem com uma descrição de "pessoa não identificada".

## Benefícios do Projeto
- **Segurança Aumentada**: Identificação automática de alunos.
- **Gestão Eficiente**: Registro automatizado de presença.
- **Solução Acessível**: Utilização de webcams e computadores comuns.

## Desafios
- **Precisão**: A precisão do reconhecimento facial pode ser afetada pela qualidade da imagem e iluminação.
- **Capacidade de Processamento**: O hardware precisa ter capacidade adequada para rodar os algoritmos de IA.
- **Privacidade**: Garantir a segurança dos dados dos alunos.
