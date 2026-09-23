# 杨译鑫 · Yixin Yang 的个人学术主页

基于 [tangjyan/zh-cn](https://github.com/tangjyan/zh-cn) 定制的中文 Jekyll 学术主页，保留 [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) 的 MIT 许可与来源署名。

主页内容根据本人提供的简历整理，包含电子科技大学与四川农业大学的学习经历、研究方向、科研项目和获奖信息。论文明确分为 **已发表（2 篇）**、**在投（3 篇）**、**准备投稿（1 篇）**；在投状态不代表接收或发表。两篇已发表论文附 DOI 与 BibTeX。头像使用姓名缩写。

[访问主页](https://yyx-9527.github.io/) · [源代码](https://github.com/yyx-9527/yyx-9527.github.io) · [部署状态](https://github.com/yyx-9527/yyx-9527.github.io/actions/workflows/pages.yml)

## 页面与维护

- 桌面双栏布局，移动端折叠菜单；支持键盘导航与减少动画偏好。
- 个人简介、研究方向、论文列表、科研项目、教育经历、荣誉与奖励、联系方式。
- 论文按年份分组，可添加摘要、BibTeX、PDF、代码与 DOI 链接。
- 未填写的个人链接自动隐藏；空列表显示待补充提示。
- 不依赖远程字体；Google Analytics 和 Scholar 统计默认关闭。
- GitHub Actions 自动构建和部署，PR 只运行构建检查。

| 修改内容 | 文件 |
| --- | --- |
| 姓名、单位、邮箱、头像、学术链接 | `_config.yml` |
| 个人简介 | `_pages/about.md` |
| 研究方向 | `_data/research.yml` |
| 论文 | `_data/publications.yml` |
| 教育经历 | `_data/education.yml` |
| 科研项目 | `_data/projects.yml` |
| 荣誉与奖励 | `_data/honors.yml` |
| 排版样式 | `_sass/_academic.scss` |
| 菜单 | `_data/navigation.yml` |

填写方式与数据示例见 [内容维护指南](docs/CONTENT.md)。

## 本地运行

需要 Ruby 3.3、Bundler；Windows 推荐 [RubyInstaller + Devkit](https://rubyinstaller.org/downloads/)。不会在启动脚本里自动安装系统级工具。

```sh
bundle install
bundle exec jekyll serve --livereload --host 127.0.0.1
```

访问 `http://127.0.0.1:4000`。macOS / Linux 也可运行 `bash run_server.sh`。修改 `_config.yml` 后重启服务。

Windows 推荐运行 `run_server.bat` 或 `python scripts/preview.py`（需要 Python 3.10+）。该启动器会将源码复制到临时英文路径后构建，以兼容本项目的中文目录名；构建缓存也保存在临时目录。本次会话已准备便携 Ruby 工具链，启动器可自动发现；临时目录被系统清理后需安装 Ruby + Devkit。使用此启动器修改源码后需重新启动预览，不会自动刷新。

```sh
bundle exec jekyll build
python scripts/check_site.py _site
```

## 开源与发布

使用 **yyx-9527** 账号创建公开仓库 **yyx-9527.github.io**，推送源码并在 **Settings → Pages** 选择 **GitHub Actions**。完整步骤见 [部署指南](docs/DEPLOY.md)。

源码使用 [MIT License](LICENSE)。第三方资源来源见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。个人论文、头像和简历应只添加你有权公开的材料。
