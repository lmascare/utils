#!/usr/bin/env python

"""
A menu driven utility.

The menus in this script allow you to choose various options.
Of importance in this example script is the definition of a dictionary to
execute the various options. As opposed to using case statements.
"""
import sys
import os


def open_tvm_webapp():
    """Run the TVM WebApp."""
    print "Opening TVM Web App"


def search_idefense():
    """Search iDefense for a CVE."""
    print "Searching iDefense"


def exit_menu():
    """Exit gracefully."""
    print "Exiting. Bye bye..."
    sys.exit(0)


def fail():
    """Invalid option. Exit with error code 1."""
    print "Valid options are -- {}".format(menu_items.keys())
    sys.exit(1)


def init():
    """Not used is not used for now."""
    pass


menu_items = {
    "1": open_tvm_webapp,
    "2": search_idefense,
    "88": exit_menu
    }


def main():
    """Menu to perform different functions."""
    os.system('clear')
    print 20 * '-'
    print "|   TVM Operations  |"
    print 20 * '-'
    print ""
    print "  1. Open TVM WebApp"
    print "  2. Search iDefense"
    print ""
    print "  88. Exit"

    response = raw_input("Enter Selection : ")
    menu_items.get(response, fail)()


if __name__ == "__main__":
    init()
    main()
