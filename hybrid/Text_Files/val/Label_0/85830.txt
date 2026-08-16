#include <bits/stdc++.h>
using namespace std;
const long long int N = 5005;
const long long int mod = 1e17 + 7;
long long int k, n;
string s[N];
long long int high, idx;
long long int cnt[26];
bool satisfy(long long int x) {
  long long int ret = 0;
  for (long long int i = 0; i < n; i++) {
    if (s[x][i] != s[idx][i]) ret++;
  }
  if (ret == 2 or (ret == 0 and high >= 2) or (x == idx)) return true;
  return false;
}
int main() {
  long long int occ;
  ios::sync_with_stdio(false);
  cin >> k >> n;
  for (long long int i = 1; i < k + 1; i++) {
    cin >> s[i];
  }
  bool flag = true;
  for (long long int i = 1; i < k; i++) {
    for (long long int j = 0; j < n; j++) {
      if (s[i][j] != s[i + 1][j]) {
        idx = i;
        flag = false;
        occ = j;
        break;
      }
    }
    if (!flag) break;
  }
  if (flag) {
    swap(s[1][0], s[1][1]);
    cout << s[1] << endl;
    return 0;
  }
  for (long long int i = 0; i < n; i++) {
    cnt[s[1][i] - 'a']++;
    high = max(high, cnt[s[1][i] - 'a']);
  }
  for (long long int i = 2; i < k + 1; i++) {
    vector<long long int> tmp(26, 0);
    for (long long int j = 0; j < n; j++) {
      tmp[s[i][j] - 'a']++;
    }
    for (long long int j = 0; j < 26; j++) {
      if (tmp[j] != cnt[j]) {
        cout << "-1\n";
        return 0;
      }
    }
  }
  bool yo = false;
  for (long long int i = 0; i < n; i++) {
    if (i == occ) continue;
    swap(s[idx][i], s[idx][occ]);
    bool ret = true;
    for (long long int j = 1; j < k + 1; j++) {
      if (!satisfy(j)) {
        ret = false;
        break;
      }
    }
    if (ret) {
      yo = true;
      break;
    }
    swap(s[idx][i], s[idx][occ]);
  }
  if (yo) {
    cout << s[idx] << endl;
  } else {
    idx++;
    yo = false;
    for (long long int i = 0; i < n; i++) {
      if (i == occ) continue;
      swap(s[idx][i], s[idx][occ]);
      bool ret = true;
      for (long long int j = 1; j < k + 1; j++) {
        if (!satisfy(j)) {
          ret = false;
          break;
        }
      }
      if (ret) {
        yo = true;
        break;
      }
      swap(s[idx][i], s[idx][occ]);
    }
    if (yo) {
      cout << s[idx] << endl;
      return 0;
    }
    cout << "-1\n";
  }
  return 0;
}
