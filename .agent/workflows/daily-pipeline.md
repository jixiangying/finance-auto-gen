---
description: 自动执行每日市场报告全流程：调研、撰写、推送到 GitHub。
---

# 每日报告自动化流水线

这个工作流将按顺序调用三个 Agent 技能，完成从获取数据到发布网页的全过程。

## 执行步骤

1. **执行市场调研**
   使用 `market-researcher` 技能获取当前最相关的市场数据。
   > 注意：Agent 会根据当前时间（早/晚）自动切换国际/国内市场。

2. **生成报告内容**
   使用 `content-creator` 技能将调研结果转化为 Markdown 报告，并生成行情卡片和情绪插图。

3. **推送到 GitHub**
   使用 `github-deployer` 技能将生成的文件提交并推送到代码仓库，触发网页自动更新。

## 如何自动化触发

由于本环境在本地运行，你可以通过以下方式实现定时触发：

### 方法一：Crontab 定时提醒 (macOS)
在终端运行 `crontab -e` 并添加以下两行，每天 9:00 和 16:00 会弹出系统通知提醒你打开 IDE 执行此工作流：
```bash
0 9 * * * osascript -e 'display notification "该生成早报了！" with title "金融助手"'
0 16 * * * osascript -e 'display notification "该生成收盘报了！" with title "金融助手"'
```

### 方法二：日历事项
在 macOS 日历中设置重复日程，添加闹钟提醒。
