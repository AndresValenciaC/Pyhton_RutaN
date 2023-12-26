import unittest
import os
from proyecto_final.DEVICES.generate_mission_files import Generate_Files

class TestGenerateFiles(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Generate files successfully
    def test_generate_files(self):
        generator = Generate_Files()
        result = generator.generate_files(3, 5)
        self.assertTrue(result,"Generate files was not successfully")

    # Create folders successfully
    def test_create_folders(self):
        num_files_from = 3
        num_files_to = 5
        generator = Generate_Files()
        generator.generate_files(num_files_from, num_files_to)
        output_directory = generator.create_output_directory(num_files_from)
        self.assertTrue(os.path.exists(output_directory), "Folders not created")

#if __name__ == '__main__':
    #unittest.main()