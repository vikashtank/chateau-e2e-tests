# Château end-to-end tests

End to end tests for Château.

## Installation

```sh
$ brew install chromedriver
```

## Running

### Staging

```sh
$ poetry run pytest --driver Chrome --base-url "https://www.chateau-staging.com"
```

### Production

```sh
$ poetry run pytest --driver Chrome --base-url "https://www.chateauapp.co"
```
