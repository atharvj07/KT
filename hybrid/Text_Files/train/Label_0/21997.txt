#include<bits/stdc++.h>
using namespace std;
int main(){
  int a,b,c;
  cin >> a >> b >> c;
  cout << min(b+c,b+min(a+b+1,c));
}
