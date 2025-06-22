## Profiling Explanation

After running `cProfile`, it was found that the most time-consuming function is `analyze_data`, specifically:
- Merging dataframes (`merge`)
- Calculating population density and other derived metrics

This is expected since several tables are being processed and aggregated. With the current dataset size, it does not cause performance issues. However, for larger datasets, the following optimizations could be considered:
- Indexing the `region` columns before merging
- Using more efficient data storage formats such as Parquet

No optimization has been applied yet, as it was not a requirement.
