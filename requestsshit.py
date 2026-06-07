''' we use requests send HTTP request and extract the raw data
 it Fetches HTML / JSON / files, but Cannot parse HTML and  Cannot run JavaScript
🔹 Use when: Calling APIs , Downloading pages , Getting raw HTML
'''
import time 
import requests
#  requests is a Python library used to send HTTP requests easily. which lets you: Fetch web pages (GET) , Send data (POST) , Work with APIs , Handle headers, cookies, sessions  . can update header using session.headers.update({'x-test': 'true'})
 
url = "https://www.exampleshit.com"
header = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive" 
}
# A session lets your program remember things between requests. keep cookies for persist data for namual use to store cookies  jar = requests.cookies.RequestsCookieJar() 
# to define manually where the cookies to sent we use  jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')

session = requests.session() # cookies are stored in the  session.cookies 
# searches keyword python in page number 1 
params = {"q": "python", "page": 1}
# it doesn't remember anything , new request everytime , not remember the last request .
# r = requests.get(url , headers=header)
r = session.get(url ) 
proxies = {
    "http": "http://123.45.67.89:8080",
    "https": "http://123.45.67.89:8080"
}
cred = ('user', 'password')

r1 = session.get(url, headers=header)   # Sends request with custom headers (like User-Agent, Accept) → used to mimic browser or send metadata
r2 = session.get(url, params=params)   # Adds query parameters to URL → converts dict into ?key=value format in URL
r3 = session.get(url, timeout=10)   # Stops request if it takes more than 10 seconds → prevents hanging
r4 = session.get(url, allow_redirects=False)   # Prevents automatic redirection → you can manually handle 301/302 responses
r5 = session.get(url, auth=('user','pass')) # Sends Basic Authentication → username and password go in Authorization header
r6 = session.get(url, auth=cred)   # Uses credentials stored in variable (must be tuple or Auth object) → same as above but dynamic
r7 = session.get(url, stream=True)   # Downloads response in chunks → useful for large files, saves memory
r8 = session.get(url, proxies=proxies)   # Routes request through proxy server → hides your IP or bypass restrictions
r9 = session.get(url, cert=("cert.pem", "key.pem"))   # Uses client-side SSL certificate → required for secure APIs that verify client identity
r10 = session.get(url, json={"key": "value"})   # Sends JSON data in request body → rarely used in GET, but some APIs accept it
import certifi    # ita Python package that provides a bundle of trusted SSL certificates (CA bundle).
r11 = session.get(url, verify=certifi.where()) # SSL certificate verfication : Server sends its SSL certificate , requests checks it using certifi CA bundle .Certificate is like a digital ID card for a website.
multiple_files = [
    ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
    ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
r12 = requests.post(url, files=multiple_files) # upload multiple file in one request 

r14 = requests.get( "https://secure-api.com", cert=("client.crt", "client.key") ) # client certificate verification : it Usually uses 2 files which inlcude Client Certificate → client.crt , Private Key → client.key . sometimes combined into one .pem file 
'''
the above 3 files for the client verification are provided by company /created by youself 
creating Client certificate files : 
Step 1: Generate private key
    openssl genrsa -out client.key 2048
        👉 Creates:
            client.key  (KEEP THIS SAFE 🔒)
Step 2: Create certificate request (CSR)
    openssl req -new -key client.key -out client.csr
        👉 You’ll be asked:
        country
        organization
        name (can be anything for testing)
Step 3:Generate certificate
    openssl x509 -req -in client.csr -signkey client.key -out client.crt -days 365
        👉 Creates:
            client.crt
Optional step : Combine into .pem (optional)
        openssl pkcs12 -export -out client.pem -inkey client.key -in client.crt
    OR simple combine:
        cat client.crt client.key > client.pem

'''
# This shows the HTTP status code returned by the server. 200	✅ Success , 404	❌ Not Found , 500	❌ Server Error , 403	❌ Forbidden
print(r.status_code) 
# saving the data gotten by the url 
file = open("tt.txt","w")
file.write(r.text)
time.sleep(2)
print("data extracted")
 # This gives you the actual content of the webpage (as text)
print(r.text) 
# read a response in chunks .
for chunk in r.iter_content(1024):
    if chunk :
        print(chunk)
# reading text line by line .
for line in r.iter_lines():
    if line:
        print(line.decode('utf-8')) # each line is in byte so we need to decode it 
#  r.raw gives you the raw response stream from the server (without decompression and decoding )
r.raw
# read first 10 bytes from that stream
r.raw.read(10)
print(r.url)        # final URL
print(r.history)    # redirect chain
# give the raw body of the response 
print(r.content)
# this gets cookies from the server manually by requests
recievecookiesM = requests.get("https://www.exampleshit.com")
print(recievecookiesM.cookies)
# this send cookies to the server manually by requests
cookis = r.cookies 
sendcookiesM = requests.get("https://example.com/dashboard", cookies=cookis) 
# to delete  all the cookies 
session.cookies.clear()
# to delete the specific cookies by details 
session.cookies.clear(domain='httpbin.org', path='/cookies', name='tasty_cookie')
# to delte the specific cookies using just the name 
session.cookies.pop('session_id', None)
# this gets the cookies from the server automatically by session 
recievecookiesA = session.get("https://example.com")
# this sends data to the server automatically by session (when you post to the server and server responds with a session it , session stores it as cookies )
sendcookiesA = session.get("https://example.com/dashboard")
# gets the type of the data returned by the server 
r.headers['content-type']
# tells how response text is encoded 
r.encoding
# show the response as python dictionary 
r.json()
# to acces the data from the json file (python dictionary )
r.json()['login']
# compared two dictionary . give boolean result 
r1.json()['form'] == r2.json()['form']

# sending the data to the server 
data = {
    "username": "faizan",
    "password": "1234"
}
response = session.post("https://www.exampleshit.com", data=data)

# send files to the server
files = {"file": open("test.txt", "r")}
res = requests.post(url, files=files)

# could be session insted of requests
requests.put(url) 
requests.delete(url)
requests.patch(url)
requests.head(url)

"""
Method          | Purpose                          | Sends Data | Gets Response Body | Common Use
----------------|----------------------------------|------------|--------------------|-------------------------
GET             | Retrieve data                    | ❌ No      | ✅ Yes             | Fetch webpage/API data
POST            | Create new resource              | ✅ Yes     | ✅ Yes             | Submit form / API create
PUT             | Replace entire resource          | ✅ Yes     | ✅ Yes             | Update full data
PATCH           | Update part of resource          | ✅ Yes     | ✅ Yes             | Partial update
DELETE          | Remove resource                  | ❌ Usually | ✅ Yes             | Delete data
HEAD            | Get headers only (no body)       | ❌ No      | ❌ No              | Check status/metadata
OPTIONS         | Get allowed methods              | ❌ No      | ✅ Yes             | API capabilities check
"""
# error handling 
try:
    rx = requests.get("https://wrong-url", timeout=3)
    rx.raise_for_status()
except requests.exceptions.HTTPError:
    print("HTTP error")
except requests.exceptions.ConnectionError:
    print("Connection error")
except requests.exceptions.Timeout:
    print("Timeout")

# retry logic to connect 
for i in range(3):
    try:
        r = requests.get("https://httpbin.org/get", timeout=3)
        print(r.status_code)
        break
    except requests.exceptions.RequestException:
        print("Retrying...")
        time.sleep(2)
# When a server sends a response compressed using Brotli (br), requests can automatically decompress it for you — but only if you have a Brotli library installed.It’s a modern compression method (better than gzip in many cases) , Servers use it to reduce response size . with brokli installed you dont need to write any code of brokli , requests handles it all by itself . there are many types of compresssion 
# incase of compression detection and decompressing it 
def decompress_response(r):
    encoding = r.headers.get("Content-Encoding", "").lower()
    # Disable auto decoding to handle manually
    r.raw.decode_content = False
    compressed = r.raw.read()
    print("Detected Encoding:", encoding if encoding else "None")
    try:
        if encoding == "gzip":
            import gzip
            return gzip.decompress(compressed)
        elif encoding == "deflate":
            import zlib
            try:
                return zlib.decompress(compressed)
            except zlib.error:
                # Some servers send raw deflate
                return zlib.decompress(compressed, -zlib.MAX_WBITS)
        elif encoding == "br":
            try:
                import brotli
                return brotli.decompress(compressed)
            except ImportError:
                print("⚠ Brotli not installed (pip install brotli)")
        elif encoding == "zstd":
            try:
                import zstandard as zstd
                dctx = zstd.ZstdDecompressor()
                return dctx.decompress(compressed)
            except ImportError:
                print("⚠ zstandard not installed (pip install zstandard)")
        elif encoding == "bz2":
            import bz2
            return bz2.decompress(compressed)
        elif encoding in ("lzma", "xz"):
            import lzma
            return lzma.decompress(compressed)
        elif encoding in ("identity", ""):
            # No compression
            return compressed
        else:
            print(f"⚠ Unknown encoding: {encoding}")
            return compressed
    except Exception as e:
        print("❌ Decompression failed:", e)
        return compressed
# 🔹 Example usage
url = "https://example.com"
r = requests.get(url, stream=True)
data = decompress_response(r)
# Try decoding to text
try:
    print(data.decode("utf-8")[:500])
except:
    print("Binary data received")

# Compression Types Overview
# Type      | Built-in | Speed        | Compression   | Use
# ----------|----------|-------------|---------------|----------------
# gzip      | Yes      | Fast        | Medium        | Web (HTTP)
# deflate   | Yes      | Fast        | Medium        | Web (HTTP)
# brotli    | No       | Fast        | High          | Modern web
# zstd      | No       | Very fast   | High          | Modern systems
# bz2       | Yes      | Slow        | High          | File compression
# lzma/xz   | Yes      | Very slow   | Very high     | Archives
# zip       | Yes      | Medium      | Medium        | Multiple files
# tar       | Yes      | N/A         | Archive only  | Linux/Unix


# error handling 
import requests
try:
    r = requests.get(url, timeout=(3.05, 27)) # Connect → max 3.05 sec , Read → max 27 sec
    r.raise_for_status()   # It raises an exception if the HTTP status code is an error
    data = r.json()

except requests.exceptions.Timeout:
    print("Timeout")

except requests.exceptions.ConnectionError:
    print("Connection failed")

except requests.exceptions.HTTPError:
    print("Bad response")

except requests.exceptions.JSONDecodeError:
    print("Invalid JSON")

except requests.exceptions.RequestException as e:
    print("Other error:", e)

#         AUTHENTICATION   
# 1. BASIC AUTHENTICATION
from requests.auth import HTTPBasicAuth 
basic = HTTPBasicAuth('user', 'pass')
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)  # for basic authentication 

