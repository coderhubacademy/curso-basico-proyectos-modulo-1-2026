## Proyecto Final Individual — Módulo 1  
### Ruta Software Developer Nivel 1

Este proyecto final tiene como objetivo que cada estudiante aplique de forma práctica los conocimientos vistos durante el Módulo 1, desarrollando una aplicación de consola en Python dentro de su carpeta asignada en este repositorio.

Cada estudiante tendrá un proyecto específico asignado y deberá construir una solución funcional, organizada y correctamente versionada usando Git y GitHub.

---

## Fecha de entrega

**Miércoles 01 de abril de 2026**

---

## Objetivo general

Desarrollar una aplicación de consola en Python que permita demostrar el manejo de fundamentos de programación, organización del código, persistencia en archivos y uso correcto del flujo de trabajo con Git y Pull Request.

---

## Requisitos generales del proyecto

Tu proyecto debe:

- estar desarrollado en **Python**,
- ejecutarse en **consola**,
- estar construido **únicamente dentro de tu carpeta asignada**,
- resolver el problema planteado en tu archivo `requerimientos.md`,
- aplicar los conocimientos vistos en clase,
- guardar la información usando archivos **`.json` o `.txt`**,
- estar versionado correctamente con **Git**,
- entregarse mediante **Pull Request**.

---

## Contenidos que deben aplicarse

Tu proyecto debe evidenciar el uso de los siguientes temas:

- variables y tipos de datos,
- operadores,
- condicionales,
- ciclos,
- funciones,
- listas y/o diccionarios,
- modularización del código,
- manejo de archivos,
- persistencia de datos en `.json` o `.txt`.

---

## Requerimientos funcionales mínimos

Como mínimo, tu proyecto debe incluir:

- un **menú principal en consola**,
- una opción para **registrar información**,
- una opción para **listar información**,
- una opción para **buscar información**,
- una opción para **editar al menos un registro**,
- una opción para **eliminar al menos un registro**,
- lectura de datos al iniciar el programa,
- guardado de datos en archivo al realizar cambios.

---

## Reglas de trabajo en el repositorio

Cada estudiante debe:

- clonar este repositorio en su computadora,
- trabajar **solo dentro de su carpeta asignada**,
- crear una **rama propia** para desarrollar el proyecto,
- realizar commits frecuentes con mensajes claros,
- subir su rama al repositorio remoto,
- crear un **Pull Request** para revisión.

### Creacion de una rama

- git checkout -b: crea una rama y cambia a ella
- git branch: lista las ramas
- git checkout: cambia de rama
- git add: agrega archivos al stage
- git commit: guarda los cambios
- git push: sube los cambios al repositorio
- git pull: descarga los cambios del repositorio

Ejemplo de creacion de una rama:
```bash
git checkout -b proyecto-[nombre]-[apellido]
```

### Regla importante
No debes trabajar directamente sobre la rama principal.

---

## Convención sugerida para la rama

Debes crear una rama con un nombre claro.  
Formato sugerido:

```bash
feature/nombre-apellido-proyecto-final
```

---

## Reglas para commits

Se espera que hagas commits frecuentes y con mensajes entendibles.

Ejemplos:

```bash
git commit -m "feat: crear estructura inicial del proyecto"
git commit -m "feat: agregar menu principal"
git commit -m "feat: implementar guardado en archivo json"
git commit -m "fix: corregir validacion del menu"
git commit -m "docs: actualizar informacion del proyecto"
```

Evita hacer un solo commit al final con todo el proyecto.

---

## Reglas del Pull Request

La entrega oficial del proyecto será mediante Pull Request.

Debes cumplir con lo siguiente:

- el Pull Request debe ser creado con al menos 3 días de anticipación a la fecha de entrega.
- el PR debe estar abierto como máximo el domingo 29 de marzo de 2026.
- el Pull Request debe tener al menos 2 revisiones de compañeros.
- esas revisiones pueden ser:
  - aprobaciones, o
  - solicitudes de cambio.
- debes atender las observaciones que recibas si aplica.
- el proyecto no se considerará correctamente entregado sin un PR abierto y revisado.
- el merge final se hará con la aprobación correspondiente del profesor o responsable.

---

## Flujo de trabajo sugerido

1. Clona el repositorio.
2. Entra en tu carpeta asignada.
3. Crea tu rama de trabajo.
4. Desarrolla tu proyecto paso a paso.
5. Realiza commits frecuentes.
6. Sube tu rama al repositorio remoto.
7. Abre tu Pull Request antes de la fecha límite indicada.
8. Solicita revisión a compañeros.
9. Atiende observaciones si te solicitan cambios.
10. Espera la revisión final.

---

## Qué sí puedes usar

Está permitido:

- Python estándar,
- consola,
- funciones propias,
- módulos separados en varios archivos `.py`,
- archivos `.json` o `.txt` para guardar datos,
- estructuras como listas y diccionarios,
- validaciones de datos,
- Git y GitHub para versionado,
- apoyo de IA solo como herramienta de consulta, explicación o ayuda para entender errores.

---

## Qué no puedes usar

No está permitido:

- usar frameworks web como Flask, Django o similares,
- usar bases de datos SQL,
- usar interfaces gráficas,
- trabajar fuera de tu carpeta asignada,
- editar el trabajo de otros compañeros,
- subir el proyecto directamente a la rama principal,
- copiar proyectos completos de internet,
- generar todo el proyecto con IA sin comprenderlo,
- entregar solo código sin haber abierto el Pull Request.

---

## Uso responsable de IA

Puedes apoyarte en herramientas de IA para:

- entender errores,
- pedir explicaciones de conceptos,
- revisar ideas de mejora,
- resolver dudas puntuales de sintaxis o lógica.

No debes usar IA para:

- generar el proyecto completo sin entenderlo,
- copiar y pegar código sin revisarlo,
- sustituir tu proceso de aprendizaje.

Recuerda que debes poder explicar tu proyecto y defender las decisiones tomadas.

---

## Criterios generales de evaluación

Se tomará en cuenta:

- funcionamiento del proyecto,
- correcta aplicación de los fundamentos,
- organización del código,
- manejo de archivos,
- claridad de la lógica,
- uso adecuado de Git y commits,
- apertura correcta del Pull Request,
- revisiones entre compañeros,
- cumplimiento de la fecha de entrega.

---

## Entrega final

Tu proyecto será considerado entregado únicamente si:

- está desarrollado dentro de tu carpeta asignada,
- está subido a tu rama correspondiente,
- el Pull Request fue abierto dentro del plazo indicado,
- el PR tiene al menos 2 revisiones de compañeros,
- el proyecto ejecuta correctamente.