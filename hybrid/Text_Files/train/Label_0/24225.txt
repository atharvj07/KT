#include<bits/stdc++.h>
using namespace std;
 
#define int long long
pair<int,int> b[55][55];
 
signed main(){
  int n;
  cin >> n;
 
  int a[n+1];
 
  for(int i= 0;i<n;i++){
    cin >> a[i];
 
    for(int j = 1;j<=a[i];j++){
      cin >> b[i][j].first >> b[i][j].second ;
      b[i][j].first--;
    }
  }
    int ans = 0;
  for(int i = 0; i<(1<<n) ;i++){
    bool flag = true;
    for(int j = 0;j<n;j++){
      if(i&(1<<j)){
        for(int k = 1;k<=a[j] ; k++){
          if(b[j][k].second != (bool)(i&(1<<b[j][k].first)))flag = false;
        }
    }
    }
          if(flag) ans = max(ans, (int)__builtin_popcount(i));
  
    }
 
    cout << ans <<'\n';
}