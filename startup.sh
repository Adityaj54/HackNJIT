gunicorn -w 1 -k uvicorn.workers.UvicornWorker hacks.main:app
