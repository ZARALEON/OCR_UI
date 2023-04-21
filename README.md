## 一、如何运行？

1、创建虚拟环境

```text
conda create -n OCR_UI python=3.7
```

2、在虚拟环境中创建依赖

```text
activate OCR_UI
pip install -r ruqirements.txt
```

3、运行主文件

```text
python OCR_UI.py
```

![2023-04-21](Images/2023-04-21.png)



## 二、想要制作成exe文件？

```text
pip install pyinstaller
pyinstaller -D -w OCR_UI.py
```

错误提示参考网址[ paddleOCR 打包 _](https://blog.csdn.net/u012254599/article/details/128003574)