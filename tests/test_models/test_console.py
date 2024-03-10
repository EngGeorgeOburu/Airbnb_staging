#!/usr/bin/python3
"""
Tests for the console
"""

import sys
import models
import unittest
from io import StringIO
from unittest.mock import create_autospec
from console import HBNBCommand
from unittest.mock import create_autospec


class TestConsole(unittest.TestCase):
    """
    This is the test cases for the console module.
    """


    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        """
        Test if the quit command isin the console
        """
        console = HBNBCommand()
        console.onecmd("quit")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF_command(self, mock_stdout):
        """
        Test if 'EOF' command exit the console
        """
        console = HBNBCommand()
        console.onecmd("EOF")
        self.assertEqual(mock_stdout.getvalue(), "")

   @patch('sys.stdout', new_callable=StringIO)
   def test_create_command(self, mock_stdout):
       """
       Test case for the create command
       """
       console = HBNBCommand()
       console.onecmd("create BaseModel")
       self.assertIsInstance(mock_stdout.getvalue(), str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        """
        Test case for the show command.
        """
        console = HBNBCommand()
        console.onecmd("create BaseModel")
        console.onecmd("show BaseModel")
        self.assertIsInstance(mock_stdout.getvalue(), str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_command(self, mock_stdout):
        """
        Test case for all commands.
        """
        console = HBNBCommand()
        console.onecmd("all")
        self.assertIsInstance(mock_stdout.getvalue(), str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        """
        Test case for destroy command
        """
        console = HBNBCommand()
        console.onecmd("create BaseModel")
        console.onecmd("Destroy BaseModel")
        self.assertIsInstance(mock_stdout.getvalue(), str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        """
        Test case for the update command
        """
        console = HBNBCommand()
        console.onecmd("create BaseModel")
        console.onecmd("update BaseModel")
        self.assertIsInstance(mock_stdout.getvalue(), str)

    if __name__ == '__main__':
        unittest.main()
