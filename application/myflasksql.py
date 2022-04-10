from application import db
from application.models.address import Address
from application.models.book import Book
# from application.models.member import Member
# from application.models.cat import Cat
# from application.models.info import Info
# from application.models.loan import Loan
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:password@localhost/group_d_library', echo=False, future=True)
Session = sessionmaker(bind=engine)
session = Session()

address = session.query(Address).filter_by(id=1).first()
print(address.first_line, address.second_line, address.town, address.postcode)

for address in session.query(Address).all():
    print(address.first_line, address.postcode)

book = session.query(Book).filter_by(id=1).first()
print(book.book_title, book.author)


# team = Teams(affiliation='X-men', objective='Being eXXXtra cool')
# session.add(team)
# session.commit()

# hero = Heroes(name='Clinton Barton', alias='Hawkeye', superPower='Master Archer', teamID=4)
# session.add(hero)
# session.commit()

#
# hero = session.query(Heroes).filter_by(id=2).first()
# print(hero.name, hero.superPower, hero.alias, hero.teamID)
#
# hero = session.query(Heroes).filter_by(alias='Iron Man').first()
# print(hero.name, hero.superPower, hero.alias, hero.teamID)
#
# team = session.query(Teams).filter_by(id=4).first()
# print(team.affiliation, team.objective)
# for hero in team.heroes:
#     print(hero.name, '=', hero.alias)