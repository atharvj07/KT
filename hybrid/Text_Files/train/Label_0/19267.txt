#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

#define SIZE 300000
#define INF 1000000000

int blockState[SIZE];
int blockL[SIZE], blockR[SIZE];
int item[SIZE];
int rN;

void applyBlock(int id, int x) {
  if (blockState[id] == 0) {
    blockL[id] = blockR[id] = x;
    blockState[id] = 1;
  }
  else if (blockState[id] == 1) {
    if (blockR[id] + 1 == x)
      blockR[id] = x;
    else
      blockState[id] = 2;
  }
}

void applyNode(int pos, int x) {
  int id = pos / rN;
  int l = id * rN;
  int r = (id + 1) * rN;

  if (blockState[id] == 1) {
    for (int i=l; i<r; i++) {
      if (item[i] + 1 == blockL[id])
        item[i] = blockR[id];
      else
        item[i] = INF;
    }
    blockState[id] = 0;
  }

  if (blockState[id] == 2) {
    for (int i=l; i<r; i++)
      item[i] = INF;
    blockState[id] = 0;
  }

  if (x == -1) return;

  if (item[pos] + 1 == x) {
    item[pos] = x;
  } else {
    item[pos] = INF;
  }
}

int main() {
  int N, K, T;

  scanf("%d%d%d", &N, &K, &T);

  rN = sqrt(N);

  int blockSize = (N + rN-1) / rN;

  for (int i=0; i<blockSize; i++) {
    blockL[i] = -1;
    blockR[i] = -1;
  }

  for (int i=0; i<T; i++) {
    int l, r, x;
    scanf("%d%d%d", &l, &r, &x);
    l--;

    //[l, r)
    for (int i=l; i<(l/rN+1)*rN; i++)
      if (i < r)
        applyNode(i, x);

    for (int i=r/rN*rN; i<r; i++)
      if (i >= (l/rN+1)*rN)
        applyNode(i, x);

    for (int i=l/rN+1; i<r/rN; i++)
      applyBlock(i, x);
  }

  for (int i=0; i<blockSize; i++)
    applyNode(i*rN, -1);

  int ans = 0;

  for (int i=0; i<N; i++)
    ans += item[i] == K;

  printf("%d\n", ans);

  return 0;
}

