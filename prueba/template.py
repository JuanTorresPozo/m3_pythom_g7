from string import Template



html = Template('''
<!DOCTYPE html>
<html lang="es">
    
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
</head>

<body>
    <h1>Aves de Chile</h1>

    $contenido

</body>
</html>                
''')

aves =Template('''
     <img src="$url_img" alt="$titulo_esp" width="250">
    <h2>$titulo_esp</h2>
    <h2>$titulo_en</h2>
    <hr>         
''')