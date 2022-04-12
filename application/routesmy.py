import json

from flask import render_template, jsonify

from application import app, servicemy


@app.route('/home/address', methods=['GET'])
def show_addresses():
    error = ""
    address = servicemy.get_all_addresses()
    if len(address) == 0:
        error = "There are no addresses to display"
    return render_template('address.html', address=address, message=error)


@app.route('/home/library_member/<int:this_id>', methods=['GET'])
def show_member(this_id):
    error = ""
    check_member = servicemy.get_member_by_id(this_id)
    if not check_member:
        return jsonify("There is no member with ID: " + str(this_id))
    return jsonify(check_member)


@app.route('/home/books', methods=['GET'])
def show_books():
    error = ""
    details = servicemy.display_books()
    if len(details) == 0:
        error = "There are no books to display"
    return render_template('book.html', books=details, message=error)


@app.route('/book/<int:book_id>', methods=['GET'])
def show_book(book_id):
    error = ""
    check_id = servicemy.get_book_by_id(book_id)
    if not check_id:
        return jsonify("There are no books with ID: " + str(book_id))
    return jsonify(check_id)


@app.route('/booksbygenre/<int:genre_id>', methods=['GET'])
def book_genre(genre_id):
    error = ""
    kind = servicemy.get_book_by_genre(genre_id)
    if not kind:
        error = "There is no book with genre: " + str(genre_id)
    return render_template('books_by_genre.html', genre=kind, message=error, title="Books by genre")


# @app.route('/hero/<int:hero_id>', methods=['GET'])
# def show_hero(hero_id):
#     error = ""
#     hero = service.get_hero_by_id(hero_id)
#     print(hero.name, hero.alias)
#     if not hero:
#         return jsonify("There is no heroes with ID: " + str(hero_id))
#     return jsonify(hero)
#
#
# @app.route('/teamandheroes/<int:team_id>', methods=['GET'])
# def team_and_heroes(team_id):
#     error = ""
#     team = service.get_team_by_id(team_id)
#     if not team:
#         error = "There is no team with ID: " + str(team_id)
#     return render_template('teams_and_heroes.html', team=team, message=error, title="Team and its Heroes")


