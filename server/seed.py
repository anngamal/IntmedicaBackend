from model import *
from app import app
# app.config["SQLALCHEMY_DATABASE_URI"] = "your_database_uri_here"



with app.app_context():

    productTable = Theragun.query.all()
    for item in productTable:
        prod=Products(
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
       


    productTable = Theraface.query.all()
    for item in productTable:
        prod=Products(
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        

    productTable = Waveseries.query.all()
    for item in productTable:
        prod=Products(
       
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
    


    productTable = Recoveryair.query.all()
    for item in productTable:
        prod=Products(
 
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()


    productTable = Powerdot.query.all()
    for item in productTable:
        prod=Products(
        
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
  

    productTable = Smartgoggles.query.all()
    for item in productTable:
        prod=Products(
    
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
   

    productTable = Theracup.query.all()
    for item in productTable:
        prod=Products(
        
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
       
    productTable = ELectrotherapy.query.all()
    for item in productTable:
        prod=Products(
     
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)

    productTable = PortableElectrotherapy.query.all()
    for item in productTable:
        prod=Products(
    
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)

    productTable = Shockwave.query.all()
    for item in productTable:
        prod=Products(
 
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)

    productTable = LightforceTherapy.query.all()
    for item in productTable:
        prod=Products(
          
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)


    productTable = VitalstimTherapy.query.all()
    for item in productTable:
        prod=Products(
           
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)

    productTable = Tables.query.all()
    for item in productTable:
        prod=Products(
       
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)

    productTable = Mobility.query.all()
    for item in productTable:
        prod=Products(
         
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)

    productTable = HotandCold.query.all()
    for item in productTable:
        prod=Products(
        
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)

    productTable = Electrodes.query.all()
    for item in productTable:
        prod=Products(
         
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)

    productTable = Clinicsupplies.query.all()
    for item in productTable:
        prod=Products(
 
            name=item.name,
            price=item.price,
            classification= item.classification,
            compatible=item.compatible,
            brand=item.brand,
            href= item.href,
            description= item.description,
            image= item.image,
            category=item.category
        )
        db.session.add(prod)
        db.session.commit()
        print(prod)


    # db.session.commit()

    # print("Seeding... complete.")
   