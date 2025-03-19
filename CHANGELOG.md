# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] - 2025-03-19

- add possibility to specify which objective a selection strategy
  should use.
- implement roulette wheel selection.
- add a fitness function for the absolute distance between to unitaries.
- implement the ranking-based fitness function from Williams et al. (1998)

## [0.2.0] - 2025-03-12

- add generation id parameter to multiple interfaces.
- add before generation callbacks.
- move ga parameters to a custom dataclass and add it to the
  constructor of any classes that use one or more of these parameters.

## [0.1.0] - 2025-03-11

- initial version.
