import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
x = np.linspace(-2.5, 2.5, 300); y = np.linspace(-2.5, 2.5, 300)
X, Y = np.meshgrid(x, y); Z = X**2 + Y**2
fig = plt.figure(figsize=(10, 7)); ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none", alpha=0.85)
ax.contourf(X, Y, Z, zdir='z', offset=0, cmap="viridis", levels=30, alpha=0.9)
fig.colorbar(surf, ax=ax, shrink=0.6, aspect=10, pad=0.1, label="værdi af f(x,y)")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.view_init(elev=25, azim=35); ax.set_zlim(0, Z.max())
plt.tight_layout(); fig.savefig("figure/da/contour_da.png", dpi=150, bbox_inches="tight")
