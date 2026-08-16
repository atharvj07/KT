#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <cmath>
#include <bitset>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <complex>
#include <unordered_map>
#include <unordered_set>
#include <random>
#include <cassert>
using namespace std;
typedef long long int ll;
typedef pair<int, int> P;

int main()
{
	int n; cin>>n;
  string s[501];
  for(int i=0; i<n; i++){
    cin>>s[i];
  }
  int ctt=0;
  bool nuee[501];
  fill(nuee, nuee+n, 1);
  bool dame=1;
  for(int j=0; j<n; j++){
    bool ok=1;
    for(int i=0; i<n; i++){
      if(s[i][j]=='.'){
        ok=0;
      }else{
        nuee[j]=0;
      }
    }
    if(ok) ctt++;
    if(!nuee[j]) dame=0;
  }
  if(dame){
    cout<<-1<<endl; return 0;
  }
  int ans=2*n;
  for(int i=0; i<n; i++){
    int cty=0;
    for(int j=0; j<n; j++){
      if(s[i][j]=='#') cty++;
    }
    if(cty==n){
      cout<<n-ctt<<endl;
      return 0;
    }
    if(nuee[i]){
      ans=min(ans, n-ctt+n-cty+1);
    }else{
      ans=min(ans, n-ctt+n-cty);
    }
  }
  cout<<ans<<endl;
	return 0;
}