
# from bookproject import app
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash

from flask import  Blueprint
from .extensions import mongo



bp=Blueprint('bp',__name__)
@bp.route("/add",methods=["POST"])
def add_user():
    _json=request.json
    _bookname=_json['bookname']
    _pages=_json['pages']
    _price=_json['price']
    _author=_json['author']

    if _bookname and _pages and _price and _author and request.method == 'POST':
        mongo.db.book.insert({'bookname': _bookname, 'pages': _pages, 'price': _price,'author':_author})
        resp = jsonify("User Added Successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@bp.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


# search in bookilist

@bp.route('/booklist',methods=['GET'])
def users():
     
    bookname=request.args.get('bookname')
    author=request.args.get('author')
    
    if author or bookname:
        output = []    

        for q in mongo.db.book.find({"$or":[{'bookname':bookname},{'author':author}]}):   
            output.append({'bookname' : q['bookname'], 'author' : q['author'],'price' : q['price'],'pages' : q['pages']})
        if len(output)!=0 :
            return jsonify({'result' : output})
        else:
            return jsonify({'result' : 'No Results Found'})
    else:     
        users=mongo.db.book.find()
        resp=dumps(users)
        return resp                 
            

@bp.route('/book/<id>',methods=["GET"])
def user(id):
    user=mongo.db.book.find_one({'_id':ObjectId(id)})
    resp=dumps(user)
    return resp


@bp.route('/bookupdate/<id>',methods=["PUT","PATCH"])
def update_book(id):
    _id=id 
    _json=request.json
    
    if _json and  request.method == 'PATCH' or request.method=="PUT":
        mongo.db.book.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                         {'$set':_json})   
        resp=jsonify("book updated successfully!!")
        resp.status_code = 200
        return resp
    else:
        return not_found()



@bp.route('/bookdelete/<id>',methods=["DELETE"])
def delete_user(id):
    user=mongo.db.book.delete_one({'_id':ObjectId(id)})
    resp=jsonify("book deleted successfully!!")

    resp.status_code=200
    return resp



# @app.route('/search', methods = ['GET'])
# def search():
#     search = mongo.db.Book
#     bookname=request.args.get('bookname')
#     author=request.args.get('author')

#     output = []
#     for q in search.find({"$or":[{'bookname':bookname},{'author':author}]}):   
#         output.append({'bookname' : q['bookname'], 'author' : q['author']})
#     if len(output)!=0 :
#         return jsonify({'result' : output})
#     else:
#         return jsonify({'result' : 'No Results Found'})




# search in booklist
# @app.route('/booklist',methods=['GET'])
# def users():
#     b=request.args.get('bookname')
#     a=request.args.get('author')
            
#     if a or b  is not None:       
#         a1=mongo.db.book.find({"$or":[{'author':a},{'bookname':b}]})
#         output = []
#         for author in a1:
#             output.append({'bookname' : author['bookname'], 'author' : author['author'],'pages' : author['pages'],'price' : author['price']})
                
#         if len(output)!=0 :
#             return jsonify({'result' : output})
#         else:
                            
#             return jsonify({'result' : 'No Results Found'})
#     else:
            
#         users=mongo.db.book.find()
#         resp=dumps(users)
#         return resp                 











