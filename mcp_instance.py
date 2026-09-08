from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

mcp = FastMCP(
    "city_eye",
    transport_security=TransportSecuritySettings(
        allowed_hosts=["35.87.188.43:*", "localhost:*", "127.0.0.1:*"],
    ),
)