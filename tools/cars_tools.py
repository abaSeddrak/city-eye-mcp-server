from mcp_instance import mcp
from data.cars import cars_data
@mcp.tool()
def number_of_cars()->int:
    """ this tool is used to get the number of cars in the mcp server """
    return len(cars_data)