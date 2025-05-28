from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("gaode")

base_url="https://restapi.amap.com"
key="XXXX"

async def get_request(url: str) -> dict[str, Any] | None:
    """请求http接口get方法"""
    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as exc:
        print(f"Error while requesting {exc.request.url!r}.")
        return None

@mcp.tool()
async def get_weather(city: str , extensions: str = 'base') -> dict[str, Any] | None:
    """
    获取城市实况/预报天气接口

    Params:
        city: 中国的城市，如北京。
        extensions: base/all，base:返回实况天气，all:返回预报天气。

    """
    url = f"{base_url}/v3/weather/weatherInfo?key={key}&city={city}&extensions={extensions}"
    data = await get_request(url)
    return data

@mcp.tool()
async def get_ip(ip: str) -> dict[str, Any] | None:
    """
    将 IP 信息转换为地理位置信息接口

    Params:
        ip: 需要搜索的 IP 地址（仅支持中国）

    """
    url = f"{base_url}/v3/ip?key={key}&ip={ip}"
    data = await get_request(url)
    return data

@mcp.tool()
async def get_busstop(city: str , keywords: str) -> dict[str, Any] | None:
    """
    通过城市/关键字，查询公交站信息接口

    Params:
        keywords: 需要查询公交站的关键字。
        city: 中国的城市，如北京。

    """
    url = f"{base_url}/v3/bus/stopname?key={key}&city={city}&keywords={keywords}"
    data = await get_request(url)
    return data

if __name__ == "__main__":
    mcp.run()
