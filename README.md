- add to .gitignore: `__pycache__`, `**/__pycache`

- confirm pip3 w/ `pip3 --version`
  - get it from `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`, `python3 get-pip.py`
- `python3 -m venv virtual-environment`, confirm in file structure
- setting up a virtual virtual-environment
  - `which python3` should yield a system install like /usr/local/bin/python3
  - `source virtual-environment/bin/activate`
  - now `which python3` yields this specific folder
  - add `virtual-environment` to .gitignore

- `pip3 install alembic` will install into our virtual-environment/lib like node_modules

- `alembic init migrations`
  - look at folder
  - start trying to run `alembic upgrade head`, this is our finish line

- look at alembic.ini: this is a config file that includes a placeholder db url. we are going to replace this, but we don't want to hardcode it into this file.
  - install python-dotenv
  - look at env.py: this is the script that loads alembic.ini
  - top of env.py:
    from dotenv import load_dotenv
    load_dotenv()
    import os
  - after config = context.config:
    config.set_main_option('sqlalchemy.url', os.environ.get('DATABASE_URL'))
- make a .env with DATABASE_URL=postgresql://localhost:5432/python-db
- now `alembic upgrade head` yields a different error. (is it finding our db url? you can `print(os.environ.get('DATABASE_URL'))` in env.py to confirm that it is)
- new error is about psycopg2, pip3 install it
- now `alembic upgrade head` yields database "python-db" does not exist. create it w/ createdb or through psql
- now `alembic upgrade head` is rolling

- to make a migration: `alembic revision -m create-dinos
  - open that migration file in migrations/versions
  - put into upgrade function:
    ```
      op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False)
      )
    ```
  - optionally put into downgrade: `op.drop_table('users')`
  - `alembic upgrade head`; note also `alembic downgrade -1`
  - confirm table in psql

- making a model
  - `pip3 install flask_sqlalchemy`
  - make `models.py`and add
  ```
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()
  ```
  - add our model class
  ```
    class Dino(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String, nullable=False, unique=True)
      type = db.Column(db.String)
  ```

- db_test
  - can only run inside a flask application!
  - make `application.py`
  - skeleton:
  ```
    from flask import Flask
    app = Flask(__name__)

    import os
    from dotenv import load_dotenv
    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    import models
    models.db.init_app(app)

    def db_test():
      dino = models.Dino(
        name="Test Dino 2",
        type="Testing"
      )
      models.db.session.add(dino)
      models.db.session.commit()
      return 'ok'
    app.route('/db_test', methods=["GET"])(db_test)


    if __name__ == '__main__':
      port = int(os.environ.get('PORT', 5000))
      app.run(host='0.0.0.0', port=port, debug=True)
  ```
  - replace db_test route w/ different test commands: models.Dino.query.all(), models.Dino.query.where(), etc

