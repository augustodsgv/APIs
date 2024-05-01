import unittest
from ..api.date import Date

class DateTest(unittest.TestCase):
    ## Test of the __init__ construction function ##
    # Valid init
    def test_init_valid(self):
        day = 15
        month = 10
        year = 1967
        d1 = Date(day, month, year)
        self.assertEqual(day, d1.day)
        self.assertEqual(month, d1.month)
        self.assertEqual(year, d1.year)

    # Exception: invalid days
    def test_init_invalid_days(self):
        month = 9
        year = 1967
        self.assertRaises(Exception, Date, -1, month, year) # Negative day
        self.assertRaises(Exception, Date, 0, month, year) # "0" day
        self.assertRaises(Exception, Date, 31, month, year) # Too high value day (already tested in is_valid_day)
    
    # Exception: invalid month
    def test_init_invalid_month(self):
        day = 10
        year = 1967
        self.assertRaises(Exception, Date, day, -1, year) # Negative month
        self.assertRaises(Exception, Date, day, 0, year) # "0" month
        
    ## Test of the __eq__ comparing function ##
    def test_eq_equals(self):
        d1 = Date(15, 10, 2021)
        d2 = Date(15, 10, 2021)
        self.assertTrue(d1 == d2)
    
    # Day is different
    def test_eq_diff_day(self):
        d1 = Date(15, 10, 2021)
        d2 = Date(14, 10, 2021)
        self.assertTrue(d1 != d2)

    # Month is different
    def test_eq_diff_month(self):
        d1 = Date(15, 10, 2021)
        d2 = Date(15, 11, 2021)
        self.assertTrue(d1 != d2)

    # Year is different
    def test_eq_diff_month(self):
        d1 = Date(15, 10, 2021)
        d2 = Date(15, 10, 2022)
        self.assertTrue(d1 != d2)

    ## Test of the is_valid_month ##
    # Valid month
    def test_is_valid_month_valid(self):
        self.assertTrue(Date.is_valid_month(1))
        self.assertTrue(Date.is_valid_month(12))

    # Negative month
    def test_is_valid_month_negative_month(self):
        self.assertFalse(Date.is_valid_month(-1))
    
    # Month "0"
    def test_is_valid_month_month_zero(self):
        self.assertFalse(Date.is_valid_month(0))

    # Month over 12
    def test_is_valid_month_month_zero(self):
        self.assertFalse(Date.is_valid_month(13))
    
    ## Test of the is_valid_year ##
    # Nothing to test, once it also accepts negative and 0 numbers
    
    ## Test of the is_valid_day ##
    # Valid day
    def test_is_valid_day_not_feb_valid_day(self):
        day = 15
        month = 10
        year = 1967
        self.assertTrue(Date.is_valid_day(day, month, year))
    
    # Negative integer day
    def test_is_valid_not_feb_negative_day(self):
        day = -1
        month = 10
        year = 1967
        self.assertFalse(Date.is_valid_day(day, month, year))
    
    # Day "0"
    def test_is_valid_not_feb_day_zero(self):
        day = 0
        month = 10
        year = 1967
        self.assertFalse(Date.is_valid_day(day, month, year))
    
    # Test of edge cases in upper limit of each month, except february
    def test_is_valid_months_upper_limit_not_feb(self):
        year = 1967

        # jan
        self.assertTrue(Date.is_valid_day(31, 1, year))
        self.assertFalse(Date.is_valid_day(32, 1, year))
        # mar
        self.assertTrue(Date.is_valid_day(31, 3, year))
        self.assertFalse(Date.is_valid_day(32, 3, year))
        # apr
        self.assertTrue(Date.is_valid_day(30, 4, year))
        self.assertFalse(Date.is_valid_day(31, 4, year))
        # may
        self.assertTrue(Date.is_valid_day(31, 5, year))
        self.assertFalse(Date.is_valid_day(32, 5, year))
        # jun
        self.assertTrue(Date.is_valid_day(30, 6, year))
        self.assertFalse(Date.is_valid_day(31, 6, year))
        # jul
        self.assertTrue(Date.is_valid_day(31, 7, year))
        self.assertFalse(Date.is_valid_day(32, 7, year))
        # aug
        self.assertTrue(Date.is_valid_day(31, 8, year))
        self.assertFalse(Date.is_valid_day(32, 8, year))
        # sep
        self.assertTrue(Date.is_valid_day(30, 9, year))
        self.assertFalse(Date.is_valid_day(31, 9, year))
        # oct
        self.assertTrue(Date.is_valid_day(31, 10, year))
        self.assertFalse(Date.is_valid_day(32, 10, year))
        # nov
        self.assertTrue(Date.is_valid_day(30, 11, year))
        self.assertFalse(Date.is_valid_day(31, 11, year))
        # dec
        self.assertTrue(Date.is_valid_day(31, 12, year))
        self.assertFalse(Date.is_valid_day(32, 12, year))

    # Test of edge cases in upper limit for february, in NON leap year
    def test_is_valid_months_upper_limit_feb_not_leap(self):
        valid_day = 28
        invalid_day = 29
        month = 2

        # Not divisible by 4
        self.assertTrue(Date.is_valid_day(valid_day, month, 1953))
        self.assertFalse(Date.is_valid_day(invalid_day, month, 1953))

        # divisible by 100, but not 400
        self.assertTrue(Date.is_valid_day(valid_day, month, 1700))
        self.assertFalse(Date.is_valid_day(invalid_day, month, 1700))

    # Test of edge cases in upper limit for february, in NON leap year
    def test_is_valid_months_upper_limit_feb_leap(self):
        valid_day = 29
        invalid_day = 30
        month = 2

        # divisible by 4, and not by 100
        self.assertTrue(Date.is_valid_day(valid_day, month, 1604))
        self.assertFalse(Date.is_valid_day(invalid_day, month, 1604))

        # divisible by 4 and 100, but also by 400
        self.assertTrue(Date.is_valid_day(valid_day, month, 1600))
        self.assertFalse(Date.is_valid_day(invalid_day, month, 1600))

    ## Test of property month_str ##
    def test_month_str(self):
        date = Date(15, 1, 2001)
        self.assertEqual('jan', date.month_str)
        date.month += 1
        self.assertEqual('feb', date.month_str)
        date.month += 1
        self.assertEqual('mar', date.month_str)
        date.month += 1
        self.assertEqual('apr', date.month_str)
        date.month += 1
        self.assertEqual('may', date.month_str)
        date.month += 1
        self.assertEqual('jun', date.month_str)
        date.month += 1
        self.assertEqual('jul', date.month_str)
        date.month += 1
        self.assertEqual('aug', date.month_str)
        date.month += 1
        self.assertEqual('sep', date.month_str)
        date.month += 1
        self.assertEqual('oct', date.month_str)
        date.month += 1
        self.assertEqual('nov', date.month_str)
        date.month += 1
        self.assertEqual('dec', date.month_str)
        
    ## Tests for get_date method ##
    # Short date format
    def test_get_date_short(self):
        date = Date(15, 9, 2016)
        self.assertEqual(date.get_date('s'), '9/15/2016')
    
    # Long date format
    def test_get_date_short(self):
        date = Date(15, 9, 2016)
        self.assertEqual(date.get_date('l'), '15 sep, 2016')
        
    

if __name__ == '__main__':
    unittest.main()