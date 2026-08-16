#include <bits/stdc++.h>
using namespace std;
long long n, A, cf, cm, m, a[100005], ex[100005], pref[100005], Ans[100005];
pair<long long, long long> b[100005];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n >> A >> cf >> cm >> m;
  long long cnt = 0;
  for (long long i = 1; i <= n; ++i) {
    cin >> a[i];
    if (a[i] == A) cnt++;
    b[i] = make_pair(a[i], i);
  }
  sort(b + 1, b + 1 + n);
  if (cnt == n) {
    cout << n * cf + A * cm << endl;
    for (long long i = 1; i <= n; ++i) cout << A << " ";
    cout << endl;
    return 0;
  }
  for (long long i = 1; i <= n - cnt; ++i) {
    pref[i] = pref[i - 1] + (A - b[i].first);
  }
  long long en, ans, ix, val, idx, chk, no;
  for (long long i = 1; i <= n - cnt; ++i) {
    ex[i] = ex[i - 1] + (i - 1) * (b[i].first - b[i - 1].first);
    if (ex[i] == m) {
      en = i;
      chk = 0;
      ans = cnt * cf + b[i].first * cm;
      ix = i;
      val = b[i].first;
      no = cnt;
      break;
    }
    if (ex[i] > m) {
      ex[i] = m;
      en = i;
      ans = cnt * cf + (((m - ex[i - 1]) / (i - 1)) + b[i - 1].first) * cm;
      ix = i - 1;
      val = (((m - ex[i - 1]) / (i - 1)) + b[i - 1].first);
      no = cnt;
      break;
    }
    if (i == n - cnt) {
      en = i;
      ix = i;
      val = min(A, b[i].first + (m - ex[i]) / i);
      if (val == A) {
        cout << cf * n + cm * A << endl;
        for (long long i = 1; i <= n; ++i) cout << A << " ";
        cout << endl;
        return 0;
      }
      ans = val * cm + cf * cnt;
      no = cnt;
    }
  }
  for (long long i = n - cnt; i > 0; i--) {
    long long rem = m - (pref[n - cnt] - pref[i - 1]);
    if (rem < 0) break;
    idx = lower_bound(ex + 1, ex + min(en, i - 1) + 1, rem) - ex;
    if (ex[idx] != rem) idx--;
    if (ans < (n - i + 1) * cf + (b[idx].first + (rem - ex[idx]) / idx) * cm) {
      ans = (n - i + 1) * cf + (b[idx].first + (rem - ex[idx]) / idx) * cm;
      ix = idx;
      val = (b[idx].first + (rem - ex[idx]) / idx);
      no = n - i + 1;
    }
  }
  for (long long i = 1; i <= ix; ++i) b[i].first = val;
  for (long long i = n - no + 1; i <= n; ++i) b[i].first = A;
  for (long long i = 1; i <= n; ++i) Ans[b[i].second] = b[i].first;
  cout << ans << endl;
  for (long long i = 1; i <= n; ++i) cout << Ans[i] << " ";
  cout << endl;
}
