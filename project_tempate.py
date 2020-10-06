class ProjectTemplate(object):
    def generate(self, project_name):
        if not project_name:
            raise ValueError('No project name')
