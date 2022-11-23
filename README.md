# A simple authentication functionality implemented with Flask

This is a webapp showcasing a bare minimum auth functionality.
The main ingredient is Flask. On top of that, we use the Flask-Session
extension to keep login data across a session. For the database, we're
using sqlite. (python supports sqlite with the built-in sqlite3 module)

## To clone and run the app ...
 - First, well, clone it : ) and go into the cloned directory
 - Create a new python virtual environment with `python3 -m venv [env_name]` and activate the environment.
 - Download the dependencies listed in the requirements.txt file manually or just do `pip install -r requirements.txt`
 - In a terminal window, do `flask run`
 - Open your browser and navigate to the url mentioned in the terminal.
 - You'll run into a problem while trying to register or login. This is because the database is not set up yet. Hit the "/setup" route and the database will be set up automatically.

### EXTRA
 - If you want to change the database file or switch between databases, edit the `DATABASE_FILE_NAME = "test_database.db"` line in the database_helper.py file and hit the "/setup" url again.

### FINALLY
This is probably the minimal auth functionality one can implement. It lacks many important things like password hashing. DO NOT use it without modification for any real world application.