# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801
"""Test lambda_openai_v2 function."""

# python stuff
import json
import os
import sys
import unittest
from pathlib import Path

import yaml


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = str(Path(HERE).parent.parent)
PYTHON_ROOT = str(Path(PROJECT_ROOT).parent)
if PYTHON_ROOT not in sys.path:
    sys.path.append(PYTHON_ROOT)  # noqa: E402


# pylint: disable=no-name-in-module
from openai_api.lambda_openai_function.function_refers_to import (
    get_additional_info,
    info_tool_factory,
)
from openai_api.lambda_openai_function.refers_to import CustomConfig
from openai_api.lambda_openai_function.tests.test_setup import get_test_file_path


class TestLambdaOpenaiFunctionRefersTo(unittest.TestCase):
    """Test OpenAI Function Calling hook for refers_to."""

    def setUp(self):
        """Set up test fixtures."""
        self.config_path = get_test_file_path("config/everlasting-gobbstopper.yaml")
        self.config = CustomConfig(config_path=self.config_path)

    # pylint: disable=broad-exception-caught
    def test_get_additional_info(self):
        """Test default return value of get_additional_info()"""
        try:
            # pylint: disable=no-value-for-parameter
            additional_information = get_additional_info(inquiry_type=self.config.additional_information.keys[0])
        except Exception:
            self.fail("get_additional_info() raised ExceptionType")

        self.assertTrue(additional_information is not None)

    def test_info_tool_factory(self):
        """Test integrity info_tool_factory()"""
        itf = info_tool_factory(config=self.config)
        self.assertIsInstance(itf, dict)

        self.assertIsInstance(itf, dict)
        self.assertTrue("type" in itf)
        self.assertTrue("function" in itf)
