# 英文主页与原样例版式调整

## 已确认的目标

用户要求“用英文来做主导，要求基本跟原博主的样例基本一样”。沿用已授权的 GitHub 发布流程，并继续遵守“不上传照片”的要求。

## 参考与实现

- 以 tangjyan/zh-cn 原始模板和原作者英文站为依据，恢复原有 Trebuchet 字体、导航、侧栏宽度、正文宽度、蓝色链接、图标标题和列表式排版。
- 简介与研究兴趣在首屏，随后为 Education、Publications、Honors and Awards、Research Projects、Contact；不添加没有个人资料支持的栏目。
- 英文作为页面、导航、元数据和交互提示的主语言，个人姓名保留中文括注。
- 移除此前自定义的大标题、品牌装饰和卡片，沿用模板原生布局类。头像位置使用简单圆形文字缩写，不上传照片。
- 保留 DOI、BibTeX 和论文状态分组。事实来自上一版本已核对的简历，不推断学位、导师或录用状态。
- 按用户后续指定的 zhouxiuze.com 分类：Under Review（3 篇在投）在前，Recent Publications（2 篇已发表）在后，各组独立编号；另保留 Working Papers（1 篇准备投稿），不混入在投列表。
- 仅在投论文在条目末尾以括号显示投递期刊；Working Papers 不显示期刊，已发表论文保留正常发表信息，不添加投递期刊标注。
- 全部论文中本人姓名加粗；通讯作者按简历中的星号标注，并添加 `* Corresponding author.` 说明，未注明的两篇暂不标记。
- 继续使用 YAML 维护资料，保留 GitHub Actions 自动构建部署。

## 验证与发布

运行真实 Jekyll 构建和内部链接检查，核对英文文本、6 篇论文及其状态、无照片和无空链接；推送到已存在的 main 分支，检查 Pages 部署和线上页面。浏览器连接可用时补充可视检查。

## 参考

- https://github.com/tangjyan/zh-cn
- https://tangjian.hgmri.top/
- https://rayeren.github.io/acad-homepage.github.io/
- https://zhouxiuze.com/
