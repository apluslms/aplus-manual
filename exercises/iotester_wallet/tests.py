import unittest
import random

from graderutils.graderunittest import points
from graderutils.iotester import IOTester, ENTER


# Name of the Python modules that are going to be tested
module_to_test_1 = "wallet"
module_to_test_2 = "wallet_program"

# Use default settings
iotester = IOTester()


# Define functions that are run in tests to test the methods of class Wallet
def create_wallet(owner_name, balance):
    from wallet import Wallet
    my_wallet = Wallet(owner_name, balance=balance)
    return my_wallet


def prog_get_owner_name(owner_name, balance=0):
    my_wallet = create_wallet(owner_name, balance)
    result = my_wallet.get_owner_name()
    return result


def prog_get_balance(owner_name, balance=0):
    my_wallet = create_wallet(owner_name, balance)
    result = my_wallet.get_balance()
    return result


def prog_deposit(amount, owner_name, balance=0):
    my_wallet = create_wallet(owner_name, balance)
    result = my_wallet.deposit(amount)
    return result


def prog_withdraw(amount, owner_name, balance=0):
    my_wallet = create_wallet(owner_name, balance)
    result = my_wallet.withdraw(amount)
    return result


def prog_has_more_money(owner_name1, owner_name2, balance1=0, balance2=0):
    wallet1 = create_wallet(owner_name1, balance1)
    wallet2 = create_wallet(owner_name2, balance2)
    result = wallet1.has_more_money(wallet2)
    return result


def prog__str__(owner_name, balance=0):
    my_wallet = create_wallet(owner_name, balance)
    result = my_wallet.__str__()
    return result


def prog_run_model_program():
    import wallet_program # Runs main() function


# Define argument lists that are going to be used in the tests
args_init = [
    ["Teemu"],
    ["Eino"],
    ["Anna"],
]

kwargs_init = [
    {"balance": random.randint(10000, 500000) / 100},
    {},
    {"balance": random.randint(1000, 50000) / 100},
]

params_deposit = [
    [100.00, ["Teemu"], {"balance": random.randint(10000, 500000) / 100}],
    [random.randint(1000, 50000) / 100, ["Eino"], {}],
    [0.0, ["Anna"], {"balance": random.randint(1000, 50000) / 100}],
    [random.randint(-50000, -1000) / 100, ["Joonas"], {"balance": random.randint(1000, 50000) / 100}],
]

params_withdraw = [
    [90.00, ["Teemu"], {"balance": random.randint(10000, 500000) / 100}],                               # True
    [random.randint(1000, 5000) / 100, ["Eila"], {"balance": random.randint(10000, 500000) / 100}],     # True
    [150.00, ["Jaakko"], {"balance": random.randint(10000, 12000) / 100}],                              # False
    [random.randint(1000, 50000) / 100, ["Eino"], {}],                                                  # False
    [0.0, ["Anna"], {"balance": random.randint(1000, 50000) / 100}],                                    # False
    [random.randint(-50000, -1000) / 100, ["Joonas"], {"balance": random.randint(1000, 50000) / 100}],  # False
]

params_has_more_money = [
    [["Anna"], {"balance": 530.30}, ["Eila"], {"balance": 102.90}],                                                            # True
    [["Teemu"], {"balance": random.randint(10000, 500000) / 100}, ["Jaakko"], {"balance": random.randint(1000, 9000) / 100}],  # True
    [["Eino"], {}, ["Johanna"], {"balance": random.randint(1000, 9000) / 100}],                                                # False
    [["Jenna"], {"balance": random.randint(1000, 9000) / 100}, ["Joonas"], {"balance": random.randint(10000, 500000) / 100}],  # False
]

