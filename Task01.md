# Task01笔记

**练习题**：

leetcode 习题 136. 只出现一次的数字

给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

尝试使用位运算解决此题。

```python
"""
Input file
example1: [2,2,1]
example2: [4,1,2,1,2]

Output file
result1: 1
result2: 4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            
     # your code here
    
        x=0
        for num in nums:
            x=x^num
        return x
```



**练习题**：

1. 怎样对python中的代码进行注释？

   单行注释：`#` 。

   ```python
   # 这是一个注释
   print("Hello world")
   
   # Hello world
   ```

   区间注释：`''' '''` 或 `""" """` 

   ```python
   '''
   这是多行注释，用三个单引号
   这是多行注释，用三个单引号
   这是多行注释，用三个单引号
   '''
   print("Hello china") 
   # Hello china
   
   """
   这是多行注释，用三个双引号
   这是多行注释，用三个双引号 
   这是多行注释，用三个双引号
   """
   print("hello china") 
   # hello china
   ```

   

2. python有哪些运算符，这些运算符的优先级是怎样的？

   <b>算术运算符</b>

   | 操作符 |      名称      |   示例   |
   | :----: | :------------: | :------: |
   |  `+`   |       加       | `1 + 1`  |
   |  `-`   |       减       | `2 - 1`  |
   |  `*`   |       乘       | `3 * 4`  |
   |  `/`   |       除       | `3 / 4`  |
   |  `//`  | 整除（地板除） | `3 // 4` |
   |  `%`   |      取余      | `3 % 4`  |
   |  `**`  |       幂       | `2 ** 3` |

   <b>比较运算符</b>

   | 操作符 |   名称   |   示例   |
   | :----: | :------: | :------: |
   |  `>`   |   大于   | `2 > 1`  |
   |  `>=`  | 大于等于 | `2 >= 4` |
   |  `<`   |   小于   | `1 < 2`  |
   |  `<=`  | 小于等于 | `5 <= 2` |
   |  `==`  |   等于   | `3 == 4` |
   |  `!=`  |  不等于  | `3 != 5` |

   <b>逻辑运算符</b>

   | 操作符 | 名称 |         示例          |
   | :----: | :--: | :-------------------: |
   | `and`  |  与  | `(3 > 2) and (3 < 5)` |
   |  `or`  |  或  | `(1 > 3) or (9 < 2)`  |
   | `not`  |  非  |     `not (2 > 1)`     |

   位运算符</b>

   | 操作符 |   名称   |   示例   |
   | :----: | :------: | :------: |
   |  `~`   | 按位取反 |   `~4`   |
   |  `&`   |  按位与  | `4 & 5`  |
   |  `|`   |  按位或  | `4 | 5`  |
   |  `^`   | 按位异或 | `4 ^ 5`  |
   |  `<<`  |   左移   | `4 << 2` |
   |  `>>`  |   右移   | `4 >> 2` |

   【例子】有关二进制的运算，参见“位运算”部分的讲解。

   ```python
   print(bin(4))  # 0b100
   print(bin(5))  # 0b101
   print(bin(~4), ~4)  # -0b101 -5
   print(bin(4 & 5), 4 & 5)  # 0b100 4
   print(bin(4 | 5), 4 | 5)  # 0b101 5
   print(bin(4 ^ 5), 4 ^ 5)  # 0b1 1
   print(bin(4 << 2), 4 << 2)  # 0b10000 16
   print(bin(4 >> 2), 4 >> 2)  # 0b1 1
   ```


   <b>三元运算符</b>

   【例子】

   ```python
   x, y = 4, 5
   if x < y:
       small = x
   else:
       small = y
   
   print(small)  # 4
   ```

   有了这个三元操作符的条件表达式，你可以使用一条语句来完成以上的条件判断和赋值操作。

   【例子】

   ```python
   x, y = 4, 5
   small = x if x < y else y
   print(small)  # 4
   ```

   <b>其他运算符</b>

|  操作符  |  名称  |             示例             |
| :------: | :----: | :--------------------------: |
|   `in`   |  存在  |   `'A' in ['A', 'B', 'C']`   |
| `not in` | 不存在 | `'h' not in ['A', 'B', 'C']` |
|   `is`   |   是   |     `"hello" is "hello"`     |
| `is not` |  不是  |   `"hello" is not "hello"`   |


   【例子】

   ```python
   letters = ['A', 'B', 'C']
   if 'A' in letters:
       print('A' + ' exists')
   if 'h' not in letters:
       print('h' + ' not exists')
   
   # A exists
   # h not exists
   ```

   【例子】比较的两个变量均指向不可变类型。

   ```python
   a = "hello"
   b = "hello"
   print(a is b, a == b)  # True True
   print(a is not b, a != b)  # False False
   ```

   【例子】比较的两个变量均指向可变类型。

   ```python
   a = ["hello"]
   b = ["hello"]
   print(a is b, a == b)  # False True
   print(a is not b, a != b)  # True False
   ```

   注意：

   - ==is, is not 对比的是两个变量的内存地址==
   - ====, != 对比的是两个变量的值==
   - 比较的两个变量，指向的都是地址不可变的类型（str等），那么is，is not 和 ==，！= 是完全等价的。
   - 对比的两个变量，指向的是地址可变的类型（list，dict，tuple等），则两者是有区别的。


   <b>运算符的优先级</b>

   - 一元运算符优于二元运算符。例如`3 ** -2`等价于`3 ** (-2)`。
   - 先算术运算，后移位运算，最后位运算。例如 `1 << 3 + 2 & 7`等价于 `(1 << (3 + 2)) & 7`。
   - 逻辑运算最后结合。例如`3 < 4 and 4 < 5`等价于`(3 < 4) and (4 < 5)`。

   【例子】

   ```python
   print(-3 ** 2)  # -9
   print(3 ** -2)  # 0.1111111111111111
   print(1 << 3 + 2 & 7)  # 0
   print(-3 * 2 + 5 / -2 - 4)  # -12.5
   print(3 < 4 and 4 < 5)  # True
   ```


   ## 

3. python 中 `is`, `is not` 与 `==`, `!=` 的区别是什么？

   is, is not 对比的是两个变量的内存地址

   ==, != 对比的是两个变量的值

   

4. python 中包含哪些数据类型？这些数据类型之间如何转换？

   - 基本类型：整型、浮点型、布尔型
   - 容器类型：字符串、元组、列表、字典和集合

   | 类型  |          名称           |      示例      |
   | :---: | :---------------------: | :------------: |
   |  int  |  整型 `<class 'int'>`   |   `-876, 10`   |
   | float | 浮点型`<class 'float'>` | `3.149, 11.11` |
   | bool  | 布尔型`<class 'bool'>`  | `True, False`  |

   **类型转换**

   - 转换为整型 `int(x, base=10)`
   - 转换为字符串 `str(object='')`
   - 转换为浮点型 `float(x)`

   【例子】

   ```python
   print(int('520'))  # 520
   print(int(520.52))  # 520
   print(float('520.52'))  # 520.52
   print(float(520))  # 520.0
   print(str(10 + 10))  # 20
   print(str(10.1 + 5.2))  # 15.3
   ```


   ## 

