#include <bits/stdc++.h>
using namespace std;

int prime[300000];
void make_prime(){
  prime[0] = prime[1] = 1;
  for(int i = 2; i * i <= 300000; i++){
    if(!prime[i]){
      for(int j = i; i * j < 300000; j++){
        prime[i*j] = 1;
      }
    }
  }
}

int main(){
  int n, p;
  make_prime();
  while(cin >> n >> p){
    if(n == -1 && p == -1) break;
    int idx = n, cnt = 0;
    int sum[100] = {};
    while(cnt < 100){
      idx++;
      if(prime[idx] == 0){
        sum[cnt] = idx;
        cnt++;
      }
    }
    vector<int> ans;
    for(int i = 0; i < 100; i++){
      for(int j = i; j < 100; j++){
        ans.push_back(sum[i] + sum[j]);
      }
    }
    sort(ans.begin(), ans.end());
    cout << ans[p-1] << endl;
  }
  return 0;
}

