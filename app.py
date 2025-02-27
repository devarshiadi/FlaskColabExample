from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aditya's Console</title>
    <link rel="icon" href="https://www.adityadevarshi.online/favicon.ico" type="image/x-icon">
    <style>
        body { background-color: black; color: limegreen; font-family: monospace; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .console { max-width: 90%; width: 600px; white-space: pre-wrap; font-size: 1.2rem; overflow: hidden; padding: 15px; box-shadow: 0px 0px 10px rgba(0,255,0,0.5); border-radius: 5px; background: rgba(0, 0, 0, 0.9); }
        .cursor { display: inline-block; width: 10px; height: 18px; background: limegreen; animation: blink 0.7s infinite; }
        a { color: limegreen; text-decoration: none; word-break: break-word; }
        a:hover { text-decoration: underline; }
        @keyframes blink { 50% { opacity: 0; } }
        @media (max-width: 768px) {
            .console { font-size: 1rem; padding: 10px; max-width: 95%; }
            .cursor { width: 8px; height: 16px; }
        }
    </style>
</head>
<body>
    <div class="console">
        <pre id="typing-text"></pre><span class="cursor"></span>
    </div>
    <script>
        const text = `
Welcome to Aditya's Console
============================
Time: {current_time}

Name: Aditya Devarshi
GitHub: https://github.com/devarshiadi
LinkedIn: https://www.linkedin.com/in/aditya-devarshi/
Portfolio: https://www.adityadevarshi.online/

Open to Work: Yes
Interests: Python, Data Science, AI/ML
============================

Thanks for reading my article! More at
 https://medium.com/@devarshia5
`;
        let index = 0;
        function typeEffect() {
            if (index < text.length) {
                let preElement = document.getElementById("typing-text");
                preElement.textContent += text.charAt(index);
                index++;
                setTimeout(typeEffect, 50);
            } else {
                let preElement = document.getElementById("typing-text");
                preElement.innerHTML = preElement.textContent.replace(/(https?:\/\/\S+)/g, '<a href="$1" target="_blank">$1</a>');
            }
        }
        typeEffect();
    </script>
</body>
</html>
""".replace("{current_time}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
