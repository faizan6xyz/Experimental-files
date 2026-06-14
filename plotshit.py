"""
COMPREHENSIVE MATPLOTLIB TUTORIAL
All major topics covered with detailed comments and examples
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# SECTION 1: BASIC PLOTTING

print("=" * 80)
print("SECTION 1: BASIC PLOTTING")
print("=" * 80)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot data
ax.plot(x, y, 'b-', linewidth=2, label='sin(x)')

# Add labels and title
ax.set_xlabel('X Axis', fontsize=12, fontweight='bold')
ax.set_ylabel('Y Axis', fontsize=12, fontweight='bold')
ax.set_title('Basic Line Plot', fontsize=14, fontweight='bold')

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Add grid
ax.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.show()

# SECTION 2: DIFFERENT PLOT TYPES

print("\nSECTION 2: DIFFERENT PLOT TYPES\n")

# Create subplots grid (3 rows, 3 columns)
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle('Different Plot Types in Matplotlib', fontsize=16, fontweight='bold', y=1.00)

# Data for plotting
x = np.linspace(0, 10, 50)
y = np.sin(x)
y2 = np.cos(x)
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

# 1. Line Plot
axes[0, 0].plot(x, y, 'b-', linewidth=2, marker='o', markersize=4)
axes[0, 0].set_title('1. Line Plot', fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# 2. Scatter Plot
axes[0, 1].scatter(x, y, c=y, cmap='viridis', s=100, alpha=0.6, edgecolors='black')
axes[0, 1].set_title('2. Scatter Plot (with color)', fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# 3. Bar Plot
axes[0, 2].bar(categories, values, color='steelblue', edgecolor='black', linewidth=1.5)
axes[0, 2].set_title('3. Bar Plot', fontweight='bold')
axes[0, 2].set_ylabel('Values')

# 4. Horizontal Bar Plot
axes[1, 0].barh(categories, values, color='coral', edgecolor='black')
axes[1, 0].set_title('4. Horizontal Bar Plot', fontweight='bold')
axes[1, 0].set_xlabel('Values')

# 5. Histogram
data = np.random.normal(100, 15, 1000)
axes[1, 1].hist(data, bins=30, color='green', alpha=0.7, edgecolor='black')
axes[1, 1].set_title('5. Histogram', fontweight='bold')
axes[1, 1].set_xlabel('Value')
axes[1, 1].set_ylabel('Frequency')

# 6. Box Plot
data_box = [np.random.normal(0, std, 100) for std in range(1, 4)]
axes[1, 2].boxplot(data_box, labels=['Var 1', 'Var 2', 'Var 3'])
axes[1, 2].set_title('6. Box Plot', fontweight='bold')
axes[1, 2].set_ylabel('Value')

# 7. Area Plot
axes[2, 0].fill_between(x, y, y2, alpha=0.5, color='blue', label='sin vs cos')
axes[2, 0].plot(x, y, 'b-', label='sin(x)', linewidth=2)
axes[2, 0].plot(x, y2, 'r-', label='cos(x)', linewidth=2)
axes[2, 0].set_title('7. Area Plot', fontweight='bold')
axes[2, 0].legend()
axes[2, 0].grid(True, alpha=0.3)

# 8. Pie Chart
sizes = [30, 25, 20, 25]
labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
axes[2, 1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', 
               startangle=90, shadow=True)
axes[2, 1].set_title('8. Pie Chart', fontweight='bold')

# 9. Multiple Line Plot
axes[2, 2].plot(x, y, 'b-', linewidth=2, label='sin(x)', marker='o', markersize=3)
axes[2, 2].plot(x, y2, 'r-', linewidth=2, label='cos(x)', marker='s', markersize=3)
axes[2, 2].set_title('9. Multiple Lines', fontweight='bold')
axes[2, 2].legend()
axes[2, 2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# SECTION 3: COLORS, MARKERS, AND LINE STYLES

print("\nSECTION 3: COLORS, MARKERS, AND LINE STYLES\n")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Colors, Markers, and Line Styles', fontsize=16, fontweight='bold')

x = np.linspace(0, 10, 50)

# 3.1: Different Colors
ax = axes[0, 0]
ax.plot(x, np.sin(x), color='red', linewidth=2, label='red')
ax.plot(x, np.cos(x), color='blue', linewidth=2, label='blue')
ax.plot(x, np.sin(x) + 0.5, color='#FF6B6B', linewidth=2, label='hex color')
ax.plot(x, np.cos(x) - 0.5, color=(0.2, 0.8, 0.3), linewidth=2, label='RGB tuple')
ax.set_title('Different Color Types', fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

# 3.2: Different Markers
ax = axes[0, 1]
markers = ['o', 's', '^', 'v', 'D', '*', 'p', 'h', 'x', '+']
for i, marker in enumerate(markers):
    ax.plot(i, i, marker=marker, markersize=15, label=f"'{marker}'")
ax.set_title('Different Markers', fontweight='bold')
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 10)
ax.legend(ncol=2, fontsize=8)
ax.grid(True, alpha=0.3)

# 3.3: Different Line Styles
ax = axes[1, 0]
linestyles = ['-', '--', '-.', ':']
labels = ['solid (-)', 'dashed (--)', 'dashdot (-.)', 'dotted (:)']
for i, (ls, label) in enumerate(zip(linestyles, labels)):
    ax.plot(x, np.sin(x) + i*0.5, linestyle=ls, linewidth=3, label=label)
ax.set_title('Different Line Styles', fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

# 3.4: Combining Color, Marker, Line Style
ax = axes[1, 1]
ax.plot(x, np.sin(x), 'r-o', linewidth=2, markersize=6, label='red solid line + circle')
ax.plot(x, np.cos(x), 'b--s', linewidth=2, markersize=6, label='blue dashed + square')
ax.plot(x, np.tan(x % np.pi - np.pi/2), 'g:^', linewidth=2, markersize=6, label='green dotted + triangle')
ax.set_title('Combined Formatting', fontweight='bold')
ax.set_ylim(-3, 3)
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# SECTION 4: LABELS, TITLES, AND ANNOTATIONS

print("\nSECTION 4: LABELS, TITLES, AND ANNOTATIONS\n")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Labels, Titles, and Annotations', fontsize=16, fontweight='bold')

x = np.linspace(0, 10, 100)
y = np.sin(x)

# 4.1: Basic Labels and Title
ax = axes[0, 0]
ax.plot(x, y, 'b-', linewidth=2)
ax.set_xlabel('Time (seconds)', fontsize=11, fontweight='bold')
ax.set_ylabel('Amplitude', fontsize=11, fontweight='bold')
ax.set_title('Basic Labels and Title', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3)

# 4.2: Text Annotations
ax = axes[0, 1]
ax.plot(x, y, 'b-', linewidth=2)
# Add text at specific location
ax.text(2, 0.8, 'Peak Point', fontsize=10, ha='center', 
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
# Annotate with arrow
ax.annotate('Zero Crossing', xy=(np.pi, 0), xytext=(np.pi+1, -0.5),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, color='red', fontweight='bold')
ax.set_title('Annotations with Arrows', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3)

# 4.3: Axis Labels and Ticks
ax = axes[1, 0]
ax.plot(x, y, 'b-', linewidth=2)
# Custom x-axis labels
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'], fontsize=10)
# Custom y-axis labels
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticklabels(['-1.0', '-0.5', '0.0', '0.5', '1.0'], fontsize=10)
ax.set_xlabel('Angle (radians)', fontsize=11, fontweight='bold')
ax.set_ylabel('sin(x)', fontsize=11, fontweight='bold')
ax.set_title('Custom Ticks and Labels', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3)

# 4.4: Legend with Different Positions
ax = axes[1, 1]
ax.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
ax.plot(x, np.cos(x), 'r-', linewidth=2, label='cos(x)')
ax.plot(x, np.tan(x % np.pi - np.pi/2), 'g-', linewidth=2, label='tan(x)')
# Different legend locations
ax.legend(loc='upper right', fontsize=10, framealpha=0.9, shadow=True)
ax.set_title('Legend Positioning', fontsize=12, fontweight='bold')
ax.set_ylim(-3, 3)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# SECTION 5: SUBPLOTS AND LAYOUTS

print("\nSECTION 5: SUBPLOTS AND LAYOUTS\n")

# 5.1: Different Subplot Arrangements
fig = plt.figure(figsize=(15, 10))
fig.suptitle('Different Subplot Arrangements', fontsize=16, fontweight='bold')

# Arrangement 1: Regular grid
ax1 = plt.subplot(2, 3, 1)
ax1.plot(np.sin(np.linspace(0, 10, 100)))
ax1.set_title('Subplot (2,3,1)')

ax2 = plt.subplot(2, 3, 2)
ax2.plot(np.cos(np.linspace(0, 10, 100)))
ax2.set_title('Subplot (2,3,2)')

ax3 = plt.subplot(2, 3, 3)
ax3.plot(np.tan(np.linspace(0, 3, 100)))
ax3.set_title('Subplot (2,3,3)')

# Arrangement 2: Spanning subplots
ax4 = plt.subplot(2, 3, (4, 5))
ax4.bar(['A', 'B', 'C'], [10, 20, 15])
ax4.set_title('Subplot (2,3,(4,5)) - spanning 2 columns')

ax5 = plt.subplot(2, 3, 6)
ax5.scatter(np.random.rand(20), np.random.rand(20))
ax5.set_title('Subplot (2,3,6)')

plt.tight_layout()
plt.show()

# 5.2: Using GridSpec for Complex Layouts
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(14, 8))
gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)

# Large plot spanning 2x2
ax1 = fig.add_subplot(gs[0:2, 0:2])
ax1.plot(np.sin(np.linspace(0, 10, 100)), linewidth=2)
ax1.set_title('Large plot (0:2, 0:2)', fontweight='bold')

# Smaller plots
ax2 = fig.add_subplot(gs[0, 2])
ax2.plot(np.cos(np.linspace(0, 10, 100)))
ax2.set_title('Plot (0, 2)')

ax3 = fig.add_subplot(gs[1, 2])
ax3.scatter(np.random.rand(20), np.random.rand(20))
ax3.set_title('Plot (1, 2)')

ax4 = fig.add_subplot(gs[2, :])
ax4.bar(['A', 'B', 'C', 'D', 'E'], [10, 20, 15, 25, 18])
ax4.set_title('Bottom plot spanning all columns (2, :)', fontweight='bold')

fig.suptitle('Complex Layout using GridSpec', fontsize=16, fontweight='bold', y=0.995)
plt.show()

# SECTION 6: LEGENDS AND TEXT

print("\nSECTION 6: LEGENDS AND TEXT\n")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Legends and Text Formatting', fontsize=16, fontweight='bold')

x = np.linspace(0, 10, 100)

# 6.1: Basic Legend
ax = axes[0, 0]
ax.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
ax.plot(x, np.cos(x), 'r-', linewidth=2, label='cos(x)')
ax.plot(x, np.sin(2*x), 'g--', linewidth=2, label='sin(2x)')
ax.legend(loc='upper right', fontsize=10, title='Functions', title_fontsize=11)
ax.set_title('Basic Legend', fontweight='bold')
ax.grid(True, alpha=0.3)

# 6.2: Legend with Multiple Columns
ax = axes[0, 1]
for i in range(6):
    ax.plot(x, np.sin(x + i*np.pi/3), label=f'Line {i+1}')
ax.legend(loc='upper center', ncol=3, fontsize=9, 
          framealpha=0.9, shadow=True, borderpad=1)
ax.set_title('Legend with Multiple Columns', fontweight='bold')
ax.grid(True, alpha=0.3)

# 6.3: Text Box and Formatting
ax = axes[1, 0]
ax.plot(x, np.sin(x), 'b-', linewidth=2)
# Add text with different styles
textstr = 'This is a text box\nwith multiple lines\nand bold formatting'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax.text(0.5, 0.95, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='center', 
        bbox=props, fontweight='bold')
ax.set_title('Text Box with Formatting', fontweight='bold')
ax.grid(True, alpha=0.3)

# 6.4: Different Text Styles
ax = axes[1, 1]
ax.text(0.5, 0.9, 'Normal Text', ha='center', fontsize=12)
ax.text(0.5, 0.8, 'Bold Text', ha='center', fontsize=12, fontweight='bold')
ax.text(0.5, 0.7, 'Italic Text', ha='center', fontsize=12, style='italic')
ax.text(0.5, 0.6, 'Bold Italic', ha='center', fontsize=12, 
        fontweight='bold', style='italic')
ax.text(0.5, 0.5, 'Monospace Text', ha='center', fontsize=12, 
        family='monospace')
ax.text(0.5, 0.4, 'Colored Text', ha='center', fontsize=12, color='red')
ax.text(0.5, 0.3, 'Small Text', ha='center', fontsize=8)
ax.text(0.5, 0.2, 'Large Text', ha='center', fontsize=16)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Different Text Styles', fontweight='bold')

plt.tight_layout()
plt.show()

# SECTION 7: COLORMAPS AND COLOR NORMALIZATION

print("\nSECTION 7: COLORMAPS AND COLOR NORMALIZATION\n")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Colormaps and Color Normalization', fontsize=16, fontweight='bold')

# Create 2D data
X = np.linspace(-3, 3, 100)
Y = np.linspace(-3, 3, 100)
X_grid, Y_grid = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X_grid**2 + Y_grid**2))

# 7.1: Viridis Colormap
im1 = axes[0, 0].contourf(X_grid, Y_grid, Z, cmap='viridis')
axes[0, 0].set_title('Viridis Colormap')
plt.colorbar(im1, ax=axes[0, 0])

# 7.2: Plasma Colormap
im2 = axes[0, 1].contourf(X_grid, Y_grid, Z, cmap='plasma')
axes[0, 1].set_title('Plasma Colormap')
plt.colorbar(im2, ax=axes[0, 1])

# 7.3: Cool Colormap
im3 = axes[0, 2].contourf(X_grid, Y_grid, Z, cmap='cool')
axes[0, 2].set_title('Cool Colormap')
plt.colorbar(im3, ax=axes[0, 2])

# 7.4: Hot Colormap
im4 = axes[1, 0].contourf(X_grid, Y_grid, Z, cmap='hot')
axes[1, 0].set_title('Hot Colormap')
plt.colorbar(im4, ax=axes[1, 0])

# 7.5: RdBu Colormap (Red-Blue diverging)
im5 = axes[1, 1].contourf(X_grid, Y_grid, Z, cmap='RdBu')
axes[1, 1].set_title('RdBu Colormap (Diverging)')
plt.colorbar(im5, ax=axes[1, 1])

# 7.6: Scatter with colormap
scatter = axes[1, 2].scatter(X_grid.ravel(), Y_grid.ravel(), c=Z.ravel(), 
                              cmap='twilight', s=20, alpha=0.6)
axes[1, 2].set_title('Scatter with Twilight Colormap')
plt.colorbar(scatter, ax=axes[1, 2])

plt.tight_layout()
plt.show()

# SECTION 8: HEATMAPS AND 2D DATA VISUALIZATION

print("\nSECTION 8: HEATMAPS AND 2D DATA VISUALIZATION\n")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Heatmaps and 2D Data Visualization', fontsize=16, fontweight='bold')

# Create sample data
data = np.random.randn(10, 10)
data2 = np.random.randint(0, 100, (8, 8))

# 8.1: Heatmap using imshow
im1 = axes[0, 0].imshow(data, cmap='viridis', aspect='auto')
axes[0, 0].set_title('Heatmap using imshow')
plt.colorbar(im1, ax=axes[0, 0], label='Value')

# 8.2: Contour plot
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X_grid, Y_grid = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X_grid**2 + Y_grid**2))
contour = axes[0, 1].contour(X_grid, Y_grid, Z, levels=15, cmap='plasma')
axes[0, 1].clabel(contour, inline=True, fontsize=8)
axes[0, 1].set_title('Contour Plot')

# 8.3: Filled contour plot
contourf = axes[1, 0].contourf(X_grid, Y_grid, Z, levels=15, cmap='coolwarm')
axes[1, 0].set_title('Filled Contour Plot')
plt.colorbar(contourf, ax=axes[1, 0])

# 8.4: Heatmap with annotations
im4 = axes[1, 1].imshow(data2, cmap='YlOrRd', aspect='auto')
# Add text annotations
for i in range(data2.shape[0]):
    for j in range(data2.shape[1]):
        text = axes[1, 1].text(j, i, data2[i, j],
                              ha="center", va="center", color="black", fontsize=8)
axes[1, 1].set_title('Heatmap with Annotations')
axes[1, 1].set_xticks(np.arange(data2.shape[1]))
axes[1, 1].set_yticks(np.arange(data2.shape[0]))
plt.colorbar(im4, ax=axes[1, 1])

plt.tight_layout()
plt.show()

# SECTION 9: 3D PLOTTING

print("\nSECTION 9: 3D PLOTTING\n")

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(15, 10))
fig.suptitle('3D Plotting in Matplotlib', fontsize=16, fontweight='bold')

# 9.1: 3D Line Plot
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
t = np.linspace(0, 10, 100)
x = np.cos(t)
y = np.sin(t)
z = t
ax1.plot(x, y, z, 'b-', linewidth=2)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('3D Line Plot (Helix)')

# 9.2: 3D Scatter Plot
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
n = 100
xs = np.random.rand(n)
ys = np.random.rand(n)
zs = np.random.rand(n)
colors = np.random.rand(n)
scatter = ax2.scatter(xs, ys, zs, c=colors, cmap='viridis', s=50, alpha=0.6)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('3D Scatter Plot')
plt.colorbar(scatter, ax=ax2, shrink=0.5)

# 9.3: 3D Surface Plot
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)
X_grid, Y_grid = np.meshgrid(X, Y)
Z_grid = np.sin(np.sqrt(X_grid**2 + Y_grid**2))
surf = ax3.plot_surface(X_grid, Y_grid, Z_grid, cmap='coolwarm', alpha=0.8)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_title('3D Surface Plot')
plt.colorbar(surf, ax=ax3, shrink=0.5)

# 9.4: 3D Bar Plot
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
xpos = np.arange(5)
ypos = np.arange(5)
zpos = np.zeros(25)
dx = 0.8 * np.ones_like(zpos)
dy = 0.8 * np.ones_like(zpos)
dz = np.random.rand(25) * 10
colors_bar = plt.cm.viridis(np.linspace(0, 1, 25))
ax4.bar3d(xpos.repeat(5), np.tile(ypos, 5), zpos, dx, dy, dz, color=colors_bar)
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_title('3D Bar Plot')

plt.tight_layout()
plt.show()

# SECTION 10: SPECIAL PLOTS AND ADVANCED FEATURES

print("\nSECTION 10: SPECIAL PLOTS AND ADVANCED FEATURES\n")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Special Plots and Advanced Features', fontsize=16, fontweight='bold')

# 10.1: Violin Plot
ax = axes[0, 0]
data_violin = [np.random.normal(0, std, 100) for std in range(1, 4)]
parts = ax.violinplot(data_violin, positions=[1, 2, 3], showmeans=True, showmedians=True)
ax.set_title('Violin Plot')
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3'])

# 10.2: Hexbin Plot
ax = axes[0, 1]
x_hex = np.random.randn(1000)
y_hex = np.random.randn(1000)
hexbin = ax.hexbin(x_hex, y_hex, gridsize=20, cmap='YlOrRd', mincnt=1)
ax.set_title('Hexbin Plot')
plt.colorbar(hexbin, ax=ax, label='Count')

# 10.3: Streamplot
ax = axes[0, 2]
X = np.linspace(-3, 3, 100)
Y = np.linspace(-3, 3, 100)
X_grid, Y_grid = np.meshgrid(X, Y)
U = -1 - X_grid**2 + Y_grid
V = 1 + X_grid - Y_grid**2
ax.streamplot(X_grid, Y_grid, U, V, color=np.sqrt(U**2 + V**2), 
              cmap='viridis', linewidth=1)
ax.set_title('Streamplot (Vector Field)')

# 10.4: Stacked Bar Plot
ax = axes[1, 0]
categories = ['A', 'B', 'C', 'D']
values1 = [10, 20, 15, 25]
values2 = [15, 10, 20, 15]
values3 = [5, 15, 10, 10]
x_pos = np.arange(len(categories))
ax.bar(x_pos, values1, label='Series 1', color='steelblue')
ax.bar(x_pos, values2, bottom=values1, label='Series 2', color='coral')
ax.bar(x_pos, values3, bottom=np.array(values1)+np.array(values2), 
       label='Series 3', color='lightgreen')
ax.set_xticks(x_pos)
ax.set_xticklabels(categories)
ax.set_title('Stacked Bar Plot')
ax.legend()

# 10.5: Error Bar Plot
ax = axes[1, 1]
x_err = np.linspace(0, 10, 10)
y_err = np.sin(x_err)
error = 0.1 + 0.1 * np.random.rand(len(x_err))
ax.errorbar(x_err, y_err, yerr=error, fmt='o-', linewidth=2, 
            markersize=6, capsize=5, capthick=2, color='blue', 
            ecolor='red', label='Data with error')
ax.set_title('Error Bar Plot')
ax.legend()
ax.grid(True, alpha=0.3)

# 10.6: Stem Plot
ax = axes[1, 2]
x_stem = np.linspace(0, 10, 20)
y_stem = np.sin(x_stem)
markerline, stemlines, baseline = ax.stem(x_stem, y_stem, basefmt=' ')
markerline.set_markerfacecolor('red')
markerline.set_markeredgecolor('red')
markerline.set_markersize(8)
stemlines.set_color('blue')
stemlines.set_linewidth(2)
ax.set_title('Stem Plot')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# SECTION 11: STYLING AND THEMES

print("\nSECTION 11: STYLING AND THEMES\n")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Styling and Themes', fontsize=16, fontweight='bold')

x = np.linspace(0, 10, 100)
y = np.sin(x)

# 11.1: Different Styles
try:
    # Style 1: Default
    ax = axes[0, 0]
    ax.plot(x, y, linewidth=2, marker='o', markersize=4)
    ax.set_title('Default Style', fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Style 2: Dark background
    ax = axes[0, 1]
    ax.plot(x, y, 'y-', linewidth=2, marker='s', markersize=4)
    ax.set_facecolor('#1a1a1a')
    ax.set_title('Dark Background', fontweight='bold', color='white')
    ax.tick_params(colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, color='white')
    
    # Style 3: No spine
    ax = axes[1, 0]
    ax.plot(x, y, 'g-', linewidth=3, marker='^', markersize=5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title('No Top/Right Spine', fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    # Style 4: Minimal
    ax = axes[1, 1]
    ax.plot(x, y, 'r-', linewidth=2.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('Minimal Style', fontweight='bold')
    
except Exception as e:
    print(f"Style error: {e}")

plt.tight_layout()
plt.show()

# SECTION 12: FIGURE SIZE, DPI, AND SAVING

print("\nSECTION 12: FIGURE SIZE, DPI, AND SAVING\n")

# Different figure sizes
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Different Figure Sizes and DPI', fontsize=16, fontweight='bold')

x = np.linspace(0, 10, 100)

# 12.1: Small figure
ax = axes[0, 0]
ax.plot(x, np.sin(x), 'b-', linewidth=2)
ax.set_title('Small Figure (figsize=(4,3))', fontweight='bold')
ax.grid(True, alpha=0.3)

# 12.2: Large figure
ax = axes[0, 1]
ax.plot(x, np.cos(x), 'r-', linewidth=2)
ax.set_title('Large Figure (figsize=(10,8))', fontweight='bold')
ax.grid(True, alpha=0.3)

# 12.3: Wide figure
ax = axes[1, 0]
ax.plot(x, np.sin(2*x), 'g-', linewidth=2)
ax.set_title('Wide Figure (figsize=(12,4))', fontweight='bold')
ax.grid(True, alpha=0.3)

# 12.4: Tall figure
ax = axes[1, 1]
ax.plot(x, np.cos(2*x), 'm-', linewidth=2)
ax.set_title('Tall Figure (figsize=(6,10))', fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Save figure (commented out as per your preference)
# plt.savefig('figure.png', dpi=300, bbox_inches='tight')  # High DPI PNG
# plt.savefig('figure.pdf', bbox_inches='tight')           # PDF format
# plt.savefig('figure.jpg', dpi=150, bbox_inches='tight')  # JPG format

# SECTION 13: ANIMATION AND INTERACTIVE PLOTS

print("\nSECTION 13: ANIMATION BASICS\n")

# Note: Animation requires specific setup and is shown as code example
animation_code = """
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(10, 6))

