from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

mcp = FastMCP(
    "city_eye",
    transport_security=TransportSecuritySettings(
        allowed_hosts=["*"],
        allowed_origins=["*"],
    ),
)