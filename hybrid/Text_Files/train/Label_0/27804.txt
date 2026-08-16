#include<bits/stdc++.h>
using namespace std;
int a,b,c,d;
int main(){
	cin>>a>>b>>c>>d;
	if(a+b>c+d) cout<<"Left"<<endl;
	else if(a+b==c+d) cout<<"Balanced"<<endl;
	else cout<<"Right"<<endl;
	return 0;
} 