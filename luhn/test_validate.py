from unittest import TestCase
from luhn import validate

class TestValidate(TestCase):
    def test_validate(self):
        self.assertEqual(validate(123), False)
        self.assertEqual(validate(1), False)
        self.assertEqual(validate(2121), True)
        self.assertEqual(validate(1230), True)
        self.assertEqual(validate(8675309), False)
        self.assertEqual(validate(4111111111111111), True)
        self.assertEqual(validate(26), True)
        self.assertEqual(validate(2626262626262626), True)
        self.assertEqual(validate(91), True)
        self.assertEqual(validate(92), False)
        self.assertEqual(validate(912030), True)
        self.assertEqual(validate(922030), False)