# PDF Parser

PDF に埋め込まれた画像オブジェクトを OCR で処理して、日本語テキストを取り出します。

## セットアップ

### OCR engine (Tesseract)

OCR には [Tesseract](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file) を利用します。利用している OS と利用したい言語に応じて Tesseract をインストールしてください。以下は Ubuntu 24.04 で日本語を OCR する場合の例です。

```shell
sudo apt -y install tesseract-ocr tesseract-ocr-jpn libtesseract-dev libleptonica-dev tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert
```

### pip

Python の外部ライブラリ pyocr, pypdf, PIL (pillow) を利用します。 requirements.txt に必要なライブラリは列挙済みなので、下記でインストールできます。

```shell
pip install -r requirements.txt
```

## pdf からテキストを抜き出す

```extract_text_from_pdf.py``` は

* pdf 内の画像オブジェクトを取り出す
* OCR で画像オブジェクトから日本語テキストを取り出す
* 日本語テキストを標準出力に出力する

という処理を行います。

```shell
python extract_text_from_pdf.py input.py > result.md
```

とすると、処理結果を ```result.md``` に保存します。
入力 pdf ファイルのページ数や環境に応じて処理時間が長くなります。

処理結果は

```text
# input.pdf

## page.1

OCR で読み取った日本語テキスト

## page.2

...

## page.n

...
```

のように、マークダウン形式でページごとに OCR で読み取った結果が記載されます。

## テキストからカタカナの単語を抜き出す

前段の [pdf からテキストを抜き出す](#pdf-からテキストを抜き出す) で保存したテキストファイルを入力として、カタカナの単語を抜き出します。

```shell
python extract_katakana.py result.txt > katakana.txt
```

とすると、処理結果を ```katakana.txt``` に保存します。

処理結果は

```text
# input.pdf

## page.1

アアアア
イイイイ
ウウウウ
アアアア

## page.2

...

## page.n

...

## 一覧

アアアア
イイイイ
ウウウウ
...

```

のように

* ページごとのカタカナの単語を改行区切りで出力
* 最後に「一覧」として重複を除いたカタカナの単語を改行区切りで出力

としてまとめています。
