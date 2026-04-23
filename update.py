import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(
    r'<div class="grid-card">\s*<div class="card-img-box">\s*<img src="([^"]+)" alt="([^"]+)" style="([^"]+)">\s*<div class="price-badge">([^<]+)</div>\s*</div>\s*<div class="card-info">\s*<p class="card-title">([^<]+)</p>\s*<div class="card-actions">\s*<a href="([^"]+)" class="btn-buy-small">COMPRAR</a>\s*<button class="btn-heart-small"><i class="fa-regular fa-heart"></i></button>\s*</div>\s*</div>\s*</div>',
    re.IGNORECASE
)

def replace_card(match):
    img_src = match.group(1)
    img_alt = match.group(2)
    img_style = match.group(3)
    price = match.group(4)
    title = match.group(5)
    buy_href = match.group(6)
    
    new_html = f'''<div class="grid-card">
                    <img src="{img_src}" alt="{img_alt}" style="width: 100%; height: auto; object-fit: cover; border-radius: 4px;">
                    <div class="card-info-row">
                        <p class="card-title">{title}</p>
                        <div class="price-box-new">{price}</div>
                    </div>
                    <a href="{buy_href}" class="btn-buy-full">COMPRAR</a>
                </div>'''
    return new_html

new_html_content = pattern.sub(replace_card, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html_content)
