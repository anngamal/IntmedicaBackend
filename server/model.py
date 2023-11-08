from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()
from sqlalchemy.orm import validates
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


bcrypt = Bcrypt()

class Theragun(db.Model, SerializerMixin):
    __tablename__ ="theragunProducts"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

    def __repr__(self):
        return f"<Product {self.name}>"
    

class Theraface(db.Model, SerializerMixin):
    __tablename__="therafaceProducts"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class Waveseries(db.Model, SerializerMixin):
    __tablename__="waveseriesProducts"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class Recoveryair(db.Model, SerializerMixin):
    __tablename__="recoveryairProducts"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class Powerdot(db.Model, SerializerMixin):
    __tablename__="powerdotProducts"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class Recoverytherm(db.Model, SerializerMixin):
    __tablename__="recoverythermProducts"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class Smartgoggles(db.Model, SerializerMixin):
    __tablename__="smartgogglesProducts"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class Theracup(db.Model, SerializerMixin):
    __tablename__="theracupProducts"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class ELectrotherapy(db.Model, SerializerMixin):
    __tablename__="electrotherapy"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class PortableElectrotherapy(db.Model, SerializerMixin):
    __tablename__="portableElectrotherapy"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class Shockwave(db.Model, SerializerMixin):
    __tablename__="shockwave & RPW"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class LightforceTherapy(db.Model, SerializerMixin):
    __tablename__="lightforceTherapy"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class VitalstimTherapy(db.Model, SerializerMixin):
    __tablename__="vitalstimTherapy"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class Tables(db.Model, SerializerMixin):
    __tablename__="tables"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class Mobility(db.Model, SerializerMixin):
    __tablename__="mobility"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class HotandCold(db.Model, SerializerMixin):
    __tablename__="hot and cold"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class Electrodes(db.Model, SerializerMixin):
    __tablename__="electrodes"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())
 



# //in the navbar ineed to call my check session function and say if thry logged ,
#  send a fetch request to check if i got 200 error or 401 if it is 200 change sign in to logout 

class Clinicsupplies(db.Model, SerializerMixin):
    __tablename__="clinicsupplies"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    category=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class Products(db.Model, SerializerMixin):
    __tablename__ ="products"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())
    category=db.Column(db.String())
    
    carts = db.relationship('Cart', back_populates='product')


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    _password_hash = db.Column(db.String())
    firstName =db.Column(db.String())
    lastName= db.Column(db.String())
    phoneNumber= db.Column(db.Integer())

    carts = db.relationship('Cart', back_populates='user')

   
    @property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, new_pass):
        self._password_hash = bcrypt.generate_password_hash(new_pass.encode('utf-8')).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, 
            password.encode('utf-8')
        )
    
       
    carts = db.relationship('Cart', back_populates='user')
  



# class Cart
# product table foreign key 
# user table foreign key 
# quantity 


class Cart (db.Model, SerializerMixin):
    __tablename__="carts"
    id = db.Column(db.Integer(), primary_key=True)
    quantity = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    product = db.relationship('Product', back_populates='carts')
    user =db.relationship('User', back_populates='carts')




# // app routing for cart 
# add route (post)
# add get  route by user id to get the info of the cart about the user  which 


    
