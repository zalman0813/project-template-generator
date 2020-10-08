import glob
import os
import re


class ProjectTemplate(object):
    def generate(self, project_name, dir_path, template_dir=None):
        if not project_name:
            raise ValueError('No tests name')
        root_directory = f'{project_name}-project-development'
        os.mkdir(os.path.join(dir_path, root_directory))

        if template_dir:
            for file_path in glob.glob(os.path.join(template_dir, '*')):
                new_dir = os.path.join(dir_path, root_directory)
                search_end_idx = re.search('template/', file_path).end()
                new_path = os.path.join(new_dir, file_path[search_end_idx:]).replace('/project',
                                                                                     f'/{project_name}_project')
                object_name = file_path.split('/')[-1]
                if object_name == 'project' and os.path.isdir(file_path):
                    os.mkdir(new_path)
