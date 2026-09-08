from mcp_instance import mcp
from data.car_wash import car_wash_data
@mcp.tool()
def number_of_subscribers()-> int:
    """ this tool is used to get the number of subscribers in the mcp server """
    return len(car_wash_data)