#include<bits/stdc++.h>
using namespace std;

int main(){
	int x,a,b,n;	cin>>x>>a>>b>>n;
	for(int i=0;i<n;i++){
		string s;	cin>>s;
		switch(s[0]){
			case 'n':
				x=max(x+a,0);
				break;
			case 't':
				x=max(x+b,0);
				break;
			case 'k':
				x=0;
				break;
		}
	}

	cout<<x<<endl;

	return 0;
}

