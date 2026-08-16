#include <bits/stdc++.h>
using namespace std;
int n, l, r;
long long mod;
vector<int> primes;
vector<long long> powPrime, modFact[100000 + 1];
long long modPow(long long a, long long pow, long long m) {
  if (pow == 0) return 1;
  if (pow & 1)
    return (a * modPow(a, pow ^ 1, m)) % m;
  else {
    long long sqrt = modPow(a, pow >> 1, m);
    return (sqrt * sqrt) % m;
  }
}
int numFactorsInFact(int fact, int prime) {
  int res = 0;
  while (fact > 0) {
    fact /= prime;
    res += fact;
  }
  return res;
}
long long inverseInPrimePowMod(int a, int prime) {
  return modPow(a, powPrime[prime] / primes[prime] * (primes[prime] - 1) - 1,
                powPrime[prime]);
}
long long getBaseFactModWithoutPrime(int fact, int prime) {
  long long res = 1;
  while (fact > 0) {
    res *= modFact[fact][prime];
    res %= powPrime[prime];
    fact /= primes[prime];
  }
  return res;
}
long long C(int a, int b) {
  if (b < 0 || b > a) return 0;
  if (a == 0) return 1;
  long long curr = 0;
  long long base = 1;
  for (int i = 0; i < (primes.size()); i++) {
    int af = numFactorsInFact(a, primes[i]);
    int bf = numFactorsInFact(b, primes[i]);
    int cf = numFactorsInFact(a - b, primes[i]);
    long long aa = getBaseFactModWithoutPrime(a, i);
    long long bb = getBaseFactModWithoutPrime(b, i);
    long long cc = getBaseFactModWithoutPrime(a - b, i);
    long long c = modPow(primes[i], af - bf - cf, powPrime[i]);
    c *= aa;
    c %= powPrime[i];
    c *= inverseInPrimePowMod(bb, i);
    c %= powPrime[i];
    c *= inverseInPrimePowMod(cc, i);
    c %= powPrime[i];
    curr += base * (c - curr) * inverseInPrimePowMod(base, i);
    base *= powPrime[i];
    curr %= base;
    curr += base;
    curr %= base;
  }
  return curr;
}
long long solve(int a, int lo, int hi) {
  if (a & 1) {
    return (solve(a - 1, lo - 1, hi - 1) + solve(a - 1, lo + 1, hi + 1)) % mod;
  } else {
    lo = (lo + 1) / 2;
    hi >>= 1;
    if (lo > hi) return 0;
    return ((C(a, a / 2 + lo) - C(a, a / 2 + hi + 1)) % mod + mod) % mod;
  }
}
void calculateMods(long long i, long long m) {
  long long curr = 1;
  for (int j = 0; j < (100000 + 1); j++) {
    if (j % i != 0) {
      curr *= j;
      curr %= m;
    }
    modFact[j].push_back(curr);
  }
}
void findFactors() {
  long long tmod = mod;
  for (long long i = 2; i * i <= tmod; i++) {
    if (tmod % i == 0) {
      primes.push_back((int)i);
      powPrime.push_back(1);
    } else
      continue;
    while (tmod % i == 0) {
      tmod /= i;
      powPrime[powPrime.size() - 1] *= i;
    }
    calculateMods(i, powPrime[powPrime.size() - 1]);
  }
  if (tmod > 1) {
    primes.push_back(tmod);
    powPrime.push_back(tmod);
    calculateMods(tmod, tmod);
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> mod >> l >> r;
  findFactors();
  long long res = 0;
  for (int vips = 0; vips < (n + 1); vips++) {
    res += (C(n, vips) * solve(n - vips, l, r)) % mod;
    res %= mod;
  }
  cout << res << endl;
  return 0;
}
