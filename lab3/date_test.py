import unittest

# Import the format_date function from your script
from mirasol_lab3_1 import format_date

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

    def test_gen_invalid_format(self):
        # general
        self.assertEqual(format_date(""), "Invalid date format.")
        self.assertEqual(format_date("  "), "Invalid date format.")
    
    def test_mdy_invalid_format(self):
        # mdy
        self.assertEqual(format_date(" december, 25, 1992 "), "December 25, 1992")
        self.assertEqual(format_date(" december, 25 1992 "), "December 25, 1992")
        self.assertEqual(format_date(" december 25, 1992 "), "December 25, 1992")
        self.assertEqual(format_date(" december 25, 199"), "December 25, 199")
        self.assertEqual(format_date(" december 25, 19922"), "Invalid DMY year.")
        self.assertEqual(format_date(" december 25, lkjk"), "Invalid date format.")
        self.assertEqual(format_date("  december, lksjdf , 1992 "), "Invalid date format.")
        self.assertEqual(format_date("  lkjdlkj, 25 , 1992 "), "Invalid DMY month.")
        self.assertEqual(format_date("  december , 25 , lksdjf "), "Invalid DMY year.")
        self.assertEqual(format_date(" december 35, 1992 "), "Invalid MDY day.")
        self.assertEqual(format_date(" december, 0 1992 "), "Invalid MDY day.")
    
    def test_dmy_invalid_format(self):
        # (dmy) day month, year       ->      month day, year
        self.assertEqual(format_date("  25, december, 1992 "), "December 25, 1992")
        self.assertEqual(format_date(" 25, december 1992 "), "December 25, 1992")
        self.assertEqual(format_date(" 25 december , 1992 "), "December 25, 1992")
        self.assertEqual(format_date("  25 , december 199"), "December 25, 199")
        self.assertEqual(format_date("  25 , december 19920"), "Invalid DMY year.")
        self.assertEqual(format_date("  lksjdf , december, 1992 "), "Invalid date format.")
        self.assertEqual(format_date("  25 , lkjdlkj, 1992 "), "Invalid DMY month.")
        self.assertEqual(format_date("  25 , december , lksdjf "), "Invalid DMY year.")
        self.assertEqual(format_date(" 25 december, lkjk"), "Invalid date format.")
        self.assertEqual(format_date(" 35 december , 1992 "), "Invalid DMY day.")
        self.assertEqual(format_date(" 0, december 1992 "), "Invalid DMY day.")
    
    def test_iso_invalid_format(self):
        # (iso) yyyy-mm-dd            ->      month day, year
        self.assertEqual(format_date("lksdj - 12 - 23 "), "Invalid ISO year.")
        self.assertEqual(format_date(" lkjs -  12 -  23  "), "Invalid date format.")
        self.assertEqual(format_date(" 2023 - lskdjf - 23 "), "Invalid date format.")
        self.assertEqual(format_date(" 2023 - 12 - lskjdflk "), "Invalid date format.")
        self.assertEqual(format_date(" 202 -  12 -  23  "), "December 23, 202")
        self.assertEqual(format_date(" 20230 -  12 -  23  "), "Invalid ISO year.")
        self.assertEqual(format_date(" 2023 -  13 -  23  "), "Invalid ISO month.")
        self.assertEqual(format_date(" 2023 -  12 -  35  "), "Invalid ISO day.")
        self.assertEqual(format_date(" 2023 -  12 -  0  "), "Invalid ISO day.")
    
    def test_usa_invalid_format(self):
        # (usa) mm/dd/yyyy            ->      month day, year
        self.assertEqual(format_date(" lskdjf / 23 / 2023 "), "Invalid date format.")
        self.assertEqual(format_date(" 12 / lskjdflk / 2023 "), "Invalid date format.")
        self.assertEqual(format_date("  12 /  23 /  lkjs "), "Invalid date format.")
        self.assertEqual(format_date("12 / 23  / lksdj"), "Invalid USA year.")
        self.assertEqual(format_date("  12 /  23  / 202 "), "December 23, 202")
        self.assertEqual(format_date("  12 /  23  / 20233 "), "Invalid USA year.")
        self.assertEqual(format_date("  13 /  23 /  2023 "), "Invalid USA month.")
        self.assertEqual(format_date("  12 /  35 / 2023  "), "Invalid USA day.")
        self.assertEqual(format_date("  12 /  0 / 2023  "), "Invalid USA day.")
    
    def test_eur_invalid_format(self):
        # (eur) dd.mm.yyyy            ->      month day, year
        self.assertEqual(format_date(" lskj . 12. 2023  "), "Invalid date format.")
        self.assertEqual(format_date("  23 . lskd . 2023 "), "Invalid date format.")
        self.assertEqual(format_date("  23  . 12.  lkjs  "), "Invalid date format.")
        self.assertEqual(format_date(" 23. 12 . lksdj  "), "Invalid EUR year.")
        self.assertEqual(format_date("  23 . 12 .  202  "), "December 23, 202")
        self.assertEqual(format_date("  23  . 13 .  2023 "), "Invalid EUR month.")
        self.assertEqual(format_date("  35  .  12 . 2023 "), "Invalid EUR day.")
        self.assertEqual(format_date("  0  .  12 . 2023 "), "Invalid EUR day.")

    def test_ymd_invalid_format(self):
        # (ymd) year month day        ->      month day, year
        self.assertEqual(format_date("lksdj  december  23 "), "Invalid YMD year.")
        self.assertEqual(format_date(" lkjs   december   23  "), "Invalid date format.")
        self.assertEqual(format_date(" 2023  lskdjf  23 "), "Invalid YMD month.")
        self.assertEqual(format_date(" 2023  december lskjdflk "), "Invalid date format.")
        self.assertEqual(format_date(" 202   december   23  "), "December 23, 202")
        self.assertEqual(format_date(" 20233   december   23  "), "Invalid YMD year.")
        self.assertEqual(format_date(" 2023   december   35  "), "Invalid YMD day.")
        self.assertEqual(format_date(" 2023   december   0  "), "Invalid YMD day.")
    
    def test_jis_invalid_format(self):
        # (jis) yyyymmdd              ->      month day, year
        self.assertEqual(format_date(" 2023132  "), "Invalid date format.")
        self.assertEqual(format_date(" 202313   2  "), "Invalid date format.")
        self.assertEqual(format_date("lksdj  12  23 "), "Invalid date format.")
        self.assertEqual(format_date(" lkjs   12   23  "), "Invalid date format.")
        self.assertEqual(format_date(" 2023lskdjf23 "), "Invalid date format.")
        self.assertEqual(format_date(" 2023  12 lskjdflk "), "Invalid date format.")
        self.assertEqual(format_date(" 2023 ls 23 "), "Invalid date format.")
        self.assertEqual(format_date(" 202   12   23  "), "Invalid date format.")
        self.assertEqual(format_date(" 2023   13   23  "), "Invalid JIS month.")
        self.assertEqual(format_date(" 2023   12   35  "), "Invalid JIS day.")
        self.assertEqual(format_date(" 2023   12   00  "), "Invalid JIS day.")
    
    def test_incomplete_fields(self):
        # mdy
        self.assertEqual(format_date(" december, 25,  "), "Incomplete DMY format or Invalid date format.")
        self.assertEqual(format_date(" december, 25  "), "Incomplete DMY format or Invalid date format.")
        self.assertEqual(format_date(" december 25,  "), "Incomplete DMY format or Invalid date format.")
        # dmy
        self.assertEqual(format_date("  25, december, "), "Incomplete DMY format or Invalid date format.")
        self.assertEqual(format_date(" 25, december  "), "Incomplete DMY format or Invalid date format.")
        self.assertEqual(format_date(" 25 december ,  "), "Incomplete DMY format or Invalid date format.")
        # iso
        self.assertEqual(format_date(" 2023 - 12 23  "), "Incomplete ISO format or Invalid date format.")
        self.assertEqual(format_date(" 2023  12 -  23  "), "Incomplete ISO format or Invalid date format.")
        self.assertEqual(format_date(" 2023 - 12 -   "), "Incomplete ISO format or Invalid date format.")
        # usa
        self.assertEqual(format_date(" 12  / 23 2023 "), "Incomplete USA format or Invalid date format.")
        self.assertEqual(format_date(" 12  23  / 2023 "), "Incomplete USA format or Invalid date format.")
        self.assertEqual(format_date(" 12  / 23 / "), "Incomplete USA format or Invalid date format.")
        # eur
        self.assertEqual(format_date("  23 . 12 2023 "), "Incomplete EUR format or Invalid date format.")
        self.assertEqual(format_date("  23  12 . 2023 "), "Incomplete EUR format or Invalid date format.")
        self.assertEqual(format_date("  23 . 12 . "), "Incomplete EUR format or Invalid date format.")
        # ymd
        self.assertEqual(format_date("2023 December"), "Incomplete YMD format or Invalid date format.")
        self.assertEqual(format_date("2023 31"), "Invalid date format.")

    #     self.assertEqual(format_date("December 25"), "Incomplete date fields/Invalid date format.")
    #     self.assertEqual(format_date("2023-12"), "Incomplete date fields/Invalid date format.")
    #     self.assertEqual(format_date("12/25"), "Incomplete date fields/Invalid date format.")
    #     self.assertEqual(format_date("25.12"), "Incomplete date fields/Invalid date format.")


if __name__ == "__main__":
    unittest.main()