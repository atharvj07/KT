#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;
typedef long long ll;

int main(){
  int ans=0;
  int n[4];
  for(int i=0;i<4;++i)
    cin >> n[i];
  sort(n,n+4);
  if(n[0]==n[1] && n[2]==n[3] )
    cout << "yes" << endl;
  else
    cout << "no" << endl;
}

