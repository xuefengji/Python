# Python

### python简介

1、解释器

用来执行 Python 代码，对于 Python 存在多种解释器：

+ CPython
官方的 Python 解释器，从官网下载 Python 安装后会直接获得这个解释器。这个解释器是由 C 语言开发的，所以叫 CPython。在命令下运行 python 就是启动 CPython 解释器

+ IPython
IPython 是基于 CPython 之上的一个交互式解释器，也就是说 IPython 只是在交互方式上有所增强，执行 python 代码的功能个 CPython 是完全一样的

+ PyPy
这个解释器目标是执行速度。PyPy 采用JIT技术，对 Python 代码进行动态编译（不是解释），可以显著提高 Python 代码的执行速度。绝大多数 Python 代码都可在 PyPy 下运行，但是 PyPy 和CPython 有些不同的，会导致相同的代码在两种解释器下执行可能会有不同的结果。

+ Jython
是运行在 Java 平台上的 Python 解释器，可以直接把 Python 代码编译成 Java 字节码

+ IronPython
和 Jython 类似，只不过此编译器是运行在 .net 平台上的 Python 解释器，可以直接把 Python 代码编译成 .net 的字节码

2、输出和输入

+ print()

+ input()
