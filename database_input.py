from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Catalog_db import Catalog, Base, Items, User

engine = create_engine('sqlite:///ItemsCatalog.db')
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


# Create dummy user
User1 = User(name="Hassan Gamal", email="hassangamal358@gmail.com",
             picture='https://avatars2.githubusercontent.com/u/10533500?s=400&u=6c76671520d7b69bdc14885c8c813bcc6ade8475&v=4')
session.add(User1)
session.commit()

User2 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User2)
session.commit()


# Menu for Hotels
catalog1 = Catalog(user_id=1, name="Hotels",
                   picture='https://www.flightexpert.com/blog/wp-content/uploads/2017/11/Dhaka-Hotels.jpg')

session.add(catalog1)
session.commit()

item1 = Items(user_id=1, name="Dhaka", description="this is Dhaka Hotels",
                     price="$7.50", picture='https://www.flightexpert.com/blog/wp-content/uploads/2017/11/Dhaka'
                                            '-Hotels.jpg', catalog=catalog1)

session.add(item1)
session.commit()

item2 = Items(user_id=1, name="Dhaka", description="this is Dhaka Hotels",
                     price="$7.50", picture='https://www.flightexpert.com/blog/wp-content/uploads/2017/11/Dhaka'
                                            '-Hotels.jpg', catalog=catalog1)

session.add(item2)
session.commit()

item3 = Items(user_id=1, name="Dhaka", description="this is Dhaka Hotels",
                     price="$7.50", picture='https://www.flightexpert.com/blog/wp-content/uploads/2017/11/Dhaka'
                                            '-Hotels.jpg', catalog=catalog1)

session.add(item3)
session.commit()
item4 = Items(user_id=1, name="Dhaka", description="this is Dhaka Hotels",
                     price="$7.50", picture='https://www.flightexpert.com/blog/wp-content/uploads/2017/11/Dhaka'
                                            '-Hotels.jpg', catalog=catalog1)

session.add(item4)
session.commit()

item5 = Items(user_id=2, name="Dhaka", description="this is Dhaka Hotels",
                     price="$7.50", picture='https://www.flightexpert.com/blog/wp-content/uploads/2017/11/Dhaka'
                                            '-Hotels.jpg', catalog=catalog1)

session.add(item5)
session.commit()

item6 = Items(user_id=2, name="Dhaka", description="this is Dhaka Hotels",
                     price="$7.50", picture='https://www.flightexpert.com/blog/wp-content/uploads/2017/11/Dhaka'
                                            '-Hotels.jpg', catalog=catalog1)

session.add(item6)
session.commit()


# Menu for Foods
catalog2 = Catalog(user_id=1, name="Foods",
                   picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106edca1ba048c4df3cbda1b6ff2a9e67'
                           '.jpg_facebook.jpg')


session.add(catalog2)
session.commit()

item1 = Items(user_id=1, name="Foods", description="this is Foods List",
                     price="$7.50", picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106edca1ba048c4df3cbda1b6ff2a9e67'
                           '.jpg_facebook.jpg', catalog=catalog2)
session.add(item1)
session.commit()

item2 = Items(user_id=1, name="Foods", description="this is Foods List",
                     price="$7.50", picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106edca1ba048c4df3cbda1b6ff2a9e67'
                           '.jpg_facebook.jpg', catalog=catalog2)
session.add(item2)
session.commit()


item3 = Items(user_id=1, name="Foods", description="this is Foods List",
                     price="$7.50", picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106edca1ba048c4df3cbda1b6ff2a9e67'
                           '.jpg_facebook.jpg', catalog=catalog2)
session.add(item3)
session.commit()


item4 = Items(user_id=1, name="Foods", description="this is Foods List",
                     price="$7.50", picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106edca1ba048c4df3cbda1b6ff2a9e67'
                           '.jpg_facebook.jpg', catalog=catalog2)
session.add(item4)
session.commit()

item5 = Items(user_id=1, name="Foods", description="this is Foods List",
                     price="$7.50", picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106edca1ba048c4df3cbda1b6ff2a9e67'
                           '.jpg_facebook.jpg', catalog=catalog2)
session.add(item5)
session.commit()

item6 = Items(user_id=2, name="Foods", description="this is Foods List",
                     price="$7.50", picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106edca1ba048c4df3cbda1b6ff2a9e67'
                           '.jpg_facebook.jpg', catalog=catalog2)
session.add(item6)
session.commit()

item7 = Items(user_id=2, name="Foods", description="this is Foods List",
                     price="$7.50", picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106edca1ba048c4df3cbda1b6ff2a9e67'
                           '.jpg_facebook.jpg', catalog=catalog2)
session.add(item7)
session.commit()






print "added menu items!"
