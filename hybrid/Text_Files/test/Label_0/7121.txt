#include <bits/stdc++.h>
using namespace std;
int t, SA[21010], RA[21010], c[21010], tempRA[21010], tempSA[21010], n,
    behind[21010], LCP[21010], PLCP[21010];
int f[21010], cnt[11][21010], lef[11], rig[11];
string s;
set<pair<pair<int, int>, int> > ma;
void countingSort(int k) {
  int sum = 0, maxi = max(300, n);
  memset(c, 0, sizeof(c));
  for (int i = (0), _b = (n - 1); i <= _b; i++)
    if (i + k < n)
      c[RA[i + k]]++;
    else
      c[0]++;
  for (int i = (0), _b = (maxi - 1); i <= _b; i++) {
    int t = c[i];
    c[i] = sum;
    sum += t;
  }
  for (int i = (0), _b = (n - 1); i <= _b; i++) {
    int a = 0;
    if (SA[i] + k < n) a = RA[SA[i] + k];
    tempSA[c[a]++] = SA[i];
  }
  for (int i = (0), _b = (n - 1); i <= _b; i++) SA[i] = tempSA[i];
}
void suffixArray() {
  int r;
  for (int i = (0), _b = (n - 1); i <= _b; i++) SA[i] = i;
  for (int i = (0), _b = (n - 1); i <= _b; i++) RA[i] = s[i];
  for (int k = 1; k < n; k <<= 1) {
    countingSort(k);
    countingSort(0);
    tempRA[SA[0]] = r = 0;
    for (int i = (1), _b = (n - 1); i <= _b; i++) {
      if (RA[SA[i]] != RA[SA[i - 1]]) {
        tempRA[SA[i]] = ++r;
        continue;
      }
      int a, b;
      if (SA[i] + k >= n)
        a = 0;
      else
        a = RA[SA[i] + k];
      if (SA[i - 1] + k >= n)
        b = 0;
      else
        b = RA[SA[i - 1] + k];
      if (a == b)
        tempRA[SA[i]] = r;
      else
        tempRA[SA[i]] = ++r;
    }
    for (int i = (0), _b = (n - 1); i <= _b; i++) RA[i] = tempRA[i];
    if (r == n - 1) break;
  }
}
void buildLCP() {
  behind[SA[0]] = -1;
  for (int i = (1), _b = (n - 1); i <= _b; i++) behind[SA[i]] = SA[i - 1];
  int L = 0;
  for (int i = (0), _b = (n - 1); i <= _b; i++) {
    if (behind[i] == -1) {
      PLCP[i] = 0;
      continue;
    }
    while (s[i + L] == s[behind[i] + L]) L++;
    PLCP[i] = L;
    L = max(L - 1, 0);
  }
  for (int i = (0), _b = (n - 1); i <= _b; i++) LCP[i] = PLCP[SA[i]];
}
int main() {
  int m;
  ios::sync_with_stdio(0);
  cin >> s;
  int N = s.length();
  for (int i = (0), _b = (s.length()); i <= _b; i++) f[i] = 0;
  s = s + "$";
  cin >> m;
  for (int i = (1), _b = (m); i <= _b; i++) {
    string st;
    cin >> st >> lef[i] >> rig[i];
    int h = s.length();
    s += st + "$";
    for (int j = (h), _b = (s.length() - 1); j <= _b; j++) f[j] = i;
  }
  n = s.length();
  suffixArray();
  buildLCP();
  for (int i = (1), _b = (m); i <= _b; i++)
    for (int j = (m + 1), _b = (n - 1); j <= _b; j++)
      if (f[SA[j]] == i)
        cnt[i][j] = cnt[i][j - 1] + 1;
      else
        cnt[i][j] = cnt[i][j - 1];
  int res = 0;
  for (int i = (0), _b = (N - 1); i <= _b; i++) {
    int l = m + 1, r = n - 1;
    for (int j = (1), _b = (N); j <= _b; j++) {
      if (i + j - 1 >= N) break;
      int dau = l, cuoi = r;
      while (dau <= cuoi) {
        int mid = (dau + cuoi) >> 1;
        if (s[SA[mid] + j - 1] >= s[i + j - 1])
          cuoi = mid - 1;
        else
          dau = mid + 1;
      }
      l = dau;
      dau = l, cuoi = r;
      while (dau <= cuoi) {
        int mid = (dau + cuoi) >> 1;
        if (s[SA[mid] + j - 1] <= s[i + j - 1])
          dau = mid + 1;
        else
          cuoi = mid - 1;
      }
      r = cuoi;
      bool co = true;
      for (int k = (1), _b = (m); k <= _b; k++)
        if (!(cnt[k][r] - cnt[k][l - 1] >= lef[k] &&
              cnt[k][r] - cnt[k][l - 1] <= rig[k])) {
          co = false;
          break;
        }
      if (co) {
        if (!ma.count(pair<pair<int, int>, int>(pair<int, int>(l, r), j))) {
          ma.insert(pair<pair<int, int>, int>(pair<int, int>(l, r), j));
          res++;
        }
      }
    }
  }
  cout << res;
  return 0;
}
