import yagmail

EMAIL_FROM = "contaemail776@gmail.com" 
EMAIL_PASSWORD = "owfg ldlt wkvn bfbt"    
EMAIL_TO = "lucasmotta-2011@hotmail.com"  

def enviar_email(assunto, mensagem, arquivos=None):
    yag = yagmail.SMTP(EMAIL_FROM, EMAIL_PASSWORD)

    try:
        if arquivos:
            # Enviar e-mail com anexo
            yag.send(to=EMAIL_TO, subject=assunto, contents=mensagem, attachments=arquivos)
        else:
            # Enviar e-mail sem anexo
            yag.send(to=EMAIL_TO, subject=assunto, contents=mensagem)
        
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
