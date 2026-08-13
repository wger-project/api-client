# Changelog

Changes to the wger REST API itself are documented in the backend's release
notes, linked below. This file records important changes to *this package*.

## 2.6.0

First version of the package. See [backend release notes]( https://github.com/wger-project/wger/releases/tag/2.6).

## Unreleased

* The `*__in` filters (`id__in`, `category__in`, `muscles__in`, and so on) now
  send their values as one comma-separated parameter, as the API expects. They
  were sent as repeated parameters before, and the server applied only the last
  value of each.

## 2.7.0

...