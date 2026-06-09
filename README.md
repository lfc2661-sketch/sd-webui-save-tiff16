# sd-webui-save-tiff16

WebUI で生成した画像を TIFF 16bit 形式でも自動保存する拡張機能です。  
An extension that automatically saves generated images as TIFF 16-bit files.

---

## 概要 / Overview

通常の PNG 保存に加えて、TIFF 16bit ファイルを同じフォルダに追加保存します。  
Lightroom や Photoshop でのトーンカーブ調整など、後処理時の階調破綻（バンディング）を軽減できます。

In addition to the standard PNG output, this extension saves a TIFF 16-bit file in the same folder.  
This helps reduce banding and tonal breakup when applying tone curves in Lightroom or Photoshop.

> **注意 / Note:**  
> この TIFF は PNG（8bit）をスケールアップ変換したものです。実際のダイナミックレンジは増えません。  
> This TIFF is an upscaled conversion of the 8-bit PNG. Actual dynamic range does not increase.

---

## 動作環境 / Requirements

- Stable Diffusion WebUI Forge Neo（A1111系）
- Python 3.11 以上 / Python 3.11 or later
- imageio
- numpy, Pillow（WebUI に同梱 / bundled with WebUI）

---

## インストール / Installation

**1. フォルダ構成 / Folder structure**

```
extensions/
└── sd-webui-save-tiff16/
    └── scripts/
        └── save_tiff16.py
```

**2. imageio をインストール / Install imageio**

```
venv\Scripts\pip.exe install imageio
```

**3. WebUI を再起動 / Restart WebUI**

---

## 使い方 / How to Use

1. txt2img または img2img タブを開く / Open txt2img or img2img tab
2. ページ下部の「スクリプト」から **Save as TIFF 16bit** を選択 / Select **Save as TIFF 16bit** from the Scripts dropdown
3. 「TIFF 16bit でも保存する」をチェック / Check the checkbox
4. 通常通り生成 / Generate as usual
5. PNG と同じフォルダに `.tiff` が保存される / A `.tiff` file is saved alongside the PNG

---

## 出力ファイル / Output

| 項目 | 内容 |
|---|---|
| 保存先 / Location | PNG と同じフォルダ / Same folder as PNG |
| ファイル名 / Filename | `{seed}.tiff` |
| 形式 / Format | RGB TIFF 16-bit (uint16) |

---

## License

MIT
