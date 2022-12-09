# Nonfollowers searcher


----

## Descripción

Sistema para detectar los usuarios que no te siguen de vuelta

### Requisitos

* Python 3.10

### Instalación

Crear un entorno virtual e instalar las dependencias.
```python
pip install -r requirements.txt
```

### Ejecutar el buscador


```sh
$ pyton run -h

usage: run.py [-h] -u USERNAME -p PASSWORD

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username to login
  -p PASSWORD, --password PASSWORD
                        Password to login

```

#### Ejemplo


```sh
$ python run -u <USERNAME> -p <PASSWORD>

[/usuario1/, /usuario2/, /usuario3/, /usuario4/]
```