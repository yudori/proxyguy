#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_proxyguy
----------------------------------

Tests for `proxyguy` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from proxyguy import cli


class TestProxyguy(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.init)
        assert result.exit_code == 0
        help_result = runner.invoke(cli.init, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    @classmethod
    def teardown_class(cls):
        pass

