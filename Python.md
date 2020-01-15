# Python

### python简介

1、解释器

用来执行Python代码，对于Python存在多种解释器：

+ CPython
官方的Python解释器，从官网下载Python安装后会直接获得这个解释器。这个解释器是由C语言开发的，所以叫CPython。在命令下运行python就是启动CPython解释器

+ IPython
IPython是基于CPython之上的一个交互式解释器，也就是说IPython只是在交互方式上有所增强，执行python代码的功能个CPython是完全一样的

+ PyPy
这个解释器目标是执行速度。PyPy采用JIT技术，对Python代码进行动态编译（不是解释），可以显著提高Python代码的执行速度。绝大多数Python代码都可在PyPy下运行，但是PyPy和CPython有些不同的，会导致相同的代码在两种解释器下执行可能会有不同的结果。

+ Jython
是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码

+ IronPython
和Jython类似，只不过此编译器是运行在.net平台上的Python解释器，可以直接把Python代码编译成.net的字节码

2、
