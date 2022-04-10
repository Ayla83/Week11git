
from application.models.address import Address
# from application.models.book import Book
# from application.models.member import Member
# from application.models.cat import Cat
# from application.models.info import Info
# from application.models.loan import Loan
# from application import db

def get_all_addresses():
    return Address.query.all()

# def get_member_by_id(id):
#     if id > 0:
#         return Member.query.get(id)
#     else:
#         return None
#
# def get_book_by_id(id):
#     if id < 100:
#         return Book.query.get(id)
#     else:
#         return None
