import random
import string

from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_project = app.project.get_project_list()
    project = Project(name=random_string("Name Project3", 10), status="release", inherit_global="checked", view_state="private",
                      description=random_string("Description", 10))
    app.project.create(project)
    new_project = app.project.get_project_list()
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

