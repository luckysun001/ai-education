# 更新日志

本文件记录「开源 AI 实战指南」的重要变更。

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/)，版本语义：

- **主版本号**：内容体系重构，或学习路径发生变化
- **次版本号**：新增章节/模块，或大范围内容更新
- **修订号**：错误修正、链接修复、措辞调整

> ⚠️ 工具名称、模型版本与价格会随时间变化。文档中涉及具体产品的地方均标注了「最后更新」时间，
> 实际请以各产品官网为准。

---

## [v2.1] — 2026-10-10

面向 2026 年的一次**时效性刷新**。方法论部分（Prompt 黄金法则、CoT、Few-shot、迭代优化）保持不变，
更新集中在工具、模型与新能力层。

### 新增

- **AI 智能体（Agent）入门**（`ai-industry-toolkit/getting-started/04-ai-agent.md`）
  - 智能体与普通 AI 助手的区别：一个「说」，一个「做」
  - 三类你现在就能用上的智能体：大模型自带智能体模式、AI 编程智能体、零代码搭建平台
  - 核心方法：给智能体下指令要讲「**目标 + 约束 + 交付形式**」，而不是一步步教它怎么做
  - 安全提醒：涉及钱、删除、对外发送的动作必须人工确认

- **MCP 是什么**（`ai-industry-toolkit/getting-started/05-mcp.md`）
  - 用「AI 工具的 USB-C 接口」解释统一连接标准
  - N×M 集成税 → N+M 的省事逻辑
  - 普通人只需判断「这个授权该不该给」，附最小权限原则

### 更新

- **常用工具介绍**（`03-common-tools.md`）重写
  - 按「能力分层 + 选型方法」组织，不再罗列易过时的精确版本号与价格
  - 新增「推理模式」「AI 智能体」两节
  - 代码类工具改按「AI 编辑器 / 命令行智能体 / 国产」三类划分
- `ai-industry-toolkit/industries/finance/README.md` 推荐工具表刷新，补充国产模型与 AI 搜索工具
- 统一加入「最后更新：2026 年 10 月」时间锚点，便于后续维护
- 版本徽章 v2.0 → v2.1

### 修复

- 清理硬编码年份示例：`02-prompt-engineering.md` 的「2024 年 AI 行业发展趋势」→「最近一年」
- `finance/README.md` 模板占位符「[2024 年 Q1]」→「[最新一期]」

### 工程

- 新增 `.github/workflows/ci.yml`（多版本 Python CI），CI 首次在远程生效

---

## [v2.0] — 2026-08-12

### 新增

- `.github/scripts/check_links.py`：自动校验文档内相对链接，防止断链再次累积

### 修复

- 修复 **35 处断链**：跨仓链接改为绝对 URL、修正相对路径深度错误

### 更新

- 补齐 `ai-industry-toolkit` 下的 `tools/` 与 `use-cases/` 章节

---

## [v1.1] — 2026-08-10

### 修复

- 修复 CONTRIBUTING.md 及各分册 README 中不存在的组织链接（原 `opensource-ai-projects` 组织不存在，
  统一改为 `luckysun001/<仓库>` 实际地址）

---

## [v1.0] — 2026-07-13

首个正式版本发布，包含三个子项目：

- 🏭 **AI 行业应用百宝箱**：8 个行业的应用指南
- 💼 **AI 职业技能加速器**：7 个职业的技能手册
- 🧪 **无代码 AI 实验室**：6 个模块的实战教程

合计 15 个行业与职业、20 万+ 字、100+ 个可直接使用的场景 Prompt。

---

[v2.1]: https://github.com/luckysun001/ai-education/compare/v2.0...v2.1
[v2.0]: https://github.com/luckysun001/ai-education/compare/v1.1...v2.0
[v1.1]: https://github.com/luckysun001/ai-education/compare/v1.0...v1.1
[v1.0]: https://github.com/luckysun001/ai-education/releases/tag/v1.0
