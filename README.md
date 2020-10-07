# mangabz_spider
Spidering comics from mangabz.

从http://www.mangabz.com/上爬取漫画，项目灵感来源于看电锯人的时候，电锯人太好看了忍不住就想爬下来。

# 依赖

环境依赖还蛮多的，具体直接看py代码吧，本来想着整合一下嫌麻烦就不整了。

# 使用方法

运行起来之后会等待输入网址，格式很重要因为要分析。

“Input the URL you want to download(such as http://www.mangabz.com/577bz/)”

“Pay attention to the ending '/' :”

大意是要输入你想爬下来的漫画的网址，有例子可以对比，重要的是不要丢掉最后的“/”,不然会失败。

# 提醒

如果下载过程中因为网络或是其他意外原因被迫中止，可以在代码里自己修改下次开始的起点和终点位置，在代码中已有标注。