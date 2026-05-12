from tests.tests import *
import argparse

parser = argparse.ArgumentParser(
                    prog='TP1',
                    description='Main program to execute the first TP of Python Selenium')

parser.add_argument('-t', '--test', choices=("dynamic_controls", "dynamic_loading", "add_remove_elements", "all"), default="all")
args = parser.parse_args()


if args.test == "dynamic_controls" or args.test == "all":
    print("="*20 + "\tdynamic_controls\t" + "="*20)
    test_dynamic_controls()
if args.test == "dynamic_loading" or args.test == "all":
    print("="*20 + "\tdynamic_loading\t" + "="*20)
    test_dynamic_loading()
if args.test == "add_remove_elements" or args.test == "all":
    print("="*20 + "\ttest_add_remove_elements\t" + "="*20)
    #test_add_remove_elements()