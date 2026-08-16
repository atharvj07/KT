#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int days[12]={31,28,31,30,31,30,31,31,30,31,30,31};
int main()
{
	while(true){
		string S;
		cin >> S;
		if(S=="#")break;
		int cou=0;
		for(int i=0;i<(int)S.length();i++){
			if(S[i]=='.')cou++;
		}
		if(cou==2){
			int y=0,m=0,d=0;cou=0;
			for(int i=0;i<(int)S.length();i++){
				if(S[i]=='.'){
					cou++;
					continue;
				}
				if(cou==0){
					y*=10;
					y+=S[i]-'0';
				}
				else if(cou==1){
					m*=10;
					m+=S[i]-'0';
				}
				else{
					d*=10;
					d+=S[i]-'0';
				}
			}
			ll sumday=0;int y1=2013;int m1=1;
			if(y==2012){
				sumday=(ll)(d-21);
			}
			else{
				sumday=11;
				while(y1<y-400){
					y1+=400;
					sumday+=(ll)(366*97+365*303);
				}
				while(y1<y){
					if(y1%400==0)sumday+=(ll)366;
					else if(y1%100==0)sumday+=(ll)365;
					else if(y1%4==0)sumday+=(ll)366;
					else sumday+=(ll)365;
					y1++;
				}
				while(m1<m){
					if(m1==2){
						if(y1%400==0)sumday+=(ll)29;
						else if(y1%100==0)sumday+=(ll)28;
						else if(y1%4==0)sumday+=(ll)29;
						else sumday+=(ll)28;
					}
					else{
						sumday+=(ll)days[m1-1];
					}
					m1++;
				}
				sumday+=(ll)(d-1);
			}
			ll b1,ka1,t1,w1,ki1;
			ki1=sumday%(ll)20;
			sumday/=(ll)20;
			w1=sumday%(ll)18;
			sumday/=(ll)18;
			t1=sumday%(ll)20;
			sumday/=(ll)20;
			ka1=sumday%(ll)20;
			sumday/=(ll)20;
			b1=sumday%(ll)13;
			printf("%lld.%lld.%lld.%lld.%lld\n",b1,ka1,t1,w1,ki1);
		}
		else{
			int b=0,ka=0,t=0,w=0,ki=0;cou=0;
			for(int i=0;i<(int)S.length();i++){
				if(S[i]=='.'){
					cou++;
					continue;
				}
				if(cou==0){
					b*=10;
					b+=S[i]-'0';
				}
				else if(cou==1){
					ka*=10;
					ka+=S[i]-'0';
				}
				else if(cou==2){
					t*=10;
					t+=S[i]-'0';
				}
				else if(cou==3){
					w*=10;
					w+=S[i]-'0';
				}
				else{
					ki*=10;
					ki+=S[i]-'0';
				}
			}
			int y=2012;int m=12;int d=21;
			d+=b*(20*20*18*20)+ka*(20*18*20)+t*(18*20)+w*20+ki;
			while(d>days[m-1]){
				d-=days[m-1];
				m++;
				if(m==13){
					y++;m=1;
					if(y%400==0)days[1]=29;
					else if(y%100==0)days[1]=28;
					else if(y%4==0)days[1]=29;
					else days[1]=28;
				}
			}
			days[1]=28;
			printf("%d.%d.%d\n",y,m,d);
		}
	}
	return 0;
}