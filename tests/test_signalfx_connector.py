# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import types
import unittest
from unittest.mock import Mock


phantom_package = types.ModuleType("phantom")
phantom_package.__path__ = []
phantom_app = types.ModuleType("phantom.app")
phantom_app.APP_ERROR = 1
phantom_app.APP_SUCCESS = 0
phantom_app.is_fail = lambda status: status != 0
phantom_action_result = types.ModuleType("phantom.action_result")


class DummyActionResult:
    def __init__(self, *_args, **_kwargs):
        pass


phantom_action_result.ActionResult = DummyActionResult
phantom_base_connector = types.ModuleType("phantom.base_connector")
phantom_base_connector.BaseConnector = object
phantom_package.app = phantom_app
sys.modules.setdefault("phantom", phantom_package)
sys.modules.setdefault("phantom.app", phantom_app)
sys.modules.setdefault("phantom.action_result", phantom_action_result)
sys.modules.setdefault("phantom.base_connector", phantom_base_connector)

from signalfx_connector import SignalfxConnector


class FakeActionResult:
    def __init__(self):
        self.data = []
        self.summary = {}
        self.status = None

    def add_data(self, data):
        self.data.append(data)

    def update_summary(self, summary):
        self.summary = summary
        return summary

    def set_status(self, status, *_args):
        self.status = status
        return status

    def get_status(self):
        return self.status


class SignalfxConnectorTest(unittest.TestCase):
    def test_run_query_collects_every_dimension_page(self):
        connector = object.__new__(SignalfxConnector)
        connector._headers = {"X-SF-TOKEN": "test-token"}  # pragma: allowlist secret
        connector.save_progress = Mock()
        connector.get_action_identifier = Mock(return_value="run_query")
        action_result = FakeActionResult()
        connector.add_action_result = Mock(return_value=action_result)
        connector._make_rest_call = Mock(
            side_effect=[
                (0, {"count": 3, "results": [{"value": "one"}, {"value": "two"}]}),
                (0, {"count": 3, "results": [{"value": "three"}]}),
            ]
        )

        status = connector._handle_run_query({"query": "host"})

        self.assertEqual(status, 0)
        self.assertEqual(action_result.summary, {"total_results": 3})
        self.assertEqual(
            action_result.data,
            [{"count": 3, "results": [{"value": "one"}, {"value": "two"}, {"value": "three"}]}],
        )
        self.assertEqual(connector._make_rest_call.call_count, 2)
        self.assertEqual(connector._make_rest_call.call_args_list[0].kwargs["params"], {"query": "host", "limit": 100, "offset": 0})
        self.assertEqual(connector._make_rest_call.call_args_list[1].kwargs["params"], {"query": "host", "limit": 100, "offset": 2})


if __name__ == "__main__":
    unittest.main()
