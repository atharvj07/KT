#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mx 1

int main()
{	
	ios_base::sync_with_stdio(0);
	int n,a;
	cin>>n;
	int fours=0,twos=0;
	for(int i=1; i<=n; i++){
		cin>>a;
		if(a%4==0) fours++;
		else if(a%2==0) twos++;
	}
	if(fours+fours+1 >=n || fours+fours+twos >=n) cout<<"Yes"<<endl;
	else cout<<"No"<<endl;
}

