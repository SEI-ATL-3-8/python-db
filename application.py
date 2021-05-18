from flask import Flask
app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

import models
models.db.init_app(app)

def db_test():
    #POST
    # owner1 = models.Owner(name="William",age=29)
    # owner2 = models.Owner(name="Jane", age=43)
    # owner3 = models.Owner(name="Yuki", age=67)

    # apt1 = models.Apartment(name="Archstone",units=20)
    # apt2 = models.Apartment(name="Zenith Hills",units=10)
    # apt3 = models.Apartment(name="Willowsprin",units=30)


    # models.db.session.add(owner1)
    # models.db.session.add(owner2)
    # models.db.session.add(owner3)

    # models.db.session.add(apt1)
    # models.db.session.add(apt2)
    # models.db.session.add(apt3)

    # models.db.session.commit()


    #GET
    #(1)Print all the data in the owners table.
    # owners = models.Owner.query.all()
    # print(owners)
    
    #(2)Print all the data in the apartments table.
    # apartments = models.Apartment.query.all()
    # print(apartments)


    #(3)Print just the names of all owners.
    owner1 = models.Owner.query.filter_by(name="William").first()
    owner2 = models.Owner.query.filter_by(name="Jane").first()
    owner3 = models.Owner.query.filter_by(name="Yuki").first()
    print(owner1)
    print(owner2)
    print(owner3)

    #(4)Print the names and ages of all owners who are older than 30.

    #(5)Look up William, save him to a variable, and print it

    #(6)Look up archstone, save it to a variable, and print it.

    #(7)Change Jane's age to 30.

    #(8)Change Jane's name to Janet.


    return 'ok'
app.route('/db_test', methods=["GET"])(db_test)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)