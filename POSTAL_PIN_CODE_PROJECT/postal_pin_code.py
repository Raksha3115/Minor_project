import http.server
import urllib.parse
import urllib.request
import json
import webbrowser
import threading

PORT = 8000


class PostalPINHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # URL se PIN Code lena
        query = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(query.query)

        pincode = params.get("pincode", [""])[0]

        result_html = ""

        # Agar PIN code enter kiya gaya hai
        if pincode:

            if len(pincode) == 6 and pincode.isdigit():

                try:
                    # Postal PIN Code API
                    api_url = "https://api.postalpincode.in/pincode/" + pincode

                    response = urllib.request.urlopen(api_url)
                    data = json.loads(response.read().decode())

                    if data[0]["Status"] == "Success":

                        post_offices = data[0]["PostOffice"]

                        result_html = """
                        <div class="result">
                            <h2>📍 PIN Code Details</h2>
                        """

                        for office in post_offices:

                            result_html += f"""
                            <div class="card">

                                <h3>{office["Name"]}</h3>

                                <p><b>Branch Type:</b>
                                {office["BranchType"]}</p>

                                <p><b>Delivery Status:</b>
                                {office["DeliveryStatus"]}</p>

                                <p><b>District:</b>
                                {office["District"]}</p>

                                <p><b>Division:</b>
                                {office["Division"]}</p>

                                <p><b>Region:</b>
                                {office["Region"]}</p>

                                <p><b>State:</b>
                                {office["State"]}</p>

                                <p><b>Country:</b>
                                {office["Country"]}</p>

                            </div>
                            """

                        result_html += "</div>"

                    else:

                        result_html = """
                        <div class="error">
                            ❌ PIN Code not found.
                        </div>
                        """

                except Exception as e:

                    result_html = f"""
                    <div class="error">
                        ❌ Unable to fetch data.<br>
                        Please check your internet connection.
                    </div>
                    """

            else:

                result_html = """
                <div class="error">
                    ⚠️ Please enter a valid 6-digit PIN Code.
                </div>
                """

        # Complete webpage
        html = f"""
        <!DOCTYPE html>

        <html>

        <head>

            <title>Postal PIN Code Finder</title>

            <style>

                * {{
                    box-sizing: border-box;
                }}

                body {{
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    min-height: 100vh;
                    padding: 40px 20px;
                }}

                .container {{
                    max-width: 850px;
                    margin: auto;
                    background: white;
                    padding: 35px;
                    border-radius: 20px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                }}

                h1 {{
                    text-align: center;
                    color: #333;
                    margin-bottom: 10px;
                }}

                .subtitle {{
                    text-align: center;
                    color: #666;
                    margin-bottom: 30px;
                }}

                form {{
                    display: flex;
                    gap: 10px;
                    justify-content: center;
                    margin-bottom: 30px;
                }}

                input {{
                    width: 300px;
                    padding: 14px;
                    border: 2px solid #ddd;
                    border-radius: 10px;
                    font-size: 16px;
                    outline: none;
                }}

                input:focus {{
                    border-color: #667eea;
                }}

                button {{
                    padding: 14px 25px;
                    border: none;
                    border-radius: 10px;
                    background: #667eea;
                    color: white;
                    font-size: 16px;
                    cursor: pointer;
                }}

                button:hover {{
                    background: #5568d8;
                }}

                .result h2 {{
                    text-align: center;
                    color: #333;
                }}

                .card {{
                    background: #f7f8ff;
                    border-left: 5px solid #667eea;
                    padding: 20px;
                    margin: 15px 0;
                    border-radius: 10px;
                }}

                .card h3 {{
                    color: #667eea;
                    margin-top: 0;
                }}

                .card p {{
                    margin: 8px 0;
                    color: #444;
                }}

                .error {{
                    text-align: center;
                    background: #ffe6e6;
                    color: #cc0000;
                    padding: 15px;
                    border-radius: 10px;
                    margin-top: 20px;
                }}

                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    color: #888;
                    font-size: 13px;
                }}

            </style>

        </head>

        <body>

            <div class="container">

                <h1>📮 Postal PIN Code Finder</h1>

                <p class="subtitle">
                    Find Indian Post Office details using PIN Code
                </p>

                <form method="GET">

                    <input
                        type="text"
                        name="pincode"
                        placeholder="Enter 6-digit PIN Code"
                        maxlength="6"
                        value="{pincode}"
                    >

                    <button type="submit">
                        🔍 Search
                    </button>

                </form>

                {result_html}

                <div class="footer">
                    Powered by Postal PIN Code API
                </div>

            </div>

        </body>

        </html>
        """

        # Browser ko HTML bhejna
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(html.encode("utf-8"))


# Server start karna
server = http.server.HTTPServer(("localhost", PORT), PostalPINHandler)

url = f"http://localhost:{PORT}"

# Browser automatically open hoga
threading.Timer(1, lambda: webbrowser.open(url)).start()

print("Postal PIN Code Finder started...")
print("Browser is opening...")

# Server continuously run hoga
server.serve_forever()