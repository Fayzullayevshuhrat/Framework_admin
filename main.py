from app import FrameWorkApp
import json

app = FrameWorkApp()


def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)
    return users


def load_views():
        with open("views.json", "r") as file:
            return json.load(file)


def save_views(views):
    with open("views.json", "w") as file:
        json.dump(views, file)


def increase_view(path):
    views = load_views()
    views[path] = views.get(path, 0) + 1
    save_views(views)


@app.route("/home")
def home(request, response):
    increase_view("/home")

    with open("id.json", "r") as file:
        cnt = json.load(file)
    cnt += 1

    response.text = f"Home pagedan alangali salom! -> {cnt}"

    with open("id.json", "w") as file:
        json.dump(cnt, file)


@app.route("/about")
def about(request, response):
    increase_view("/about")
    response.text = "About pagedan alangali salom!"


@app.route("/u/{login}")
def get_info(request, response, d):
    path = f"/u/{d.get('login')}"
    increase_view(path)

    users = load_users()
    user = users.get(d.get("login", -1), "Bunday user yo'q!")

    response.text = json.dumps(user)


@app.route("/admin/{login}")
def get_admin(request, response, d):
    path = f"/admin/{d.get('login')}"
    increase_view(path)

    response.text = f"Admin page {d.get('login', -1)}"


@app.route("/status")
def status(request, response):
    views = load_views()
    stats_text = "Status: "
    for path, count in views.items():
        stats_text += f"{path} - {count} marta ko'rilgan\n"

    response.text = stats_text
