from flask import Flask, jsonify, request
from models import db, User, Video, Comment

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

@app.route('/users/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/videos/upload', methods=['POST'])
def upload_video():
    # This will be more involved in a real application. You'd handle video uploads, save them, and kick off processing tasks.
    data = request.json
    video = Video(title=data['title'], description=data['description'], user_id=data['user_id'])
    db.session.add(video)
    db.session.commit()
    return jsonify({"message": "Video uploaded successfully!"}), 201

# ... more endpoints ...

if __name__ == '__main__':
    app.run(debug=True)
