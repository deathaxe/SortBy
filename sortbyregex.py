#     Copyright 2014 - 2021 Yannick Watier
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
import json
import re

import sublime
import sublime_plugin


class SrtbyreCommand(sublime_plugin.TextCommand):
    def run(self, edit, regex, regex_group, available_sort):

        available_sort["regex"] = {
            "regex": regex,
            "group": regex_group,
        }

        self.view.run_command('srtbyli', available_sort)

    def input(self, args):
        if "regex" not in args:
            return RegexInputHandler()
        elif "regex_group" not in args:
            return RegexGroupInputHandler()
        elif "available_sort" not in args:
            return AvailableSortInputHandler()
        else:
            return None


class RegexInputHandler(sublime_plugin.TextInputHandler):
    def placeholder(self):
        return "Python RegEx"

    def validate(self, text):
        try:
            re.compile(text)
            return True
        except re.error:
            return False


class RegexGroupInputHandler(sublime_plugin.TextInputHandler):
    def placeholder(self):
        return "Regex group (Starting at ZERO)"

    def validate(self, text):
        try:
            return int(text) >= 0
        except ValueError:
            return False


class AvailableSortInputHandler(sublime_plugin.ListInputHandler):
    def list_items(self):
        current_commands = json.loads(sublime.load_resource('Packages/SortBy/Commands.sublime-commands'))
        values = []
        if len(current_commands) > 0:
            for command in current_commands:

                extracted_command = self.extract_command(command, "command")

                if extracted_command is None or extracted_command == "srtbyre":
                    continue  # Skip the regex sort

                extracted_args = self.extract_command(command, "args")
                extracted_caption = self.extract_command(command, "caption")
                values.append((extracted_caption, extracted_args))

        return values

    def extract_command(self, command, name):
        try:
            return command[name]
        except KeyError:
            return None

    def placeholder(self):
        return "Sort"
