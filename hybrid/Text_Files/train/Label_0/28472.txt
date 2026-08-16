#include<iostream>
#include<algorithm>
using namespace std;
int n;
int t[100][100];
int u[100],v[100];

void solve(){
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      if(u[i]!=v[j])continue;
      cout<<t[i][j]<<endl;
      return;
    }
  }
  cout<<0<<endl;
}

int main(){
  while(cin>>n&&n){
    for(int i=0;i<n;i++){
      u[i]=1e8;v[i]=-1;
      for(int j=0;j<n;j++){
	cin>>t[i][j];
      }
    }
    
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	u[i]=min(u[i],t[i][j]);
	v[j]=max(v[j],t[i][j]);
      }
    }
    
    solve();

  }
  return 0;
}