# README

## Crear la imagen

```bash
$ docker build -t ml .
```

## Crear un contenedor temporal

```bash
$ docker run --rm -v $(pwd):/home/juvyan/work -d -p 8888:8888 -d ml
```

## Mostrar contenedor activo

```bash
$ docker ps
```

## Ver logs del contenedor para Copiar token

```bash
$ docker logs nombre_contenedor
```
