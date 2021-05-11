## ¿Cuál es estado actual?
Cada vez que revisamos los archivos `analyses.json` prestamos atención a dos puntos:
    - [ ] Los objetivos del `Makefile` están en `analyses.json` en orden alfabético y sin ruta
    - [ ] Pasa el `geci-checkanalyses`
    
 Entonces tenemos, de alguna manera, dos archivos para contrastar su contenido. Con el `Makefile` generamos nuestros reportes y los resultados necesarios para los  reportes. Cada uno de los elementos del `analyses.json` es un reporte.  Cada  elemento del `analyses.json` tienen las secciones `data`, `scripts` y `results`.

En la sección `data` ponemos en una lista los datos (crudos) que ocupamos para generar el reporte (a veces los resultados). En `scripts` todos los archivos de código que intervienen para generar el reporte. En `results` solo agregamos las tablas, figuras y _json_'s que agregamos al reporte. En `results` no deberían de venir los resultados intermedios.  
# Check analyses

## ¿Cuál es el problema?
En este momento para revisar los archivos `analyses.json` hacemos usos de instrucciones desde la línea de comando como `cat analyses.json | jq '.[1]["results"]' | grep ".png"`:
![image](https://user-images.githubusercontent.com/35377740/117888558-1b0acb80-b267-11eb-843f-2c273a1d9bcc.png)
con lo que obtenemos una lista de los figuras que tenemos en `analyses.json`. Para saber si todas esas figuras están en el reporte correspondiente corremos la instrucción `grep ".png" reports/estimacion_poblacional_petrel_san_benito.tex | cut -d "/" -f 2 | cut -d "}" -f 1`:
![image](https://user-images.githubusercontent.com/35377740/117889091-d29fdd80-b267-11eb-9e38-d8c6da29ed0c.png)
En el recuadro rojo viene el nombre del reporte. Ese nombre también lo podríamos obtener de la sección `reports` de cada elemento del `analyses.json`.
