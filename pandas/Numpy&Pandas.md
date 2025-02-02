# Numpy



## np.where()

**用法1**：

```python
np.where(condition, x, y)
```

**`condition`**中包含一个待处理的**`ndarray`**（这里记为A），那么对于**`A`**中的每个元素，如果满足条件，则将这个元素替换为**`x`**，否则，替换为**`y`**：

```python
>>> import numpy as np

>>> A = np.array([1, 2, 3, 4, 5])
>>> res = np.where(A > 3, 1, 0)

>>> print(res)
[0 0 0 1 1]
```

对于**`A`**中的每个元素，逐个对比其是否大于3，是则将对应位置"替换"为**1**，不是则为**0**。



**用法2**：

```python
np.where(condition)
```

类似的，对于A中的每个元素，检查其是否满足**`condition`**，如果是则返回其**坐标**：

```python
>>> A = np.array([1, 2, 3, 4, 5])
>>> res = np.where(A > 3)

>>> print(res)
(array([3, 4], dtype=int32),)
>>> print(A[res])
[4 5]
```







# Pandas



## loc()

**经典用法**

```python
# 单行选择（按标签）
df.loc["2023-01-01"]		# 假设索引是日期

# 多行多列选择
df.loc["row1":"row3", ["a", "b"]]	# 包含row3

# 条件筛选（无需预先计算）
df.loc[df["A"] > 0, "B"]	# A列大于0的行 & B列

# 修改数据（原地操作）
df.loc[df["A"] > 0, "B"] = 100	# 直接修改原数据
```



## iloc()

**经典用法**

```python
# 选择单行
df.iloc[3]				# 第4行（索引从0开始）

# 选择多行
df.iloc[2:5]			# 第3-5行（左闭右开，不含索引5）

# 选择行列组合
df.iloc[2:5, [0, 3]]	# 第3-5行 & 第1列和第4列

# 布尔索引（需长度匹配）
mask = [True, False, True, ...]	# 长度必须等于行数
df.iloc[mask]
```







## fillna()

> **`fillna`**是**pandas**中用于处理缺失值（NaN）的核心方法。

```python
DataFrame.fillna(
	value=None,		# 填充的固定值（标量、字典、series或DataFrame）
    method=None,	# 填充方法：'ffill'（向前填充）、'bfill'（向后填充)
    axis=None,		# 填充方向：0（沿行方向，默认）、1（沿列方向）
    limit=None,		# 最大连续填充量
)
```

**常用场景**：

- **固定值填充**：**`df.fillna(0)`**（所有NaN替换为0）
- **向前填充**：**`df.fillna(method='ffill')`**（用前面的非NaN值填充）
- **向后填充**：**`df.fillna(method='bfill')`**（用后面的非NaN值填充）

---

### Parameters

**按方向填充：`axis`参数**

**1. 向下填充（沿行方向）**

用**上方单元格的值**填充下方单元格的**NaN**：

```python
# 等效简写：df.ffill(axis=0)
df_filled = df.fillna(method='ffill', axis=0)
```

**实例输入**：

|      | A    | B    | C    |
| ---- | ---- | ---- | ---- |
| 0    | 1.0  | NaN  | NaN  |
| 1    | NaN  | 2.0  | NaN  |
| 2    | 3.0  | NaN  | NaN  |

**输出**：

|      | A    | B    | C    |
| ---- | ---- | ---- | ---- |
| 0    | 1.0  | NaN  | NaN  |
| 1    | 1.0  | 2.0  | NaN  |
| 2    | 3.0  | 2.0  | NaN  |

**2. 向右填充（按列方向）**

用**左侧单元格的值**填充右侧单元格的**NaN**：

```python
# 等效简写：df.ffill(axis=1)
df.filled = df.fillna(method='ffill', axis=1)
```

**实例输入**：

|      | A    | B    | C    |
| ---- | ---- | ---- | ---- |
| 0    | 1.0  | NaN  | NaN  |
| 1    | NaN  | 2.0  | NaN  |
| 2    | 3.0  | NaN  | NaN  |

**输出**：

|      | A    | B    | C    |
| ---- | ---- | ---- | ---- |
| 0    | 1.0  | 1.0  | 1.0  |
| 1    | NaN  | 2.0  | 2.0  |
| 2    | 3.0  | 3.0  | 3.0  |

**3. 组合填充**

```python
# 先向下填充，再向右填充
df_filled = df.ffill(axis=0).ffill(axis=1)

# 先向右填充，再向下填充
df_filled = df.ffill(axis=1).ffill(axis=0)
```

