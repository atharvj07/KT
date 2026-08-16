#include <iostream>
using namespace std;

int main(void){
	int n;
	cin >> n;
	for(int i=0;i<n;++i){
		double xa,ya,ra,xb,yb,rb,ab;
		cin >> xa >> ya >> ra >> xb >> yb >> rb;
		double d_2 = (xa-xb)*(xa-xb)+(ya-yb)*(ya-yb);
		if(d_2>(ra+rb)*(ra+rb)){
			cout << "0\n";
		}else if(d_2==(ra+rb)*(ra+rb)){
			cout << "1\n";
		}else{
			if(d_2<(ra-rb)*(ra-rb)&&(ra>rb)){
				cout << "2\n";
			}else if(d_2<(rb-ra)*(rb-ra)&&(ra<rb)){
				cout << "-2\n";
			}else{
				cout << "1\n";
			}
		}
	}
	return 0;
}