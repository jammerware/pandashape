# 0.0.7
- Added a describer that summarizes discrete column values for columns that appear to be categorical]
- Moved label-encoding suggestion to new describer (CategoricalDescriber)
- Describers are no longer reported if they don't return messages.
- Added tests to support the above.

# 0.0.6
- Added PyTest!
- Binary columns are now ignored when describing distribution

# 0.0.5
- Corrected project homepage in setup.py
- Resolved a bug that prevented single-column transformer definitions from resolving correctly (e.g. 'Gender' rather than ['Gender'])
- Added `DistributionDescriber` to describe skew and identify outliers.
- Added `DTypesDescriber` to summarize frame data types.
- Added pypi version badge.

# 0.0.4
- Updated README
- `GenericTransformer` and `GenericDescriber` have been renamed to `Transformer` and `Describer` respectively for succinctness.
- Expansive refactoring to improve internal design and the external API surface.
- `Scaling` is now exported from the `pandashape` module.
- New describer: `CorrelationDescriber`

# 0.0.3
Renamed `MassLabelEncoder` to `CategoricalEncoder` for clarity.

# 0.0.2 
Fixed a build config issue that failed to include required files.

# 0.0.1
Initial publish!