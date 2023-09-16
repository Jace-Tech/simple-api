from flask import Flask, request, abort

app = Flask(__name__)
users = []

# FUNCTIONS
def response(message, data = None, success = True):
  return {
    "messsage": message,
    "data": data,
    "success": success
  }


@app.get("/")
def get_users():
  return response("All users", users), 200


@app.post("/create")
def create_user():
  data = request.get_json()
  if not data.get("name"): return abort(400, "Name is required")
  if not data.get("email"): return abort(400, "Email is required")
  if not data.get("password"): return abort(400, "Password is required")
  users.append(data)
  return response("User Created", data), 201


@app.errorhandler(400)
def handle_bad_request(error):
  print(error)
  return response(str(error).split(":")[1].strip(), success=False), 400



if __name__ == "__main__":
  app.run(debug=True)