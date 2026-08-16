#include <iostream>
#include <algorithm>
using namespace std;

const int H = 10;
const int W = 10;
int G[H][W];
int ans[H][W];

void put(int i, int j) {
  const static int di[5] = {0,1,0,-1,0};
  const static int dj[5] = {1,0,-1,0,0};
  for(int k = 0; k < 5; ++k) {
    int ni = i + di[k];
    int nj = j + dj[k];
    if(ni < 0 || ni >= H) continue;
    if(nj < 0 || nj >= W) continue;
    G[ni][nj] ^= 1;
  }
}

bool rec(int i, int j) {
  if(j == W) {
    ++i;
    j = 0;
  }

  if(i == H) {
    for(int j = 0; j < W; ++j) {
      if(G[H-1][j]) return false;
    }
    return true;
  }

  if(i == 0) {
    ans[i][j] = 0;
    if(rec(i, j+1)) return true;
    ans[i][j] = 1;
    put(i, j);
    if(rec(i, j+1)) return true;
    put(i, j);
  } else {
    if(G[i-1][j]) {
      ans[i][j] = 1;
      put(i, j);
      if(rec(i, j+1)) return true;
      put(i, j);
    } else {
      ans[i][j] = 0;
      if(rec(i, j+1)) return true;
    }
  }
  return false;
}

int main() {
  int n;
  cin >> n;
  while(n--) {
    for(int i = 0; i < H; ++i) {
      for(int j = 0; j < W; ++j) {
        cin >> G[i][j];
      }
    }
    rec(0, 0);
    for(int i = 0; i < H; ++i) {
      for(int j = 0; j < W; ++j) {
        if(j) cout << " ";
        cout << ans[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}