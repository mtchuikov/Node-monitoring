import http.client
import re
import utils

from aiohttp import web
from functools import wraps

def ip() -> str:
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    return conn.getresponse().read().decode("utf-8")

def _catchErr(func):
    @wraps(func)
    async def wrap(req):
        try:
            func_result = await func(req)
        except KeyError:
            return web.HTTPBadRequest()
        return func_result
    return wrap

def _passwordAuth(func):
    @wraps(func)
    async def wrap(req: web.Request):
        if req.headers["Content-Type"] != "application/json":
            return web.HTTPUnsupportedMediaType()
        config = utils.read_config()
        if req.headers["Authorization"] != config["passwordHash"]:
            return web.HTTPForbidden()
        return await func(req)
    return wrap

def _apiAuth(func):
    @wraps(func)
    async def wrap(req: web.Request):
        if req.headers["Content-Type"] != "application/json":
            return web.HTTPUnsupportedMediaType()
        config = utils.read_config()
        if req.headers["Authorization"] != config["apiKeyHash"]:
            return web.HTTPForbidden()
        return await func(req)
    return wrap

@_catchErr
@_passwordAuth
async def settings(req: web.Request):
    load_settings = await req.json()
    pattern = re.compile(ip())
    if "apiKeyHash" not in load_settings.keys():
        raise KeyError
    for index, elem in enumerate(load_settings["hostList"]):
        if pattern.search(elem):
            load_settings["hostList"].pop(index)
    load_settings.update(utils.read_config())
    utils.write_config(load_settings)
    return web.HTTPOk()

@_catchErr
@_apiAuth
async def health(req: web.Request):
    return web.HTTPOk()

@_catchErr
@_apiAuth
async def get_server_status(req: web.Request):
    pass

@_catchErr
@_apiAuth
async def get_node_status(req: web.Request):
    pass

def router():
    rootAPI_url = "/api/v1/"
    return (
        web.post(rootAPI_url + "settings", settings),
        web.post(rootAPI_url + "health", health),
        web.post(rootAPI_url + "get-server-status", get_server_status),
        web.post(rootAPI_url + "get-node-status", get_node_status),
    )

# class APITools:
#
#     @classmethod
#     async def _gossip_request(cls, host) -> List[bool, str]:
#         Response = namedtuple("Response", ["status", "host"])
#         async with aiohttp.ClientSession() as s:
#             try:
#                 headers = {"content-type": "application/json", "Authorization":Config.api_key}
#                 await s.post(f"http://{host}/api/v1/health", headers=headers)
#             except aiohttp.ClientConnectionError:
#                 return Response(False, host)
#         return Response(True, host)
#
#     @classmethod
#     async def gossip(cls):
#         response_received = {key: False for key in Config.host_list}
#         while True:
#             req = [asyncio.create_task(cls._gossip_request(host)) for host in Config.host_list]
#             for resp in await asyncio.gather(*req):
#                 host = resp.host
#                 if not resp.status:
#                     if response_received[host]:
#                         response_received[host] = False
#                         print("Server down", host)
#                 else:
#                     print("OK", host)
#                     if not response_received[host]:
#                         response_received[host] = True
#             await asyncio.sleep(5)
