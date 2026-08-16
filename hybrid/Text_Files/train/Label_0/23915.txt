#include<iostream>
#include<math.h>

using namespace std;

int main(){
  int n;
  cin >> n;
  for(int i=0;i<n;i++){
	double xa,ya,ra,xb,yb,rb,l;
	cin >> xa >> ya >> ra >> xb >> yb >> rb;
	l = sqrt(pow((xa-xb),2)+pow((ya-yb),2));
	if(l > ra + rb) 
	  cout << 0 << endl;	
	else if(ra > l + rb) 
	  cout << 2 << endl;	
	else if(rb > l + ra) 
	  cout << -2 << endl;	
	else 
	  cout << 1 << endl;  
  }
  return 0;
}