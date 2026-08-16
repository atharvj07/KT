#include <bits/stdc++.h>
using namespace std;

int main(){
  int d, n;
  cin >> d >> n;
  
  int ans = n + n / 100;
  cout << setprecision(9) << ans * pow(100, d) << endl;
}
