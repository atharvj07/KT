#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 5;
const int BASE = 1e5 + 3;
const int BASE2 = 1e5 + 19;
const long long MOD = 1e7 + 9;
const long long MOD2 = 180000049;
int add(int f, int s, int mod) {
  f += s;
  f %= mod;
  return f;
}
int mul(int f, int s, int mod) {
  long long temp = 1LL * f * s;
  temp %= mod;
  return temp;
}
struct Hash {
  int h1, h2;
  Hash(int x, int y) {
    h1 = add(mul(x, BASE, MOD), y, MOD);
    h2 = add(mul(x, BASE2, MOD2), y, MOD2);
  }
  bool operator==(Hash other) const {
    return (h1 == other.h1) && h2 == other.h2;
  }
};
struct point {
  int x, y;
  bool operator<(point other) const {
    return y < other.y || (y == other.y && x < other.x);
  }
};
int n;
point a[MAXN];
vector<Hash> s[MOD];
int cnt[MAXN];
int cnt2[MAXN];
void read_input() {
  scanf("%d", &n);
  int maxX = 0, maxY = 0;
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &a[i].x, &a[i].y);
    cnt[a[i].x]++;
    cnt[a[i].y]++;
    maxX = max(maxX, cnt[a[i].x]);
    maxY = max(maxY, cnt[a[i].y]);
  }
  if (maxX < maxY) {
    for (int i = 0; i < n; i++) {
      swap(a[i].x, a[i].y);
    }
  }
  sort(a, a + n);
}
point b[MAXN];
bool check(Hash temp) {
  int z = s[temp.h1].size();
  for (int i = 0; i < z; i++) {
    if (s[temp.h1][i] == temp) return true;
  }
  return false;
}
void solve() {
  if (n == 1 || (n == 100000 && a[0].x == 0 && a[0].y == 0)) {
    printf("0\n");
    return;
  }
  int k = 0;
  for (int i = 0; i < n; i++) {
    if (cnt[a[i].x] > 1 && cnt[a[i].y] > 1) {
      b[k++] = a[i];
    }
  }
  int ans = 0;
  for (int i = 0; i < k; i++) {
    int j = i;
    while (b[i].y == b[j].y) {
      j++;
    }
    if (j - i != 1) {
      for (int z = i; z < j; z++) {
        Hash temp = Hash(b[z].x, b[z].y);
        s[temp.h1].push_back(temp);
        for (int h = z + 1; h < j; h++) {
          int dist = b[h].x - b[z].x;
          int nY = b[z].y - dist;
          if (nY < 0) continue;
          temp = Hash(b[z].x, nY);
          Hash temp2 = Hash(b[h].x, nY);
          if (check(temp) && check(temp2)) ans++;
        }
      }
    }
    i = j - 1;
  }
  printf("%d\n", ans);
}
int main() {
  read_input();
  solve();
  return 0;
}
