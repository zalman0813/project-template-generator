import os


class ProjectTemplate(object):
    def generate(self, project_name, dir_path):
        if not project_name:
            raise ValueError('No project name')
        os.mkdir(os.path.join(dir_path, project_name))
