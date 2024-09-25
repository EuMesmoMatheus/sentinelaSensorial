import yagmail

EMAIL_FROM = "contaemail776@gmail.com"  # E-mail do remetente
EMAIL_PASSWORD = "owfg ldlt wkvn bfbt"        # Senha do e-mail
EMAIL_TO = "lucasmotta-2011@hotmail.com"  # E-mail do destinatário

def enviar_email(assunto, mensagem, arquivos=None):
    yag = yagmail.SMTP(EMAIL_FROM, EMAIL_PASSWORD)

    try:
        if arquivos:
            # Enviar e-mail com anexo
            yag.send(to=EMAIL_TO, subject=assunto, contents=mensagem, attachments= arquivos)
        else:
            # Enviar e-mail sem anexo
            yag.send(to=EMAIL_TO, subject=assunto, contents=mensagem)
        
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