inputs1 = [
    "Teemu",
    random.randint(10000, 20000) / 100,
    "Anna",
    random.randint(30000, 40000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
]

inputs2 = [
    "Teemu",
    random.randint(30000, 40000) / 100,
    "Anna",
    random.randint(10000, 20000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
]

inputs3 = [
    "Teemu",
    random.randint(30000, 40000) / 100,
    "Anna",
    random.randint(10000, 20000) / 100,
    random.randint(-2000, -1000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
]

inputs4 = [
    "Teemu",
    random.randint(30000, 40000) / 100,
    "Anna",
    random.randint(10000, 20000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(1000, 2000) / 100,
    random.randint(60000, 70000) / 100,
]

all_inputs = [inputs1, inputs2, inputs3, inputs4]


class TestCaseWallet(unittest.TestCase):

    # In this exercise iotester.prepare() is called in the beginning of each test method instead of
    # in setUp() because we test two different Python modules.

    def tearDown(self):
        # After running a test method, restore IOTester state and clean up possible files created.
        # Do not forget this, otherwise weird things might happen.
        iotester.restore()

    # In this exercise the maximum amount of points is set to 100 in the exercise RST file,
    # so we make sure that all the points from each test method add up to 100.

    @points(10)
    def test_01_class_structure(self):
        """Test class structure (wallet.py)"""
        # Prepare the Python module containing the class Wallet
        iotester.prepare(self, module_to_test_1)
        checks = ["object_attrs", "class_attrs", "no_extra_object_attrs", "no_extra_class_attrs"]
        for args, kwargs in zip(args_init, kwargs_init):
            iotester.class_structure_test(class_name="Wallet", args=args, kwargs=kwargs, checks=checks)


    @points(10)
    def test_02_init(self):
        """Test function '__init__' (wallet.py)"""
        # Prepare the Python module containing the class Wallet
        iotester.prepare(self, module_to_test_1)
        # Run class_init_test to make sure __init__ works and required object attributes are
        # initialized correctly.
        for args, kwargs in zip(args_init, kwargs_init):
            # Set run_no_output_test to True to check that __init__ doesn't output anything
            iotester.class_init_test(class_name="Wallet", args=args, kwargs=kwargs, run_no_output_test=True)


    # Decorated in the parent test below (test_03_get_owner_name).
    def subtest_get_owner_name(self, my_wallet, args, kwargs):
        # This subtest makes sure that method get_owner_name doesn't change the object's attributes
        original_owner_name = args[0]
        original_balance = kwargs.get("balance", 0)

        my_wallet.get_owner_name()

        # Compare current attributes to original attributes after calling method get_owner_name
        owner_name = my_wallet._Wallet__owner_name
        balance = my_wallet._Wallet__balance

        msg = "Calling get_owner_name shouldn't change the wallet's owner name."
        self.assertEqual(owner_name, original_owner_name, msg)
        msg = "Calling get_owner_name shouldn't change the wallet's balance."
        self.assertEqual(balance, original_balance, msg)


    @points(5)
    def test_03_get_owner_name(self):
        """Test function 'get_owner_name' (wallet.py)"""
        # Prepare the Python module containing the class Wallet
        iotester.prepare(self, module_to_test_1)
        for args, kwargs in zip(args_init, kwargs_init):
            # Returned Wallet object is used later in subtest_get_owner_name
            obj, _ = iotester.class_init_test(class_name="Wallet", args=args, kwargs=kwargs, run_no_output_test=True)

            # Run return_value_test with prog_get_owner_name to make sure method get_owner_name returns the correct value
            iotester.return_value_test(func_name="get_owner_name", prog=prog_get_owner_name, prog_args=args, prog_kwargs=kwargs)

            # Run no_output_test with prog_get_owner_name to make sure method get_owner_name doesn't output anything
            iotester.no_output_test(func_name="get_owner_name", prog=prog_get_owner_name, prog_args=args, prog_kwargs=kwargs)

            # Decorate and run subtest_get_owner_name to make sure that method get_owner_name doesn't change the object's attributes
            iotester.feedback(func_name="get_owner_name", simple=True, show_used_inputs_and_params=True)(self.subtest_get_owner_name)(obj, args, kwargs)


    # Decorated in the parent test below (test_04_get_balance).
    def subtest_get_balance(self, my_wallet, args, kwargs):
        # This subtest makes sure that method get_balance doesn't change the object's attributes
        original_owner_name = args[0]
        original_balance = kwargs.get("balance", 0)

        my_wallet.get_balance()

        # Compare current attributes to original attributes after calling method get_balance
        owner_name = my_wallet._Wallet__owner_name
        balance = my_wallet._Wallet__balance

        msg = "Calling get_balance shouldn't change the wallet's owner name."
        self.assertEqual(owner_name, original_owner_name, msg)
        msg = "Calling get_balance shouldn't change the wallet's balance."
        self.assertEqual(balance, original_balance, msg)


    @points(5)
    def test_04_get_balance(self):
        """Test function 'get_balance' (wallet.py)"""
        # Prepare the Python module containing the class Wallet
        iotester.prepare(self, module_to_test_1)
        for args, kwargs in zip(args_init, kwargs_init):
            # Returned Wallet object is used later in subtest_get_owner_name
            obj, _ = iotester.class_init_test(class_name="Wallet", args=args, kwargs=kwargs, run_no_output_test=True)

            # Run return_value_test with prog_get_balance to make sure method get_balance returns the correct value
            iotester.return_value_test(func_name="get_balance", prog=prog_get_balance, prog_args=args, prog_kwargs=kwargs)

            # Run no_output_test with prog_get_balance to make sure method get_balance doesn't output anything
            iotester.no_output_test(func_name="get_balance", prog=prog_get_balance, prog_args=args, prog_kwargs=kwargs)

            # Decorate and run subtest_get_balance to make sure that method get_balance doesn't change the object's attributes
            iotester.feedback(func_name="get_balance", simple=True, show_used_inputs_and_params=True)(self.subtest_get_balance)(obj, args, kwargs)


    # Decorated in the parent test below (test_05_deposit).
    def subtest_deposit(self, my_wallet, amount, args, kwargs):
        # This subtest makes sure that method deposit changes the correct attributes only
        original_owner_name = args[0]
        original_balance = kwargs.get("balance", 0)

        my_wallet.deposit(amount)

        # Compare current attributes to original attributes after calling method deposit
        owner_name = my_wallet._Wallet__owner_name
        balance = my_wallet._Wallet__balance

        msg = "Calling deposit shouldn't change the wallet's owner name."
        self.assertEqual(owner_name, original_owner_name, msg)
        if amount > 0:
            msg = "Expected attribute '__balance' to be {} after calling deposit,\nbut it was {} instead.".format(original_balance + amount, balance)
            self.assertEqual(balance, original_balance + amount, msg)
        else:
            msg = "Expected attribute '__balance' to be {} after calling deposit,\nbut it was {} instead.".format(original_balance, balance)
            self.assertEqual(balance, original_balance, msg)


    @points(10)
    def test_05_deposit(self):
        """Test function 'deposit' (wallet.py)"""
        # Prepare the Python module containing the class Wallet
        iotester.prepare(self, module_to_test_1)
        for amount, args, kwargs in params_deposit:
            # Returned Wallet object is used later in subtest_deposit
            obj, _ = iotester.class_init_test(class_name="Wallet", args=args, kwargs=kwargs, run_no_output_test=True)

            # Run return_value_test with prog_deposit to make sure method deposit returns the correct value
            iotester.return_value_test(func_name="deposit", args=[amount], prog=prog_deposit, prog_args=[amount, *args], prog_kwargs=kwargs)

            # Run no_output_test with prog_deposit to make sure method deposit doesn't output anything
            iotester.no_output_test(func_name="deposit", args=[amount], prog=prog_deposit, prog_args=[amount, *args], prog_kwargs=kwargs)

            # Decorate and run subtest_deposit to make sure that method deposit changes the correct attributes only
            iotester.feedback(func_name="deposit", args=[amount], simple=True, show_used_inputs_and_params=True)(self.subtest_deposit)(obj, amount, args, kwargs)


    # Decorated in the parent test below (test_06_withdraw).
    def subtest_withdraw(self, my_wallet, amount, args, kwargs):
        # This subtest makes sure that method withdraw changes the correct attributes only
        original_owner_name = args[0]
        original_balance = kwargs.get("balance", 0)

        my_wallet.withdraw(amount)

        # Compare current attributes to original attributes after calling method withdraw
        owner_name = my_wallet._Wallet__owner_name
        balance = my_wallet._Wallet__balance

        msg = "Calling withdraw shouldn't change the wallet's owner name."
        self.assertEqual(owner_name, original_owner_name, msg)
        if amount > 0 and original_balance >= amount:
            msg = "Expected attribute '__balance' to be {} after calling withdraw,\nbut it was {} instead.".format(original_balance - amount, balance)
            self.assertEqual(balance, original_balance - amount, msg)
        else:
            msg = "Expected attribute '__balance' to be {} after calling withdraw,\nbut it was {} instead.".format(original_balance, balance)
            self.assertEqual(balance, original_balance, msg)


    @points(10)
    def test_06_withdraw(self):
        """Test function 'withdraw' (wallet.py)"""
        # Prepare the Python module containing the class Wallet
        iotester.prepare(self, module_to_test_1)
        for amount, args, kwargs in params_withdraw:
            # Returned Wallet object is used later in subtest_withdraw
            obj, _ = iotester.class_init_test(class_name="Wallet", args=args, kwargs=kwargs, run_no_output_test=True)

            # Run return_value_test with prog_withdraw to make sure method withdraw returns the correct value
            iotester.return_value_test(func_name="withdraw", args=[amount], prog=prog_withdraw, prog_args=[amount, *args], prog_kwargs=kwargs)

            # Run no_output_test with prog_withdraw to make sure method withdraw doesn't output anything
            iotester.no_output_test(func_name="withdraw", args=[amount], prog=prog_withdraw, prog_args=[amount, *args], prog_kwargs=kwargs)

            # Decorate and run subtest_withdraw to make sure that method withdraw changes the correct attributes only
            iotester.feedback(func_name="withdraw", args=[amount], simple=True, show_used_inputs_and_params=True)(self.subtest_withdraw)(obj, amount, args, kwargs)


    # Decorated in the parent test below (test_07_has_more_money).
    def subtest_has_more_money(self, wallet1, wallet2, args1, kwargs1, args2, kwargs2):
        # This subtest makes sure that method has_more_money doesn't change either object's attributes
        wallet1_original_owner_name = args1[0]
        wallet1_original_balance = kwargs1.get("balance", 0)

        wallet2_original_owner_name = args2[0]
        wallet2_original_balance = kwargs2.get("balance", 0)

        wallet1.has_more_money(wallet2)

        # Compare current attributes to original attributes after calling method has_more_money
        wallet1_owner_name = wallet1._Wallet__owner_name
        wallet1_balance = wallet1._Wallet__balance

        wallet2_owner_name = wallet2._Wallet__owner_name
        wallet2_balance = wallet2._Wallet__balance

        msg = "Calling has_more_money shouldn't change the wallet's owner name."
        self.assertEqual(wallet1_owner_name, wallet1_original_owner_name, msg)
        msg = "Calling has_more_money shouldn't change the wallet's balance."
        self.assertEqual(wallet1_balance, wallet1_original_balance, msg)

        msg = "Calling has_more_money shouldn't change the other wallet's owner name."
        self.assertEqual(wallet2_owner_name, wallet2_original_owner_name, msg)
        msg = "Calling has_more_money shouldn't change the other wallet's balance."
        self.assertEqual(wallet2_balance, wallet2_original_balance, msg)


    @points(10)
    def test_07_has_more_money(self):
        """Test function 'has_more_money' (wallet.py)"""
        # Prepare the Python module containing the class Wallet
        iotester.prepare(self, module_to_test_1)
        for args1, kwargs1, args2, kwargs2 in params_has_more_money:
            # Returned Wallet objects are used later in subtest_has_more_money
            obj1, _ = iotester.class_init_test(class_name="Wallet", args=args1, kwargs=kwargs1, run_no_output_test=True)
            obj2, _ = iotester.class_init_test(class_name="Wallet", args=args2, kwargs=kwargs2, run_no_output_test=True)

            description = "Wallet 1:              Wallet 2:\n__balance: {:<6.2f}      __balance: {:<6.2f}".format(kwargs1.get("balance", 0), kwargs2.get("balance", 0))
            prog_args = [*args1, *args2]
            prog_kwargs = {
                "balance1": kwargs1.get("balance", 0),
                "balance2": kwargs2.get("balance", 0),
            }

            # Run return_value_test with prog_has_more_money to make sure method has_more_money returns the correct value
            iotester.return_value_test(func_name="has_more_money", args=[obj2], prog=prog_has_more_money, prog_args=prog_args, prog_kwargs=prog_kwargs, desc=description)

            # Run no_output_test with prog_has_more_money to make sure method has_more_money doesn't output anything
            iotester.no_output_test(func_name="has_more_money", args=[obj2], prog=prog_has_more_money, prog_args=prog_args, prog_kwargs=prog_kwargs, desc=description)

            # Decorate and run subtest_has_more_money to make sure that method has_more_money doesn't change either object's attributes
            iotester.feedback(func_name="has_more_money", args=[obj2], simple=True, show_used_inputs_and_params=True)(self.subtest_has_more_money)(obj1, obj2, args1, kwargs1, args2, kwargs2)


    # Decorated in the parent test below (test_08__str__).
    def subtest__str__(self, my_wallet, args, kwargs):
        # This subtest makes sure that method __str__ doesn't change the object's attributes
        original_owner_name = args[0]
        original_balance = kwargs.get("balance", 0)

        my_wallet.__str__()

        # Compare current attributes to original attributes after calling method __str__
        owner_name = my_wallet._Wallet__owner_name
        balance = my_wallet._Wallet__balance

        msg = "Calling __str__ shouldn't change the wallet's owner name."
        self.assertEqual(owner_name, original_owner_name, msg)
        msg = "Calling __str__ shouldn't change the wallet's balance."
        self.assertEqual(balance, original_balance, msg)


    @points(10)
    def test_08__str__(self):
        """Test function '__str__' (wallet.py)"""
        # Prepare the Python module containing the class Wallet
        iotester.prepare(self, module_to_test_1)
        for args, kwargs in zip(args_init, kwargs_init):
            # Returned Wallet object is used later in subtest__str__
            obj, _ = iotester.class_init_test(class_name="Wallet", args=args, kwargs=kwargs, run_no_output_test=True)
            description = "Wallet:\n__owner_name: {}\n__balance: {}".format(args[0], kwargs.get("balance", 0))

            # Run return_value_test with prog__str__ to make sure method __str__ returns the correct value
            iotester.return_value_test(func_name="__str__", prog=prog__str__, prog_args=args, prog_kwargs=kwargs, desc=description)

            # Run no_output_test with prog__str__ to make sure method __str__ doesn't output anything
            iotester.no_output_test(func_name="__str__", prog=prog__str__, prog_args=args, prog_kwargs=kwargs, desc=description)

            # Decorate and run subtest__str__ to make sure that method __str__ doesn't change the object's attributes
            iotester.feedback(func_name="__str__", simple=True, show_used_inputs_and_params=True)(self.subtest__str__)(obj, args, kwargs)


    @points(10)
    def test_09_main_output_1(self):
        """Test your wallet.py by using the model solution of wallet_program.py"""
        # Here we run the model solution for wallet_program.py, which imports the student solution for wallet.py
        iotester.prepare(self, module_to_test_1, used_model_modules=[module_to_test_2])
        description = "In this test, we test your wallet.py by running the model solution of wallet_program.py"
        for inputs in all_inputs:
            iotester.text_test(func_name="main", inputs=inputs, prog=prog_run_model_program, prog_inputs=inputs, desc=description)
            iotester.numbers_test(func_name="main", inputs=inputs, prog=prog_run_model_program, prog_inputs=inputs, compare_formatting=True, desc=description)


    @points(10)
    def test_10_main_output_2(self):
        """Test your wallet_program.py by using the model solution of wallet.py"""
        # Here we run the student solution for wallet_program.py, which imports the model solution for wallet.py
        iotester.prepare(self, module_to_test_2, used_model_modules=[module_to_test_1])

        # Check that __str__() method isn't called directly e.g., print(wallet1.__str__()) vs. print(wallet1)
        iotester.class_str_call_test(object_name="wallet1")

        description = "In this test, your wallet_program.py imports the model solution for wallet.py"
        for inputs in all_inputs:
            iotester.text_test(func_name="main", inputs=inputs, desc=description)
            iotester.numbers_test(func_name="main", inputs=inputs, compare_formatting=True, desc=description)


    @points(10)
    def test_11_main_output_3(self):
        """Test your wallet_program.py by using your solution of wallet.py"""
        # Here we run the student solution for wallet_program.py, which imports the student solution for wallet.py
        iotester.prepare(self, module_to_test_2)

        # Check that __str__() method isn't called directly e.g., print(wallet1.__str__()) vs. print(wallet1)
        iotester.class_str_call_test(object_name="wallet1")

        description = "In this test, your wallet_program.py imports your own solution for wallet.py"
        for inputs in all_inputs:
            iotester.text_test(func_name="main", inputs=inputs, desc=description)
            iotester.numbers_test(func_name="main", inputs=inputs, compare_formatting=True, desc=description)


    # The following six test methods are examples of how to use the feedback decorator to
    # produce better looking test feedback for generic unit tests, and how to use the
    # model_directory context manager to import model modules.
    @points(0)
    def test_12_generic_unit_test_fail_1(self):
        """Example unit test (fail, no feedback decorator)"""
        # Import model wallet.py
        with iotester.model_directory():
            import wallet as model_wallet

        # Import student wallet.py
        import wallet as student_wallet
        # Do some testing
        # ...

        # Force fail to show difference between the three test method outputs
        msg = "See how the modules were imported from different files?"
        self.assertEqual(student_wallet.__file__, model_wallet.__file__, msg)


    @points(0)
    @iotester.feedback(simple=False, desc="With simple=False, you can show all the available information.")
    def test_13_generic_unit_test_fail_2(self):
        """Example unit test (fail, feedback decorator, simple=False)"""
        # Import model wallet.py
        with iotester.model_directory():
            import wallet as model_wallet

        # Import student wallet.py
        import wallet as student_wallet
        # Do some testing
        # ...

        # Force fail to show difference between the three test method outputs
        msg = "See how the modules were imported from different files?"
        self.assertEqual(student_wallet.__file__, model_wallet.__file__, msg)


    @points(0)
    @iotester.feedback(simple=True, desc="With simple=True, you can provide simple feedback with just the AssertionError message.")
    def test_14_generic_unit_test_fail_3(self):
        """Example unit test (fail, feedback decorator, simple=True)"""
        # Import model wallet.py
        with iotester.model_directory():
            import wallet as model_wallet

        # Import student wallet.py
        import wallet as student_wallet
        # Do some testing
        # ...

        # Force fail to show difference between the three test method outputs
        msg = "See how the modules were imported from different files?"
        self.assertEqual(student_wallet.__file__, model_wallet.__file__, msg)


    @points(0)
    def test_15_generic_unit_test_error_1(self):
        """Example unit test (error, no feedback decorator)"""
        # Import model wallet.py
        with iotester.model_directory():
            import wallet as model_wallet

        # Import student wallet.py
        import wallet as student_wallet
        # Do some testing
        # ...

        # Force error to show difference between the three test method outputs
        1/0


    @points(0)
    @iotester.feedback(simple=False)
    def test_16_generic_unit_test_error_2(self):
        """Example unit test (error, feedback decorator, simple=False)"""
        # Import model wallet.py
        with iotester.model_directory():
            import wallet as model_wallet

        # Import student wallet.py
        import wallet as student_wallet
        # Do some testing
        # ...

        # Force error to show difference between the three test method outputs
        1/0


    @points(0)
    @iotester.feedback(simple=True)
    def test_17_generic_unit_test_error_3(self):
        """Example unit test (error, feedback decorator, simple=True)"""
        # Import model wallet.py
        with iotester.model_directory():
            import wallet as model_wallet

        # Import student wallet.py
        import wallet as student_wallet
        # Do some testing
        # ...

        # Force error to show difference between the three test method outputs
        1/0
