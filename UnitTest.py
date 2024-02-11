import unittest

from DataLoader import files, data_1, data_2


class MyTestCase(unittest.TestCase):
    def test_dataloader_file(self):
        message = "There are no files in the folder"
        self.assertTrue(files, message)

    def test_dataloader_data_1(self):
        message = "There is no data in the dataframe"
        self.assertNotEqual(len(data_1), 0, message)

    # DataFrame data_1 testing
    def test_dataloader_data_1_columns(self):
        message = "There is no column named RawText"
        self.assertEqual(data_1.columns, 'RawText', message)

    def test_dataloader_data_1_length(self):
        len_files = len(files)
        len_data = len(data_1)
        message = f"The number of files and records in dataframe don't match"
        self.assertEqual(len_files, len_data, message)

    # DataFrame data_2 testing
    def test_dataloader_data_2_columns(self):
        message = "Dataframe data_2 columns not as expected"
        expected_columns = ["RawText", "CleanedText"]
        actual_columns = list(data_2.columns)
        self.assertEqual(expected_columns, actual_columns, message)

    def test_dataloader_data_2_length(self):
        len_files = len(files)
        len_data = len(data_2)
        message = f"The number of files and records in dataframe don't match"
        self.assertEqual(len_files, len_data, message)


if __name__ == '__main__':
    unittest.main()
