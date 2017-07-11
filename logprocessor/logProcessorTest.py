import unittest
import utils

class TestLogProcessor(unittest.TestCase):

    def test_should_return_false(self):
        isLineEmptyResult = utils.isEmptyLine('Line with text')

        self.assertFalse(isLineEmptyResult)

    def test_should_return_false_when_line_is_empty(self):
        isLineEmptyResult = utils.isEmptyLine('')

        self.assertFalse(isLineEmptyResult)

    def test_should_return_true_when_line_contains_only_new_CR(self):
        isLineEmptyResult = utils.isEmptyLine('\n')

        self.assertTrue(isLineEmptyResult)

    def test_should_return_false_when_line_contains_CR_but_is_too_long(self):
        isLineEmptyResult = utils.isEmptyLine('\n test')

        self.assertFalse(isLineEmptyResult)



    def test_should_return_true_when_line_starts_with_tab(self):
        isRegularLine = utils.isRegularStackTraceLine('\terror')

        self.assertTrue(isRegularLine)

    def test_should_return_false_when_line_does_not_starts_with_tab(self):
        isRegularLine = utils.isRegularStackTraceLine('error')

        self.assertFalse(isRegularLine)

    def test_should_return_false_when_line_contains_tab_only_inside(self):
        isRegularLine = utils.isRegularStackTraceLine('error\ttest')

        self.assertFalse(isRegularLine)

    def test_should_return_date(self):
        date = utils.findDate(' 20:12:30')

        self.assertEquals(date, '20:12:30')

    def test_should_return_date_when_contains_other_content_including_stick_comma(self):
        date = utils.findDate('2016-01-21 15:49:58,462 INFO  [TableMetadata.java:69] : HHH000126: Indexes: [epu_account_pkey]')

        self.assertEquals(date, '15:49:58')

    def test_should_return_date_when_contains_other_content(self):
        date = utils.findDate('lut 20, 2017 9:19:00 AM org.apache.catalina.core.ApplicationContext log')

        self.assertEquals(date, '9:19:00')

    def test_should_return_none(self):
        date = utils.findDate('lut 20, 2017 a9:19:00 AM org.apache.catalina.core.ApplicationContext log')

        self.assertIsNone(date)

    def test_should_return_none_when_line_is_empty(self):
        date = utils.findDate('')

        self.assertIsNone(date)

    def test_should_return_proper_time_obj(self):
        time = utils.parseDate('9:19:00')

        self.assertEquals(time, utils.datetime.time(9, 19, 00))

    def test_should_return_none_when_input_does_not_contains_date(self):
        time = utils.parseDate('\n')

        self.assertIsNone(time)






























def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
