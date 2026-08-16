#include <bits/stdc++.h>
using namespace std;
int main() {
  string s;
  cin >> s;
  list<char> L;
  for (int i = 0; i < s.length(); i++) L.push_back(s[i]);
  list<char>::iterator it1 = L.begin();
  list<char>::iterator it2 = L.begin();
  ++it2;
  for (; it2 != L.end();)
    if (*it1 == *it2) {
      list<char>::iterator tmp1;
      list<char>::iterator tmp2;
      if (it1 == L.begin()) {
        tmp1 = it1;
        ++tmp1;
        ++tmp1;
        tmp2 = it2;
        ++tmp2;
        ++tmp2;
      } else {
        tmp1 = it1;
        --tmp1;
        tmp2 = it2;
        ++tmp2;
      }
      L.erase(it1, ++it2);
      it1 = tmp1;
      it2 = tmp2;
    } else {
      ++it1;
      ++it2;
    }
  for (list<char>::iterator it = L.begin(); it != L.end(); it++) cout << *it;
exit:
  return (0);
}
