# 发布到 GitHub Pages

目标仓库：`yyx-9527/yyx-9527.github.io`

预期网址：`https://yyx-9527.github.io/`

这是发布说明，不代表网站已经上线。

## 1. 使用目标账号创建仓库

在 GitHub 登录 **yyx-9527**，创建名为 **yyx-9527.github.io** 的 **Public** 仓库。保持仓库为空，不勾选自动生成 README、许可证或 .gitignore；本地项目已经包含这些文件。

本项目直接源自 tangjyan/zh-cn，保留其 MIT 许可证和来源说明；无需再次复制模板文件。

## 2. 推送本地代码

在项目目录运行：

```sh
git remote add origin https://github.com/yyx-9527/yyx-9527.github.io.git
git push -u origin HEAD:main
```

如果已配置 origin，先用 `git remote -v` 核对它指向上述仓库。不要覆盖其他仓库或强制推送。认证时使用 yyx-9527 的 GitHub 登录，不要把访问令牌写进配置文件或提交到仓库。

## 3. 启用 Pages

进入仓库 **Settings → Pages → Build and deployment → Source**，选择 **GitHub Actions**。

进入 **Actions → Build and deploy academic homepage → Run workflow**，选择 main 后运行。若首次推送发生在 Pages 设置完成之前，重新运行该工作流即可。

构建与部署成功后，打开 `https://yyx-9527.github.io/`。首次发布可能需要几分钟。之后对 main 的提交会自动构建并发布；拉取请求只执行构建检查。

## 自定义域名与子路径

目前默认使用账号主页，不需要 `CNAME` 文件。若以后改成项目仓库，修改 `_config.yml` 的 `repository` 和 `baseurl`，并用以下方式检查子路径：

```sh
bundle exec jekyll build --baseurl /仓库名
python scripts/check_site.py _site --baseurl /仓库名
```

参考：
- [GitHub Pages 自定义工作流](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Jekyll 安装](https://jekyllrb.com/docs/installation/)
