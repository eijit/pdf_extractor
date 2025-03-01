import re
import sys

def main():
    argv = sys.argv
    if len(argv) < 2:
        sys.stderr.write('python {} input.txt'.format(argv[0]))
        return

    p = re.compile('[\u30A1-\u30FF]+') # katakana
    s = set()
    with open(argv[1], 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            if line.startswith('#'):
                print('\n' + line)
                continue
            results = p.findall(line)
            if len(results) > 0:
                print('\n'.join(results))
            for result in results:
                s.add(result)

    print("\n## 一覧\n")
    print('\n'.join(s))


if __name__ == '__main__':
    main()
