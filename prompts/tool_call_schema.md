# Tool call schema

The recommended tool call schema is simple JSON:

## Tool call

```json
{
  "action": "tool",
  "tool": "calculator",
  "args": {
    "expression": "2+2"
  }
}
```

## Final response

```json
{
  "action": "final",
  "content": "The answer is 4."
}
```

If the model cannot comply, it may output plain text, which the runtime treats as final.
