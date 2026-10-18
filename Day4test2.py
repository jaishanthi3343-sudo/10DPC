servers=["aws","linux","docker"]
servers.append("terraform")
print(servers)

servers.insert(0,"python")
print(servers)

servers.remove("aws")
print(servers)

print(len(servers))

for server in servers:
    print(server)