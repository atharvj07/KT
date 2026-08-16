#include <bits/stdc++.h>
using namespace std;
bool composite[1000000];
vector<int> primes;
void sieve() {
  for (int i = 2; i < 1000000; i++) {
    if (composite[i]) continue;
    primes.push_back(i);
    for (int j = i + i; j < 1000000; j += i) {
      composite[j] = true;
    }
  }
}
int main() {
  long n;
  cin >> n;
  sieve();
  vector<int> emirp;
  for (int i = 0; i < primes.size(); i++) {
    stringstream ss;
    ss << primes[i];
    string s = ss.str();
    for (int j = 0; j < s.length() / 2; j++) {
      char temp = s[j];
      s[j] = s[s.length() - 1 - j];
      s[s.length() - 1 - j] = temp;
    }
    stringstream ss2;
    ss2 << s;
    int x;
    ss2 >> x;
    if (!composite[x] && x != primes[i]) emirp.push_back(primes[i]);
  }
  cout << emirp[n - 1] << endl;
  return 0;
}
