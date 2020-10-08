import glob
import os
import re
from distutils.file_util import copy_file
from string import Template


class ProjectTemplate(object):
    def generate(self, project_name, dir_path, template_dir=None):
        if not project_name:
            raise ValueError('No tests name')
        root_directory = f'{project_name}-project-development'
        project_folder = project_name + '_project'
        os.mkdir(os.path.join(dir_path, root_directory))

        if template_dir:
            for file_path in glob.glob(os.path.join(template_dir, '*')):
                new_dir = os.path.join(dir_path, root_directory)
                search_end_idx = re.search('template/', file_path).end()
                new_path = os.path.join(new_dir, file_path[search_end_idx:]).replace('/project',
                                                                                     f'/{project_folder}')
                if os.path.isdir(file_path):
                    os.mkdir(new_path)
                elif os.path.isfile(file_path):
                    self.copy_file_from_template(file_path, new_path, project_folder)

    def copy_file_from_template(self, file_path, new_path, project_folder):
        with open(file_path, 'r') as f:
            lines = f.read()
        if '${project_name}' in lines:
            src = Template(lines)
            substitute = {'project_name': project_folder}
            with open(new_path, 'w') as outfile:
                outfile.write(src.substitute(substitute))
        else:
            copy_file(file_path, new_path)
