# mlOpsStack

## Docker

Quick dockerized setup for development (Django web + FastAPI backend).

Build the images:

```bash
docker-compose build
```

Start the services:

```bash
docker-compose up
```

This exposes:
- Django app: http://localhost:8000
- FastAPI backend: http://localhost:8002

Notes:
- The project uses SQLite files located in the repository; bind mounts are used so database files remain on the host.
- `torch` may require platform-specific wheels; if you encounter build errors, install a matching CPU wheel or remove `torch` from `requirements.txt` and install it manually on the host.
