from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()

class Product(db.Model, SerializerMixin):
    __tablename__ ="theragunProducts"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    classification=db.Column(db.String())
    compatible=db.Column(db.String())
    brand=db.Column(db.String())
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
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())


class ELectrotherapy(db.Model, SerializerMixin):
    __tablename__="electrotherapy"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class PortableElectrotherapy(db.Model, SerializerMixin):
    __tablename__="portableElectrotherapy"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class Shockwave(db.Model, SerializerMixin):
    __tablename__="shockwave & RPW"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class LightforceTherapy(db.Model, SerializerMixin):
    __tablename__="lightforceTherapy"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class VitalstimTherapy(db.Model, SerializerMixin):
    __tablename__="vitalstimTherapy"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class Tables(db.Model, SerializerMixin):
    __tablename__="tables"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class Mobility(db.Model, SerializerMixin):
    __tablename__="mobility"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class HotandCold(db.Model, SerializerMixin):
    __tablename__="hot and cold"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class Electrodes(db.Model, SerializerMixin):
    __tablename__="electrodes"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())

class Clinicsupplies(db.Model, SerializerMixin):
    __tablename__="clinicsupplies"
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price= db.Column(db.Integer())
    brand=db.Column(db.String())
    href=db.Column(db.String())
    description=db.Column(db.String())
    image=db.Column(db.String())



    
