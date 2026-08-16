#include <bits/stdc++.h>
using namespace std;
int n, m, ans1[3], ans2[3];
long long a[2005], b[2005], sa, sb;
vector<pair<long long, pair<int, int> > > A, B;
int main() {
  ios_base ::sync_with_stdio(false);
  cin >> n;
  for (int i = (1), _b = (n); i <= _b; i++) cin >> a[i], sa += a[i];
  cin >> m;
  for (int i = (1), _b = (m); i <= _b; i++) cin >> b[i], sb += b[i];
  bool swapped = false;
  if (sa > sb) {
    swapped = true;
    swap(sa, sb), swap(n, m);
    for (int i = (1), _b = (max(n, m)); i <= _b; i++) swap(a[i], b[i]);
  }
  long long best = sb - sa;
  int step = 0;
  for (int i = (1), _b = (n); i <= _b; i++)
    for (int j = (1), _b = (m); j <= _b; j++)
      if (abs(sa - sb - 2LL * a[i] + 2LL * b[j]) < best) {
        best = abs(sa - sb - 2LL * a[i] + 2LL * b[j]);
        step = 1, ans1[1] = i, ans2[1] = j;
      }
  for (int i = (1), _b = (n - 1); i <= _b; i++)
    for (int j = (i + 1), _b = (n); j <= _b; j++)
      A.push_back(make_pair(a[i] + a[j], make_pair(i, j)));
  for (int i = (1), _b = (m - 1); i <= _b; i++)
    for (int j = (i + 1), _b = (m); j <= _b; j++)
      B.push_back(make_pair(b[i] + b[j], make_pair(i, j)));
  sort(A.begin(), A.end()), sort(B.begin(), B.end());
  int j = (int)B.size() - 1;
  for (int i = (0), _b = ((int)A.size() - 1); i <= _b; i++) {
    while (j >= 0 && 2LL * (B[j].first - A[i].first) > sb - sa) j--;
    if (j == -1) break;
    if (sb - sa - 2LL * B[j].first + 2LL * A[i].first < best) {
      best = sb - sa - 2LL * B[j].first + 2LL * A[i].first;
      step = 2;
      ans1[1] = A[i].second.first, ans1[2] = A[i].second.second;
      ans2[1] = B[j].second.first, ans2[2] = B[j].second.second;
    }
  }
  j = 0;
  for (int i = (0), _b = ((int)A.size() - 1); i <= _b; i++) {
    while (j < (int)B.size() && 2LL * (B[j].first - A[i].first) < sb - sa) j++;
    if (j == (int)B.size()) break;
    if (2LL * B[j].first - 2LL * A[i].first - sb + sa < best) {
      best = 2LL * B[j].first - 2LL * A[i].first - sb + sa;
      step = 2;
      ans1[1] = A[i].second.first, ans1[2] = A[i].second.second;
      ans2[1] = B[j].second.first, ans2[2] = B[j].second.second;
    }
  }
  cout << best << '\n' << step << '\n';
  for (int i = (1), _b = (step); i <= _b; i++)
    if (!swapped)
      cout << ans1[i] << ' ' << ans2[i] << '\n';
    else
      cout << ans2[i] << ' ' << ans1[i] << '\n';
  return 0;
}
