import re
import sys

def main():
    argv = sys.argv
    if len(argv) < 2:
        sys.stderr.write('python {} input.txt'.format(argv[0]))
        return

    p = re.compile('[\u30A1-\u30FF]+') # katakana
    s = set()
    texts = []
    with open(argv[1], 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            if line.startswith('#'):
                if len(texts) > 0:
                    text = ''.join(texts)
                    texts = []
                    results = p.findall(text)
                    if len(results) > 0:
                        print('\n'.join(results))
                    for result in results:
                        s.add(result)
                print('\n' + line)
            else:
                texts.append(line.replace('\n', ''))

    if len(texts) > 0:
        text = ''.join(texts)
        results = p.findall(text)
        if len(results) > 0:
            print('\n'.join(results))
        for result in results:
            s.add(result)

    print("\n## 一覧\n")
    print('\n'.join(s))


if __name__ == '__main__':
    main()
