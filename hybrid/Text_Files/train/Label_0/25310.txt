#include <bits/stdc++.h>
using namespace std;

int main() {
  int N,K; cin >> N >> K;
  long ans = 15000000000;
  vector<long> a(N);
  for (int i =0; i<N; i++) cin >> a[i]; 
  vector<long> maxA(N); maxA[0] = a[0];
  for (int i =1; i<N; i++)  
    maxA[i] = max(a[i-1],maxA[i-1]);
  
  for (int i =0; i< (1<<(N-1)); i++) {
    bitset<14> bit(i);
    long count =0;
    if (bit.count() == K-1) {
      long tmp = a[0]; int k =0; 
      for (int j =0; j<N-1; j++) {
        if (bit.test(j)) {
          k++;
          tmp = max(tmp,maxA[j+1]);
          if (a[j+1] - tmp <= 0) {
            count += tmp - a[j+1] + 1;
            tmp = tmp + 1;
          } else {
            tmp = a[j+1];
          }
          if (k == K) break;
        }
      }
      ans = min(count,ans);
    }
  }
  cout << ans << endl;  
}