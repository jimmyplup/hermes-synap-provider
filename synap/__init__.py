"""Synap model-provider plugin for Hermes Agent."""

from providers import register_provider
from providers.base import ProviderProfile


SYNAP_MODELS = (
    "qwen/qwen3-vl-30b-a3b-instruct",
    "qwen/qwen3-30b-a3b-instruct-2507",
    "qwen3-coder-30b",
    "meta/muse-glimmer-30b",
    "gpt-oss-20b",
    "gemma-4-26b-a4b-it",
)


synap = ProviderProfile(
    name="synap",
    aliases=("synap402", "linkrra"),
    display_name="Synap",
    description="Synap — OpenAI-compatible hosted inference",
    signup_url="https://synap402.com",
    env_vars=("SYNAP_API_KEY",),
    base_url="https://synap402.com/v1",
    models_url="https://synap402.com/v1/models",
    auth_type="api_key",
    default_aux_model="gpt-oss-20b",
    fallback_models=SYNAP_MODELS,
)

register_provider(synap)
