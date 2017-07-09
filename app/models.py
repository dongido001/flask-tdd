
# app/models.py

from app import db

class CommentCategory(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'comment_category'

    id = db.Column(db.Integer, primary_key=True)
    comment_category = db.Column(db.String(255))
    created_by = "" #for now let it be empty
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, created_by, comment_category):
        """initialize with name."""
        self.created_by = created_by
        self.comment_category = comment_category

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return CommentCategory.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<CommentCategory: {}>".format(self.comment_category, self.created_by)


class CommentObject(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'comment_object'

    id = db.Column(db.Integer, primary_key=True)
    object_type = db.Column(db.String(255))
    created_by  = db.Column(db.String(255))
    category_id  = db.Column( db.Integer )
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, object_type, category_id):
        """initialize with name."""
        self.object_type = object_type
        self.category_id = category_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return CommentObject.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<CommentObject: {}>".format(self.category_id, self.object_type)


class Comments(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer )
    comment = db.Column(db.String(255) )
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, category_id, object_id, comment):
        """initialize with name."""
        self.comment = comment
        self.category_id = category_id
        self.object_id = object_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Comments.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Comments: {}>".format(self.comment, self.object_id, self.category_id)