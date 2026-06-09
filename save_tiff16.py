import modules.scripts as scripts
import gradio as gr
import numpy as np
import imageio
from PIL import Image
import os

class SaveTiff16Script(scripts.Script):

    def title(self):
        return "Save as TIFF 16bit"

    def show(self, is_img2img):
        return True

    def ui(self, is_img2img):
        enabled = gr.Checkbox(
            label="TIFF 16bit でも保存する",
            value=False
        )
        return [enabled]

    def run(self, p, enabled):
        from modules.processing import process_images
        processed = process_images(p)

        if not enabled:
            return processed

        print(f"[TIFF16] 変換開始 画像数={len(processed.images)}")

        for i, image in enumerate(processed.images):
            if not isinstance(image, Image.Image):
                continue

            arr = np.array(image.convert("RGB"), dtype=np.uint16)
            arr_16 = arr * 257

            save_dir = p.outpath_samples
            tiff_path = os.path.join(save_dir, f"{processed.seed + i}.tiff")

            os.makedirs(save_dir, exist_ok=True)
            imageio.imwrite(tiff_path, arr_16)
            print(f"[TIFF16] 保存: {tiff_path}")

        return processed