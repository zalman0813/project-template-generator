import filecmp
import os
import shutil
import unittest

from project_tempate import ProjectTemplate


class ProjectTemplateTest(unittest.TestCase):

    def setUp(self):
        self.project_name = 'watson'
        self.root_directory = f'{self.project_name}-project-development'
        self.template = ProjectTemplate()

    def tearDown(self):
        if os.path.exists(self.root_directory):
            shutil.rmtree(self.root_directory)

    def test_no_project_name(self):
        with self.assertRaises(ValueError):
            self.template.generate('', '.')

    def test_if_root_folder_exists_with_project_name(self):
        self.template.generate(f'{self.project_name}', '.', None)
        self.template_should_be_equal('template_case1')

    def test_if_project_folder_exists_with_project_name(self):
        self.template.generate(f'{self.project_name}', '.', 'test_example/template_case2/template')
        self.template_should_be_equal('template_case2')

    def test_if_other_folder_exists_with_project_name(self):
        self.template.generate(f'{self.project_name}', '.', 'test_example/template_case3/template')
        self.template_should_be_equal('template_case3')

    def test_if_a_file_without_keyword_exists(self):
        self.template.generate(f'{self.project_name}', '.', 'test_example/template_case4/template')
        self.template_should_be_equal('template_case4')

    def test_if_a_file_with_keyword_exists(self):
        self.template.generate(f'{self.project_name}', '.', 'test_example/template_case5/template')
        self.template_should_be_equal('template_case5')

    def template_should_be_equal(self, test_case):
        cmp = filecmp.dircmp(self.root_directory, f'test_example/{test_case}/{self.root_directory}')
        self.assertEqual(cmp.diff_files, [])
        self.assertEqual(cmp.left_only, [])
        self.assertEqual(cmp.right_only, [])


if __name__ == '__main__':
    unittest.main()
