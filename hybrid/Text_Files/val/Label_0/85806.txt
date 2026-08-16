#include <bits/stdc++.h>
using namespace std;
int a[50];
int b[50];
int biao;
int shu;
map<int, int> shuji;
map<int, int> ji;
map<int, int> duia, duib;
void check(int ta, int ta1) {
  if (biao == -1) return;
  ji[a[ta * 2 - 1]] = 1;
  ji[a[ta * 2]] = 1;
  if (ji[b[ta1 * 2]] == 1 && ji[b[ta1 * 2 - 1]] == 1) {
    ji[a[ta * 2 - 1]] = 0;
    ji[a[ta * 2]] = 0;
    return;
  } else {
    if (ji[b[ta1 * 2 - 1]] == 1 || ji[b[ta1 * 2]] == 1) {
      int chong = 0;
      if (ji[b[ta1 * 2 - 1]] == 1)
        chong = b[ta1 * 2 - 1];
      else
        chong = b[ta1 * 2];
      if ((biao == -100 && shu == -1) || (shuji[chong] == 1 && biao == 1)) {
        biao = 1;
        shu = chong;
        shuji[chong] = 1;
        duia[ta] = 1;
        duib[ta1] = 1;
      } else {
        if ((duia[ta] == 1 || duib[ta1] == 1) && shuji[chong] != 1) {
          biao = -1;
          duia[ta] = 1;
          duib[ta1] = 1;
          shuji[chong] = 1;
        } else {
          biao = 0;
          duia[ta] = 1;
          duib[ta1] = 1;
          shuji[chong] = 1;
        }
      }
    }
  }
  ji[a[ta * 2 - 1]] = 0;
  ji[a[ta * 2]] = 0;
}
int main() {
  int n, m;
  shu = -1;
  cin >> n >> m;
  for (int i = 1; i <= n; ++i) {
    cin >> a[i * 2 - 1] >> a[i * 2];
  }
  for (int i = 1; i <= m; ++i) {
    cin >> b[i * 2 - 1] >> b[i * 2];
  }
  biao = -100;
  for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= m; ++j) {
      check(i, j);
    }
  if (biao == 1)
    cout << shu << endl;
  else
    cout << biao << endl;
}
