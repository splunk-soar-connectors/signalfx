# File: signalfx_consts.py
#
# Copyright (c) 2021-2022 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#
# exception handling
ERROR_MSG_UNAVAILABLE = "Error message unavailable. Please check the asset configuration and|or action parameters"
PARSE_ERROR_MSG = "Unable to parse the error message. Please check the asset configuration and|or action parameters"

# Integer validation constants
VALID_INTEGER_MSG = "Please provide a valid integer value in the {key}"
POSITIVE_INTEGER_MSG = "Please provide a valid non-zero positive integer value in the {key}"
NON_NEGATIVE_INTEGER_MSG = "Please provide a valid non-negative integer value in the {key}"

# page size
PAGE_SIZE = 100
LIMIT_PARAM_KEY = "'limit' action parameter"

DEFAULT_TIMEOUT = 30
