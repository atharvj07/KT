#include <iostream>
#include <cmath>
using namespace std;

int main(){
  long n,p;
  cin >> n >> p;
  if(n == 1){
    cout << p << endl;
    return 0;
  } else if(n >= 40){
    cout << 1 << endl;
    return 0;
  }
  int cnt = 0;
  int ans = 1;
  for(int i = 2; i <= p && i <= 1000000  ; i++){
//	  cout << "A" << i << endl;
	  while((p % i) == 0){
		  p/=i;
		  cnt++;
//		  cout << "b p;" << p << "cnt" << cnt << endl;
	  }
	  while(cnt >= n){
		  ans *= i;
		  cnt -= n;
	  }
         cnt = 0;
  }

  cout << ans << endl;
}
