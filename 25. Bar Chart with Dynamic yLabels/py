import matplotlib.pyplot as plt
import numpy as np

products = [
    "Quantum Blaster 2.0", "Eco-Friendly Spatula", "Hyper-Speed Drone",
    "Vintage Toaster 9000", "Smart Pet Feeder", "Ergonomic Keyboard Pro",
    "Solar-Powered Charger", "Noise-Cancelling Earbuds", "DIY Robotics Kit",
    "Biodegradable Toothbrush"
]

changes = [18.5, -7.2, 32.1, -15.8, 10.3, -4.1, 25.0, -9.5, 12.7, -6.0]

sorted_data = sorted(zip(changes, products), key=lambda x: x[0])
sorted_changes = [item[0] for item in sorted_data]
sorted_products = [item[1] for item in sorted_data]

fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('#282C34')
ax.set_facecolor('#282C34')
text_color = 'lightgray'

y_positions = np.arange(len(sorted_products))
bar_colors = ["#4E0CE9" if c > 0 else "#FD5507" for c in sorted_changes]
bars = ax.barh(y_positions, sorted_changes, color=bar_colors, height=0.6)

ax.set_yticks([])
ax.set_ylabel('')

for i, rect in enumerate(bars):
    change = sorted_changes[i]
    product = sorted_products[i]
    width = rect.get_width()
    y_center = rect.get_y() + rect.get_height() / 2
    percent_label_offset = 0.5
    x_pos_percent = width - percent_label_offset if width >= 0 else width + percent_label_offset
    ha_percent_align = 'right' if width >= 0 else 'left'
    ax.text(x_pos_percent, y_center, f'{change:.1f}%', ha=ha_percent_align, va='center', color=text_color, fontsize=9, fontweight='bold')
    category_label_x_offset_from_zero = 1.0
    if change >= 0:
        x_pos_category = -category_label_x_offset_from_zero
        ha_category_align = 'right'
    else:
        x_pos_category = category_label_x_offset_from_zero
        ha_category_align = 'left'
    ax.text(x_pos_category, y_center, product, ha=ha_category_align, va='center', color=text_color, fontsize=10, wrap=True, bbox=dict(boxstyle="round,pad=0.3", fc="#3A3F47", ec="none", alpha=0.8))

ax.set_xlabel('Year-over-Year Change (%)', fontsize=12, labelpad=10, color=text_color)
ax.set_title('Product Performance: Year-over-Year Change\n(Year-over-Year Comparison)', fontsize=18, pad=20, color=text_color, fontweight='bold')
ax.axvline(0, color='lightgray', linestyle='--', linewidth=0.8)

min_val = min(sorted_changes)
max_val = max(sorted_changes)
max_abs_val = max(abs(min_val), abs(max_val))
padding = 5
ax.set_xlim(-(max_abs_val + padding), (max_abs_val + padding))

ax.tick_params(axis='x', colors=text_color)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['bottom'].set_color(text_color)
ax.xaxis.grid(True, linestyle='--', alpha=0.5, color='gray')
ax.yaxis.grid(False)

plt.tight_layout()
plt.show()
