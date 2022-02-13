import io

import numpy as np
from PIL import Image


def image_grid(images, pad=10):
    rows = len(images)
    cols = max([len(lst) for lst in images])
    for i in range(rows):
        for j in range(cols):
            if isinstance(images[i][j], np.ndarray):
                images[i][j] = Image.fromarray(images[i][j])

    widths = np.array([[(i.width if i else 0) for i in lst] for lst in images])
    heights = np.array([[(i.height if i else 0) for i in lst] for lst in images])

    col_w = widths.max(axis=0)
    row_h = heights.max(axis=1)

    full_w = col_w.sum() + (cols - 1) * pad
    full_h = row_h.sum() + (rows - 1) * pad

    new_image = Image.new("RGBA", (full_w, full_h))
    for ir, row in enumerate(images):
        for ic, img in enumerate(row):
            if img is None:
                continue
            x = np.hstack(([0], col_w))[: ic + 1].sum() + ic * pad
            y = np.hstack(([0], row_h))[: ir + 1].sum() + ir * pad
            new_image.paste(img, (x, y))

    return new_image


def fig_to_pil(fig):
    fig_bytes = fig.to_image(format="png")
    buf = io.BytesIO(fig_bytes)
    return Image.open(buf)
