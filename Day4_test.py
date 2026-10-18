servers = ["AWS", "Linux", "Docker"]
servers.append("terraform")
print(servers)

###servers = ["AWS", "Linux", "Docker"]
servers.insert(2,"python")
print(servers)


#servers = ["AWS", "Linux", "Docker"]
servers.remove("AWS")
print(servers)

print(len(servers))

for server in servers:
    print(server)