from App import app  # App已成為package，因此可以引入(需有__init__.py)
from App.views.user import views  # 依層次引入
from flask import url_for
from jinja2 import TemplateNotFound

# index page
@app.route('/', methods=['GET'])  # 使用裝飾器定義路由
def index():
    return views.index()  # view去顯示根目錄(於views/user.py內撰寫

# Create new user page
@app.route('/new', methods=['GET'])
def new():
    url = url_for("create", id=id)
    return views.new(url)

# Create a new user
@app.route('/create', methods=['POST'])
def create():
    return views.create()

# show user data
@app.route('/<int:id>', methods=['GET'])
def show(id):
    try:
        url_update = url_for("edit", id=id)
        return views.show(id, url_update)
    except TemplateNotFound:
        return abort(404)

@app.route('/<int:id>/edit', methods=['GET'])
def edit(id):
    url_update = url_for("update", id=id)
    url_delete = url_for("destroy", id=id)
    return views.edit(id, url_update=url_update, url_delete=url_delete)

@app.route('/<int:id>', methods=['POST'])
def update(id):
    views.update(id)
    return "User update successful"

@app.route('/<int:id>/delete', methods=['POST'])
def destroy(id):
    views.destroy(id)
    return "User deleted"
