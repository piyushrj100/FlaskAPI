import re
from flask import Flask, request
from flask_restful import Api, Resource,reqparse, abort, fields,marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views =db.Column(db.Integer, nullable = False)
    likes=db.Column(db.Integer,nullable=False)

    def __repr__(self) :
        return f"Video(name={self.name},views={self.views}, likes={self.likes})"
# db.create_all()  it was used first time to create the model now after every run not needed


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the Video is required", required=True, location='form')
video_put_args.add_argument("views", type=str, help="views of the Video", required=True,location='form')
video_put_args.add_argument("likes", type=str, help="Likes of the Video", required=True, location='form')

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the Video is required", location='form')
video_update_args.add_argument("views", type=str, help="views of the Video",location='form')
video_update_args.add_argument("likes", type=str, help="Likes of the Video", location='form')

video_get_args=reqparse.RequestParser()
#location as args will parse from the query string
video_get_args.add_argument("name", type=str, help="name required", location='args',required=True)
video_get_args.add_argument("views", type=str, help="name required",location='args',required=True)

# def abort_if_video_doesnt_exist(video_id) :
#     if video_id not in videos :
#         abort(404,message="Video is not valid")

# def abort_if_video_exists(video_id) :
#     if video_id in videos :
#         abort(400, message="Video already exists...")

resource_fields ={
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer

}

class Video(Resource) :

    @marshal_with(resource_fields)
    def get(self, video_id) :
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result :
            abort(404, message="Could not find Video Id....")
        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id) :
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result :
            abort(409, message="Video id already exists...")

        video = VideoModel(id=video_id,name = args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
        
    @marshal_with(resource_fields)
    def patch(self, video_id) :
        args=video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result :
            abort(404, message="Video does not exist! Cannot update..")
        if args['name'] :
            result.name=args['name']
        if args['views'] :
            result.views=args['views']
        if args['likes'] :
            result.likes=args['likes']
        db.session.commit()
        return result
    

    @marshal_with(resource_fields)
    def  delete(self,video_id) :
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result :
            abort(403)
        db.session.delete(result)
        db.session.commit()
        return '', 204

class video_info(Resource) :
        
        @marshal_with(resource_fields)              
        def get(self) :
            parsed=video_get_args.parse_args() 
            result = VideoModel.query.filter_by(name=parsed["name"]).filter_by(views=parsed["views"]).all()
            if not result :
                abort(400, message="Not found!!!!")
            return result

class all_video_info(Resource) :
    @marshal_with(resource_fields)
    def get(self) :
        results = VideoModel.query.all()
        if not results :
            abort(404, message="No video exists!!....")
        return results



            
        

api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(video_info, "/video")
api.add_resource(all_video_info,"/video/")

if __name__ == "__main__" :
    app.run(debug=True) 

