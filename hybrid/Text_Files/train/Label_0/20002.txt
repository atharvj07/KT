#include <bits/stdc++.h>
using namespace std;
#define modulo 1000000007
#define mod(mod_x) ((((long long)mod_x+modulo))%modulo)
#define Inf 100000000000000000


int main(){
	
	int H,W;
	cin>>H>>W;
	
	vector<int> cnt(26,0);
	
	vector<string> S(H);
	
	for(int i=0;i<H;i++)cin>>S[i];
	
	for(int i=0;i<H;i++){
		for(int j=0;j<W;j++){
			cnt[S[i][j]-'a']++;
		}
	}
	
	int mul_1 = 0,mul_2 = 0;
	if((H*W)%2==1)mul_1 = 1;
	
	if(H%2==1)mul_2 += W/2;
	if(W%2==1)mul_2 += H/2;
	
	int Mul_1 = 0,Mul_2 = 0;
	
	
	for(int i=0;i<26;i++){
		if(cnt[i]%2==1){
			Mul_1 ++;
		}
		if(cnt[i]%4==2||cnt[i]%4==3){
			Mul_2 ++;
		}
	}
	
	if(Mul_1<=mul_1&&Mul_2<=mul_2){
		cout<<"Yes"<<endl;
	}
	else{
		cout<<"No"<<endl;
	}
		
	
	return 0;
}
