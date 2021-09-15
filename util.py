from flask_restful import reqparse, fields


def getVideoPutArgs():
    video_put_args = reqparse.RequestParser()

    video_put_args.add_argument(
        "name", type=str, help="Name of the video is required", required=True)
    video_put_args.add_argument(
        "views", type=int, help="Views of the video is req", required=True)
    video_put_args.add_argument(
        "likes", type=int, help="Likes on the video is req", required=True)

    return video_put_args


def getVideoUpdateArgs():

    video_update_args = reqparse.RequestParser()
    video_update_args.add_argument(
        "name", type=str, help="Name of the video is required")
    video_update_args.add_argument(
        "views", type=int, help="Views of the video")
    video_update_args.add_argument(
        "likes", type=int, help="Likes on the video")

    return video_update_args


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}
