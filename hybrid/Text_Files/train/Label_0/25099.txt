#include <bits/stdc++.h>
#define r(i,n) for(int i=0;i<n;i++)
#define int long long
using namespace std;
typedef pair<int,int>P;
#define fi first
#define se second


signed main(){
  int n,s=0;
  cin>>n;
  while(n--){
    int a;
    cin>>a;
    if(a%2==0)s++;
  }
  cout<<s<<endl;
}

