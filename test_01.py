import testlib
import random
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

TIMEOUT=6 * 2 # VM warp factor

@ddt
class Test(testlib.TestCase):
    def do_test(self, matches, k, expected):
        """Test implementation
        - matches:		list of players' plays
        - k:			tournament parameter
        - expected:		expected result
        TIMEOUT: 2 seconds for each test
        """
        if DEBUG:
                import program01 as program
                result = program.ex(matches, k)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_imports(allowed=['program01','_io']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                result = program.ex(matches, k)
        self.assertEqual(type(result), list,
                         ('The output type should be: list\n'
                          '[Il tipo di dato in output deve essere: list]'))
        for p in result:
            self.assertEqual(type(p), int,
                         ('The elements of the output should be: int\n '
                          '[Gli elementi della lista devono essere int.]'))
        self.assertEqual(len(result), len(expected),
                         ('The output list should have '+str(len(expected))+' elements\n'
                          '[La lista deve avere ' +str(len(expected))+' elementi\n'))
        self.assertEqual(result, expected,
                         ('The return value is incorrect\n'
                          '[Il valore di ritorno è errato]'))
        return 1

    def test_example1(self):
        matches  = [ "abc",  "dba" , "eZo"]
        k        = 10
        expected = [0, 1, 2]
        return self.do_test(matches, k, expected)

    def test_example2(self):
        k        = 50
        matches  = [ "A ƐÈÜ",  "BEAR" , "c Ʈ  ´  ."]
        expected = [1, 2, 0]
        return self.do_test(matches, k, expected)

    def test_simple1(self):
        k        = 5
        matches  = ["aaa", "bbb", "ccc", "ddd", "eee"]
        expected = [4, 3, 2, 1, 0]
        return self.do_test(matches, k, expected)

    def test_simple2(self):
        k        = 3
        matches  = ["aaa", "bbb", "ccc", "ddd", "eee"]
        expected = [3, 4, 2, 0, 1]
        return self.do_test(matches, k, expected)


    @file_data("test_runic_3_15_20.json")
    def test_runic_3_15_20(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_joyokanji_4_20_1000.json")
    def test_joyokanji_4_20_1000(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_emoji_5_10_100.json")
    def test_emoji_5_10_100(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_emoji_10_10_50.json")
    def test_emoji_10_10_50(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_hiragana_10_100_50.json")
    def test_hiragana_10_100_50(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_runic_30_100_20.json")
    def test_runic_30_100_20(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_joyokanji_40_200_1000.json")
    def test_joyokanji_40_200_1000(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_hiragana_10_1000_30.json")
    def test_hiragana_10_1000_30(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_emoji_50_100_100.json")
    def test_emoji_50_100_100(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_runic_100_1000_20.json")
    def test_runic_100_1000_20(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_joyokanji_100_1000_1000.json")
    def test_joyokanji_100_1000_1000(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_hiragana_100_1000_20.json")
    def test_hiragana_100_1000_20(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    ######################### SECRET TESTS START HERE! #########################


if __name__ == '__main__':
    Test.main()


