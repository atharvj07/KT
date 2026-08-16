#include <bits/stdc++.h>
using namespace std;
const int MAXN = 107;
const int INF = 1e9 + 7;
int T;
int N;
int A[MAXN];
int l[MAXN];
vector<int> save;
void solve() {
  cin >> N;
  for (int i = 1; i <= N; i++) cin >> A[i];
  for (int i = 1; i <= N; i++) cin >> l[i];
  save.clear();
  for (int i = 1; i <= N; i++)
    if (!l[i]) save.push_back(A[i]);
  sort(save.begin(), save.end());
  int pos = 0;
  for (int i = N; i >= 1; i--)
    if (l[i] == 0) A[i] = save[pos++];
  for (int i = 1; i <= N; i++) cout << A[i] << " ";
  cout << '\n';
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> T;
  while (T--) solve();
  return 0;
}
