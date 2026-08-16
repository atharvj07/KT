#include<iostream>
#include<algorithm>
using namespace std;
string S,T,V="AIZUNYAN";
int main(){
	cin>>S;T=S;
	if(S.size()<8){cout<<S<<endl;return 0;}
	for(int i=0;i<S.size()-7;i++){
		string U=S.substr(i,8);
		char p[8];
		for(int j=0;j<8;j++){p[j]=U[j];}
		sort(p,p+8);U="";
		for(int j=0;j<8;j++){U+=p[j];}
		if(U=="AADINNUY"){
			for(int j=0;j<8;j++){
				T[i+j]=V[j];
			}
		}
	}
	cout<<T<<endl;
	return 0;
}