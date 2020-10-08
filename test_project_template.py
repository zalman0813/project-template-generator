import filecmp
import os
import shutil
import unittest

from project_tempate import ProjectTemplate


class ProjectTemplateTest(unittest.TestCase):

    def setUp(self):
        self.project_name = 'watson'
        self.template = ProjectTemplate()

    def tearDown(self):
        if os.path.exists(self.project_name):
            shutil.rmtree(self.project_name)

    def test_no_project_name(self):
        with self.assertRaises(ValueError):
            self.template.generate('', '.')

    def test_project_folder_exists_with_project_name(self):
        self.template.generate(f'{self.project_name}', '.')

        cmp = filecmp.dircmp(self.project_name, f'test_example/template_case1/{self.project_name}')
        self.assertEqual(cmp.diff_files, [])
        self.assertEqual(cmp.left_only, [])
        self.assertEqual(cmp.right_only, [])


if __name__ == '__main__':
    unittest.main()
