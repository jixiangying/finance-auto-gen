import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

output_dir = "images/charts/"
os.makedirs(output_dir, exist_ok=True)

# 设置中文字体 (macOS)
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/PingFang.ttc"
prop = fm.FontProperties(fname=font_path)

fig, ax = plt.subplots(figsize=(10.8, 7.2))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【核心行情信息图】(2026/07/16 周四晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Market Events
ax.text(0.06, 0.82, "▌ 核心事件与市场逻辑", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("科技芯片高位获利回吐", "半导体、存储芯片等前期大涨赛道集体回调，两市超2800只个股下跌", "高低切换迹象明显，影视院线、医药及消费电子等板块逆势走强"),
    ("央行引导信贷降速提质", "强调贷款扩张从规模导向转向质量导向，精准调控创造适宜货币金融环境", "央行逆周期和跨周期调节持续发力，买断式逆回购保障流动性平稳"),
    ("长鑫科技新股开启申购", "科创板IPO新股今日开启申购，发行价8.66元，中金担任联席保荐人", "作为国产存储巨头，其大体量上市夯实并提振半导体国产替代信心"),
    ("港股逆势大涨收复两万五", "恒指大涨1.33%收复25000点，恒生科技指数大涨1.98%表现强劲", "大型科技互联网股受资金追捧，与A股市场呈现明显的估值分化")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.04, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产收盘表现", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,882.41 (-1.85%) 🟢", "A股大幅整理，主要宽基指数集体下挫"),
    ("深证成指 (SDEC)", "14,488.65 (-1.97%) 🟢", "深证走低，两市全天合计成交约2.42万亿"),
    ("创业板指 (CHINEXT)", "3,692.46 (-2.95%) 🟢", "半导体大幅杀跌拖累，创业板指跌幅居前"),
    ("恒生指数 (HSI)", "25,008.60 (+1.33%) 🔴", "港股逆势大涨，大厂科技与互联网领涨板块"),
    ("恒生科技指数 (HSTECH)", "4,834.44 (+1.98%) 🔴", "科技股展现韧性，多只权重龙头股暴力反弹")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.035, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.0075 + 0.02
    ax.text(0.58 + val_width, y_right-0.035, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.075

plt.tight_layout()
output_path = "images/charts/2026-07-16-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