# Initialize
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.grid(True, alpha=0.3)

# Animation function
def animate(frame):
    y = np.sin(x + frame * 0.1)
    line.set_data(x, y)
    ax.set_title(f'Frame: {frame}')
    return line,

# Create animation
anim = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()
"""
print(animation_code)

# SECTION 14: HISTOGRAM WITH STATISTICS

print("\nSECTION 14: HISTOGRAM WITH STATISTICS\n")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Histograms with Statistical Information', fontsize=16, fontweight='bold')

# Generate data
data = np.random.normal(100, 15, 1000)

# 14.1: Simple histogram
ax = axes[0, 0]
ax.hist(data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
ax.axvline(np.mean(data), color='red', linestyle='--', linewidth=2, label=f'Mean: {np.mean(data):.1f}')
ax.axvline(np.median(data), color='green', linestyle='--', linewidth=2, label=f'Median: {np.median(data):.1f}')
ax.set_title('Histogram with Mean and Median')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# 14.2: Histogram with distribution curve
ax = axes[0, 1]
n, bins, patches = ax.hist(data, bins=30, color='coral', alpha=0.7, edgecolor='black', density=True)
# Fit normal distribution
from scipy import stats
mu, sigma = np.mean(data), np.std(data)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
ax.plot(x, stats.norm.pdf(x, mu, sigma), 'k-', linewidth=2, label='Normal Distribution')
ax.set_title('Histogram with Distribution Curve')
ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# 14.3: Multiple histograms
ax = axes[1, 0]
data1 = np.random.normal(100, 10, 500)
data2 = np.random.normal(110, 15, 500)
ax.hist(data1, bins=25, alpha=0.6, label='Distribution 1', color='blue', edgecolor='black')
ax.hist(data2, bins=25, alpha=0.6, label='Distribution 2', color='red', edgecolor='black')
ax.set_title('Multiple Histograms Overlay')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# 14.4: Cumulative histogram
ax = axes[1, 1]
ax.hist(data, bins=30, cumulative=True, color='green', alpha=0.7, 
        edgecolor='black', label='Cumulative')
ax.set_title('Cumulative Histogram')
ax.set_xlabel('Value')
ax.set_ylabel('Cumulative Frequency')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# SECTION 15: TIME SERIES PLOTTING

print("\nSECTION 15: TIME SERIES PLOTTING\n")

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Time Series Plotting', fontsize=16, fontweight='bold')

# Create time series data
dates = pd.date_range('2024-01-01', periods=365, freq='D')
values = np.cumsum(np.random.randn(365)) + 100
df = pd.DataFrame({'Date': dates, 'Value': values})

# 15.1: Simple time series
ax = axes[0, 0]
ax.plot(df['Date'], df['Value'], 'b-', linewidth=2)
ax.set_title('Simple Time Series')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.grid(True, alpha=0.3)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

# 15.2: Time series with fill
ax = axes[0, 1]
ax.fill_between(df['Date'], df['Value'], alpha=0.3, color='skyblue')
ax.plot(df['Date'], df['Value'], 'b-', linewidth=2, label='Price')
ax.set_title('Time Series with Fill')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.legend()
ax.grid(True, alpha=0.3)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

# 15.3: Multiple time series
ax = axes[1, 0]
ax.plot(df['Date'], df['Value'], 'b-', linewidth=2, label='Series 1')
ax.plot(df['Date'], df['Value'] + 5, 'r-', linewidth=2, label='Series 2')
ax.plot(df['Date'], df['Value'] - 5, 'g-', linewidth=2, label='Series 3')
ax.set_title('Multiple Time Series')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.legend()
ax.grid(True, alpha=0.3)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

# 15.4: Time series with moving average
ax = axes[1, 1]
window = 30
moving_avg = df['Value'].rolling(window=window).mean()
ax.plot(df['Date'], df['Value'], 'b-', alpha=0.5, linewidth=1, label='Original')
ax.plot(df['Date'], moving_avg, 'r-', linewidth=2.5, label=f'{window}-day Moving Average')
ax.fill_between(df['Date'], df['Value'], alpha=0.2, color='skyblue')
ax.set_title('Time Series with Moving Average')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.legend()
ax.grid(True, alpha=0.3)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

plt.tight_layout()
plt.show()

# SECTION 16: CORRELATION HEATMAP

print("\nSECTION 16: CORRELATION HEATMAP\n")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Correlation Matrix Heatmap', fontsize=16, fontweight='bold')

# Create sample data
data = np.random.randn(100, 5)
df = pd.DataFrame(data, columns=['Var1', 'Var2', 'Var3', 'Var4', 'Var5'])
correlation_matrix = df.corr()

# 16.1: Basic correlation heatmap
ax = axes[0]
im = ax.imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1, aspect='auto')
ax.set_xticks(np.arange(len(correlation_matrix.columns)))
ax.set_yticks(np.arange(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns, rotation=45)
ax.set_yticklabels(correlation_matrix.columns)
ax.set_title('Correlation Heatmap')
# Add text annotations
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        text = ax.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                      ha="center", va="center", color="black", fontsize=10)
plt.colorbar(im, ax=ax)

# 16.2: Alternative representation with squares
ax = axes[1]
im = ax.imshow(correlation_matrix, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
ax.set_xticks(np.arange(len(correlation_matrix.columns)))
ax.set_yticks(np.arange(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns, rotation=45)
ax.set_yticklabels(correlation_matrix.columns)
ax.set_title('Correlation Heatmap (RdBu)')
# Add circle markers for stronger correlations
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        corr_val = correlation_matrix.iloc[i, j]
        if abs(corr_val) > 0.7:
            circle = plt.Circle((j, i), 0.25, color='black', fill=False, linewidth=2)
            ax.add_patch(circle)
plt.colorbar(im, ax=ax)

plt.tight_layout()
plt.show()

# SECTION 17: CUSTOM FIGURE AND AXES

print("\nSECTION 17: CUSTOM FIGURE AND AXES\n")

# Create custom figure with tight layout
fig = plt.figure(figsize=(14, 8))
fig.patch.set_facecolor('#f0f0f0')  # Set background color

# Add title to figure
fig.suptitle('Custom Figure and Axes Formatting', fontsize=18, fontweight='bold', y=0.98)

# Create axes with custom positions
ax1 = fig.add_axes([0.1, 0.5, 0.35, 0.4])  # [left, bottom, width, height]
ax2 = fig.add_axes([0.55, 0.5, 0.35, 0.4])
ax3 = fig.add_axes([0.1, 0.05, 0.8, 0.35])

# Plot in ax1
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), 'b-', linewidth=2.5)
ax1.set_title('Sine Wave', fontweight='bold', fontsize=12)
ax1.set_xlabel('X')
ax1.set_ylabel('sin(X)')
ax1.grid(True, alpha=0.3)
ax1.set_facecolor('#ffffcc')

# Plot in ax2
ax2.plot(x, np.cos(x), 'r-', linewidth=2.5)
ax2.set_title('Cosine Wave', fontweight='bold', fontsize=12)
ax2.set_xlabel('X')
ax2.set_ylabel('cos(X)')
ax2.grid(True, alpha=0.3)
ax2.set_facecolor('#e6f3ff')

# Plot in ax3
categories = ['A', 'B', 'C', 'D', 'E']
values = [20, 35, 30, 45, 40]
bars = ax3.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'],
               edgecolor='black', linewidth=2, alpha=0.8)
ax3.set_title('Bar Chart', fontweight='bold', fontsize=12)
ax3.set_ylabel('Values')
ax3.set_ylim(0, 50)
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}', ha='center', va='bottom', fontweight='bold')
ax3.grid(True, alpha=0.3, axis='y')

plt.show()

# SECTION 18: DUAL AXIS PLOTTING

print("\nSECTION 18: DUAL AXIS PLOTTING\n")

fig, ax1 = plt.subplots(figsize=(12, 6))
fig.suptitle('Dual Axis Plotting', fontsize=14, fontweight='bold')

# Data 1
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
color1 = 'tab:blue'
ax1.set_xlabel('X', fontweight='bold')
ax1.set_ylabel('sin(x)', color=color1, fontweight='bold')
line1 = ax1.plot(x, y1, color=color1, linewidth=2.5, label='sin(x)')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, alpha=0.3)

# Create second axis
ax2 = ax1.twinx()
y2 = np.exp(-x/5) * np.cos(2*x)
color2 = 'tab:red'
ax2.set_ylabel('exp(-x/5)·cos(2x)', color=color2, fontweight='bold')
line2 = ax2.plot(x, y2, color=color2, linewidth=2.5, label='exp(-x/5)·cos(2x)')
ax2.tick_params(axis='y', labelcolor=color2)

# Combine legends
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=11)

plt.tight_layout()
plt.show()

# SECTION 19: QUANTILE-QUANTILE PLOT (Q-Q Plot)

print("\nSECTION 19: Q-Q PLOT AND PROBABILITY PLOTS\n")

from scipy import stats

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Q-Q Plots and Probability Plots', fontsize=14, fontweight='bold')

# 19.1: Normal distribution Q-Q plot
ax = axes[0, 0]
data_normal = np.random.normal(0, 1, 1000)
stats.probplot(data_normal, dist="norm", plot=ax)
ax.set_title('Q-Q Plot (Normal Data)')

# 19.2: Skewed distribution Q-Q plot
ax = axes[0, 1]
data_skewed = np.random.exponential(2, 1000)
stats.probplot(data_skewed, dist="norm", plot=ax)
ax.set_title('Q-Q Plot (Skewed Data)')

# 19.3: Probability plot
ax = axes[1, 0]
data = np.random.normal(100, 15, 1000)
stats.probplot(data, dist="norm", plot=ax)
ax.set_title('Probability Plot (Normal Data)')

# 19.4: Compare two distributions
ax = axes[1, 1]
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(0.5, 1.2, 1000)
stats.probplot(data1, dist="norm", plot=ax)
ax.scatter(stats.norm.ppf(np.linspace(0.01, 0.99, len(data2))), 
          np.sort(data2), alpha=0.5, color='red', label='Another Distribution')
ax.set_title('Comparing Distributions')
ax.legend()

plt.tight_layout()
plt.show()

# SECTION 20: SUMMARY AND BEST PRACTICES

print("\n" + "=" * 80)
print("SECTION 20: MATPLOTLIB BEST PRACTICES SUMMARY")
print("=" * 80)

best_practices = """
1. FIGURE AND AXES:
   - Use fig, ax = plt.subplots() for better control
   - Always specify figsize for consistency
   
