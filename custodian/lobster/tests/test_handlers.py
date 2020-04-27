import os
import unittest

from custodian.lobster.handlers import ChargeSpillingValidator, EnoughBandsValidator, LobsterFilesValidator

# get location of module
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
test_files_lobster = os.path.join(MODULE_DIR, '../../../test_files/lobster/lobsterouts')


class TestChargeSpillingValidator(unittest.TestCase):

    def test_check_and_correct(self):
        v = ChargeSpillingValidator(output_filename=os.path.join(test_files_lobster, "lobsterout.normal"))
        self.assertFalse(v.check())

        v2 = ChargeSpillingValidator(output_filename=os.path.join(test_files_lobster, "lobsterout.largespilling"))
        self.assertTrue(v2.check())

        v2b = ChargeSpillingValidator(output_filename=os.path.join(test_files_lobster, "lobsterout.largespilling_2"))
        self.assertTrue(v2b.check())

        v3 = ChargeSpillingValidator(output_filename=os.path.join(test_files_lobster, "nolobsterout", "lobsterout"))
        self.assertFalse(v3.check())

        # TODO: get non spin polarized lobsterout
        v4 = ChargeSpillingValidator(output_filename=os.path.join(test_files_lobster, "no_spin", "lobsterout"))
        self.assertFalse(v4.check())

    def test_as_dict(self):
        v = ChargeSpillingValidator(output_filename=os.path.join(test_files_lobster, "lobsterout.normal"))
        d = v.as_dict()
        v2 = ChargeSpillingValidator.from_dict(d)
        self.assertIsInstance(v2, ChargeSpillingValidator)

    @classmethod
    def tearDownClass(cls):
        pass


class TestLobsterFilesValidator(unittest.TestCase):

    def test_check_and_correct(self):
        os.chdir(test_files_lobster)
        v = LobsterFilesValidator()
        self.assertFalse(v.check())
        os.chdir(os.path.join(MODULE_DIR,test_files_lobster, "nolobsterout"))
        v2 = LobsterFilesValidator()
        self.assertTrue(v2.check())
        os.chdir(os.path.join(MODULE_DIR,test_files_lobster, "crash"))
        v2 = LobsterFilesValidator()
        self.assertTrue(v2.check())
        os.chdir(MODULE_DIR)

    def test_as_dict(self):
        os.chdir(test_files_lobster)
        v = LobsterFilesValidator()
        d = v.as_dict()
        v2 = LobsterFilesValidator.from_dict(d)
        self.assertIsInstance(v2, LobsterFilesValidator)
        os.chdir(MODULE_DIR)


class TestEnoughBandsValidator(unittest.TestCase):

    def test_check_and_correct(self):
        v = EnoughBandsValidator(output_filename=os.path.join(test_files_lobster, "lobsterout.normal"))
        self.assertFalse(v.check())

        v2 = EnoughBandsValidator(output_filename=os.path.join(test_files_lobster, "lobsterout.nocohp"))
        self.assertTrue(v2.check())

        v3 = EnoughBandsValidator(output_filename=os.path.join(test_files_lobster, "nolobsterout"))
        self.assertFalse(v3.check())

    def test_as_dict(self):
        v = EnoughBandsValidator(output_filename=os.path.join(test_files_lobster, "lobsterout.normal"))
        d = v.as_dict()
        v2 = EnoughBandsValidator.from_dict(d)
        self.assertIsInstance(v2, EnoughBandsValidator)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
