#include<iostream>
#include<algorithm>
using namespace std;

int main(){

  long long int a[1000000] = {0};

  a[0] = 1;
  a[1] = 1;
  for(int i=2;i*i<=1000000;i++){
    if(a[i] == 0){
      for(int j=i+i;j<=1000000;j+=i) a[j] = 1;
    }
  }

  int n;

  while(cin >> n, n){
    int ans = 0,t = 0,s = 0;

    while(t < n){
      if(a[s] == 0){
	ans += s;
	t++;
      }
      s++;
    }
    cout << ans << endl;
  }
}