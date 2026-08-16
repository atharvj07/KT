#include <bits/stdc++.h>
using namespace std;
int main() {
  int n; cin>>n;
  for(int i=1;i<=9;i++) if(n%i==0&&n/i<10){cout<<"Yes"; return 0;}
  cout<<"No";
}