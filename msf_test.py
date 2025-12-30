from pymetasploit3.msfrpc import MsfRpcClient

try:
    client = MsfRpcClient(password='yourpassword', server='127.0.0.1', port=55553, ssl=False)
    version = client.core.version
    print("Success:", version)
except Exception as e:
    print("Error:", e)
