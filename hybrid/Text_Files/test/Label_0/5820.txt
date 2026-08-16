#include <bits/stdc++.h>
using namespace std;
const int N = 101;
double a[N][N][N];
double b[N][N][N];
double c[N][N][N];
bool v[N][N][N];
int ca, cb, cc;
void input() { cin >> ca >> cc >> cb; }
void calc(int i, int j, int k) {
  if (v[i][j][k]) {
    return;
  }
  if (i && !j && !k) {
    a[i][j][k] = 1;
    b[i][j][k] = 0;
    c[i][j][k] = 0;
    return;
  }
  if (!i && j && !k) {
    a[i][j][k] = 0;
    b[i][j][k] = 1;
    c[i][j][k] = 0;
    return;
  }
  if (!i && !j && k) {
    a[i][j][k] = 0;
    b[i][j][k] = 0;
    c[i][j][k] = 1;
    return;
  }
  double ab = i * j;
  double bc = j * k;
  double ca = k * i;
  double all = (i ? ab : 0) + (j ? bc : 0) + (k ? ca : 0);
  if (i) calc(i - 1, j, k);
  if (j) calc(i, j - 1, k);
  if (k) calc(i, j, k - 1);
  a[i][j][k] = (ab * (i ? a[i - 1][j][k] : 0) + bc * (j ? a[i][j - 1][k] : 0) +
                ca * (k ? a[i][j][k - 1] : 0)) /
               all;
  b[i][j][k] = (ab * (i ? b[i - 1][j][k] : 0) + bc * (j ? b[i][j - 1][k] : 0) +
                ca * (k ? b[i][j][k - 1] : 0)) /
               all;
  c[i][j][k] = (ab * (i ? c[i - 1][j][k] : 0) + bc * (j ? c[i][j - 1][k] : 0) +
                ca * (k ? c[i][j][k - 1] : 0)) /
               all;
  v[i][j][k] = 1;
}
void solve() {
  calc(ca, cb, cc);
  double ans_a = a[ca][cb][cc];
  double ans_b = b[ca][cb][cc];
  double ans_c = c[ca][cb][cc];
  cout << fixed << setprecision(12) << ans_a << " " << ans_c << " " << ans_b
       << "\n";
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0), cout.tie(0);
  input();
  solve();
}
