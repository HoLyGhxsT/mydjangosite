# Mydjangosite

My First Django Project.

## Getting Started

### Create Environment

Make a new environment **env** (or whatever name you prefer) using

```bash
py -m venv env
```

It is recommended that to create environment before pulling repo or outside the repo

### Activate Environment

Activate the environment on windows

```bash
env\Scripts\activate
```

Must be in the **env** folder to run this command

### Collect Static

Collect the static files to a pre-defined folder

```bash
py manage.py collectstatic
```

Must be inside project folder / Repo folder

### Run the server

Run the debug server

```bash
py manage.py runserver
```

you can specify desired port number after the command.
Default port is 8000.
