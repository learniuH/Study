# PyQt5.QtWidget





## QFileDialog



### getOpenFileName()

> 用于打开文件选择对话框，允许用户选择一个文件并返回文件路径。

```python
QFileDialog.getOpenFileName(
	parent: QWidget 	= None,			# 父窗口
    caption: str		= '',			# 对话框标题
    directory: str		= '',			# 初始目录
    filter: str			= '',			# 文件过滤器
    initialFilter:str	= '',			# 初始选中的过滤器
    options: QFileDialog.Options = 0	# 对话框选项
) -> Tuple[str, str]					# 返回（文件路径，选中的过滤器）
```



---

#### Parameters

1. **`parent: QWidget = None`**

   - **作用**：指定对话框的父窗口。
   - **要求**：必须是**`QWidget`**或其子类（如**`QMainWindow`**、**`QDialog`**）。
   - **`None`**表示无父窗口（对话框独立显示）

2. **`caption: str = ''`**

   - **作用**：设置对话框的标题

3. **`directory: str = ''`**

   - **作用**：设置初始打开的目录
   - **规则**：
     - 传空字符串时，默认使用系统最近访问的目录。
     - 可传绝对路径（如**`D:/Users`**）或相对路径（如**`./data`**）。

4. **`filter: str = ''`**

   - **作用**：定义文件类型过滤器，限制用户只能选择特定类型的文件。
   - **语法**：
     - 过滤器由多个描述符组成，用分号**`;;`**分割。
     - 每个描述符格式：**`"显示名称 (*.扩展名1 *.扩展名2)"`**

   - **示例**：

   ```python
   filter = "ExcelFile (*.xlsx *.xls);; ImageFile (*.png *.jpg);; AllFiles (*)"
   ```

   ![](C:\Users\L\Desktop\PyQt5\img\filterExample.png)

   > 用户可以选择**Excel文件**或**图片文件**或**所有文件**。

5. **`initialFilter: str = ''`**

   - **作用**：设置初始选中的过滤器（需与**`filter`**中的某个描述完全匹配）。
   - **示例**：

   ```python
   filter = "ExcelFile (*.xlsx *.xls);; ImageFile(*.png *.jpg)"
   initialFilter = "ImageFile(*.png *.jpg)"	# 默认选中图片文件过滤器
   ```

6. **`options: QFileDialog.Options = 0`**

   - **作用**：控制对话框行为的选项（多个选项用按位或**`|`**组合）。
   - **常用选项**:

| 选项                                    | 作用                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| **`QFileDialog.DontUseNativeDialog`**   | 强制使用Qt自带对话框（而非系统原生对话框）                   |
| **`QFileDialog.ShowDirsOnly`**          | 只显示目录（隐藏文件）                                       |
| **`QFileDialog.ReadOnly`**              | 对话框以只读模式打开                                         |
| **`QFileDialog.HideNameFilterDetails`** | 隐藏过滤器中的扩展名（如显示**ExcelFile**而非ExcelFile (*.xlsx *.xls) |
| **`QFileDialog.DontResolveSymlink`**    | 不解析符号链接                                               |

- **实例**：

```python
options = QFileDialog.DontUseNativeDialog | QFileDialog.ReadOnly
```



---

#### Returns

- **类型**：**`Tuple[str, str]`**
- **内容**：
  - 第一个元素：用户选择的文件路径（未选择时返回空字符串）
  - 第二个元素：用户选择的过滤器描述符（如**`ExcelFile (*.xlsx *.xls)`**）

#### Q&A

**1. 如何跳过中间参数？**

若想跳过某个参数（如不设置**directory**但要设置**filter**），需使用**关键字参数**：

```python
file_name, _ = QFileDialog.getOpenFileName(
	parent		=	self,
    caption		=	"选择测试用例",
    filter		=	"ExcelFile (*.xls *.xlsx)",
   	directory	=	""	# 可省略
)
```

**2. 如何同时选择多个文件？**

使用**`getOpenFileNames()`**方法，返回值是文件路径列表。



---

#### Summary

| 参数          | 关键点                                                     |
| ------------- | ---------------------------------------------------------- |
| **`parent`**  | 必须是**`QWidget`**或**`None`**                            |
| **`filter`**  | 用**`;;`**分隔多个过滤器，格式为**`描述 (*.ext1 *.ext2)`** |
| **`options`** | 通过按位或**`|`**组合多个选项                              |
| **`Returns`** | 始终检查文件路径是否为空（避免用户取消操作）               |





# QSS



## TableWidget

> QTabelWidget                                                                 外框
>
> QTableWidget QTableCornerButton::section            角落
>
> QHeaderView                                                                  表头
>
> QHeaderView::section                                                   表头字段
>
> QHeaderView::section:pressed                                   表头字段点击
>
> QHeaderView::section:checked                                   表头字段选中
>
> QTableWidget QHeaderView::section:horizontal     水平表头字段
>
> QTableWidget QheaderView::section:vertical           垂直表头字段
>
> QTableWidget::item                                                       表格
>
> QTableWidget::item:selected                                       选中的表格
>
> QTableWidget::item:editing                                          编辑的表格
>
> QTableWidget QLineEdit                                               编辑表格的文字
>
> QTableWidget QScrollBar::horizontal                         水平滚动条
>
> QTableWidget QScrollBar::vertical                              垂直滚动条
>
> QTableWidget QScrollBar::handle:horizontal           水平滚动条滑块
>
> QTableWidget QScrollBar::handle:vertical                垂直滚动条滑块
>
> QScrollBar::handle:horizontal:hover                          水平滚动条滑块悬浮
>
> QScrollBar::handle:vertical:hover                               垂直滚动条滑块悬浮
>
> QTableWidget QScrollBar::add-line                            滑块上方边缘方块
>
> QTableWidget QScrollBar::sub-line                            滑块下方边缘方块
>
> QTableWidget QScrollBar::add-page                         滑块上部分滑道
>
> QTableWidget QScrollBar::sun-page                          滑块下部分滑道