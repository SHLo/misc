import sys
import codecs

def main():
    try:
        file_in = sys.argv[1]
        file_out = sys.argv[2]
    except Exception:
        print('usage: python big5_to_utf8.py ${file_in} ${file_out}')
        return

    with codecs.open(file_in, 'r', 'big5') as source:
        content = source.read()

    with codecs.open(file_out, 'w', 'utf-8') as target:
        target.write(content)

main()
