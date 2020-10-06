import unittest

from project_tempate import ProjectTemplate


class ProjectTemplateTest(unittest.TestCase):

    def test_no_project_name(self):
        template = ProjectTemplate()
        with self.assertRaises(ValueError):
            template.generate('')


if __name__ == '__main__':
    unittest.main()
