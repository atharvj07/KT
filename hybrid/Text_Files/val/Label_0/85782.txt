#include <bits/stdc++.h>
using namespace std;
int arr[132005];
int n, k;
int init_cnt = 1;
int cnt[132005 << 1];
void init(int l, int r, int p) {
  if (r - l <= 1) return;
  int mid = (l + r) >> 1, lch = p << 1, rch = p << 1 | 1;
  init_cnt += 2;
  cnt[p] += 2;
  init(l, mid, lch);
  init(mid, r, rch);
  cnt[p] += cnt[lch] + cnt[rch];
}
int fix;
void divide(int l, int r, int p) {
  if (r - l <= 1) return;
  if (cnt[p] <= fix) {
    sort(arr + l, arr + r);
    fix -= cnt[p];
  } else {
    int mid = (l + r) >> 1, lch = p << 1, rch = p << 1 | 1;
    if (cnt[lch] <= fix) {
      sort(arr + l, arr + mid);
      fix -= cnt[lch];
    } else
      divide(l, mid, lch);
    if (cnt[rch] <= fix) {
      sort(arr + mid, arr + r);
      fix -= cnt[rch];
    } else
      divide(mid, r, rch);
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> k;
  memset(cnt, 0, sizeof cnt);
  init(0, n, 1);
  for (int i = 0; i < n; i++) arr[i] = n - i;
  if (init_cnt < k)
    cout << -1 << endl;
  else {
    fix = init_cnt - k;
    divide(0, n, 1);
    if (fix != 0)
      cout << -1 << endl;
    else {
      for (int i = 0; i < n; i++) {
        if (i != 0) cout << " ";
        cout << arr[i];
      }
      cout << endl;
    }
  }
  return 0;
}
