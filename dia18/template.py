from string import Template

#paso 1

html = Template('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
</head>
<body>
    <h1> Aves de chile</h1>
    
</body>
</html>
          
                ''')

aves = Template('''
<img> src= "$url" alt= $titulo_esp"
    <h2>"aguiluchoChico"</h2>
    <h2></h2>
                
                
                ''')