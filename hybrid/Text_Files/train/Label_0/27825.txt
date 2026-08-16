#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

int main()
{
  int N;
  scanf("%d", &N);
  vector<int> A(N);
  for (int i = 0; i < N; ++i)
  {
    int a;
    scanf("%d", &a);
    A[i] = a;
  }
  sort(begin(A), end(A), less<int>());
  
  ll ans = A[N-1] - A[0];
  for (int i = 1; i < N/2; ++i)
  {
    ans += A[N-i] - A[i];
    ans += A[N-i-1] - A[i-1];
  }
  if (N % 2 == 1)
  {
    ans += max(A[N/2+1] - A[N/2], A[N/2] - A[N/2-1]);
  }
  cout << ans << '\n';
}