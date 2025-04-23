import unittest

# Import the format_date function from your script
from mirasol_lab1 import format_date

class TestFormatDate(unittest.TestCase):
    def test_dmy_format(self):
        # DMY (Day Month, Year)
        self.assertEqual(format_date("25 December, 1992"), "December 25, 1992")
        self.assertEqual(format_date("13 April, 2008"), "April 13, 2008")

    def test_ymd_format(self):
        # YMD (Year Month Day)
        self.assertEqual(format_date("2008 April 13"), "April 13, 2008")
        self.assertEqual(format_date("1992 December 25"), "December 25, 1992")

    def test_iso_format(self):
        # ISO (YYYY-MM-DD)
        self.assertEqual(format_date("2023-05-27"), "May 27, 2023")
        self.assertEqual(format_date("1985-11-01"), "November 01, 1985")

    def test_usa_format(self):
        # USA (MM/DD/YYYY)
        self.assertEqual(format_date("07/04/2015"), "July 04, 2015")
        self.assertEqual(format_date("12/25/1992"), "December 25, 1992")

    def test_eur_format(self):
        # EUR (DD.MM.YYYY)
        self.assertEqual(format_date("28.02.2024"), "February 28, 2024")
        self.assertEqual(format_date("01.11.1985"), "November 01, 1985")

    def test_jis_format(self):
        # JIS (YYYYMMDD)
        self.assertEqual(format_date("19851101"), "November 01, 1985")
        self.assertEqual(format_date("20240527"), "May 27, 2024")

    def test_whitespace_handling(self):
        # Test input with leading/trailing/in-between whitespaces
        self.assertEqual(format_date("   25    December  , 1992 "), "December 25, 1992")
        self.assertEqual(format_date("   2023  -  05  -  27   "), "May 27, 2023")
        self.assertEqual(format_date("   07  /  04  /  2015   "), "July 04, 2015")
        self.assertEqual(format_date("   28  . 02  .  2024   "), "February 28, 2024")
        self.assertEqual(format_date("   1985   11   01   "), "November 01, 1985")

if __name__ == "__main__":
    unittest.main()