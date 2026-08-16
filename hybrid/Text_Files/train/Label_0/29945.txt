#include <bits/stdc++.h>
using namespace std;
long long max(long long a, long long b) {
  if (a > b) {
    return a;
  } else {
    return b;
  }
}
long long min(long long a, long long b) {
  if (a < b) {
    return a;
  } else {
    return b;
  }
}
int n, k, ord[10001], out[10001], t[10001], len[10001], fa = 1, r = 1,
                                                        ma[10000002];
int main() {
  cin >> n >> k;
  int q = 1, cu = 1;
  for (long long i = 1; i <= n; i++) {
    out[i] = 0;
    t[i] = 0;
  }
  for (long long i = 1; i <= n; i++) {
    cin >> ord[i];
    t[ord[i]] = 1;
  }
  int yes = 1;
  while (yes) {
    int v = -1;
    for (long long i = 1; i <= n; i++) {
      if ((t[i] == 0) && (ord[i] != 0)) {
        v = i;
      }
    }
    if (v == -1) {
      yes = 0;
    } else {
      int l = 1;
      int fi = 0;
      while (ord[v] != 0) {
        if (v == k) {
          q = l;
          fi = 1;
        }
        int tmp = ord[v];
        ord[v] = -1;
        t[v] = -1;
        v = tmp;
        l++;
      }
      if (v == k) {
        q = l;
        fi = 1;
      }
      ord[v] = -1;
      t[v] = -1;
      if (fi) {
        q = l - q + 1;
        cu = l;
      }
      len[r++] = l;
    }
  }
  for (long long i = 1; i <= n; i++) {
    if (ord[i] == 0) {
      len[r++] = 1;
    }
  }
  int b = 1;
  ma[b] = q;
  out[q] = 1;
  int check = 0;
  r--;
  for (long long i = 1; i <= r; i++) {
    if ((!check) && (len[i] == cu)) {
      check = 1;
    } else {
      int t[1001];
      for (long long j = 1; j <= n; j++) {
        t[j] = 0;
      }
      for (long long j = 1; j <= n; j++) {
        if ((out[j] > 0) && ((len[i] + j) <= n)) {
          t[len[i] + j] = 1;
        }
      }
      for (long long j = 1; j <= n; j++) {
        out[j] = max(out[j], t[j]);
      }
    }
  }
  for (long long i = 1; i <= n; i++) {
    if (out[i]) {
      cout << i << endl;
    }
  }
  return 0;
}
