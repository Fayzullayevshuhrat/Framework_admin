from app import FrameWorkApp
import json

app = FrameWorkApp()


def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)
    return users


def load_admins():
    with open("admin.json", "r") as file:
        admins = json.load(file)
    return admins


@app.route("/home")
def home(request, response):
    response.text = "Home pagedan alangali salom!"


@app.route("/about")
def about(request, response):
    response.text = "About pagedan alangali salom!"


@app.route("/u/{id}")
def get_info_users(request, response, id):
    users = load_users()
    user = users.get(id)

    if user:
        response.text = json.dumps(user, indent=4)
    else:
        response.text = "Bunday user yo'q!"

@app.route("/a/{id}")
def get_info_admins(request, response, id):
    admins = load_admins()
    admin = admins.get(id)

    if admin:
        response.text = json.dumps(admin)
    else:
        response.text = "Bunday admin yo'q!"