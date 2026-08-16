#include <iostream>
#include <math.h>
using namespace std;
int main(void)
{
	double x[2],y[2],r[2];
	int n;
	cin >> n;
	while(n--){
		for(int i=0; i<2; i++){
			cin >> x[i] >> y[i] >> r[i];
		}
		double d = sqrt(pow(x[1]-x[0],2)+pow(y[1]-y[0],2));
		if(r[0]+r[1]<d) cout << "0" << endl;
		else if(r[0]>r[1]){
			if(r[0]-r[1]<=d&&d<=r[0]+r[1]) cout << "1" << endl;
			if(d < r[0] -r[1]) cout << "2" << endl;
		}else{
			if(r[1]-r[0]<=d&&d<=r[0]+r[1]) cout << "1" << endl;
			if(d < r[1] -r[0]) cout << "-2" << endl;
		}
	}
	return 0;
}