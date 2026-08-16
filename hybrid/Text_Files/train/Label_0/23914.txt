#include <iostream>
#include <stack>
#include <stdio.h>
#include <cmath>
#include <utility>
using namespace std;
int main()
{
    int n;
	cin>>n;
	while(n--){
		int ans=0;
		double ax,ay,ar,bx,by,br,d;
		cin>>ax>>ay>>ar>>bx>>by>>br;
		d=sqrt((ax-bx)*(ax-bx)+(ay-by)*(ay-by));
		if(d<abs(ar-br)){//a)b||a(b
			ans=2;
			if(ar<br)ans*=-1;
		}else if(d<=ar+br){
			ans=1;
		}
		cout<<ans<<endl;
	}
    return 0;
}