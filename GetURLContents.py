import argparse
import urllib.request


class URL_Getter:

	def __init__(self, url):
		self.error = None
		self.url = url
		if self.CheckURL(url) == True:
			self.url_contents = self.GetURLContents(url)
		else:
			self.error = "Error in url rules."
			self.url_contents = None


	def GetURLContents(self, url):
		try:
			with urllib.request.urlopen(url) as url_fp:
				# When read, the content will be in bytearray, so transormation to string is needed
				read_content = url_fp.read()
				string_url = read_content.decode("utf8")
		
				return string_url
		except Exception as e:
			self.error = "Exception: " + str(e)
			return None
	
	
	def CheckURL(self, url):
		if "http" in url:
			return True
		else:
			return False
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Module to get info from a URL')
	parser.add_argument('--url', dest='url', help='URL where you want to get the data', required=True)
	args = parser.parse_args()
	
	url_obj = URL_Getter(args.url)
	if url_obj.url_contents != None:
		print(url_obj.url_contents)
	else:
		print(url_obj.error)
