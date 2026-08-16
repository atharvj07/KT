#include <iostream>
using namespace std;
int main(){
  int a,b;
  cin >> a >> b;
  int x=max(a,b);
  int y=min(a,b);
  for(int i=0;i<x;i++){
    cout << y;
  }
}
