# `Python` 数据处理初步

本仓库主要总结了使用 `Python` 进行数据处理, 机器学习等任务时最常用的数据处理技能, 主要包括 `Matplotlib`, `Numpy`, `Pandas`. 所有程序均在 python 3.9.17 下调试通过.

## `Matplotlib`

主要介绍了各种图像的画法, 给出了绘制模板程序.

包括折线图, 散点图, 柱状图, 直方图, 饼图.

知识结构见 `Matplotlib.png`.

![Matplotlib](https://qy-2023.oss-cn-shanghai.aliyuncs.com/pic/202308061459706.png)

## `Numpy`

主要介绍了 `Numpy` 的基本用法, 包括 `ndarray` 数组的生成, 整形, 修改, 去重等常用操作, 以及各种常用的运算.

由于 `Numpy` 的很多内容被 `Pandas` 所包含, 此处介绍比较简短.

知识结构见 `Numpy.png`.

![Numpy](https://qy-2023.oss-cn-shanghai.aliyuncs.com/pic/202308061500350.png)

## `Pandas`

主要介绍了 `Pandas` 的基本数据结构, 以及增删改查的基本方法. 

![Pandas](https://qy-2023.oss-cn-shanghai.aliyuncs.com/pic/202308061452185.png)

在此基础上, 介绍了一些基本的数据处理技巧, 如缺失值, 离散化.

![Pandas 数据处理](https://qy-2023.oss-cn-shanghai.aliyuncs.com/pic/202308061500601.png)

## 关于 `DataImporter` 的说明

为了方便进行数据处理, 在此处将常用库进行导入, 并进行了常用的设定, 解决了一些常用的问题, 例如中文显示, 中文负号等, 并给出了几组实用的配色方案.

该脚本设定了导出图像使用透明背景, $\LaTeX$ 支持, 高 dpi, 和中文字体设置. 你可以根据需要修改上述设置, 修改方法已在注释中给出了说明. 其中, 值得注意的是:

> $\LaTeX$ 支持默认采用 `pdflatex`, 请你自行安装相关环境.

> 透明背景仅在使用 `savefig()` 保存时可用.

> 中文字体的可用性视环境而定, 你可以根据自己的环境和喜好设定.

使用时, 将此文件复制到目录下, 并在程序开头添加如下代码: `from DataImporter import *`.
