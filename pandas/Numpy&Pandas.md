# Numpy



## np.where

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

