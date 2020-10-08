import unittest

from project_tempate import ProjectTemplate


class ProjectTemplateTest(unittest.TestCase):

    def setUp(self):
        self.template = ProjectTemplate()

    def test_no_project_name(self):
        with self.assertRaises(ValueError):
            self.template.generate('')



if __name__ == '__main__':
    unittest.main()
