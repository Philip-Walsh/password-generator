# password-generator

```bash
( \
poetry shell && \
poetry update && \
poetry install && \
poetry run pytest  && \
poetry run pylint **/*.py && \
poetry run flake8 && \
echo "🧪 CI Passed! ✅"
) || echo "🧪 CI Failed! ❌"
```

```
poetry run python -m pass_gen --help

poetry run python -m pass_gen generate -len 20
```