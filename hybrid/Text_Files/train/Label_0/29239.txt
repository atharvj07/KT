#include <iostream>
#include <cmath>

using namespace std;

int main(){
  long long N, P;
  cin >> N >> P;
  if (N == 1) {
    cout << P;
    return 0;
  }

  long long max_ans = pow(P, 1.0 / double(N)) + 10;
  
  for (long long d = max_ans; d > 0; d--) {
    long long num = pow(d, N);

    if (P % num == 0) {
      cout << d << endl;
      break;
    }
  }
  return 0;
}
