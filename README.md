# Yixin Yang's Academic Homepage

[Homepage](https://yyx-9527.github.io/) · [Source code](https://github.com/yyx-9527/yyx-9527.github.io) · [Deployment status](https://github.com/yyx-9527/yyx-9527.github.io/actions/workflows/pages.yml)

An English academic homepage based on [tangjyan/zh-cn](https://github.com/tangjyan/zh-cn) and [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io), retaining the upstream typography, sidebar, navigation, section headings, and compact publication lists.

The content is based on Yixin Yang's CV and subsequent updates. Papers are ordered as **Working Papers (1)**, **Under Review (3)**, and **Recent Publications (2)**, following the status-based organization of [Xiuze Zhou's homepage](https://zhouxiuze.com/). Under-review entries show the submitted journal in parentheses at the end. Working papers do not show a submission venue; published entries retain their publication details and verified DOI links and BibTeX citations. A text monogram is used in place of a personal photo.

## Content

The homepage includes a biography, research interests, education, publications, honors and awards, research projects, and contact information. Chinese is retained for the native spelling of the author's name.

- Original Jekyll theme layout with responsive navigation and keyboard support.
- Publication status is explicit; manuscripts under review are not presented as published work.
- Yixin Yang is shown in bold. Corresponding authors are marked with an asterisk where indicated in the CV or subsequently confirmed by the author.
- DOI links, expandable BibTeX, and citation copying over HTTPS or localhost.
- Empty profile links and content sections are hidden.
- Local fonts and icons; analytics and Google Scholar statistics are disabled by default.
- GitHub Actions builds and deploys the site. Pull requests run build checks only.

## Updating the site

| Content | File |
| --- | --- |
| Name, affiliation, email, and profile links | `_config.yml` |
| Biography | `_pages/about.md` |
| Research interests | `_data/research.yml` |
| Publications | `_data/publications.yml` |
| Education | `_data/education.yml` |
| Research projects | `_data/projects.yml` |
| Honors and awards | `_data/honors.yml` |
| Small additions to upstream styles | `_sass/_academic.scss` |
| Navigation | `_data/navigation.yml` |

A detailed [content guide](docs/CONTENT.md) is available in Chinese for the site owner.

## Local development

Requires Ruby 3.3 and Bundler. Windows users can install [RubyInstaller with Devkit](https://rubyinstaller.org/downloads/).

```sh
bundle install
bundle exec jekyll serve --livereload --host 127.0.0.1
```

Open `http://127.0.0.1:4000`. On macOS or Linux, `bash run_server.sh` runs the same preview. Restart Jekyll after changing `_config.yml`.

For Windows projects in a directory with non-ASCII characters, use `run_server.bat` or `python scripts/preview.py` with Python 3.10+. This launcher copies the source to an ASCII temporary path before building. Restart it after editing source files; it does not watch for changes. A portable Ruby runtime prepared in the local setup is detected when present; if it has been removed, install Ruby with Devkit.

Build and check internal links:

```sh
bundle exec jekyll build
python scripts/check_site.py _site
```

## Deployment

Changes pushed to `main` are built, checked, and deployed to [yyx-9527.github.io](https://yyx-9527.github.io/) by GitHub Actions. The Pages source is set to **GitHub Actions**. See the [deployment guide](docs/DEPLOY.md) for setup and recovery instructions.

## License and attribution

Source code is distributed under the [MIT License](LICENSE). Upstream attribution is retained; see [third-party notices](THIRD_PARTY_NOTICES.md). The original CV and personal photo are not included in this repository.
