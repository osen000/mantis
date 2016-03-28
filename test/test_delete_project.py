# -*- coding: utf-8 -*-

from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    if app.project.count_project() == 0:
        app.project.create(Project(name="test"))
    old_project = app.project.get_project_list()
    app.project.delete_project_by_id()
    assert len(old_project) - 1 == app.project.count_project()
    new_project = app.project.get_project_list()
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)




