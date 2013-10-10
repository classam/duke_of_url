from just_get_my_damn_ip import get_ip

local_ip = get_ip()

cass_host = local_ip
cass_port = 9160
cass_keyspace = 'duke'
flask_host = local_ip
