# N개의 정수입력 그중 최대 최소 출력

import sys

N = int(sys.stdin.readline().strip())
a=list(map(int,sys.stdin.readline().strip().split()))

print(min(a),max(a))
