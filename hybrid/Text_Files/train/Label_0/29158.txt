#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m, k;
  cin >> n >> k >> m;
  map<string, int> mapping;
  string str;
  for (int i = 0; i < n; i++) {
    cin >> str;
    mapping.insert(make_pair(str, i));
  }
  int cost[n];
  for (int i = 0; i < n; i++) cin >> cost[i];
  for (int i = 0; i < k; i++) {
    int x;
    cin >> x;
    int a[x];
    int mi = 1000000000;
    for (int j = 0; j < x; j++) {
      cin >> a[j];
      mi = min(mi, cost[a[j] - 1]);
    }
    for (int j = 0; j < x; j++) cost[a[j] - 1] = mi;
  }
  long long int sum = 0;
  for (int i = 0; i < m; i++) {
    cin >> str;
    map<string, int>::iterator it = mapping.find(str);
    sum += cost[it->second];
  }
  cout << sum << endl;
}
