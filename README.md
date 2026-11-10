# Hermes Synap provider

Model-provider plugin for [Hermes Agent](https://github.com/NousResearch/hermes-agent).
It registers [Synap](https://synap402.com) as an OpenAI-compatible inference
provider and exposes Synap's live model catalog to the Hermes model picker.

## Install

After the plugin is accepted into the Hermes catalog:

```bash
hermes plugins install synap
```

Manual installation:

```bash
git clone https://github.com/jimmyplup/hermes-synap-provider.git
mkdir -p ~/.hermes/plugins/model-providers
cp -r hermes-synap-provider/synap ~/.hermes/plugins/model-providers/synap
```

## Configure

```bash
export SYNAP_API_KEY="your-key"
hermes --provider synap --model qwen3-coder-30b
```

Create a key at <https://synap402.com>. The plugin uses:

- API base: `https://synap402.com/v1`
- Model catalog: `https://synap402.com/v1/models`
- Environment variable: `SYNAP_API_KEY`

## Development

```bash
python -m unittest discover -s tests -v
```

The tests are offline and use a minimal Hermes provider-registry stub.
