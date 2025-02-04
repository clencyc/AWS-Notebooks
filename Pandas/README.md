# 📊 Pandas Quick Reference - Glossary

This glossary summarizes key **Pandas functions and methods** from the [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) guide.

---

## 📥 **Category: Initialization and Utility**

| **Function/Method**                               | **Description** |
|--------------------------------------------------|-----------------|
| `pandas.read_csv(relative_path_to_file)`         | Reads a CSV file from `relative_path_to_file` and loads it as a DataFrame. |
| `pandas.DataFrame(data)`                         | Returns a 2-D heterogeneous tabular data structure (DataFrame). Optional arguments are available. |
| `pandas.Series(data, index)`                     | Returns a 1-D ndarray with axis labels (Series). |
| `pandas.Series.shape` / `pandas.DataFrame.shape` | Returns a tuple representing the dimensions. |
| `pandas.Series.ndim` / `pandas.DataFrame.ndim`   | Returns the number of dimensions (rank). For Series, it returns `1`. |
| `pandas.Series.size` / `pandas.DataFrame.size`   | Returns the total number of elements. |
| `pandas.Series.values`                           | Returns the data contained in the Series. |
| `pandas.Series.index`                            | Returns the indexes of the Series. |
| `pandas.DataFrame.isnull()`                      | Returns an object of the same size with `True` for `NaN` elements, `False` otherwise. |
| `pandas.DataFrame.count(axis)`                   | Counts non-NaN values along the specified axis (`0` for columns, `1` for rows). |
| `pandas.DataFrame.head([n])`                     | Returns the first `n` rows (default is `5`). |
| `pandas.DataFrame.tail([n])`                     | Returns the last `n` rows (default is `5`). Supports negative indexing. |
| `pandas.DataFrame.describe()`                    | Generates descriptive statistics: count, mean, std deviation, min, max, etc. |
| `pandas.DataFrame.min()`                         | Returns the minimum value along the specified axis. |
| `pandas.DataFrame.max()`                         | Returns the maximum value along the specified axis. |
| `pandas.DataFrame.mean()`                        | Returns the mean of values along the specified axis. |
| `pandas.DataFrame.corr()`                        | Computes pairwise correlation of columns, excluding NA/null values. |
| `pandas.DataFrame.rolling(window)`               | Provides rolling window calculations (e.g., `rolling(15).mean()` for a rolling mean with a window of 15). |
| `pandas.DataFrame.loc[label]`                    | Accesses rows and columns by label(s). |
| `pandas.DataFrame.groupby(mapping_function)`     | Groups the DataFrame using a mapper function or a Series of columns. |

---

## 🔄 **Category: Manipulation**

| **Function/Method**                               | **Description** |
|--------------------------------------------------|-----------------|
| `pandas.Series.drop(index)`                      | Drops the element at the specified index. |
| `pandas.DataFrame.drop(labels)`                  | Drops specified labels (rows or columns) from the DataFrame. |
| `pandas.DataFrame.pop(item)`                     | Removes the specified item (column) from the DataFrame and returns it. Raises `KeyError` if not found. |
| `pandas.DataFrame.insert(location, column, values)` | Inserts a column with given values at the specified location in the DataFrame. |
| `pandas.DataFrame.rename(dictionary-like)`       | Renames labels (columns or row indexes) as specified in a dictionary-like structure. |
| `pandas.DataFrame.set_index(keys)`               | Sets one or more existing columns as the DataFrame’s index. |
| `pandas.DataFrame.dropna(axis)`                  | Removes rows (`axis=0`) or columns (`axis=1`) that contain missing values (`NaN`). |
| `pandas.DataFrame.fillna(value, method, axis)`   | Replaces `NaN` values with a specified value. Supports methods like `backfill`, `bfill`, `pad`, `ffill`, or `None`. |
| `pandas.DataFrame.interpolate(method, axis)`     | Replaces `NaN` values with interpolated values calculated using the specified method along the given axis. |

---

### 📚 **References:**
- Official Pandas Documentation: [https://pandas.pydata.org/](https://pandas.pydata.org/)
- [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)

---

> _This cheat sheet is perfect for quick reference while working with Pandas!_ 🚀
