from string import Template


html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Pajaros de Chile</title>
                            </head>
                            <body>

                            <h1>Nuestra página Web</h1>

                            $body

                            </body>
                            </html>
                        ''')

print(html_template.substitute(body = imagen))
"""
lista_url = [elemento['url'] for elemento in response]
texto_img = ''

for url in lista_url:
    texto_img += img_template.substitute(url = url) +'\n'

print(texto_img)

html = html_template.substitute(body = texto_img)
print(html)
 """ 
with open('output.html', 'w') as f:
    f.write(html)
  