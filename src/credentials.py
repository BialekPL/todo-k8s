with open('/mnt/secrets-store/db-username') as file:
    db_username = file.read().strip()

with open('/mnt/secrets-store/db-password') as file :
    db_password = file.read().strip()

with open('/mnt/secrets-store/db-server') as file :
    db_server = file.read().strip()

with open('/mnt/secrets-store/db-name') as file :
    db_name = file.read().strip()

with open('/mnt/secrets-store/ai-connection-string') as file :
    ai_connection_string = file.read().strip()