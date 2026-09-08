from mcp_instance import mcp
from data.resident import resident_data
@mcp.tool()
def number_of_residents()->int:
    """ this tool is used to get the number of residents in the mcp server """
    return len(resident_data)