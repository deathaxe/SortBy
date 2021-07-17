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

class SubSorts:
    ALPHABETICALLY = "ALPHABETICALLY"
    ALPHABETICALLY_DESCENDING = "ALPHABETICALLY_DESCENDING"

    def is_alphabetically_sort(sort_type: str) -> bool:
        return sort_type.upper() == SubSorts.ALPHABETICALLY or sort_type.upper() == SubSorts.ALPHABETICALLY_DESCENDING

    def is_alphabetically_descending(sort_type: str) -> bool:
        return sort_type.upper() == SubSorts.ALPHABETICALLY_DESCENDING
