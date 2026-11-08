# Changelog

Changes to the wger REST API itself are documented in the backend's release
notes, linked below. This file records important changes to *this package*.

## 2.7.1

**Breaking:** the client is built on [`httpx2`](https://pypi.org/project/httpx2/)
instead of `httpx`, following openapi-python-client 0.30. The endpoints and
models are unchanged; what changes is the HTTP layer underneath:

* `set_httpx_client()`, `set_async_httpx_client()`, `with_timeout()` and
  `httpx_args` are typed for `httpx2` objects (`httpx2.Client`,
  `httpx2.AsyncClient`, `httpx2.Timeout`, `httpx2.Auth`). Passing an `httpx`
  object still works at runtime, but type checkers flag it.
* Transport errors are `httpx2` exceptions (`httpx2.TimeoutException`,
  `httpx2.ConnectError`, ...). An `except httpx.…` clause no longer catches
  them, and does so silently.
* Mocks keyed to `httpx` (respx, pytest-httpx) no longer intercept requests.
  With respx, the `pytest-httpx2` plugin adds the missing `httpcore2` mocker.
* TLS certificates are verified against the operating system's trust store
  instead of the `certifi` bundle. A container without CA certificates needs
  `ca-certificates` installed or `SSL_CERT_FILE` set.
* The default User-Agent is `python-httpx2/<version>`.

Also fixed: `multipart/form-data` requests were sent with the fixed boundary
`+++`, so an upload containing `\r\n--+++` was cut short at that point. httpx2
now picks a random boundary per request.

## 2.7.0

Update to 2.7.0. See [backend release notes]( https://github.com/wger-project/wger/releases/tag/2.7).

## 2.6.1

* The `*__in` filters (`id__in`, `category__in`, `muscles__in`, and so on) now
  send their values as one comma-separated parameter, as the API expects. They
  were sent as repeated parameters before, and the server applied only the last
  value of each.

## 2.6.0

First version of the package. See [backend release notes]( https://github.com/wger-project/wger/releases/tag/2.6).
