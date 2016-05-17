#!/usr/bin/env python

"""
A brief demo of rule matching.

Use case: You have a suite of tests to perform, and
for a set of actions you want to perform based on what
combinations of results were returned.

DISPATCH_TABLE could be generated from an external source
the dummy 'data' is intended to be the stored results of
a set of functions/tests.

"""


def printrule(data):
    """A dummy function to use as an action."""
    print(data)

DISPATCH_TABLE = {
    ('Y', 'N', 'Y', None, 'Y', 'Y'): printrule,
    ('Y', 'Y', 'Y', None, 'Y', 'Y'): printrule,
    ('Y', 'N', 'N', None, 'Y', 'Y'): printrule,
    ('Y', 'N', None, None, 'Y', 'Y'): printrule,
    ('Y', 'N', 'Y', 'Y', 'Y', 'Y'): printrule,
    ('Y', 'N', 'Y', None, 'N', 'Y'): printrule,
    ('Y', 'N', 'Y', 'N', 'N', 'N'): printrule,
    ('Y', 'N', 'Y', None, 'Y', None): printrule,
    ('Y', 'Y', 'Y', None, 'Y', 'Y'): printrule,
    ('Y', 'Y', 'N', 'Y', 'Y', 'Y'): printrule
}


def match(data, rules):
    """
    Match a result set to a rule.

    Given a tuple containing test results, and a dispatch table,
    call any function for test results that match entries in the
    dispatch table
    """
    for rule in rules:
        # TODO: Set up partial matches and None padding
        if len(data) != len(rule):
            continue
        # Could also use a custom matching function that returns True/False
        # instead of `data[i] == v`
        truths = [data[i] == v for i, v in enumerate(rule) if v is not None]
        if False not in truths:
            rules[rule]("{} matched {}".format(data, rule))


if __name__ == '__main__':
    match(('Y', 'N', 'Y', 'Y', 'Y', 'Y'), DISPATCH_TABLE)
    match(('Y', 'N', 'Y', 'N', 'N', 'Y'), DISPATCH_TABLE)
