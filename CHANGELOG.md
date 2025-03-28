---
hide:
    - navigation
---
# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

To see unreleased changes, please see the [CHANGELOG on the master branch](https://github.com/gufolabs/gufo_traceroute/blob/master/CHANGELOG.md) guide.

## 0.2.1 -- 2025-03-28

### Added

* Python 3.12 and 3.13 support.

### Changed

* docs: Fancy front page.

### Removed

* Drop Python 3.8 support.

### Infrastructure

* Adopt Ruff.
* devcontainer: Move `settings` to the `customisations.vscode.settings`
* mkdocs-material 9.2.3
* mypy 1.13.0
* Ruff 0.11.2

## 0.2.0 - 2022-12-15

### Added

* `Hop.asn` field.
* Built-in whois client for autonomous system lookups.

### Infrastructure

* Switch to the `pypa/gh-action-pypi-publish@release/v1`

## 0.1.1 - 2022-12-14

### Added

* `min_ttl` parameter.
* `src_port` parameter.
* `src_addr` parameter.

### Infrastructure

* CI workflows tests

## 0.1.0 - 2022-12-11

### Added

* Initial implementation