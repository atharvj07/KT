#include <bits/stdc++.h>
typedef long long LL;
using namespace std;

int main(){
  int sum = 0;
  for (int i = 0; i < 5; i ++) {
    int t; cin >> t;
    t = max(40, t);
    sum += t;
  }

  cout << sum/5 << endl;
}
