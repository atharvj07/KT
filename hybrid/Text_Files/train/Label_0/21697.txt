#include <bits/stdc++.h>
using namespace std;
int a[10][10], b[10][10], viz[10][10], rasp[10][10], sa[10][10], sb[10][10];
int scor(int x, int y) {
  if (x == 3) {
    if (y == 3) return 0;
    if (y == 2) return 1;
    if (y == 1) return -1;
  }
  if (x == 2) {
    if (y == 2) return 0;
    if (y == 1) return 1;
    if (y == 3) return -1;
  }
  if (x == 1) {
    if (y == 1) return 0;
    if (y == 3) return 1;
    if (y == 2) return -1;
  }
}
int main() {
  long long t, a1, b1, i, j, scora = 0, scorb = 0, k, lasta, lastb, cnt = 1,
                             tempa, tempb, s1, s2;
  cin >> t >> a1 >> b1;
  for (i = 1; i <= 3; i++)
    for (j = 1; j <= 3; j++) cin >> a[i][j];
  for (i = 1; i <= 3; i++)
    for (j = 1; j <= 3; j++) cin >> b[i][j];
  if (scor(a1, b1) == 1)
    scora++;
  else if (scor(a1, b1) == -1)
    scorb++;
  lasta = a1;
  lastb = b1;
  sa[a1][b1] = 0;
  sb[a1][b1] = 0;
  viz[a1][b1] = 1;
  rasp[a1][b1] = 1;
  while (cnt < t) {
    tempa = a[lasta][lastb];
    tempb = b[lasta][lastb];
    lasta = tempa;
    lastb = tempb;
    if (viz[tempa][tempb]) break;
    cnt++;
    sa[tempa][tempb] = scora;
    sb[tempa][tempb] = scorb;
    rasp[tempa][tempb] = cnt;
    viz[tempa][tempb] = cnt;
    if (scor(tempa, tempb) == 1)
      scora++;
    else if (scor(tempa, tempb) == -1)
      scorb++;
  }
  if (cnt == t) {
    cout << scora << ' ' << scorb;
    return 0;
  }
  k = (t - cnt) / (cnt - rasp[tempa][tempb] + 1);
  scora = scora + (scora - sa[tempa][tempb]) * k;
  scorb = scorb + (scorb - sb[tempa][tempb]) * k;
  cnt = t - (t - cnt) % (cnt - rasp[tempa][tempb] + 1);
  lasta = tempa;
  lastb = tempb;
  while (cnt < t) {
    cnt++;
    if (scor(tempa, tempb) == 1)
      scora++;
    else if (scor(tempa, tempb) == -1)
      scorb++;
    tempa = a[lasta][lastb];
    tempb = b[lasta][lastb];
    lasta = tempa;
    lastb = tempb;
  }
  cout << scora << ' ' << scorb;
  return 0;
}
