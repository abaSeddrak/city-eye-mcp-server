# from tools.cars_tools import number_of_cars
# from tools.car_wash_tool import number_of_subscribers
# from tools.residents_tools import number_of_residents
# from mcp_instance import mcp

# mcp.run()


import tools.cars_tools
import tools.car_wash_tool
import tools.residents_tools
from mcp_instance import mcp
from fastapi import FastAPI

app = FastAPI()
app.mount("/", mcp.sse_app())