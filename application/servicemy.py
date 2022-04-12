
from application.models.address import Address
from application.models.book import Book
from application.models.library_member import LibraryMember
# from application.models.cat import Cat
# from application.models.info import Info
# from application.models.loan import Loan
# from application import db


def get_all_addresses():
    return Address.query.all()


def get_member_by_id(this_id):
    if this_id > 0:
        return LibraryMember.query.get(this_id)
    else:
        return None

# Emma's book searches
def display_books():
    # books = db.session.query(Book)
    return Book.query.all()


def get_book_by_id(book_id):
    if book_id > 0:
        return Book.query.get(book_id)
    else:
        return None


def get_book_by_genre(genre_id):
    return Book.query.filter_by(genre=genre_id).first()


#
# def get_book_by_id(id):
#     if id < 100:
#         return Book.query.get(id)
#     else:
#         return None
