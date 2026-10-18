server={"name":"webserver","os":"linux","port":80}

server["port"]=8080
print(server)

server["application"]="tomcat"
print(server)

server.pop("os")
print(server)

print(server["name"])
print(server["port"])
print(server["application"])

print(server.keys())
print(server.values())

for key,values in server.items():
    print(key,values)