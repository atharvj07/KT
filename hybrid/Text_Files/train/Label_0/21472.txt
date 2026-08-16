#include <bits/stdc++.h>
using namespace std;
vector<pair<long long, long long> > vpi;
int main() {
  long long r, w;
  string s;
  cin >> r;
  for (int i = 1; i <= r; i++) {
    cin >> w;
    vpi.push_back({w, i});
  }
  cin >> s;
  sort(vpi.begin(), vpi.end());
  int xt = vpi.size() - 1;
  int nt = 0;
  priority_queue<pair<int, int> > pq;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == '0')
      cout << vpi[nt++].second << " ",
          pq.push({vpi[nt - 1].first, vpi[nt - 1].second});
    else {
      int xx = pq.top().second;
      cout << xx << " ";
      pq.pop();
    }
  }
  puts("");
  return 0;
}
