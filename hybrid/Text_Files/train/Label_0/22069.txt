#include <bits/stdc++.h>
using namespace std;
const int N = 3e6 + 7;
long long int a[N], b[N], c[N], tree[N], lazy[N], cnt, sum, s2, mx;
vector<long long int> v, u;
vector<pair<long long int, long long int>> vp;
map<long long int, long long int> mp;
bool vis[111111];
pair<long long int, long long int> p;
set<pair<long long int, long long int>> ss;
queue<long long int> q;
int main() {
  ios_base ::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int n, m = 0, d, i = 0, s1 = 0, s2 = 0, q = 5, x = 0, y, k, j;
  string s = "";
  cin >> n >> x;
  if (x == 0) a[0] = 1;
  if (x == 1) a[1] = 1;
  if (x == 2) a[2] = 1;
  m = n % 6;
  if (n % 2 != 0) {
    for (i = 1; i <= m; i++) {
      if (i % 2 != 0) {
        swap(a[0], a[1]);
      } else {
        swap(a[1], a[2]);
      }
    }
    if (a[0] == 1) cout << 0;
    if (a[1] == 1) cout << 1;
    if (a[2] == 1) cout << 2;
    return 0;
  } else {
    for (i = 1; i <= m; i++) {
      if (i % 2 == 0) {
        swap(a[0], a[1]);
      } else {
        swap(a[1], a[2]);
      }
    }
    if (a[0] == 1) cout << 0;
    if (a[1] == 1) cout << 1;
    if (a[2] == 1) cout << 2;
    return 0;
  }
}
