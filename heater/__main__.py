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

from heater.utils import purify_folder_name
from heater.constants import PROJECT_TYPES
from heater.generators import generate
from heater.ux import ask_input, initialize_heater, ask_token

import time


def main():
    initialize_heater()

    # Ask for input

    project_name = ask_input("Enter the name of your project")
    project_type = ask_input(
        f"What library does {project_name} use? Discord.py (d) or Hikari (h)",
        PROJECT_TYPES,
    )
    bot_token = ask_token("Enter your bot token")
    prefix = ask_input("Enter your bot's prefix")
    dependencies = ask_input(
        "Enter additional dependencies (comma separated)", optional=True
    ).split(",")

    # Generates projects
    start = time.time()
    generate(project_name, project_type, bot_token, prefix, dependencies)
    end = time.time()

    print(f"\nGenerated {project_name} project in {round((end - start) * 1000)}ms\n")
    print(
        f"Now open up your Terminal/Command Prompt and run:\n1. cd {purify_folder_name(project_name)}"
    )
    print("2. pip install -r requirements.txt\n3. python bot.py\n")
    print("Happy bot developing :D\n")
