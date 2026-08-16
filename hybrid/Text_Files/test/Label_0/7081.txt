#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:32000000")
using namespace std;
const int MAX = 200000;
const int INF = 100000000;
const int MOD = 1000000007;
const double EPS = 1E-7;
const int IT = 10024;
map<int, vector<pair<int, int> > > r;
map<int, vector<pair<int, int> > > c;
map<int, int> R;
map<int, int> C;
int main() {
  int n, m;
  cin >> n >> m;
  int k;
  cin >> k;
  for (long long(i) = (0); i < k; i++) {
    int x1, y1, x2, y2;
    scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
    if (x1 == x2) {
      r[x1].push_back(make_pair(min(y1, y2), max(y1, y2)));
    } else {
      c[y1].push_back(make_pair(min(x1, x2), max(x1, x2)));
    }
  }
  int dr = n - 1 - r.size();
  int dc = m - 1 - c.size();
  int res = 0;
  if (dr & 1) res ^= m;
  if (dc & 1) res ^= n;
  for (map<int, vector<pair<int, int> > >::iterator it = r.begin();
       it != r.end(); ++it) {
    int cnt = 0;
    sort(it->second.begin(), it->second.end());
    cnt += it->second[0].first;
    int rigth = it->second[0].second;
    for (long long(i) = (1); i < it->second.size(); i++) {
      cnt += max(0, it->second[i].first - rigth);
      rigth = max(rigth, it->second[i].second);
    }
    cnt += m - rigth;
    R[it->first] = cnt;
    res ^= cnt;
  }
  for (map<int, vector<pair<int, int> > >::iterator it = c.begin();
       it != c.end(); ++it) {
    int cnt = 0;
    sort(it->second.begin(), it->second.end());
    cnt += it->second[0].first;
    int rigth = it->second[0].second;
    for (long long(i) = (1); i < it->second.size(); i++) {
      cnt += max(0, it->second[i].first - rigth);
      rigth = max(rigth, it->second[i].second);
    }
    cnt += n - rigth;
    C[it->first] = cnt;
    res ^= cnt;
  }
  if (res == 0) {
    cout << "SECOND\n";
    return 0;
  } else {
    cout << "FIRST\n";
  }
  if (dr && (res ^ m) <= m) {
    int cut = m - (res ^ m);
    int X;
    for (long long(i) = (1); i < 100007; i++)
      if (!R.count(i)) {
        X = i;
        break;
      }
    cout << X << ' ' << 0 << ' ' << X << ' ' << cut << endl;
    return 0;
  }
  if (dc && (res ^ n) <= n) {
    int cut = n - (res ^ n);
    int X;
    for (long long(i) = (1); i < 100007; i++)
      if (!C.count(i)) {
        X = i;
        break;
      }
    cout << 0 << ' ' << X << ' ' << cut << ' ' << X << endl;
    return 0;
  }
  for (map<int, int>::iterator it = R.begin(); it != R.end(); ++it) {
    if ((res ^ it->second) <= it->second) {
      int cut = it->second - (res ^ it->second);
      int x = it->first;
      vector<pair<int, int> > temp = r[x];
      int cnt = 0;
      cnt += temp[0].first;
      if (cut <= temp[0].first) {
        cout << x << ' ' << 0 << ' ' << x << ' ' << cut << endl;
        return 0;
      }
      int rigth = temp[0].second;
      for (long long(i) = (1); i < temp.size(); i++) {
        int add = max(0, temp[i].first - rigth);
        if (cnt + add >= cut) {
          cout << x << ' ' << 0 << ' ' << x << ' ' << rigth + cut - cnt << endl;
          return 0;
        }
        cnt += add;
        rigth = max(rigth, temp[i].second);
      }
      cout << x << ' ' << 0 << ' ' << x << ' ' << rigth + cut - cnt << endl;
      return 0;
    }
  }
  for (map<int, int>::iterator it = C.begin(); it != C.end(); ++it) {
    if ((res ^ it->second) <= it->second) {
      int cut = it->second - (res ^ it->second);
      int x = it->first;
      vector<pair<int, int> > temp = c[x];
      int cnt = 0;
      if (cut <= temp[0].first) {
        cout << 0 << ' ' << x << ' ' << cut << ' ' << x << endl;
        return 0;
      }
      cnt += temp[0].first;
      int rigth = temp[0].second;
      for (long long(i) = (1); i < temp.size(); i++) {
        int add = max(0, temp[i].first - rigth);
        if (cnt + add >= cut) {
          cout << 0 << ' ' << x << ' ' << rigth + cut - cnt << ' ' << x << endl;
          return 0;
        }
        cnt += add;
        rigth = max(rigth, temp[i].second);
      }
      cout << 0 << ' ' << x << ' ' << rigth + cut - cnt << ' ' << x << endl;
      return 0;
    }
  }
}
