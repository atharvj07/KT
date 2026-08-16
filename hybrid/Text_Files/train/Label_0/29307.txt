#include <iostream>
using namespace std;

int main() {
	int x,y,i;
	for(i=0;i<7;i++){
		cin>>x>>y;
		x=x-y;
		if(x<0) x=x-0;
		cout<<x<<endl;
	}
	return 0;
}