2. LABELS AND TITLES:
   - Always include axis labels with fontsize
   - Use descriptive titles
   - Include units in labels
   
3. LEGENDS:
   - Place legends where they don't obscure data
   - Use descriptive labels
   - Set ncol for space efficiency
   
4. GRID:
   - Use grid() with alpha=0.3 for readability
   - Set axis='both' or 'y' based on needs
   
5. COLORS:
   - Use colormaps for multi-series plots
   - Ensure colorblind-friendly palettes
   - Use colorbar() when using colormaps
   
6. DATA VISUALIZATION:
   - Choose appropriate plot type for data
   - Avoid cluttering with too many series
   - Use different styles (line, marker) for distinction
   
7. SAVING FIGURES:
   - Save with dpi=300 for publications
   - Use bbox_inches='tight' to remove whitespace
   - Prefer PNG/PDF for quality
   
8. PERFORMANCE:
   - Use scatter() for <10k points
   - Use hexbin() for >10k points
   - Limit animation frame rate for smooth playback
   
9. ACCESSIBILITY:
   - Use sufficient contrast
   - Include colorblind-friendly colors
   - Add text descriptions for plots
   
10. STYLING:
    - Use consistent font throughout
    - Remove unnecessary spines
    - Use minimal colors for cleaner look
"""

print(best_practices)

# FINAL EXAMPLE: COMPLETE DASHBOARD-LIKE PLOT

print("\nFINAL EXAMPLE: COMPLETE DASHBOARD\n")

from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(16, 10))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.3)

fig.suptitle('Complete Matplotlib Dashboard Example', fontsize=18, fontweight='bold', y=0.98)

# Generate data
dates = pd.date_range('2024-01-01', periods=100, freq='D')
sales = np.cumsum(np.random.randn(100)) + 1000
categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Sports']
category_values = [30, 25, 20, 15, 10]
monthly_data = np.random.randn(12, 5)

# 1. Main time series
ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(dates, sales, 'b-', linewidth=2.5)
ax1.fill_between(dates, sales, alpha=0.3)
ax1.set_title('Sales Trend Over Time', fontweight='bold', fontsize=12)
ax1.set_ylabel('Sales ($)')
ax1.grid(True, alpha=0.3)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# 2. KPI Box
ax2 = fig.add_subplot(gs[0, 2])
ax2.text(0.5, 0.7, 'Total Sales', ha='center', fontsize=14, fontweight='bold')
ax2.text(0.5, 0.4, f'${sales[-1]:.0f}', ha='center', fontsize=24, 
         fontweight='bold', color='green')
ax2.text(0.5, 0.1, f'Growth: {((sales[-1]-sales[0])/sales[0]*100):.1f}%', 
         ha='center', fontsize=11, color='blue')
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')
ax2.set_facecolor('#f0f0f0')

# 3. Category distribution
ax3 = fig.add_subplot(gs[1, 0])
colors_pie = plt.cm.Set3(np.linspace(0, 1, len(categories)))
ax3.pie(category_values, labels=categories, autopct='%1.1f%%', colors=colors_pie,
        startangle=90, explode=[0.05]*len(categories))
ax3.set_title('Sales by Category', fontweight='bold', fontsize=11)

# 4. Category comparison
ax4 = fig.add_subplot(gs[1, 1:])
x_pos = np.arange(len(categories))
bars = ax4.bar(x_pos, category_values, color=colors_pie, edgecolor='black', 
               linewidth=1.5, alpha=0.8)
ax4.set_xticks(x_pos)
ax4.set_xticklabels(categories)
ax4.set_ylabel('Sales (%)')
ax4.set_title('Sales Distribution by Category', fontweight='bold', fontsize=12)
ax4.grid(True, alpha=0.3, axis='y')
# Add value labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}%', ha='center', va='bottom', fontweight='bold')

# 5. Heatmap
ax5 = fig.add_subplot(gs[2, :2])
im = ax5.imshow(monthly_data, cmap='YlOrRd', aspect='auto')
ax5.set_xlabel('Month')
ax5.set_ylabel('Product Line')
ax5.set_title('Monthly Performance Heatmap', fontweight='bold', fontsize=11)
plt.colorbar(im, ax=ax5, label='Performance')

# 6. Statistics box
ax6 = fig.add_subplot(gs[2, 2])
stats_text = f"""
Statistics:
Mean: ${np.mean(sales):.0f}
Median: ${np.median(sales):.0f}
Std Dev: ${np.std(sales):.0f}
Min: ${np.min(sales):.0f}
Max: ${np.max(sales):.0f}
"""
ax6.text(0.05, 0.95, stats_text, transform=ax6.transAxes, 
        fontsize=10, verticalalignment='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
ax6.axis('off')

plt.show()

print("\n" + "=" * 80)
print("MATPLOTLIB TUTORIAL COMPLETE!")
print("=" * 80)
print("\nKey Takeaways:")
print("✓ Created 20 different plot types")
print("✓ Learned about styling and customization")
print("✓ Explored advanced features like 3D plots and annotations")
print("✓ Practiced best practices for data visualization")
print("✓ Built a complete dashboard example")
print("\nFor more information, visit: https://matplotlib.org/")