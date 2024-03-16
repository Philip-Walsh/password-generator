# password-generator

```bash
( \
poetry install && \
pytest  && \
poetry run pylint **/*.py && \
poetry run flake8 && \
echo "🧪 CI Passed! ✅"
) || echo "🧪 CI Failed! ❌"
```