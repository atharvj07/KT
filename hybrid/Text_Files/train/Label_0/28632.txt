#include <bits/stdc++.h>
using namespace std;
int room[500][3];
int paper[500][3];
int cost(int* r, int* p) {
  int l = (r[0] + r[1]) * 2;
  int h = r[2];
  int s, k, t;
  if (p[0] >= h) {
    s = p[0] / h;
    k = s * p[1];
    if (l % k == 0) {
      t = l / k;
    } else {
      t = l / k + 1;
    }
    return t * p[2];
  } else {
    return -1;
    s = h / p[0];
    k = p[1];
    if (l % k == 0) {
      t = l / k;
    } else {
      t = l / k + 1;
    }
    return t * s * p[2];
  }
}
int main() {
  int n, m;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> room[i][0] >> room[i][1] >> room[i][2];
  }
  cin >> m;
  for (int i = 0; i < m; i++) {
    cin >> paper[i][0] >> paper[i][1] >> paper[i][2];
  }
  int tot = 0;
  for (int i = 0; i < n; i++) {
    int c = cost(room[i], paper[0]);
    for (int j = 1; j < m; j++) {
      if (c == -1) {
        c = cost(room[i], paper[j]);
      } else if (cost(room[i], paper[j]) != -1) {
        c = min(c, cost(room[i], paper[j]));
      }
    }
    tot += c;
  }
  cout << tot << endl;
  return 0;
}
