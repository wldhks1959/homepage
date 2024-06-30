from flask import Flask, render_template, request, redirect

app = Flask(__name__)

nextId = 4

projects_list = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 프로젝트 페이지
@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_list)

# 프로젝트 세부 페이지
@app.route('/project/<int:id>')
def project_detail(id):
    project = next((project for project in projects_list if project['id'] == id), None)
    return render_template('project_detail.html', project=project)

# 연락처 페이지
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        new_project = {'id': nextId, 'title': title, 'body': body}
        projects_list.append(new_project)
        nextId += 1
        return redirect('/projects')

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    project = next((project for project in projects_list if project['id'] == id), None)
    if request.method == 'GET':
        return render_template('update.html', project=project)
    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        project['title'] = title
        project['body'] = body
        return redirect('/projects')
    
@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    global projects_list
    projects_list = [project for project in projects_list if project['id'] != id]
    return redirect('/projects')

if __name__ == '__main__':
    app.run(port=5000, debug=True)