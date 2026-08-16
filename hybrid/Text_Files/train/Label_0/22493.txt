#include <bits/stdc++.h>
using namespace std;
void init() {
  cin.tie(0);
  cin.sync_with_stdio(0);
}
int main() {
  init();
  long long t;
  cin >> t;
  string s, ss, x;
  long long ans = 0;
  map<string, long long> mp;
  long long frq[10][10][10][10] = {0};
  while (t--) {
    char a, b, c, d;
    cin >> a >> b >> c >> d;
    if (t != 0) cin >> x;
    int p = a - '0';
    int x = b - '0';
    int y = c - '0';
    int z = d - '0';
    if (frq[p][x][y][z] == 0)
      frq[p][x][y][z] = frq[y][p][z][x] = frq[z][y][x][p] = frq[x][z][p][y] = 1,
      ans++;
  }
  cout << ans;
}
