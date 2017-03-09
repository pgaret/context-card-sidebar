import http.client

conn = http.client.HTTPSConnection("api.kustomerapp.com")

payload = "{}"

headers = {
    'content-type': "application/json",
    'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjU4YjQ4ZTRlYzM1OTE4MTEwMGE0YTE4OCIsInVzZXIiOiI1OGI0OGU0ZDY4NGExMDExMDBhYjFiMzUiLCJvcmciOiI1OGI0OGUyYjUzMDUyZjExMDAxYTk4ZDciLCJvcmdOYW1lIjoienp6LXBlcmVncmluIiwidXNlclR5cGUiOiJtYWNoaW5lIiwicm9sZXMiOlsib3JnLnVzZXIiLCJvcmcuYWRtaW4iXSwiYXVkIjoidXJuOmNvbnN1bWVyIiwiaXNzIjoidXJuOmFwaSIsInN1YiI6IjU4YjQ4ZTRkNjg0YTEwMTEwMGFiMWIzNSJ9.ZwgabjO0svZUXmaSQwom1CdqrTg9157zjs4BUjPP_8g"
    }

conn.request("GET", "/v1/cards/58c1c4b8f5bbb71100aa4d94", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
