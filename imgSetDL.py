# from urllib.request import Request, urlopen, urlopen
# import requests
# import shutil
# import tempfile

from PIL import Image
import requests

url = 'http://worldagnetwork.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
print(result.content.decode())

for cid in range(999):
	cid_str = str(cid)
	cid_str = cid_str.zfill(3)
	print(cid_str)
	try:
		res = requests.get("https://art.hearthstonejson.com/v1/orig/BAR_"+cid_str+".png", headers={'User-Agent': 'Mozilla/5.0'})
		file = open("sample_image.png", "wb")
		file = open("Cards/Barrens/BAR_"+cid_str+".png", "wb")
		file.write(res.content)
		file.close()

		# print(res.content.decode())
		# print("1")
		# im = Image.open(res.raw.data)
		# print("2")
		# im.save("Cards/Barrens/BAR_"+cid_str+".png")
		# print("BAR_"+cid_str+".png saved")
		# f.close()
		# req.urlretrieve("https://art.hearthstonejson.com/v1/orig/BAR_"+cid_str+".png", "/Cards/Barrens/cid_str.png")
	except Exception as e: 
		# print(cid)
		# print(e)
		x = e

print("done")