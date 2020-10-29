# Project Overview

This project is a template project to scaffold or create the initial structure of your domain app.

**PROJECT STRUCTURE**

| File Name        | Description                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------- |
| `└── tests/`     | _This folder should contains the tests for your domain app._                                |
| `crud.py`        | This file should contains the methods to perform the CRUD operations.                       |
| `filters.py`     | This file should contains the filters that you want to apply to your model.                 |
| `models.py`      | This file should contains the models of your domain app.                                    |
| `README.md`      | This file contains the documentation of this project.                                       |
| `schema.py`      | This file should contains the Queries and Mutations for your domain app.                    |
| `serializers.py` | This file should contains the serializers for your domain app.                              |
| `types.py`       | This file should contains the types that you want to expose in graphql for your domain app. |

# Scaffolding a domain app

```sh
django-admin startapp --template https://github.com/danilobrinu/django-graphql-domain-app-template/archive/master.zip post
```
