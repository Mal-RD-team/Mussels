"""
Copyright (C) 2019 Cisco Systems, Inc. and/or its affiliates. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import shutil

from mussels.recipe import BaseRecipe


class Recipe(BaseRecipe):
    """
    Recipe to build clamav.
    """

    mussels_version = "0.1"

    name = "clamav_deps"
    version = "0.101.4"
    is_collection = True
    platform = ["Windows"]
    platforms = {
        "Windows": {
            "x86": {"dependencies": ["openssl<1.1.1"]},
            "x64": {"dependencies": ["openssl<1.1.1"]},
        },
        "Posix": {
            "host": {
                "dependencies": [
                    "curl",
                    "json_c",
                    "libxml2",
                    "openssl",
                    "pcre2",
                    "bzip2",
                ]
            }
        },
    }
