#include<bits/stdc++.h>
using namespace std;
int main(){
	int alice=0,bob=0;
  	int n;
  cin>>n;
  vector<int >v(n,0);
  for(int i=0;i<n;i++)cin>>v[i];
  sort(v.rbegin(),v.rend());
  for(int i=0;i<n;i++){
  	if(i%2==0)alice+=v[i];
    else bob+=v[i];
  }
  cout<<alice-bob;
}