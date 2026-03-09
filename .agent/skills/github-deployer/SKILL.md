---
name: github-deployer
description: 负责将本地生成的最新市场简报、图表及配置文件推送到 GitHub 仓库，从而触发远程服务器的 VitePress 自动构建与网页更新。
---

# 目标
自动检测本地工作区的变更，并使用终端 (Terminal) 工具将最新的文章和资源推送到 GitHub 的 main 分支。

# 执行步骤（强制按顺序执行）

## 第一步：检查变更状态
调用终端执行 `git status`。
* 观察输出结果，确认是否有新生成的 `reports/` 目录下的 .md 文件或 `images/` 目录下的图片。
* 如果没有任何变更（"nothing to commit"），则终止任务并报告“当前无新内容需要推送”。

## 第二步：暂存所有文件
调用终端执行 `git add .`。
* 这一步将把所有新增、修改或删除的文件加入 Git 暂存区。

## 第三步：生成时间戳并提交
调用终端执行 `git commit -m "Auto-update: <当前日期和时间> market report"`。
* 必须自行获取当前的真实系统日期和时间，替换占位符 `<当前日期和时间>`（例如："Auto-update: 2026-03-08 18:30 market report"）。

## 第四步：推送到云端
独立调用终端执行 `git push`。
* 不要与前面的 commit 命令合并执行，确保可以捕获独立的推送结果。
* 观察输出。如果出现 "To github.com:..." 或 "Everything up-to-date"，说明推送成功。
* 如果遇到 `fatal: Could not read from remote repository`，这通常是 SSH 代理或权限问题，应提示用户在自己的终端手动执行 `git push` 并确认鉴权。

# 输出规范
执行完毕后，向用户简要报告推送结果，并附上 GitHub Pages 的访问链接（https://jixiangying.github.io/finance-auto-gen/），提醒用户云端打包通常需要 1-2 分钟生效。