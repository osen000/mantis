import random
from model.project import Project

class ProjectHelper:


    def __init__(self, app):
        self.app = app


    project_cache = None


    def open_manage_projects(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()


    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_projects()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector('a[href^="manage_proj_edit_page.php?project_id="]'):
                text = element.text
                href = element.get_attribute("href")
                id1 = href[75:]
                self.project_cache.append(Project(name=text, id=id1))
        return list(self.project_cache)

    def create(self, project):
        wd = self.app.wd
        self.open_manage_projects()
        # init creation
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        self.fill_project_form(project)
        # submit creation
        wd.find_element_by_css_selector('input[value="Add Project"]').click()
        self.project_cache = None


    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)
        self.change_field_value_no_text()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def change_field_value_no_text(self):
        wd = self.app.wd
        # enter status
        wd.find_element_by_xpath(".//*[@name='status']/option[@value='30']").click()
        # enter inherit_global
        wd.find_element_by_name("inherit_global").click()
        # enter view_state
        wd.find_element_by_xpath(".//*[@name='view_state']/option[@value='50']").click()


    def count_project(self):
        wd = self.app.wd
        self.open_manage_projects()
        # return len(wd.find_elements_by_name("selected[]"))
        return len(wd.find_elements_by_css_selector('a[href^="manage_proj_edit_page.php?project_id="]'))


    def select_project_by_id(self):
        wd = self.app.wd
        random.choice(wd.find_elements_by_css_selector('a[href^="manage_proj_edit_page.php?project_id="]')).click()
        return list(self.project_cache)


    def delete_project_by_id(self):
        wd = self.app.wd
        self.open_manage_projects()
        self.select_project_by_id()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        self.group_cache = None
