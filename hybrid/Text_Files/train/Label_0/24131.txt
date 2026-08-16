#include <bits/stdc++.h>
using namespace std;
void solve() {
  int n, k;
  cin >> n >> k;
  int arr[n];
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  vector<int> key;
  for (int elm : arr) {
    bool found = false;
    for (int i : key) {
      if (i == elm) {
        found = true;
      }
    }
    if (!found) {
      key.push_back(elm);
    }
  }
  if (key.size() > k) {
    cout << -1 << endl;
    return;
  }
  if (key.size() == n || n == k) {
    cout << n << endl;
    for (int i : arr) {
      cout << i << " ";
    }
    cout << endl;
    return;
  }
  map<int, bool> mm;
  for (int i = 1; i <= n; i++) {
    mm[i] = false;
  }
  for (int i : key) {
    mm[i] = true;
  }
  if (key.size() < k) {
    while (key.size() != k) {
      for (int i = 1; i <= n; i++) {
        if (!mm[i]) {
          mm[i] = true;
          key.push_back(i);
          break;
        }
      }
    }
  }
  sort(key.begin(), key.end());
  map<pair<int, int>, vector<int>> myMap;
  for (int i = 0; i < key.size(); i++) {
    for (int j = 0; j < key.size(); j++) {
      if (i == j) {
        vector<int> dum;
        for (int k = i + 1; k < i + key.size(); k++) {
          dum.push_back(key[k % key.size()]);
        }
        myMap[make_pair(key[i], key[j])] = dum;
      }
      if (i < j) {
        vector<int> dum;
        for (int k = i + 1; k < j; k++) {
          dum.push_back(key[k]);
        }
        myMap[make_pair(key[i], key[j])] = dum;
      }
      if (i > j) {
        vector<int> dum;
        int k = i;
        k = (k + 1) % key.size();
        while (k != j) {
          dum.push_back(key[k]);
          k++;
          k %= key.size();
        }
        myMap[make_pair(key[i], key[j])] = dum;
      }
    }
  }
  vector<int> myVector;
  for (int i = 0; i < n - 1; i++) {
    myVector.push_back(arr[i]);
    for (int st : myMap[make_pair(arr[i], arr[i + 1])]) {
      myVector.push_back(st);
    }
  }
  myVector.push_back(arr[n - 1]);
  cout << myVector.size() << endl;
  for (int i : myVector) {
    cout << i << " ";
  }
  cout << endl;
}
int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
