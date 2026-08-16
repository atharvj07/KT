#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
using namespace std;
using namespace std;
int main() {
  string str;
  cin >> str;
  if (str.find_first_of("HQ9") != string::npos) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
}
