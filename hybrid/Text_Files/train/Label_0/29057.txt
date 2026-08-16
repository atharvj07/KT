#include <bits/stdc++.h>
using namespace std;
const int maxn = 55;
int n, m, k;
set<set<int> > ha[maxn][maxn];
string mat[maxn];
int stran[4][2] = {1, 0, -1, 0, 0, 1, 0, -1};
int br, bc;
int er, ec;
int dis(int r1, int c1, int r2, int c2) { return abs(r1 - r2) + abs(c1 - c2); }
struct node {
  int r, c;
  string s;
  int bu;
  int cu;
  string used;
  friend bool operator<(const node &a, const node &b) {
    if (a.bu + dis(a.r, a.c, er, ec) == b.bu + dis(b.r, b.c, er, ec)) {
      return a.s > b.s;
    }
    return a.bu + dis(a.r, a.c, er, ec) > b.bu + dis(b.r, b.c, er, ec);
  }
};
priority_queue<node> que;
set<int> uu;
int main() {
  cin >> n >> m >> k;
  for (int i = 0; i < n; i++) {
    cin >> mat[i];
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (mat[i][j] == 'S') {
        br = i;
        bc = j;
      }
      if (mat[i][j] == 'T') {
        er = i;
        ec = j;
      }
    }
  }
  node now, ne;
  now.bu = 0;
  now.s.clear();
  now.r = br;
  now.c = bc;
  now.cu = 0;
  now.used.clear();
  que.push(now);
  while (!que.empty()) {
    now = que.top();
    que.pop();
    if (mat[now.r][now.c] == 'T') {
      cout << now.s << endl;
      return 0;
    }
    string ss = now.used, ness;
    string ro = now.s;
    int nr = now.r, nc = now.c;
    uu.clear();
    for (int i = 0; i < ss.length(); i++) {
      uu.insert(ss[i] - 'a');
    }
    if (ha[nr][nc].find(uu) != ha[nr][nc].end()) continue;
    ha[nr][nc].insert(uu);
    int ner, nec;
    for (int i = 0; i < 4; i++) {
      ner = nr + stran[i][0];
      nec = nc + stran[i][1];
      if (ner >= 0 && ner < n && nec >= 0 && nec < m) {
        char p = mat[ner][nec];
        ne.r = ner;
        ne.c = nec;
        ne.bu = now.bu + 1;
        if (p != 'T' && p != 'S') {
          bool hu = 0;
          for (int j = 0; j < ss.length(); j++) {
            if (p == ss[j]) {
              hu = 1;
              break;
            }
          }
          if (hu == 1) {
            ne.used = ss;
            ne.cu = now.cu;
            ne.s = now.s + p;
            que.push(ne);
          } else {
            if (now.cu + 1 <= k) {
              ne.used = ss + p;
              ne.cu = now.cu + 1;
              ne.s = now.s + p;
              que.push(ne);
            }
          }
        } else if (p == 'T') {
          ne = now;
          ne.bu++;
          ne.r = er;
          ne.c = ec;
          que.push(ne);
        }
      }
    }
  }
  cout << "-1" << endl;
  return 0;
}
