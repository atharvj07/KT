#include<bits/stdc++.h>
using namespace std;

int main(){
  int w,h;
  cin >> h >> w;
  int a=0;
  char c;
  for(int i=0;i<h*w;i++){
    cin >> c;
    if(c=='#')
      a++;
  }
  cout << (a==h+w-1?"Possible":"Impossible") << endl;
  return 0;
}