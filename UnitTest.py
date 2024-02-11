import unittest

from DataLoader import files, data


class MyTestCase(unittest.TestCase):
    def test_dataloader_file(self):
        message = "There are no files in the folder"
        self.assertTrue(files, message)

    def test_dataloader_data(self):
        message = "There is no data in the dataframe"
        self.assertNotEqual(len(data), 0, message)

    def test_dataloader_files_loaded(self):
        len_files = len(files)
        len_data = len(data)
        message = f"The number of files and records in dataframe don't match"
        self.assertEqual(len_files, len_data, message)


if __name__ == '__main__':
    unittest.main()
