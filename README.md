# Back-Office Application

This project is a example of a back-office application, built using the Python web framework Flask and the CSS framework Tailwind.

## Table of Contents

- [Back-Office Application](#back-office-application)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
    - [Running the application](#running-the-application)
  - [Built With](#built-with)
  - [Authors](#authors)
  - [License](#license)

## Features

- User management
- Data reporting
- Inventory management
- Other features (e.g. email campaigns, etc.)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Flask
- Tailwind
- MySQL database server
- Packages in requirements.txt

### Installing

Clone the repository

```bash
git clone https://github.com/valentin-dlack/backend-tailwind.git
```

Install the required packages

```py
pip install -r requirements.txt
```

Create a `.env` file in the root directory of the project and set the environment variables for your database configuration.

> Example :

```bash
DATABASE_HOST=localhost
DATABASE_USER=root
DATABASE_PASSWORD=123456
DATABASE_NAME=database_name
```

### Running the application

Build the CSS file :

```bash
npm run build
```

> If you want to watch for changes in the CSS files, run the following command instead :

```bash
npm run watch
```

Run the application :

```bash
flask run
```

Open your browser and navigate to `http://localhost:5000/admin` to access the application

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [Tailwind](https://tailwindcss.com/) - The CSS framework used
- [Python](https://www.python.org/) - The programming language used

## Authors

- **Valentin Dautrement** - *Web dev student* - [Lack](https://github.com/valentin-dlack)

## License

This project is licensed under the GNU v3 License - see the [LICENSE](LICENSE) file for details
