#include <bits/stdc++.h>
using namespace std;
const int mx = 1e5 + 10;
int divs[mx];
long long int cmb[mx][7];
long long int gcd(long long int a, long long int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int bat(int b, int i) {
  if (b & (1 << i)) return true;
  return false;
}
int main() {
  cmb[0][0] = 1;
  for (int i = 1; i < mx; i++) {
    cmb[i][0] = 1;
    if (i <= 5) cmb[i][i] = 1;
    for (int j = 1; j < i && j <= 5; j++) {
      cmb[i][j] = cmb[i - 1][j] + cmb[i - 1][j - 1];
    }
  }
  for (int i = 1; i < mx; i++)
    for (int j = i; j < mx; j += i) divs[j]++;
  vector<tuple<int, int, int> > good;
  int mask[] = {1, 2, 4, 3, 5, 6, 7};
  for (int x = 0; x < 7; x++)
    for (int y = x; y < 7; y++)
      for (int z = y; z < 7; z++) {
        vector<int> p = {mask[x], mask[y], mask[z]};
        sort(p.begin(), p.end());
        bool ok = false;
        do {
          if (bat(p[0], 0) == 1 && bat(p[1], 1) == 1 && bat(p[2], 2) == 1)
            ok = true;
        } while (next_permutation(p.begin(), p.end()));
        if (ok) good.push_back(make_tuple(x, y, z));
      }
  int t;
  scanf("%d", &t);
  while (t--) {
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    int abc = divs[gcd(gcd(A, B), C)];
    int ab = divs[gcd(A, B)] - abc;
    int ac = divs[gcd(A, C)] - abc;
    int bc = divs[gcd(B, C)] - abc;
    int a = divs[A] - ab - ac - abc;
    int b = divs[B] - ab - bc - abc;
    int c = divs[C] - ac - bc - abc;
    int all[] = {a, b, c, ab, ac, bc, abc};
    long long int ans = 0;
    for (auto xyz : good) {
      int x, y, z;
      tie(x, y, z) = xyz;
      if (all[x] == 0 || all[y] == 0 || all[z] == 0) continue;
      map<int, int> mp;
      mp[x]++;
      mp[y]++;
      mp[z]++;
      long long int inc = 1;
      for (auto p : mp) {
        int s = p.second;
        int q = all[p.first];
        inc *= cmb[s + q - 1][s];
      }
      ans += inc;
    }
    cout << ans << '\n';
  }
  return 0;
}
