from __future__ import annotations
import os
import re
import sys
import random
from datetime import datetime


def hr1():
    return print("-" * 30)


def hr2():
    return print("=" * 30)


class COLORS:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class Func:
    def get_user_selection(self, options: list[str], default: int = 0) -> int:
        for i, option in enumerate(options):
            print(f"{COLORS.OKGREEN}{i+1}. {option}{COLORS.ENDC}")
        choice = input(f"choose one of the above options (default: {default+1}): ")
        while True:
            try:
                if choice == "":
                    return default
                choice = int(choice)
                if choice not in range(1, len(options) + 1):
                    raise ValueError
                return choice - 1
            except ValueError:
                choice = input(f"{COLORS.FAIL}invalid choice, try again: {COLORS.ENDC}")

    def get_user_input_number(self, prompt: str, default: int = 0) -> int:
        choice = input(f"{prompt} (default: {default}): ")
        while True:
            try:
                if choice == "":
                    return default
                choice = int(choice)
                return choice
            except ValueError:
                choice = input(f"{COLORS.FAIL}invalid choice, try again: {COLORS.ENDC}")

    def format_str(self, content: str, width: int) -> str:
        return f"| {content}{' '*(width-len(content))} "

