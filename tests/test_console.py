#!/usr/bin/python3
"""[summary]
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os
import sys


class TestConsole(TestCase):
    """[Test console]

    Args:
        TestCase ([obj]): [TestCase from unittest module]
    """
    def setUp(self):
        """[setup method]
        """
        pass

    def tearDown(self):
        """[teardown method]
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_class_name_missing(self):
        """[test class name]
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

    def test_wrong_class(self):
        """[test wrong class]
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create bouhabra")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def test_id_type(self):
        """[test type id]
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        msg = f.getvalue()[:-1]
        self.assertEqual(type(msg), str)

    def test_all_output_type(self):
        """[test type]
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        msg = f.getvalue()[:-1]
        self.assertEqual(type(msg), str)

    def test_create_user(self):
        """[test_user]
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User name="lothric"')
            HBNBCommand().onecmd('all User')
        msg = f.getvalue()[:-1]
        self.assertTrue("'name': 'lothric'" in msg)

    def test_decimal(self):
        """[test_decimal]
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User number_bathrooms=4')
            HBNBCommand().onecmd('all User')
        msg = f.getvalue()[:-1]
        self.assertTrue("'number_bathrooms': 4" in msg)

    def test_float(self):
        """[test_float]
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User price=0.069')
            HBNBCommand().onecmd('all User')
        msg = f.getvalue()[:-1]
        self.assertTrue("'price': 0.069" in msg)
