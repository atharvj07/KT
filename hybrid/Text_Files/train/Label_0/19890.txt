#include <bits/stdc++.h>
using namespace std;
int arr[100000 + 100];
int main() {
  int n;
  cin >> n;
  vector<int> v[n + 1];
  for (int i = 2; i <= n; i++) {
    int t;
    cin >> t;
    v[t].push_back(i);
    v[i].push_back(t);
  }
  queue<int> q;
  q.push(1);
  arr[1] = 1;
  int max = 1;
  int x = 0, k = 0, coun = 1;
  while (!q.empty()) {
    int t = q.front();
    q.pop();
    for (int i = 0; i < v[t].size(); i++) {
      if (arr[v[t][i]] == 0) {
        q.push(v[t][i]);
        arr[v[t][i]] = 1;
        x++;
      }
    }
    k++;
    if (k == coun) {
      if (x % 2 != 0) max++;
      coun = x;
      x = 0;
      k = 0;
    }
  }
  cout << max;
}
