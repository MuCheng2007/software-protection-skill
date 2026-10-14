# GitHub新手使用指南

这个仓库就是项目的公开主页与版本记录。首页README介绍用途，文件区保存技能内容，每次commit记录一次改动。

| 按钮/页面 | 用途 |
| --- | --- |
| Code | 查看文件；Code → Download ZIP 下载整个仓库 |
| Star | 收藏并表达支持 |
| Watch | 选择更新通知范围 |
| Issues | 接收新案例、纠错、问题与建议 |
| Pull requests | 审阅别人建议合并的修改 |
| Actions | 查看自动结构检查结果 |
| Releases | 发布固定版本与说明，区别于持续变化的main分支 |
| Settings | 管理简介、访问权限和仓库设置 |

## 修改一段说明

打开文件 → 点击铅笔编辑 → Preview检查效果 → Commit changes保存一个版本。建议新建分支再发PR；小改动也要检查diff，确认没有误删内容。

## 收录一个新案例

先在Issues选Case submission模板，核对来源和日期。确认机制与证据等级后，编辑 `skills/software-protection/references/forum-cases.json`，必要时更新失效模式、验收与案例索引。运行验证脚本，审阅后合并。

只在Issues里讨论不会自动修改技能；把已确认结论合并进文件才会进入下一版。

## 接收别人贡献

打开Pull requests → Files changed看diff → 检查Actions → 核对来源和技术结论 → 满足要求后Merge。若不确定，留言要求补证据；不用因为有人投稿就合并。

## 发一个版本

先更新CHANGELOG并确保检查通过。仓库右侧Releases → Draft a new release → 创建标签（例如v0.1.1）→ 填写版本说明 → Publish release。GitHub会提供该标签的源码归档；若另附安装包，应来自同一提交。

## 本地更新的基本命令

```bash
git clone https://github.com/MuCheng2007/software-protection-skill.git
cd software-protection-skill
git switch -c update/new-case
# 编辑文件
python scripts/validate.py
git diff
git add skills docs README.md CHANGELOG.md
git commit -m "Add reviewed licensing case"
git push -u origin update/new-case
```

首次提交前，按Git提示设置你的作者名字和邮箱；可使用GitHub提供的noreply邮箱保护个人邮箱。推送可能需要GitHub登录；不要把密码或token写进仓库。

官方入门：[仓库快速开始](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)、[Hello World与PR流程](https://docs.github.com/en/get-started/using-github/hello-world)。
