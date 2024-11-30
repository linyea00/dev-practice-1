# DevSecOps en Sistemas Autónomos

## Práctica 1

En este repositorio se han creado los siguientes workflows de GitHub:

### CI/CD Pipeline [![CI/CD Pipeline](https://github.com/linyea00/dev-practice-1/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/linyea00/dev-practice-1/actions/workflows/ci-cd.yml)

Este workflow se lanza cada vez que se hace push en la rama main. Se ejecuta en la última versión disponible de Ubuntu y realiza los siguientes pasos:
- Checkout del repositorio.
- Construcción de la imagen de Docker a partir del Dockerfile.
- Ejecución del contenedor de Docker.
- Espera de 5 segundos hasta que el contenedor está disponible.
- Comprobación de que la aplicación ha arrancado correctamente a través de un curl.
- Limpieza del entorno. Detención del contenedor y eliminación de la imagen creada.


### Code Quality [![Code Quality](https://github.com/linyea00/dev-practice-1/actions/workflows/code-quality.yml/badge.svg)](https://github.com/linyea00/dev-practice-1/actions/workflows/code-quality.yml)

Este workflow se lanza cada vez que se hace push en la rama main. Se ejecuta en la última versión disponible de Ubuntu y realiza los siguientes pasos:
- Checkout del repositorio.
- Configuración del entorno Python 3.10.
- Instalación de dependencias.
- Ejecución de la herramienta flake8 para comprobar errores de sintaxis, nombres no definidos, etc.
- Ejecución de la herramienta bandit para comprobar la seguridad del código.
- Ejecución de test mediante pytest.