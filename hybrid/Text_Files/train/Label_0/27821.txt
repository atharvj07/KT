#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  vector<long long> A(N);
  for (int i=0; i<N; i++) cin >> A[i];
  sort(A.begin(), A.end());
  long long ans = 0;
  long long lef=A[0];
  long long rig=A[N-1];
  ans += rig-lef;
  int i=1, j=N-2;
  while(i<=j){
    // cout << ans << endl;
    long long hoge = max(max(abs(lef-A[i]),abs(lef-A[j])),max(abs(rig-A[i]),abs(rig-A[j])));
    if (hoge==abs(lef-A[i])){
      ans += abs(lef-A[i]);
      lef = A[i];
      i++;
    }
    else if (hoge==abs(lef-A[j])){
      ans += abs(lef-A[j]);
      lef = A[j];
      j--;
    }
    else if (hoge==abs(rig-A[i])){
      ans += abs(rig-A[i]);
      rig = A[i];
      i++;
    }
    else {
      ans += abs(rig-A[j]);
      rig = A[j];
      j--;
    }
  }
  cout << ans << endl;
}
