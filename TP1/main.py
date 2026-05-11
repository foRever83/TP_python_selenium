from tests.tests import *
import argparse

parser = argparse.ArgumentParser(
                    prog='TP1',
                    description='Main program to execute the first TP of Python Selenium')

parser.add_argument('-t', '--test', choices=("login", "dropdown", "add_remove_elements", "all"), default="all")
args = parser.parse_args()


if args.test == "login" or args.test == "all":
    print("="*20 + "\ttest_login\t" + "="*20)
    test_loging()
if args.test == "dropdown" or args.test == "all":
    print("="*20 + "\ttest_dropdown\t" + "="*20)
    test_dropdown()
if args.test == "add_remove_elements" or args.test == "all":
    print("="*20 + "\ttest_add_remove_elements\t" + "="*20)
    test_add_remove_elements()