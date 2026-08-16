 #include<iostream>
using namespace std;
int gcd(int a,int b){return b?gcd(b,a%b):a;}
int N;
int cnt[1<<20];
int all=0;
bool isp[1<<20];
int main(){
	cin>>N;
	for(int i=0;i<N;i++){
		int A;cin>>A;
		cnt[A]++;
		all=gcd(all,A);
	}
	bool ok=true;
	for(int i=2;i<1<<20;i++){
		int sum=0;
		for(int j=i;j<1<<20;j+=i)
        	sum+=cnt[j];
		if(sum>1)
        	ok=false;
	}
	cout<<(ok?"pairwise coprime":all==1?"setwise coprime":"not coprime")<<endl;
}