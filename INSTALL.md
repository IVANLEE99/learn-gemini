# Gemini CLI 安装指南

以下是官方推荐的标准安装和配置流程：

## 1. 环境准备
在安装之前，请确保你的系统已经安装了以下环境：
*   **Node.js**: 需要 v18.0.0 或更高版本（推荐使用最新的 Node.js 20+ LTS 版本）。
*   **npm**: Node.js 自带的包管理器。

你可以通过在终端执行以下命令来检查版本：
```bash
node -v
npm -v
```

## 2. 全局安装
你可以通过 npm 将 Gemini CLI 作为一个全局包安装到系统中。在终端运行：

```bash
npm install -g @google/gemini-cli
```

*(如果你想体验最新的预览版功能，可以使用 `@preview` 标签：`npm install -g @google/gemini-cli@preview`)*

## 3. 免安装运行 (可选)
如果你不想全局安装，也可以通过 `npx` 直接在当前目录下运行它：
```bash
npx @google/gemini-cli
```

## 4. 首次运行与授权
安装完成后，在终端直接输入以下命令启动：
```bash
gemini
```
首次运行时，它会自动引导你进入浏览器完成 Google 账号的 OAuth 授权登录（如果你在无头服务器上，可以按提示通过生成的链接和代码完成授权）。

## 5. 验证安装
想要确认是否安装成功，可以检查安装的版本号：
```bash
gemini --version
```

## 6. 配置 MCP (Model Context Protocol) 插件支持
Model Context Protocol (MCP) 允许 Gemini CLI 连接到外部工具、数据源和本地服务（如操作数据库、调用 GitHub 等）。

### 如何配置 MCP 服务器
Gemini CLI 会在 `~/.gemini/settings.json`（全局）或项目下的 `.gemini/settings.json` 中读取 MCP 服务器配置。

**配置示例：**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "$GITHUB_TOKEN"
      }
    }
  }
}
```

### 常用 MCP 命令
配置完成后，可以在终端或在运行的交互式会话中使用以下命令管理：
*   `/mcp list`：查看所有已连接的 MCP 服务器及其提供的工具。
*   `/mcp reload`：无需重启即可重新加载插件配置。

