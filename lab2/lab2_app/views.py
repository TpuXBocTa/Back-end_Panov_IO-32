from lab1_app import app
from datetime import datetime

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/healthcheck")
def health_check():
    return {
        "status": "OK",
        "timestamp": datetime.now(),
    }

@app.get("/user/<int:user_id>")
def read_person(user_id: int):
    user = Data.u_data.get(user_id)
    if user is None:
        return {"error": "user not found"}, 404
    return {"id": user_id, "user_name": user}, 200

@app.get("/users")
def read_people():
    return [{"id": i, "user_name": n} for i, n in Data.u_data.items()], 200

@app.post("/user")
def create_person():
    body = request.get_json()
    if not body or "name" not in body:
        return {"error": " not enough user data"}, 400
    uid = (max(Data.u_data.keys()) + 1) if Data.u_data else 1
    Data.u_data[uid] = body["name"]
    return {"id": uid, "user_name": body["name"]}, 201

@app.delete("/user/<int:user_id>")
def drop_person(user_id: int):
    name = Data.u_data.pop(user_id, None)
    if name is None:
        return {"error": "user not found"}, 404
    return {"result": f"id: {user_id} successfully deleted", "user_name": name}, 200

@app.get("/category")
def read_kinds():
    return [{"id": i, "category_name": n} for i, n in Data.c_data.items()], 200

@app.post("/category")
def create_kind():
    body = request.get_json()
    if not body or "name" not in body:
        return {"error": " not enough user data"}, 400
    cid = (max(Data.c_data.keys()) + 1) if Data.c_data else 1
    Data.c_data[cid] = body["name"]
    return {"id": cid, "category_name": body["name"]}, 201

@app.delete("/category")
def drop_kind():
    body = request.get_json()
    if not body or "id" not in body:
        return {"error": " incorrect id to delete category_data"}, 400
    cid = int(body["id"])
    name = Data.c_data.pop(cid, None)
    if name is None:
        return {"error": "category not found"}, 404
    return {"result": f"id: {cid} successfully deleted", "category_name": name}, 200