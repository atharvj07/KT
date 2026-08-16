#include <bits/stdc++.h>
#define LL long long int
using namespace std;

LL n,s;

int check(LL b){
	LL sum=0,tmp=n;
	while(tmp){
		sum+=tmp%b;
		tmp/=b;
	} 
	return sum==s;
}

int check(int i,LL sum){
	LL x0=s-i;
	LL b=sum/i+1;
	return x0>=0 && x0<b && i<b;
}

int main(){
	cin>>n>>s;
	LL sn=(LL)sqrt(n)+1;
	for(int i=2;i<=sn;i++){
		if(check(i)){
			cout<<i<<endl;
			return 0;
		}
	}
	
	if(n<=s){
		if(n<s) cout<<-1<<endl;
		else cout<<n+1<<endl;
		return 0;
	}
	
	LL sum=n-s;
	sn=sum/sn+1;
	for(int i=sn;i>=1;i--){
		if(sum%i==0 && check(i,sum)){
			cout<<sum/i+1<<endl;
			return 0;
		}
	}
	cout<<-1<<endl;
	return 0;
} 