#include <cstdio>
#include <vector>

using namespace std;

bool table[105000];
vector<int> primes;

int main() {
  table[2] = true;
  for (int i = 3; i < 105000; i += 2)
    table[i] = true;
  for (int i = 3; i <= 324; i += 2)
    if (table[i])
      for (int j = 3 * i; j < 105000; j += 2 * i)
        table[j] = false;
  primes.push_back(2);
  for (int i = 3; i <= 105000; i += 2)
    if (table[i])
      primes.push_back(i);
  for (int i = 1; i < 10000; i++)
    primes[i] += primes[i-1];
  for (int n; scanf("%d", &n) == 1 && n;)
    printf("%d\n", primes[n-1]);
  return 0;
}