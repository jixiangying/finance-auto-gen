# 全天候金融洞察 (Finance Auto-Gen)

AI 驱动的自动化金融数据抓取、分析与可视化报告系统。
An AI-powered automated system for financial data scraping, analysis, and visual reporting.

## 🌟 项目简介 | Introduction

本项目是一个全自动化的金融市场简报生成系统。它能够自动抓取全球市场数据，通过 AI 进行深度建模与洞察分析，并生成图文并茂的早晚报。系统基于 **VitePress** 构建前端展示界面，提供极佳的阅读体验。

This project is a fully automated financial market briefing generation system. It automatically scrapes global market data, performs deep modeling and insight analysis via AI, and generates visually rich morning and evening reports. Built with **VitePress**, it provides an excellent reading experience.

## 🚀 核心特性 | Core Features

- **🤖 AI 驱动 (AI-Driven)**：利用 AI 自动感知全球市场动向，提取核心指标。
  Leverages AI to automatically sense global market trends and extract key indicators.
- **📊 自动化图表 (Automated Charts)**：使用 Python 脚本自动抓取数据并绘制专业金融图表（位于 `scripts/`）。
  Uses Python scripts to automatically fetch data and plot professional financial charts (located in `scripts/`).
- **🎨 丰富视觉 (Rich Visuals)**：系统不仅生成报告文本，还包含 AI 生成的插画（Manga 风格）和市场情绪图。
  Generates not only report text but also AI-generated illustrations (Manga style) and market sentiment charts.
- **📅 智能分类 (Smart Categorization)**：网站侧边栏根据年份和周（周一至周日）自动对海量报告进行归档。
  The sidebar automatically archives reports by year and week (Monday to Sunday).
- **⚡ 自动化同步 (Automated Sync)**：集成自动化工作流，实现定时数据抓取、报告生成与站点内容的同步更新。
  Integrated automation workflows for scheduled data scraping, report generation, and site content updates.

## 🛠️ 项目结构 | Project Structure

- `.vitepress/`: VitePress 配置文件与主题设置。 (VitePress configuration and theme settings.)
- `reports/`: 存放所有 AI 生成的 Markdown 市场报告。 (Contains all AI-generated Markdown market reports.)
- `images/`: 存放生成的图表（charts）和插画（manga）。 (Stores generated charts and illustrations.)
- `scripts/`: 用于抓取数据和生成图表的 Python 核心脚本。 (Core Python scripts for data scraping and chart generation.)
- `public/`: 静态资源文件。 (Static assets.)

## 📜 系统架构 | System Architecture

1.  **数据获取 (Data Acquisition)**：通过自动感知时区的 Agent 获取全球（美股、大宗、外汇）与国内（A股、港股）市场的核心数据。
    Acquires core data from global (US stocks, commodities, forex) and domestic (A-shares, HK stocks) markets through timezone-aware agents.
2.  **内容生成 (Content Generation)**：系统自动完成图表绘制（Python）、数据排版与插画生成（AI）。
    Automatically handles chart plotting (Python), data formatting, and illustration generation (AI).
3.  **内容同步 (Content Sync)**：通过定时任务调度实现每日两次（早晚报）的自动化内容更新与站点同步。
    Achieves automated content updates and site synchronization twice daily (morning and evening) through scheduled task orchestration.

## ⚖️ 开源协议 | License

本项目基于 **MIT** 协议开源。
This project is licensed under the **MIT** License.
