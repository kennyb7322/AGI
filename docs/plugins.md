# Plugins and extensibility

Most agent frameworks eventually need a plugin system for:

- adding tools without editing core code,
- integrating new model providers,
- swapping memory backends.

This scaffold keeps bootstrapping explicit in `src/agi/bootstrap.py`.

## Option A: explicit registration (recommended)

Pros:
- simple
- auditable
- easy to reason about

Cons:
- requires code change to add a tool

## Option B: runtime plugins (advanced)

Use `src/agi/plugins/loader.py` to load factories by dotted path.

Example config idea (not implemented by default):

```yaml
tools:
  my_tool:
    factory: "my_pkg.my_mod:create_tool"
    config:
      foo: bar
```

Then:

- load the factory
- instantiate the tool
- register it in `ToolRegistry`
- update policy allowlist

Be careful: plugin systems expand attack surface.

