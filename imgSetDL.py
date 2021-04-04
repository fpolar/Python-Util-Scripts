# from urllib.request import Request, urlopen, urlopen
# import requests
# import shutil
# import tempfile

from PIL import Image
import requests

im = Image.open(requests.get(url, stream=True).raw)

for cid in range(999):
	cid_str = str(cid)
	cid_str = cid_str.zfill(3)
	# print(cid_str)
	try:
		req = Request("https://art.hearthstonejson.com/v1/orig/BAR_"+cid_str+".png", headers={'User-Agent': 'Mozilla/5.0'})
		# webpage = urlopen(req).read()
		with urlopen(req) as response:
			print(response)
			# f = open("Cards/Barrens/BAR_"+cid_str+".png","w+")
			im = Image.open(response.raw)
			im.save("Cards/Barrens/BAR_"+cid_str+".png")
			# f.close()
		# req.urlretrieve("https://art.hearthstonejson.com/v1/orig/BAR_"+cid_str+".png", "/Cards/Barrens/cid_str.png")
	except Exception as e: 
		# print(cid)
		# print(e)
		x = e

print("done")