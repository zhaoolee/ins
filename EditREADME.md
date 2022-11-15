# INS 🍭 互联网从业者的灵感数据库


![INS灵感](https://raw.githubusercontent.com/zhaoolee/ins/master/media/ins.png)

> 本项目VI由方圆STU创始人[老罗巴扎嘿](https://huaban.com/user/syy946795671)提供设计

## 何为灵感 （◐ˍ◑）

**出处**: 唐王勃《广州宝庄严寺舍利塔碑》：以法师智遗人我，识洞幽明，思假妙因，冀通**灵感**。

- **灵感**是文艺、科技活动中瞬间产生的富有创造性的突发思维状态，无意识中突然兴起的神妙能力（某度er）
- **灵感**是根据自己的经历而联想到的一种创造性思维活动 (维基儿)
- **灵感**是**发现新世界**（省流儿）

![kokomi_teruhashi](https://raw.githubusercontent.com/zhaoolee/ins/master/media/kokomi_teruhashi.png)


## 这个INS项目有什么用？(ﾟ▽ﾟ)/

构建优秀产品，需要灵感，也需要信息，**天才也难以逾越信息差的高墙，站在巨人的肩膀上才能事半功倍**，这个仓库的目标是收集灵感，追踪存活的灵感，复活陨落的灵感。

作为一个互联网从业者，不仅要做好手头的产品，也要时刻关注市面**已有的**产品和**刚诞生**的产品，**存在的产品是我们灵感的来源**。

INS项目的灵感来自 [**阮一峰的网络日志 之 科技爱好者周刊**](https://www.ruanyifeng.com/blog/weekly/)，周刊每期都会带一些给读者带来灵感的项目，但没有给出方便查阅的项目导航列表，以及活跃项目持续追踪功能，于是本INS项目诞生了。

## INS项目运作机制（￣︶￣）↗

zhaoolee往项目根目录的 [website_info.csv](https://github.com/zhaoolee/ins/blob/main/website_info.csv) 添加数据源, 数据源被提交到Github 后, Github Action 将运行爬虫, 实时检测Url状态, 如果收到响应, 则Name后追加一个绿灯🟢, 否则为红灯🔴

Github Action每天6点定时运行, 检测Url的状态, 绿灯后面会显示响应的毫秒数, 值越小, 说明网站响应速度越快, 资金充足; 

响应速度慢的大多是公益项目，如果你很喜欢某个公益项目，建议去赞助一波，否则某天公益项目有可能会直接变红。

## INS项目的墓碑复活机制(╯-_-)╯~╩╩

项目显示红灯的项目，可能本身是个好项目，但由于种种原因搞不下去了，如果你能搞出改良版的项目，欢迎在[issues](https://github.com/zhaoolee/ins/issues)中留言，我会积极收录。

## 下载(⊙ˍ⊙)

纯净核心csv数据全量下载: [https://raw.githubusercontent.com/zhaoolee/ins/main/website_info.csv](https://raw.githubusercontent.com/zhaoolee/ins/main/website_info.csv)

在线CDN版本: [https://cdn.jsdelivr.net/gh/zhaoolee/ins/website_info.csv](https://cdn.jsdelivr.net/gh/zhaoolee/ins/website_info.csv)

如果你想复刻本项目, 建设**灵感之外**的主题仓库, 欢迎直接克隆本项目进行魔改 

```shell
git clone --depth=1 https://github.com/zhaoolee/ins
```

--insStart----insEnd--


--tagStart----tagEnd--

## 欢迎贡献╰(￣▽￣)╭

贡献方法: Fork本项目, 在项目根目录的 website_info.csv 添加数据, 提交Pr即可!

## 联系作者 (＾－＾)V

<a href="mailto:zhaoolee@gmail.com">zhaoolee@gmail.com</a>

如果你有**饱含灵感的想法**, 也可以在[issues](https://github.com/zhaoolee/ins/issues) 中留言