# Gemini CLI Skills (技能) 使用指南

在 Gemini CLI 中，**Skills（技能）** 是专门的、可重用的专业知识包。它们旨在扩展 Gemini CLI 的能力，使其在处理特定领域任务（如代码审计、特定框架开发、部署等）时变得更加专业，同时又不会让基础的上下文变得臃肿。

它采用“渐进式加载”模式：Gemini 只有在发现某项任务需要某个特定技能时，才会主动加载该技能的详细指令。

---

## 1. 安装 Skills

你可以从本地目录或 Git 仓库安装技能：

### 从 Git 仓库安装
```bash
gemini skills install https://github.com/user/repo.git
```
如果技能在仓库的子目录中：
```bash
gemini skills install https://github.com/user/repo.git --path skills/my-skill
```

### 链接本地目录 (用于本地开发)
将本地文件夹链接为一个技能，在开发自定义技能时非常有用：
```bash
gemini skills link ./path/to/skill --scope workspace
```

---

## 2. 管理 Skills

在启动 Gemini CLI 的交互式会话后，你可以使用 `/skills` 斜杠命令来管理你的技能：

* `/skills list`：显示所有已发现的技能及其状态。
* `/skills list all`：显示所有技能，包含系统内置技能（如自带的 `skill-creator`）。
* `/skills enable <name>`：在当前会话中强制启用特定技能。
* `/skills disable <name>`：防止某项技能被自动激活。
* `/skills reload`：重新加载并刷新技能列表。

---

## 3. 如何使用 Skills？

实际上，你**通常不需要手动去调用某个技能**。这是一个自动化的过程：

1. **发现机制:** 在启动时，Gemini 会自动扫描工作区 (`.gemini/skills/`) 和全局 (`~/.gemini/skills/`) 文件夹。
2. **触发机制:** 当你的对话意图匹配了某个技能的描述（例如，你安装了一个 `api-auditor` 技能，然后你对我说“请帮我审计一下这个 API 接口”），Gemini 会自动识别出相关性。
3. **激活与授权:** 此时，CLI 会请求你的**同意**。在你授权后，Gemini 就会激活该技能，读取其内部的专业指令和工具脚本来完成你的任务。

---

## 4. 创建自己的专属 Skill

创建新技能非常简单，因为 Gemini 内置了一个 **`skill-creator` (技能创建者)** 技能。

**操作步骤：**
1. 在交互会话中直接对我说：*"我想创建一个新技能，用来 [描述你要解决的任务，例如：自动检查并生成组件的 Storybook 文件]"*。
2. 此时，内置的 `skill-creator` 将会被激活。
3. 它会自动引导你创建相应的文件夹和 `SKILL.md` 指令文件。

一个典型的技能目录结构如下：
```text
my-skill/
├── SKILL.md       # 技能的核心指令和元数据 (必须)
├── scripts/       # (可选) 让 AI 调用的自定义脚本
└── reference/     # (可选) 相关的参考文档或示例
```
