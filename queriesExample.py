from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Restaurant, Base, MenuItem
 
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Get all veggie burgers
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
  print(veggieBurger.id)
  print(veggieBurger.price)
  print(veggieBurger.restaurant.name)
  print('\n')

# Select the specific one and update its price
UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 9).one()
print(UrbanVeggieBurger.price)
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()

# In case i needed to update all veggie burgers,
# i could use a for loop and then commit

# DELETE ITEM
# UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 9).one()
# session.delete(UrbanVeggieBurger)
# session.commit()

