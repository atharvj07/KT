#include <bits/stdc++.h>
using namespace std;
int seg[2 * (1 << 18)], segFlip[2 * (1 << 18)], l[2 * (1 << 18)],
    r[2 * (1 << 18)], up[2 * (1 << 18)];
void init() {
  for (int i = (1 << 18); i < 2 * (1 << 18); i++) {
    l[i] = r[i] = i - (1 << 18);
    seg[i] = 1000000000, segFlip[i] = i - (1 << 18);
  }
  for (int i = (1 << 18) - 1; i > 0; i--) {
    l[i] = l[2 * i], r[i] = r[2 * i + 1];
    seg[i] = 1000000000, segFlip[i] = l[i];
  }
}
void push(int i) {
  if (up[i]) {
    if (up[i] == 1) {
      seg[i] = l[i], segFlip[i] = 1000000000;
      if (i < (1 << 18)) up[2 * i] = up[2 * i + 1] = 1;
    } else if (up[i] == 2) {
      seg[i] = 1000000000, segFlip[i] = l[i];
      if (i < (1 << 18)) up[2 * i] = up[2 * i + 1] = 2;
    } else {
      swap(seg[i], segFlip[i]);
      if (i < (1 << 18))
        up[2 * i] = 3 - up[2 * i], up[2 * i + 1] = 3 - up[2 * i + 1];
    }
    up[i] = 0;
  }
}
int low, high;
void update(int i, int v) {
  push(i);
  if ((l[i] > high) || (r[i] < low)) return;
  if ((l[i] >= low) && (r[i] <= high)) {
    up[i] = v;
    push(i);
    return;
  }
  update(2 * i, v);
  update(2 * i + 1, v);
  seg[i] = min(seg[2 * i], seg[2 * i + 1]);
  segFlip[i] = min(segFlip[2 * i], segFlip[2 * i + 1]);
}
long long tp[100000], ql[100000], qr[100000];
int main() {
  cin.tie(0);
  ios::sync_with_stdio(0);
  int Q;
  cin >> Q;
  vector<long long> lst;
  for (int i = 0; i < Q; i++) {
    cin >> tp[i] >> ql[i] >> qr[i];
    lst.push_back(ql[i]);
    lst.push_back(qr[i] + 1);
  }
  lst.push_back(1);
  sort(lst.begin(), lst.end());
  lst.resize(distance(lst.begin(), unique(lst.begin(), lst.end())));
  init();
  for (int i = 0; i < Q; i++) {
    ql[i] = lower_bound(lst.begin(), lst.end(), ql[i]) - lst.begin();
    qr[i] = lower_bound(lst.begin(), lst.end(), qr[i] + 1) - lst.begin();
    low = ql[i], high = qr[i] - 1;
    update(1, tp[i]);
    cout << lst[segFlip[1]] << '\n';
  }
}
