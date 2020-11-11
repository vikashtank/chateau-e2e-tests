# chateau-e2e-tests
End to end tests for Château.

## Running

### Staging

```bash
$ poetry run pytest --base-url "https://www.chateauapp.co"
```

### Production

```bash
$ poetry run pytest --base-url "https://www.chateau-staging.com"
```
