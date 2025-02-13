# PyQt5.QtWidget



## QTableWidget

### 1. 基础设置

| 方法                                  | 作用             | 示例                                                     |
| :------------------------------------ | :--------------- | :------------------------------------------------------- |
| **`setRowCount(int rows)`**           | 设置表格行数     | `table.setRowCount(10)`                                  |
| **`setColumnCount(int cols)`**        | 设置表格列数     | `table.setColumnCount(5)`                                |
| **`setHorizontalHeaderLabels(list)`** | 设置水平表头标签 | `table.setHorizontalHeaderLabels(["ID", "Name", "Age"])` |
| **`setVerticalHeaderLabels(list)`**   | 设置垂直表头标签 | `table.setVerticalHeaderLabels(["Row1", "Row2"])`        |
| **`horizontalHeader()`**              | 获取水平表头对象 | `header = table.horizontalHeader()`                      |
| **`verticalHeader()`**                | 获取垂直表头对象 | `header = table.verticalHeader()`                        |

### 2. 数据操作

| 方法                                              | 作用                         | 示例                                            |
| :------------------------------------------------ | :--------------------------- | :---------------------------------------------- |
| **`setItem(int row, int col, QTableWidgetItem)`** | 设置单元格数据               | `table.setItem(0, 0, QTableWidgetItem("Data"))` |
| **`item(int row, int col)`**                      | 获取单元格对象               | `item = table.item(0, 0)`                       |
| **`takeItem(int row, int col)`**                  | 移除单元格内容               | `table.takeItem(0, 0)`                          |
| **`clear()`**                                     | 清空所有内容（保留行列数）   | `table.clear()`                                 |
| **`clearContents()`**                             | 清空数据（保留行列数和表头） | `table.clearContents()`                         |
| **`insertRow(int row)`**                          | 插入行                       | `table.insertRow(2)`                            |
| **`insertColumn(int col)`**                       | 插入列                       | `table.insertColumn(3)`                         |
| **`removeRow(int row)`**                          | 删除行                       | `table.removeRow(1)`                            |
| **`removeColumn(int col)`**                       | 删除列                       | `table.removeColumn(0)`                         |

### 3. 外观控制

| 方法                                     | 作用                 | 示例                                                         |
| :--------------------------------------- | :------------------- | :----------------------------------------------------------- |
| **`setColumnWidth(int col, int width)`** | 设置列宽             | `table.setColumnWidth(0, 100)`                               |
| **`setRowHeight(int row, int height)`**  | 设置行高             | `table.setRowHeight(0, 30)`                                  |
| **`resizeColumnsToContents()`**          | 根据内容自动调整列宽 | `table.resizeColumnsToContents()`                            |
| **`resizeRowsToContents()`**             | 根据内容自动调整行高 | `table.resizeRowsToContents()`                               |
| **`setEditTriggers(EditTriggers)`**      | 设置单元格编辑条件   | `table.setEditTriggers(QTableWidget.NoEditTriggers)`         |
| **`setSelectionMode(SelectionMode)`**    | 设置选择模式         | `table.setSelectionMode(QTableWidget.SingleSelection)`       |
| **`setStyleSheet(str)`**                 | 设置 CSS 样式        | `table.setStyleSheet("QTableWidget {background: #f0f0f0;}")` |

### 4. 信号与事件

| 信号                                | 触发条件             | 槽函数示例                                                |
| :---------------------------------- | :------------------- | :-------------------------------------------------------- |
| **`cellClicked(int row, int col)`** | 点击单元格时触发     | `def on_click(row, col): print(f"Clicked {row}, {col}")`  |
| **`cellChanged(int row, int col)`** | 单元格内容修改后触发 | `def on_change(row, col): print(f"Changed {row}, {col}")` |
| **`itemSelectionChanged()`**        | 选中项变化时触发     | `def on_selection_change(): print("Selection changed")`   |

### 5. 高级功能

| 方法                                                      | 作用               | 示例                                                |
| :-------------------------------------------------------- | :----------------- | :-------------------------------------------------- |
| **`sortItems(int col, SortOrder order)`**                 | 按指定列排序       | `table.sortItems(0, Qt.AscendingOrder)`             |
| **`findItems(str, Qt.MatchFlags)`**                       | 查找匹配的单元格   | `items = table.findItems("Alice", Qt.MatchExactly)` |
| **`setSpan(int row, int col, int rowSpan, int colSpan)`** | 合并单元格         | `table.setSpan(0, 0, 2, 2)`                         |
| **`setCellWidget(int row, int col, QWidget)`**            | 在单元格中添加控件 | `table.setCellWidget(0, 0, QPushButton("Click"))`   |
| **`cellWidget(int row, int col)`**                        | 获取单元格中的控件 | `btn = table.cellWidget(0, 0)`                      |



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



## QComboBox

 `QComboBox`                                                                                                                         未下拉时的样式

 `QComboBox::drop-down`                                                                                                  下拉箭头（含外框）

 `QComboBox::down-arrow`                                                                                                下拉箭头（仅含箭头）

 `QComboBox::drop-down:hover`                                                                                      下拉箭头悬浮状态

 `QComboBox QAbstractItemView`                                                                                    弹出列表

 `QComboBox QAbstractItemView::item`                                                                       下拉列表的单个项目

 `QComboBox QAbstractItemView::item:selected`                                                    下拉列表的选中项

 `QComboBOx QAbstractScrollArea QScrollBar:vertical`                                      垂直滚动条

`QComboBox QAbstractScrollArea QScrollBar::handle:vertical`                       垂直滚动条滑块



```python
QComboBox QAbstractItemView {
    selection-bakcground-color: #4a4a4a;	/* 选中项的背景颜色*/
    selection-color: #fff;	/* 选中项的字体颜色 */
    outline: none;
}
```





## QTableWidget

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