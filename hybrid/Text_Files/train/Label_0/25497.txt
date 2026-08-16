#include <bits/stdc++.h>

using namespace std;

int main(int argc, char**argv) {
  long n;
  cin >> n;

  unordered_map<long, int> lookup;
  for (long i = 1; i <=n; i++) {
    auto val = abs((n -i) - (i-1));
    lookup[val]++;
  }

  unordered_map<long, int> a;
  for (int i = 0; i< n; i++) {
    long aa;
    cin >> aa;
    a[aa]++;
  }

  if (lookup != a) {
    cout << 0 << endl;
    return 0;
  }

  long mod = 1e9 + 7;
  long result = 1;
  for (int i = 0; i < n / 2; i++) {
    result = (2 * result) % mod;
  }
  cout << result << endl;


  return 0;
}
