# Flask Blueprint

[![](https://travis-ci.org/presethub/flask-boilerplate.svg?branch=master)](https://travis-ci.org/presethub/flask-boilerplate)
[![](https://img.shields.io/badge/license-mit-green.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg?style=flat-square)]([https://git/](https://github.com/presethub/flask-boilerplate))

## What's in the box?

- Flask 1.0.2 + TailwindCSS 1.0.1 + jQuery 3.4.1
- Authentication using email or username.

## Quick Start

At least you will need `Python >= 3.6` and `Nodejs >= 8.15`. For database backend, you can choose between
`MariaDB >= 10.3` or `MySQL >= 5.7` or `PostgreSQL >= 9.6` or any other database engine that supported by Flask.

### Create New Project

You will need [degit](https://github.com/Rich-Harris/degit): `npm install -g degit`

```sh
degit https://github.com/presethub/flask-boilerplate.git myproject
cd myproject && python -m venv venv
```

Don't forget to change `myproject` with your own.

### Start Developing

Inside your project directory, edit or create `.env` file and then execute:

```bash
source venv/bin/activate
pip install -r requirements.txt

cd app
gunicorn -b 127.0.0.1:5000 main

deactivate
```

Default user is `admin@mail.com` and `secret` for the password.

## License

Licensed under the terms of [MIT License][choosealicense]. See [license file](./license.txt) for more information.

[choosealicense]:https://choosealicense.com/licenses/mit/
