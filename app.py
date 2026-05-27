from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Flask Kubernetes CI/CD Demo</title>
        <style>
          :root {
            color-scheme: light;
            --ink: #16213e;
            --muted: #5f6f89;
            --bg: #f6f8fc;
            --panel: #ffffff;
            --blue: #2563eb;
            --green: #16a34a;
            --orange: #f97316;
            --line: #dde5f2;
          }

          * {
            box-sizing: border-box;
          }

          body {
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            background:
              linear-gradient(135deg, rgba(37, 99, 235, 0.14), transparent 34%),
              linear-gradient(225deg, rgba(22, 163, 74, 0.14), transparent 36%),
              var(--bg);
            color: var(--ink);
            padding: 24px;
          }

          main {
            width: min(860px, 100%);
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: 0 18px 45px rgba(22, 33, 62, 0.12);
            padding: clamp(24px, 5vw, 48px);
          }

          .status {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 8px 12px;
            border-radius: 999px;
            background: #eaf8ef;
            color: #126c32;
            font-weight: 700;
            font-size: 0.92rem;
          }

          .dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--green);
            box-shadow: 0 0 0 6px rgba(22, 163, 74, 0.14);
          }

          h1 {
            margin: 24px 0 12px;
            font-size: clamp(2rem, 6vw, 4rem);
            line-height: 1.05;
            letter-spacing: 0;
          }

          p {
            margin: 0;
            color: var(--muted);
            font-size: clamp(1rem, 2vw, 1.2rem);
            line-height: 1.6;
          }

          .pipeline {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 12px;
            margin-top: 32px;
          }

          .step {
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 16px;
            background: #fbfcff;
          }

          .step strong {
            display: block;
            margin-bottom: 6px;
            font-size: 0.98rem;
          }

          .step span {
            color: var(--muted);
            font-size: 0.9rem;
          }

          .accent-blue {
            border-top: 4px solid var(--blue);
          }

          .accent-orange {
            border-top: 4px solid var(--orange);
          }

          .accent-green {
            border-top: 4px solid var(--green);
          }

          .footer {
            margin-top: 28px;
            padding-top: 20px;
            border-top: 1px solid var(--line);
            display: flex;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
            color: var(--muted);
            font-size: 0.95rem;
          }

          code {
            color: var(--blue);
            background: #eef4ff;
            padding: 3px 7px;
            border-radius: 6px;
          }

          @media (max-width: 720px) {
            body {
              padding: 16px;
            }

            .pipeline {
              grid-template-columns: 1fr;
            }
          }
        </style>
      </head>
      <body>
        <main>
          <div class="status"><span class="dot"></span> Deployment successful</div>
          <h1>Flask App Running on Kubernetes</h1>
          <p>
            Built with GitHub Actions, pushed to DockerHub, and rolled out to a Kubernetes cluster.
            This page is served from the live container.
          </p>

          <section class="pipeline" aria-label="Deployment pipeline">
            <div class="step accent-blue">
              <strong>GitHub</strong>
              <span>Code pushed to main</span>
            </div>
            <div class="step accent-orange">
              <strong>DockerHub</strong>
              <span>Image built and published</span>
            </div>
            <div class="step accent-green">
              <strong>Kubernetes</strong>
              <span>Pods updated with rollout</span>
            </div>
            <div class="step accent-blue">
              <strong>Flask</strong>
              <span>App responding on port 5000</span>
            </div>
          </section>

          <div class="footer">
            <span>Demo version: <code>v3</code></span>
            <span>Image: <code>k2009dutta/flask-k8s-cicd-demo</code></span>
          </div>
        </main>
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
