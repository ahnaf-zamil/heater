# Copyright (c) 2021 K.M Ahnaf Zamil

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from heater.utils import is_blank

import heater
import typing
import platform
import getpass


def initialize_heater():
    """Runs when heater is initialized"""
    text = f"""  _    _            _            
 | |  | |          | |                      {heater.__description__}
 | |__| | ___  __ _| |_ ___ _ __ 
 |  __  |/ _ \/ _` | __/ _ \ '__|           {heater.__copyright__}
 | |  | |  __/ (_| | ||  __/ |              Version {heater.__version__}
 |_|  |_|\___|\__,_|\__\___|_|              Python {platform.python_version()}
"""
    print(text)


def ask_input(
    message: str, answers: typing.List[str] = None, optional: bool = False
) -> str:
    """Asks for input and returns it"""
    if optional:
        return input(message + " >> ")

    while True:
        inp = input(message + " >> ")
        if not answers:
            if is_blank(inp):
                print("Invalid input, please try again.")
                continue
            else:
                return inp
        if inp.lower() not in answers:
            print("Invalid input, please try again.")
            continue
        return inp


def ask_token(message: str) -> str:
    """Asks for token in a sensitive manner ie, without echoing"""
    return getpass.getpass(message)
