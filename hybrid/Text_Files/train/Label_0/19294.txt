#include<bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	long long int I,O,T,J,L,S,Z;
	cin>>I>>O>>T>>J>>L>>S>>Z;
	if(I==0||J==0||L==0)
		cout<<O+I/2*2+J/2*2+L/2*2<<endl;
	else{
		if((I%2==0&&J%2==0&&L%2==0)||(I%2==1&&J%2==1&&L%2==1))
			cout<<O+I+J+L<<endl;
		else
			cout<<O+I+J+L-1<<endl;
	}
}
