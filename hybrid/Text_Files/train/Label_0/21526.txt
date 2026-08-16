#include <bits/stdc++.h>
using namespace std;
int n, arr[100], i, j;
bool a[100][100];
bool Ok(int x, int y) {
  while (x && y) {
    int a = x % 10;
    int b = y % 10;
    x /= 10;
    y /= 10;
    if (a && b) return false;
  }
  return true;
}
int main() {
  cin >> n;
  vector<vector<int> > v;
  for (int i = 0; i < n; i++) cin >> arr[i];
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      if (Ok(arr[i], arr[j])) a[i][j] = true;
  for (int i = 0; i < n; i++) {
    bool b = false;
    for (int j = 0; j < v.size(); j++) {
      int k;
      for (k = 0; k < v[j].size(); k++) {
        if (!a[i][v[j][k]]) break;
      }
      if (k == v[j].size()) v[j].push_back(i), b = true;
    }
    if (!b) v.push_back(vector<int>(1, i));
  }
  for (i = 0, j = 1; j < v.size(); j++)
    if (v[i].size() < v[j].size()) i = j;
  cout << v[i].size() << endl;
  for (j = 0; j < v[i].size(); j++) cout << arr[v[i][j]] << " ";
  return 0;
}
