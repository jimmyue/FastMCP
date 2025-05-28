# FastMCP
MCP服务


一、获取高德KEY
https://console.amap.com/dev/key/app

二、Cursor设置
1.设置mcp server
设置->MCP-> mcp.json
{
  "mcpServers": {
    "gaode": {
      "command": "python",
      "args": [
        "D:\\myai\\gaode.py"
      ]
    }
  }
}

2.网络问题
File->Preferences->vs code setting->搜索HTTP->Disable http2勾选上
