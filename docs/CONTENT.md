# 填写个人资料

当前个人信息已根据本人简历填写。更新资料时直接修改以下文件；清空某个列表后会显示待补充提示。

## 姓名、邮箱、头像与链接

编辑 `_config.yml` 的 `author`：

```yaml
author:
  name: "你的姓名"
  initials: "姓名缩写"
  handle: "yyx-9527"
  avatar: "/images/avatar.jpg"
  bio: "你的单位 · 职位"
  location: "你的城市"
  email: "你的公开联系邮箱"
  github: "yyx-9527"
  googlescholar: "" # 完整网址
  orcid: "" # 完整网址
  researchgate: ""
  cv: "/files/cv.pdf"
```

只设置存在的文件。头像放入 `images`，简历放入自行创建的 `files` 目录；暂时没有则留空。网址必须填写完整的 HTTPS 地址。站点标题和描述位于同一配置文件的开头。

## 个人简介

编辑 `_pages/about.md` 中第二条 `---` 之后的正文，保留开头的配置块。可直接使用 Markdown 的段落、链接和列表。

## 研究方向

将 `_data/research.yml` 中的 `[]` 替换为列表：

```yaml
- title: "你的研究方向"
  description: "简要介绍你关注的研究问题。"
```

## 论文列表

将 `_data/publications.yml` 中的 `[]` 替换为真实论文列表。下面仅为格式示例，不是学术成果：

```yaml
- title: "论文的真实标题"
  authors: "**你的姓名**, 合作者姓名"
  year: 2026
  status: "published" # published / under_review / in_preparation
  venue: "期刊或会议名称"
  type: "期刊论文"
  note: "" # 可留空，例如真实获得的奖项
  links:
    - label: "论文"
      url: "https://doi.org/替换为真实DOI"
    - label: "代码"
      url: "https://github.com/账号/仓库"
    - label: "PDF"
      url: "/files/paper.pdf"
  abstract: |
    论文摘要，可使用 Markdown。
  bibtex: |
    替换为该论文的真实 BibTeX 条目。
```

已发表论文的年份使用数字；在投和准备投稿论文可省略年份。`status` 为必填项，分别对应已发表、在投、准备投稿；论文先按状态分组，已发表论文再按年份降序分组。作者字段支持 Markdown，推荐用 `**姓名**` 突出自己。摘要和 BibTeX 可展开。提供 BibTeX 时，在支持剪贴板的 HTTPS 或 localhost 页面上会出现复制按钮。删除不需要的字段即可，不要放置无效链接。

## 教育经历

将 `_data/education.yml` 中的 `[]` 替换为：

```yaml
- period: "入学年份 — 毕业年份"
  institution: "学校名称"
  program: "专业或已确认的学位信息"
  department: "院系 / 专业"
  description: "" # 可选
```

## 项目与奖励

科研项目在 `_data/projects.yml` 维护，支持题目、时间、角色、简介和贡献列表。荣誉奖项在 `_data/honors.yml` 维护。论文录用、项目结束或专利状态发生变化后，请据实际进展更新；“专利文稿”不等同于已申请或已授权专利。

## Google Scholar（可选）

默认关闭，不会在没有 Scholar ID 时自动爬取数据。

1. 配置 `author.googlescholar`。
2. 在仓库的 Actions secrets 中添加 `GOOGLE_SCHOLAR_ID`。
3. 在 Actions variables 中添加 `ENABLE_GOOGLE_SCHOLAR=true`。
4. 手动运行 **Update Google Scholar data (optional)** 工作流。
5. 工作流成功后，将 `google_scholar_stats_enabled` 改为 `true`。

更新后的 JSON 保存在独立的 `google-scholar-stats` 分支；不会修改网页源码。需要刷新时再次手动运行。Google Scholar 可能限流；统计获取失败时页面仍正常展示其他内容。

## 校验

```sh
bundle exec jekyll build
python scripts/check_site.py _site
```

检查会验证站内链接、锚点、CSS 引用文件和 HTML 基本结构，不请求外部论文网址。头像、简历和 PDF 需要自行确认文件名大小写正确。
