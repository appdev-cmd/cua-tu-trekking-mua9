# -*- coding: utf-8 -*-
import os

base_dir = r"C:\Users\hoang\.gemini\antigravity\scratch\trekking-cua-tu"

with open(os.path.join(base_dir, "img_b64.txt"), "r", encoding="utf-8") as f:
    img_b64 = f.read().strip()

with open(os.path.join(base_dir, "logo_b64.txt"), "r", encoding="utf-8") as f:
    logo_b64 = f.read().strip()

with open(os.path.join(base_dir, "template.html"), "r", encoding="utf-8") as f:
    html_tpl = f.read()

final_html = html_tpl.replace("{{IMG_B64_PLACEHOLDER}}", img_b64).replace("{{LOGO_B64_PLACEHOLDER}}", logo_b64)

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(final_html)

print("Generated updated index.html successfully! Size:", len(final_html))
