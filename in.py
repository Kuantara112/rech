from flask import Flask, render_template_string
import time

app = Flask(__name__)

# Template URL dengan placeholder timestamp
BASE_URL = (
    "https://tvc-invdn-cf-com.investing.com/web/1.12.43/index59-prod.html"
    "?carrier=07475c3bb6111b49114c49caa6dd79ce"
    "&time={timestamp}"
    "&domain_ID=54"
    "&lang_ID=54"
    "&timezone_ID=27"
    "&version=1.12.43"
    "&locale=en"
    "&timezone=Asia/Bangkok"
    "&pair_ID=23705"
    "&interval=15"
    "&session=session"
    "&prefix=id"
    "&suffix="
    "&client=0"
    "&user=0"
    "&family_prefix=tvc4"
    "&init_page=instrument"
    "&sock_srv=https://streaming.forexpros.com"
    "&m_pids="
    "&watchlist="
    "&geoc=ID"
    "&site=https://id.investing.com"
    "&tnb_buy_color="
    "&tnb_sell_color="
    "&tnb_buy_hover_color="
    "&tnb_sell_hover_color="
    "&enable_tnb="
)

@app.route('/')
def show_chart_with_news():
    current_timestamp = int(time.time())
    full_url = BASE_URL.format(timestamp=current_timestamp)

    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Investing.com Chart + News</title>
        <style>
            body { font-family: Arial, padding: 0; margin: 0; background-color: #f2f2f2; }
            iframe { width: 100%; height: 100vh; border:none; filter: invert(1) hue-rotate(180deg); }
        </style>
    </head>
    <body>
        <iframe src="{{ chart_url }}"></iframe>
    </body>
    </html>
    '''
    return render_template_string(html_template, chart_url=full_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
