#include <bits/stdc++.h>
using namespace std;
int isvowel(char ch) {
  if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
    return 1;
  else
    return 0;
}
int isry(string s1, string s2, int k) {
  int l1, l2, ctr1 = 0, ctr2 = 0, i, j, pos1 = -1, pos2 = -1;
  l1 = s1.length();
  l2 = s2.length();
  for (i = l1 - 1; i >= 0; i--) {
    if (ctr1 >= k) break;
    if (isvowel(s1[i])) ctr1++;
    if (ctr1 >= k) break;
  }
  pos1 = i;
  for (i = l2 - 1; i >= 0; i--) {
    if (ctr2 >= k) break;
    if (isvowel(s2[i])) ctr2++;
    if (ctr2 >= k) break;
  }
  pos2 = i;
  if (pos1 == -1 || pos2 == -1) return 0;
  int f = 0;
  for (i = pos1, j = pos2; i < l1, j < l2; i++, j++) {
    if (s1[i] != s2[j]) {
      f = 1;
      break;
    }
  }
  if (f)
    return 0;
  else
    return 1;
}
int main() {
  int n, k, i, j, ctr, x, y, z, x1, x2, x3, x4, x5, f = 0;
  vector<int> ans, ans1;
  set<int> s;
  string s1, s2, s3, s4;
  cin >> n >> k;
  string a[4 * n + 1];
  for (i = 1; i <= 4 * n; i++) {
    cin >> a[i];
  }
  ctr = 0;
  for (i = 1; i <= 4 * n; i = i + 4) {
    s1 = a[i];
    s2 = a[i + 1];
    s3 = a[i + 2];
    s4 = a[i + 3];
    x = isry(s1, s2, k);
    y = isry(s2, s3, k);
    z = isry(s3, s4, k);
    x1 = isry(s3, s4, k);
    x2 = isry(s1, s3, k);
    x3 = isry(s2, s4, k);
    x4 = isry(s1, s4, k);
    x5 = isry(s2, s3, k);
    if (x && y && z)
      ans1.push_back(4);
    else if (x && x1)
      ans.push_back(1);
    else if (x2 && x3)
      ans.push_back(2);
    else if (x4 && x5)
      ans.push_back(3);
    else
      ans.push_back(-1);
  }
  for (i = 0; i < ans.size(); i++) {
    if (ans[i] == -1) {
      f = 1;
      break;
    } else
      s.insert(ans[i]);
  }
  if (ans1.size() == n)
    cout << "aaaa";
  else if (s.size() > 1 || f == 1) {
    cout << "NO";
  } else {
    x = *s.begin();
    if (x == 1)
      cout << "aabb";
    else if (x == 2)
      cout << "abab";
    else if (x == 3)
      cout << "abba";
  }
  return 0;
}
