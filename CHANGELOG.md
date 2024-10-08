# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.1] - 2024-09-26
- Add coicop mapping to utils

## [0.3.0] - X
- Accomodate for new Eurostat API

## [0.2.4] - 2023-12-19
### Changed
- Update dtype for code column in coicop_labels

## [0.2.3] - 2023-12-18
### Changed
- Switched from .parquet to .csv for the labels to maximize compatibility

## [0.2.2] - 2023-08-18
### Fixed
- HICP pre-processing: removing " er"

## [0.2.1] - 2023-07-01
### Fixed
- HICP pre-processing: removing " d" & " du"

## [0.2.0] - 2023-07-01
### Added
- HICP pre-processing
- HICP parquet cache saving

### Remove
- Eurostat cache saving


## [0.1.2] - 2023-07-01
### Changed
- Eurostat functions logging

## [0.1.1] - 2023-07-01
### Added
- Python >3.13 support

### Removed
- `scipy` and `networkx` dependencies

## [0.1.0] - 2023-07-01
### Added
- First release
- Fully working HICP
- Base classes
- EuroStat utils
- COICOP labels utils
