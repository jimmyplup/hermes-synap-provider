"""Offline contract tests for the Synap Hermes provider."""

from __future__ import annotations

import importlib.util
import sys
import types
import unittest
from dataclasses import dataclass
from pathlib import Path


@dataclass
class _ProviderProfile:
    name: str
    aliases: tuple = ()
    display_name: str = ""
    description: str = ""
    signup_url: str = ""
    env_vars: tuple = ()
    base_url: str = ""
    models_url: str = ""
    auth_type: str = "api_key"
    default_aux_model: str = ""
    fallback_models: tuple = ()


class SynapProfileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registered = []
        providers = types.ModuleType("providers")
        providers.register_provider = cls.registered.append
        base = types.ModuleType("providers.base")
        base.ProviderProfile = _ProviderProfile
        sys.modules["providers"] = providers
        sys.modules["providers.base"] = base

        plugin = Path(__file__).parents[1] / "synap" / "__init__.py"
        spec = importlib.util.spec_from_file_location("synap", plugin)
        assert spec and spec.loader
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def test_registers_one_provider(self) -> None:
        self.assertEqual(self.registered, [self.module.synap])

    def test_uses_canonical_endpoint(self) -> None:
        self.assertEqual(self.module.synap.base_url, "https://synap402.com/v1")
        self.assertEqual(
            self.module.synap.models_url, "https://synap402.com/v1/models"
        )

    def test_exposes_live_fleet_models(self) -> None:
        self.assertEqual(len(self.module.synap.fallback_models), 6)
        self.assertIn("meta/muse-glimmer-30b", self.module.synap.fallback_models)
        self.assertIn(
            "qwen/qwen3-30b-a3b-instruct-2507",
            self.module.synap.fallback_models,
        )


if __name__ == "__main__":
    unittest.main()
