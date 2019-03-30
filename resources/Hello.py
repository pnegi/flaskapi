from flask_restful import Resource


class Hello(Resource):
 def get(self):
        return {"message": "Hello GET, World!"}

 def post(self):
        return {"message": "Hello POST, World!"}
