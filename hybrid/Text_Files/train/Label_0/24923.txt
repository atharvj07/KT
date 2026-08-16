#include <bits/stdc++.h>
using namespace std;
bool is_palindrom(string a) {
  string s_reversed = "";
  for (int i = a.size() - 1; i >= 0; i--) {
    s_reversed += a[i];
  }
  if (a == s_reversed) {
    return true;
  }
  return false;
}
int main() {
  string no = "BCDEFGJKLNPQRSZ";
  string s;
  cin >> s;
  if (s.find_first_of(no) != -1 || is_palindrom(s) == false) {
    cout << "NO" << endl;
    return 0;
  }
  cout << "YES";
  return 0;
}
