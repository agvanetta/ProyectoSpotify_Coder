# ProyectoSpotify_Coder
Proyecto v1 (Pre entrega final) para el curso Python - Coderhouse

View: https://agvanetta.github.io/Spotify/

El proyecto utiliza Herencia HTML, Css, Djando Framework, Programacion orientada a objetos con Python como lenguaje de programación, SQLite, superusuario, interaccion con BD mediante GET y POST.


## A tener en cuenta:

1) Credenciales para administrar superusuario <br> 
Username : agvanetta <br> 
pw: agvanetta123

2) Funcionalidades<br> 
  A- Pestaña "Inicio" en sidebar: Muestra la "Home" de la aplicacion <br> 
  B- Pestaña "Buscar" en sidebar: Mediante el metodo GET permite buscar el perfil POR NUMERO DE DNI y renderizar abajo los datos del mismo, en caso de ingresar un DNI    que no esta en la BD arroja : " No se encontro el perfil con DNI "37732203", intente con otro numero de documento. " , si no se ingresan datos renderiza un HTML sin    style con la leyenda " No enviaste datos " (Volver atras en este caso). <br> 
  C- Pestaña "Agregar Perfil" en sidebar: Permite generar un nuevo perfil en la aplicacion, el mismo utiliza metodo post para enviar los datos a la BD.<br> 
  D- En el footer se encuentra disponible una cancion que al "navegar" por las distintas pestañas se reiniciara al tener que renderizar todo el html.<br> 
  E- Las pestañas Agregar a favoritos y subir contenido no estan disponibles en la V1, al ingresar veras la leyenda "Pendiente de desarrollo".<br> 
  
 3) Datos en la BD precargados (models):<br> 
  A- Contenido= Plan A / Paulo Londra / Cancion <br> 
  B- Favoritos= Chance / Paulo Londra / Sensillo <br> 
  C- Perfiles= 	<br> 
    Giovanni, Vanetta (DNI para buscar en la BD: 57353461) <br> 
    Agustin, Vanetta (DNI para buscar en la BD: 34440691) <br> 
    Luca, Vanetta (DNI para buscar en la BD: 1231273) <br> 

### Desarrollo: Agustín Vanetta