# 2. DIGEST AUTHENTICATION
from requests.auth import HTTPDigestAuth
digest = HTTPDigestAuth('user', 'pass')
r2 = requests.get( 'https://httpbin.org/digest-auth/auth/user/pass', auth=digest )  # Digest Auth

# 3. TOKEN-BASED AUTHENTICATION
headers_token = { "Authorization": "Token abc123" }
r3 = requests.get( 'https://httpbin.org/headers', headers=headers_token )  # Token Auth

# 4. BEARER TOKEN (JWT)
headers_bearer = { "Authorization": "Bearer your_token_here" }
r4 = requests.get( 'https://httpbin.org/headers', headers=headers_bearer )  # Bearer Token

# 5. API KEY AUTHENTICATION
# (a) API key in params
params = { "api_key": "your_api_key" }
r5 = requests.get( 'https://httpbin.org/get', params=params )

# (b) API key in headers
headers_api = { "x-api-key": "your_api_key" }
r6 = requests.get( 'https://httpbin.org/get', headers=headers_api )

# 6. OAUTH (SIMPLIFIED - USING ACCESS TOKEN)
headers_oauth = { "Authorization": "Bearer access_token" }
r7 = requests.get( 'https://httpbin.org/get', headers=headers_oauth )  # OAuth2 (after getting token)

