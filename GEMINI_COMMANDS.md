# 📱 Gemini CLI 斜杠命令 (Slash Commands) 全面使用指南

在 Gemini CLI 交互终端中，你可以通过键入 **斜杠 `/`** 开头的命令来快速管理 AI 会话状态、切换模型、查看工具或配置记忆。

以下是 Gemini CLI 支持的**最全面**的可用命令及其简要说明：

---

### 基础交互与帮助
* **`/help` (或 `/?`)** - 显示帮助菜单，列出所有当前可用的斜杠命令及其用法。
* **`/about`** - 显示版本信息（在反馈 Bug 时非常有用）。
* **`/docs`** - 在浏览器中打开 Gemini CLI 的官方在线文档。
* **`/bug`** - 直接提交 GitHub Issue，反馈 CLI 工具的 Bug 或产品改进建议。

### 会话与状态管理
* **`/clear`** - 清空当前终端的屏幕和对话滚动历史，重置 AI 的上下文窗口。
* **`/quit` (或 `/exit`)** - 退出 CLI。可附加 `--delete` 参数来擦除当前会话的临时文件/历史。
* **`/resume` (或 `/chat`)** - 打开一个交互式会话浏览器，可以从中恢复之前自动保存或手动做过 Checkpoint 的对话。
* **`/compress`** - 对当前极其冗长的对话进行“压缩总结”，以节省宝贵的 Context Token 消耗。
* **`/plan`** - 切换到“计划模式 (Plan Mode)”（只读模式），这允许你在让 AI 动手写代码之前，先审阅它生成的整体任务计划。
* **`/stats`** - 显示当前会话、模型或工具的详细 Token 使用和耗时统计。

### 撤销与代码回退
* **`/rewind`** - 强大的“时光倒流”功能。向上游溯源对话历史，可选择撤销代码修改、撤销对话或两者同时撤销。
* **`/restore`** - 将项目文件直接恢复到某个特定工具执行之前的状态。

### 配置与记忆管理
* **`/settings`** - 打开交互式编辑器，修改全局或项目级的 `.gemini/settings.json` 配置。
* **`/model`** - 调出模型选择菜单，允许你在不同的 Gemini 模型（如 Flash、Pro）之间进行实时切换。
* **`/memory`** - 查看、更新或清理 AI 从 `GEMINI.md` 及 `MEMORY.md` 提取的上下文记忆。
* **`/init`** - 分析当前项目，并自动生成一份量身定制的 `GEMINI.md` 上下文规范文件。
* **`/directory` (或 `/dir`)** - 管理多目录工作区（添加其他关联目录，或查看当前的工作区目录）。

### 高级功能与扩展
* **`/tools`** - 列出当前会话中 AI 被赋予的所有底层工具权限（使用 `desc` 显示详细描述，`nodesc` 仅显示名称）。
* **`/mcp`** - 管理 Model Context Protocol (MCP) 服务器配置（如 `list`, `reload`, `auth` 等）。
* **`/skills`** - 管理 Agent Skills（专属技能包）（如 `enable`, `disable`, `reload`, `list`）。
* **`/extensions`** - 管理 CLI 的三方扩展插件（`install`, `uninstall`, `list`, `update`, `config`）。
* **`/agents`** - 查看和管理可用的本地或远程子代理 (Subagents，如 `cli_help`, `codebase_investigator`)。
* **`/commands`** - 查看和管理从 `.toml` 文件加载的自定义斜杠命令。
* **`/hooks`** - 管理用于拦截和修改 CLI 行为的生命周期钩子配置。

### 终端与界面个性化
* **`/theme`** - 打开对话框以更改 CLI 终端界面的视觉主题。
* **`/vim`** - 切换输入区是否启用 Vim 风格的按键绑定与导航。
* **`/copy`** - 将 AI 上一次输出的文本快速复制到系统剪贴板。
* **`/shells` (或 `/bashes`)** - 切换或查看正在后台长时间运行的 Shell 进程。
* **`/ide`** - 管理 IDE 集成和配套插件的状态。
* **`/editor`** - 选择支持的外部代码编辑器。
* **`/terminal-setup`** - 在特定 IDE 的终端中配置多行输入的快捷键。

### 其他
* **`/permissions`** - 管理文件夹的信任状态和安全沙盒设置。
* **`/setup-github`** - 快速生成用于 Issue 分发和 PR 审查的 GitHub Actions 配置文件。
* **`/auth`** - 重新打开对话框更改认证方式（如切换 API Key 或 OAuth）。
* **`/policies`** - 列出当前模式下所有激活的安全策略。

---

### 💡 快捷输入符提示
除了 `/` 开头的命令外，还有两个极其常用的快捷符号：
* **`@` (At Commands)**：用于将文件或目录的内容直接包含到提示词中（例如在输入框打 `@README.md`）。
* **`!` (Shell Commands)**：用于将输入直接作为系统的 Shell 命令执行（相当于在原生终端里敲命令，如 `!git status`）。