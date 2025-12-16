"""
Script untuk membuat placeholder image menggunakan matplotlib
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(3, 3))

# Create blue rectangle
rect = patches.Rectangle((0, 0), 1, 1, linewidth=0,
                         edgecolor='none', facecolor='#4A90E2')
ax.add_patch(rect)

# Add text
ax.text(0.5, 0.5, '150x150\nPlaceholder',
        ha='center', va='center',
        fontsize=14, color='white',
        weight='bold')

# Remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Save image
script_dir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(script_dir, 'placeholder.png'),
            dpi=50, bbox_inches='tight', pad_inches=0)
plt.close()

print("Placeholder image created successfully!")
