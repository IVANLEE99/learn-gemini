# GitHub MCP 插件配置指南 (`@modelcontextprotocol/server-github`)

本指南介绍了如何在 Gemini CLI 中配置和使用官方的 GitHub MCP 插件。该插件允许 Gemini 直接访问您的 GitHub 仓库、读取代码、查看 issues 和 PRs 等。

## 1. 准备 GitHub Personal Access Token (PAT)
为了让 MCP 插件能够访问您的 GitHub 数据，您需要一个具有适当权限的 Token。

1. 登录 GitHub，前往 **Settings -> Developer settings -> Personal access tokens -> Tokens (classic)**。
2. 点击 **Generate new token (classic)**。
3. 勾选必要的权限，通常建议勾选：
   * `repo` (完全控制私有仓库，如果您需要操作代码)
   * `read:user` (读取用户资料)
4. 生成并复制该 Token（格式类似 `ghp_xxxxxxxxxxxx`）。

## 2. 配置 MCP 插件

您可以将该插件配置在 **全局级别** (所有项目可用) 或 **项目级别** (仅当前项目可用)。

### 全局配置 (推荐)
编辑文件：`~/.gemini/settings.json`

### 项目级配置
编辑文件：`<当前项目路径>/.gemini/settings.json`

在选定的 `settings.json` 文件中，添加或修改 `mcpServers` 节点，填入您的 Token：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "您的_GITHUB_TOKEN_填在这里"
      }
    }
  }
}
```

## 3. 加载并生效
配置保存后，在正在运行的 Gemini CLI 会话中输入以下命令以重新加载配置：

```bash
/mcp reload
```
如果不报错，您可以通过 `/mcp list` 查看是否已成功挂载 `github` 提供的工具列表。

## 4. 使用示例
配置完成后，您可以直接用自然语言让 Gemini 操作 GitHub，例如：
* *"帮我看一下我最近更新了哪些 GitHub 仓库。"*
* *"读取一下仓库 `IVANLEE99/learn-claude-code` 最新的提交记录。"*
* *"查看我有没有未处理的 GitHub Issues。"*