from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost:3306/book_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author}

@app.route('/api/name', methods=['GET'])
def get_api_name():
    return jsonify({"name": "Book Management API"})

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    book.title = data['title']
    book.author = data['author']
    db.session.commit()
    return jsonify(book.to_dict())

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'}), 204

@app.route('/api/check-duplicate', methods=['POST'])
def check_duplicate():
    data = request.get_json()  # Get data from Postman

    title = data.get('title')
    author = data.get('author')
    duplicate_book = Book.query.filter_by(title=title, author=author).first()

    if duplicate_book:
        return jsonify({
            "message": "Duplicate book found.",
            "book": {
                "id": duplicate_book.id,
                "title": duplicate_book.title,
                "author": duplicate_book.author
            }
        }), 400  # 400 Bad Request
    else:
        return jsonify({"message": "No duplicate found."}), 200  # 200 OK

if __name__ == '__main__':
    with app.app_context():  # Create an application context
        db.create_all()  # Create database tables
    app.run(host='0.0.0.0', port=8080, debug=True)



