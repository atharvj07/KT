#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n;
  string str;
  cin >> n >> str;
  vector<long long int> v;
  long long int l = 1;
  for (int i = 1; i < n; i++) {
    if (str[i] == str[i - 1]) {
      l++;
    } else {
      v.push_back(l);
      l = 1;
    }
  }
  v.push_back(l);
  long long int ans = n * (n - 1);
  ans = ans / 2LL;
  long int temp = -(v.front() + v.back());
  for (int i = 0; i < v.size(); i++) temp += 2LL * v[i];
  temp -= (v.size() - 1);
  ans -= temp;
  cout << ans << endl;
}
