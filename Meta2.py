
import json
import urllib.request
import sys


#mdUrl = "http://169.254.169.254/metadata/instance?api-version=2017-04-02"
#header={'Metadata': 'True'}
#request = urllib.request.Request(url=mdUrl, headers=header)
#response = urllib.request.urlopen(request)
#dataStr = data.decode("utf-8")
dataStr = '{"compute":{"location":"southeastasia","name":"Ub16-VS","offer":"UbuntuServer","osType":"Linux","platformFaultDomain":"0","platformUpdateDomain":"0","publisher":"Canonical","sku":"16.04.0-LTS","version":"16.04.201611150","vmId":"b77b6337-3519-4f5e-a85a-dc8d4c2bce08","vmSize":"Standard_DS2_v2"},"network":{"interface":[{"ipv4":{"ipAddress":[{"privateIpAddress":"10.0.0.4","publicIpAddress":"52.187.117.149"}],"subnet":[{"address":"10.0.0.0","prefix":"24"}]},"ipv6":{"ipAddress":[]},"macAddress":"000D3AA19EE2"}]}} '

jsonObj = json.loads(dataStr)

print(json.dumps(jsonObj, sort_keys=True, indent=4, separators=(',', ': ')))
print(jsonObj['network'] ['interface'])


