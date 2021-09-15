from flask import Flask
from flask_restful import Api, Resource, abort, marshal_with
from flask_sqlalchemy import SQLAlchemy
from util import getVideoPutArgs, getVideoUpdateArgs, resource_fields
from helloworld import HelloWorld

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"


db.create_all()

video_put_args = getVideoPutArgs()
video_update_args = getVideoUpdateArgs()


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with id " + str(video_id))
        return result

    @marshal_with(resource_fields)
    def post(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken...")

        video = VideoModel(
            id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()

        return result

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot delete")

        db.session.delete(result)
        db.session.commit()
        return "delete success", 200


class Videos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = VideoModel.query.all()
        print(result)
        if not result:
            abort(404, message="No Videos Found!")
        return result


api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(Videos, "/videos")
api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)
