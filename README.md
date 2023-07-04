# SQL Master
SQL Master is a Python project that allows you to manipulate relational databases by writing SQL scripts and displaying the results in a tkinter-based frontend. It provides a convenient way to interact with databases and perform various operations.

## Features

1. Write and execute SQL scripts: SQL Master enables you to write SQL queries and execute them directly from the tkinter frontend. It supports a wide range of SQL operations, including querying, updating, and deleting data from relational databases.

2. Frontend display: The project provides a user-friendly tkinter-based interface where you can input your SQL scripts and view the results in a formatted and organized manner. This allows for easier data exploration and analysis.

3. Connection persistence: SQL Master includes a JSON file, `last_connection.json`, that stores the details of the last established database connection. On subsequent launches of the code, the connection information is automatically pre-populated in the frontend, saving you time and effort.

4. Test database included: The project also contains a folder named `tests` that includes a script for creating a sample SQLite database. This database includes a table named "People" with sample information that you can use to test the code. This allows you to experiment with SQL queries and operations without connecting to an external database.

## Instalation

To get started with SQL Master, follow these steps:

1. Download or clone the "SQLMaster" folder from the repository.

2. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

3. Configure the settings (optional): If you need to customize certain aspects of the project, you can modify the `settings.py` file according to your requirements. This file contains various configurations such as database connection details, frontend settings, and other options.

## Usage

1. Ensure that you have a relational database accessible and its connection details handy.

2. Run the run.py file to start the application:

```bash
python run.py
```

3. The tkinter-based frontend window will open, displaying the SQL Master interface.

4. Connect to a database: If it's your first time using SQL Master, you will need to input the database connection details manually in the frontend. However, on subsequent launches, the information will be pre-filled based on the last saved connection in `last_connection.json`.

5. Write and execute SQL scripts: Once connected, you can enter your SQL scripts in the provided input area and execute them using the corresponding button. The results will be displayed in the frontend window, allowing you to analyze and manipulate the data conveniently.

6. Explore additional functionalities: SQL Master offers additional features such as exporting query results, managing database schemas, and performing database operations beyond basic querying. You can explore these capabilities within the project's intuitive tkinter-based interface.

7. Test with sample data: If you want to experiment with the included test database, select `SQLite` in the connection form and provide the path to the SQLite database file. After clicking the `Connect` button, the database will be accessible for queries. You can then write and execute SQL scripts to interact with the sample data in the database.

## Customization

1. You can customize various aspects of the SQL Master project by modifying the `settings.py` file. This file allows you to adjust parameters such as the database connection details, frontend appearance, and other configurations to suit your needs.

2. Please refer to the comments within the `settings.py` file for detailed instructions on how to modify each setting.
