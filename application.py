from flask import Flask, jsonify
app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

import models
models.db.init_app(app)

def db_test():
  # dino = models.Dino(
  #   name="Test Dino 2",
  #   type="Testing"
  # )
  # models.db.session.add(dino)
  # models.db.session.commit()

  # dinos = models.Dino.query.all()
  # print(dinos)

  # dinos = models.Dino.query.filter_by(name="Test Dino 2").first()
  # dinos = models.Dino.query.filter_by(id=2).all()
  # print(dinos)

  # dino = models.Dino.query.filter_by(id=1).first()
  # dino.name = dino.name + '!!!'
  # models.db.session.add(dino)
  # models.db.session.commit()

  # dino = models.Dino.query.filter_by(id=1).first()
  # models.db.session.delete(dino)
  # models.db.session.commit()

  # dino = models.Dino(
  #   name = 'Testing Dino',
  #   type = 'Testing'
  # )
  # category = models.Category(
  #   name = 'Test Category'
  # )
  # models.db.session.add(dino)
  # models.db.session.add(category)
  # models.db.session.commit()

  # dino = models.Dino.query.first()  
  # category = models.Category.query.first()
  # dinos = category.dinos
  # parent_cat = dino.category
  # print(dino, category, dinos, parent_cat)


  # dino = models.Dino.query.first()  
  # category = models.Category.query.first()
  # associating
  # category.dinos.append(dino) # OR dino.category = category
  # disassociating
  # dino.category_id = None
  # models.db.session.add(dino)
  # models.db.session.commit()
  
  return 'ok'
app.route('/db_test', methods=["GET"])(db_test)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
