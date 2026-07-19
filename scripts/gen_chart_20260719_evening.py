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

fig, ax = plt.subplots(figsize=(11.5, 7.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
ax.text(0.05, 0.93, "【新周开盘展望与核心资产表现】(2026/07/19 周日晚报)", fontproperties=prop, fontsize=14, fontweight='bold', color='#1e293b')
ax.axhline(y=0.88, xmin=0.04, xmax=0.96, color='#cbd5e1', linewidth=1.5)

# Left Side: Key Weekend Events
ax.text(0.06, 0.82, "▌ 周末重磅财经要闻汇总", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

events = [
    ("金融反腐：国开行原行长欧阳卫民被查", "中纪委通报涉嫌严重违纪违法，接受纪律审查", "显示监管层持续强化金融反腐，净化行业风气与生态"),
    ("上海WAIC人工智能大会闭幕", "倡导以人为本与人类控制，成立世界人工智能合作组织", "中方承诺向发展中国家培训与输出气象AI，彰显数字底座"),
    ("中美关系与经贸制裁微调", "美对港紧急状态到期部分制裁失效，香港特殊地位仍变", "短期利于缓和跨境经贸风险溢价，但长周期博弈不变"),
    ("券商研报展望：A股筑底磨砂，新周均衡配置", "中信/中金等建议避开拥挤科技股，逢高降低高位仓位", "等待中报业绩验证，配置红利防御公用事业与绩优科技")
]

y = 0.72
for title, val, note in events:
    ax.text(0.08, y, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    ax.text(0.08, y-0.035, f"{val}\n{note}", fontproperties=prop, fontsize=9.0, color='#64748b')
    y -= 0.11

# Right Side: Market Indicators & Assets
ax.text(0.56, 0.82, "▌ 核心资产新周开盘前瞻", fontproperties=prop, fontsize=12, fontweight='bold', color='#0f172a')

asset_data = [
    ("上证指数 (SSEC)", "3,764.15 (全周: -5.81% / 周五: -3.05%) 🟢", "上周五跌破3800，关注新周国家队宽基ETF托底"),
    ("创业板指 (CHINEXT)", "3,428.63 (全周: -10.78% / 周五: -7.15%) 🟢", "高位科技赛道拥挤出清，关注中报业绩确定性龙头"),
    ("富时A50期指 (A50)", "14,332.0 (周五收盘: -3.74%) 🟢", "周五曾跌超3%，尾盘有所拉升，反应新周部分承接"),
    ("恒生指数 (HSI)", "24,562.24 (全周: +1.60% / 周五: -1.78%) 🔴", "回调但不改周线三连阳，下周恒指聚焦重头科网股"),
    ("比特币 (BTC)", "64,920.0 (周末表现: +2.10%) 🔴", "周末逆市反弹逼近6.5万美元，资金避险与风格轮动"),
    ("WTI原油期货 (WTI)", "82.49 (周五收盘: +4.48%) 🔴", "中东美伊冲突升级威胁航道，避险溢价与能源通胀")
]

y_right = 0.72
for title, val, comment in asset_data:
    ax.text(0.58, y_right, title, fontproperties=prop, fontsize=10.5, color='#334155', fontweight='bold')
    color = '#ef4444' if '🔴' in val else '#10b981'
    clean_val = val.replace('🟢', '').replace('🔴', '')
    
    # Draw value with corresponding color
    ax.text(0.58, y_right-0.032, clean_val, fontproperties=prop, fontsize=9.0, fontweight='bold', color=color)
    # Draw comment next to it
    val_width = len(clean_val) * 0.007 + 0.02
    ax.text(0.58 + val_width, y_right-0.032, f"|  {comment}", fontproperties=prop, fontsize=9.0, color='#64748b')
    
    y_right -= 0.065

plt.tight_layout()
output_path = "images/charts/2026-07-19-evening.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print(f"Chart saved to {output_path}")