# 7. SESSION-BASED AUTHENTICATION
s1 = requests.Session()
s1.trust_env = False # By default (trust_env = True) , Requests automatically reads settings from your system environment, like: HTTP_PROXY / HTTPS_PROXY → proxy settings , REQUESTS_CA_BUNDLE → custom SSL certificates , NO_PROXY → bypass proxy
rw = s1.get('https://httpbin.org/basic-auth/user/pass')

# 8. CUSTOM AUTHENTICATION
headers_custom = { "Authorization": "Custom xyz123" }
r9 = requests.get( 'https://httpbin.org/headers', headers=headers_custom )



"""
Authentication Types Cheat Sheet

Type            Secure     Stateful     Common Use
-----------------------------------------------------------
Basic           ❌         ❌           Simple APIs
Digest          ✔️         ❌           Legacy systems
Token           ✔️         ❌           APIs
Bearer (JWT)    ✔️✔️       ❌           Modern APIs
API Key         ✔️         ❌           Public APIs
OAuth           ✔️✔️✔️     ❌           Social login (Google, etc.)
Session         ✔️         ✔️           Websites (login systems)
"""
 # types of proxies 
"""
Type              | Use Case                | Anonymity
------------------|------------------------|----------
HTTP Proxy        | Web browsing/scraping  | Medium
SOCKS Proxy       | Any traffic            | High
Transparent Proxy | Monitoring/filtering   | None
Anonymous Proxy   | Hide IP                | Medium
Elite Proxy       | Full anonymity         | High
Reverse Proxy     | Server-side use        | N/A
"""