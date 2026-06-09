================================================================
 sd-webui-save-tiff16  拡張機能 説明書 / Extension Manual
================================================================

【概要 / Overview】

日本語:
  WebUI で生成した画像を、通常の PNG に加えて
  TIFF 16bit 形式でも自動保存する拡張機能です。

English:
  This extension automatically saves generated images
  as TIFF 16-bit files in addition to the standard PNG output.

----------------------------------------------------------------

【動作環境 / Requirements】

  - Stable Diffusion WebUI Forge Neo（A1111系 WebUI）
  - Python 3.11 以上 / Python 3.11 or later
  - imageio（pip install imageio）
  - numpy, Pillow（WebUI に同梱 / bundled with WebUI）

----------------------------------------------------------------

【インストール方法 / Installation】

日本語:
  1. 以下のフォルダ構成を WebUI の extensions フォルダに作成する

       extensions\
       └── sd-webui-save-tiff16\
           └── scripts\
               └── save_tiff16.py

  2. imageio をインストールする

       venv\Scripts\pip.exe install imageio

  3. WebUI を再起動する

English:
  1. Create the following folder structure inside the
     WebUI's extensions folder:

       extensions\
       └── sd-webui-save-tiff16\
           └── scripts\
               └── save_tiff16.py

  2. Install imageio:

       venv\Scripts\pip.exe install imageio

  3. Restart WebUI.

----------------------------------------------------------------

【使い方 / How to Use】

日本語:
  1. txt2img または img2img 画面を開く
  2. ページ下部の「スクリプト」ドロップダウンから
     「Save as TIFF 16bit」を選択する
  3. 「TIFF 16bit でも保存する」チェックボックスをONにする
  4. 通常通り画像を生成する
  5. PNG と同じフォルダに .tiff ファイルが追加保存される

English:
  1. Open the txt2img or img2img tab.
  2. Select "Save as TIFF 16bit" from the Scripts dropdown
     at the bottom of the page.
  3. Check the "TIFF 16bit でも保存する" checkbox.
  4. Generate images as usual.
  5. A .tiff file will be saved alongside the PNG output.

----------------------------------------------------------------

【TIFF 16bit について / About TIFF 16-bit】

日本語:
  この拡張機能が保存する TIFF 16bit は、
  PNG（8bit）をスケールアップ変換したものです。

  ・得られるメリット
    - Lightroom や Photoshop でトーンカーブを大きく動かしても
      階調の破綻（バンディング）が出にくくなる
    - 明暗・色調整の編集余地が増える

  ・増えないもの
    - 実際の情報量やダイナミックレンジ
    - ディテールや色域
    ※ AI が 8bit で生成した時点で情報量の上限は決まっています。
      あくまで「後処理に強い器」を用意するための変換です。

English:
  The TIFF 16-bit file saved by this extension is an
  upscaled conversion of the original 8-bit PNG.

  Benefits:
    - Reduces banding and tonal breakup when applying
      heavy tone curves in Lightroom or Photoshop.
    - Provides more headroom for brightness and color edits.

  What does NOT increase:
    - Actual dynamic range or image information.
    - Detail or color gamut.
    Note: The information ceiling is set at generation time
    (8-bit). This conversion simply provides a more
    edit-friendly container for post-processing.

----------------------------------------------------------------

【出力ファイルについて / Output Files】

日本語:
  保存先: PNG と同じフォルダ（outputs\txt2img-images 等）
  ファイル名: {シード値}.tiff
  形式: RGB TIFF 16bit（uint16）

English:
  Location : Same folder as PNG (e.g. outputs\txt2img-images)
  Filename : {seed}.tiff
  Format   : RGB TIFF 16-bit (uint16)

----------------------------------------------------------------

【注意事項 / Notes】

日本語:
  - PNG ファイルは削除されません。両方が保存されます。
  - チェックボックスが OFF の場合は TIFF は保存されません。
  - スクリプトを選択し忘れると動作しません。

English:
  - PNG files are NOT deleted; both files are saved.
  - TIFF is not saved if the checkbox is unchecked.
  - The script must be selected from the dropdown to work.

----------------------------------------------------------------

【バージョン / Version】

  1.0.0  初版 / Initial release

================================================================
