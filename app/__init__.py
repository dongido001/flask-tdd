
# app/__init__.py

from flask import request, jsonify, abort
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy


# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

#imports all the models we are using.

from app.models import CommentCategory
from app.models import CommentObject
from app.models import Comments

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/comment_category', methods=['POST', 'GET'])
    def Comment_category():

        if request.method == "POST":
            comment_category = str(request.form.get('comment_category', ''))
            if comment_category:
                comment_category = CommentCategory(comment_category=comment_category,\
                 created_by='')
                comment_category.save()
                response = jsonify({
                    'id': comment_category.id,
                    'comment_category': comment_category.comment_category,
                    'date_created': comment_category.date_created,
                    'date_modified': comment_category.date_modified
                })
                response.status_code = 201
                return response
        else:
            comment_categories = CommentCategory.get_all()
            results = []
            for comment_category in comment_categories:
                obj = {
                    'id': comment_category.id,
                    'comment_category': comment_category.comment_category,
                    'date_created': comment_category.date_created,
                    'date_modified': comment_category.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response


    @app.route('/comment_object', methods=['POST', 'GET'])
    def Comment_object():
        if request.method == "POST":
            category_id = int(request.form.get('category_id', ''))
            object_type = str(request.form.get('object_type', ''))
            if category_id and object_type:
                comment_object = CommentObject(object_type=object_type,category_id=category_id)
                comment_object.save()
                response = jsonify({
                    'id': comment_object.id,
                    'category_id': comment_object.category_id,
                    'object_type': comment_object.object_type,
                    'date_created': comment_object.date_created,
                    'date_modified': comment_object.date_modified
                })
                response.status_code = 201
                return response
        else:
            comment_objects = CommentObject.get_all()
            results = []

            for comment_object in comment_objects:
                obj = {
                    'id': comment_object.id,
                    'category_id': comment_object.category_id,
                    'object_type': comment_object.object_type,
                    'date_created': comment_object.date_created,
                    'date_modified': comment_object.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response


    @app.route('/comment', methods=['POST', 'GET'])
    def Comment():
        if request.method == "POST":
            category_id = int(request.form.get('category_id', ''))
            object_id   = int(request.form.get('object_id', ''))
            comment     = str(request.form.get('comment', ''))
            if category_id and object_id and comment:
                comment = Comments(object_id=object_id,category_id=category_id, comment=comment)
                comment.save()
                response = jsonify({
                    'id': comment.id,
                    'category_id': comment.category_id,
                    'object_id': comment.object_id,
                    'comment': comment.comment,
                    'date_created': comment.date_created,
                    'date_modified': comment.date_modified
                })
                response.status_code = 201
                return response
        else:
            comments = Comments.get_all()
            results = []

            for comment in comments:
                obj = {
                    'id': comment.id,
                    'comment': comment.comment,
                    'object_id': comment.object_id,
                    'category_id': comment.category_id,
                    'date_created': comment.date_created,
                    'date_modified': comment.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response


    @app.route('/comment_category/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def comment_category_rud(id, **kwargs):
     # retrieve a comment category using it's ID
        comment_category = CommentCategory.query.filter_by(id=id).first()
        if not comment_category:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            comment_category.delete()
            return {
            "message": "comment_category {} deleted successfully".format(comment_category.id) 
         }, 200

        elif request.method == 'PUT':
            comment_cat = str(request.data.get('comment_category', ''))
            comment_category.comment_category = comment_cat
            comment_category.save()
            response = jsonify({
                'id': comment_category.id,
                'comment_catgory': comment_category.comment_category,
                'date_created': comment_category.date_created,
                'date_modified': comment_category.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': comment_category.id,
                'comment_catgory': comment_category.comment_category,
                'date_created': comment_category.date_created,
                'date_modified': comment_category.date_modified
            })
            response.status_code = 200
            return response
            
    return app