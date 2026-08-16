#include <bits/stdc++.h>
using namespace std;
int main() {
  long long t;
  cin >> t;
  while (t--) {
    long long n;
    cin >> n;
    n *= 2;
    long long a[n];
    vector<long long> ve, vo;
    for (long long i = 0; i < n; i++) {
      cin >> a[i];
      if (a[i] % 2 == 0)
        ve.push_back(i + 1);
      else
        vo.push_back(i + 1);
    }
    if (vo.size() % 2 == 0) {
      if (vo.size() == 0) {
        for (long long i = 2; i < ve.size(); i += 2)
          cout << ve[i] << " " << ve[i + 1] << endl;
      } else if (ve.size() == 0) {
        for (long long i = 2; i < vo.size(); i += 2)
          cout << vo[i] << " " << vo[i + 1] << endl;
      } else {
        for (long long i = 0; i < vo.size(); i += 2)
          cout << vo[i] << " " << vo[i + 1] << endl;
        for (long long i = 2; i < ve.size(); i += 2)
          cout << ve[i] << " " << ve[i + 1] << endl;
      }
    } else {
      for (long long i = 1; i < vo.size(); i += 2)
        cout << vo[i] << " " << vo[i + 1] << endl;
      for (long long i = 1; i < ve.size(); i += 2)
        cout << ve[i] << " " << ve[i + 1] << endl;
    }
  }
}
