# 🛡️ Atenea - Plataforma de Seguridad

Proyecto desarrollado en Flask para la gestión de usuarios, formularios y documentación de seguridad. Esta plataforma forma parte del sistema **Atenea**, diseñado para la atención y reporte de incidentes mediante una interfaz web ligera y funcional. PROXIMAMENTE EN APLICACION MOVIL...

## 📁 Estructura del Proyecto

```
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── templates/           # Archivos HTML (Jinja2)
├── usrs/                # Módulo para gestión de usuarios
├── venv/                # Entorno virtual (no subir a producción)
├── app.py               # Archivo principal de la app Flask
├── config.py            # Configuración de la base de datos
├── forms.py             # Formularios WTForms
├── harpo.py             # Modulo de seguridad en proteccion de datos (nombre misterioso 👀)
├── models.py            # Modelos de base de datos
├── try1.py              # Script de pruebas o prototipo
├── venv.env             # Archivo de entorno (revisar qué contiene)
├── README.md            # Este archivo XD
├── IEE830 Atenea.pdf    # Documento técnico o institucional
```

## ⚙️ Requisitos

- Python 3.8+
- pip
- Virtualenv

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

> Si agregaste nuevas librerias  y no aparecen en `requirements.txt`, puedes generarlo con:
> ```bash
> pip freeze > requirements.txt
> ```

## 🚀 Cómo ejecutar

1. Activa el entorno virtual (si no lo has hecho):
   ```bash
   source venv/bin/activate   # Linux/Mac
   .\venv\Scripts\activate    # Windows
   ```

2. Corre la app:
   ```bash
   python app.py
   ```

3. Abre tu navegador en [http://localhost:5000](http://localhost:5000)

## 🧠 Módulos clave

- `forms.py`: Define los formularios usados en la plataforma.
- `models.py`: Contiene los modelos para la base de datos (ORM).
- `usrs/`: gestión de usuarios.
- `harpo.py`: Funcionalidad de cifrados, creacion de directorios de usuario, etc...
- `config.py`: Configuraciones de la base de datos (entorno, claves, etc).

## 📝 Documentación

Consulta el archivo **IEE830 Atenea.pdf** para más detalles técnicos y de implementación.

## 🛡️ Seguridad

> Si usas información sensible, asegúrate de configurar correctamente variables de entorno y nunca subir tus claves o tokens al repositorio.

## 📌 Notas

- Evita subir la carpeta `venv/` al repositorio (usa `.gitignore`).
- `try1.py` parece ser un archivo de prueba, no incluir en producción.

## 📜 Licencia

Proyecto académico / institucional. Licencia a definir.
