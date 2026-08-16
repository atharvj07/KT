#include<iostream>
#include<vector>
#include<math.h>
#include<complex>

#define EPS 1e-4

#define PI 3.141592
#define EQ(a,b) (abs((a)-(b))<EPS)
using namespace std;

typedef complex<double> P;

vector<P> house;
vector<P> ume,sak,mo;

double cross(P v1,P v2){
	return v1.real()*v2.imag()-v1.imag()*v2.real();
}

bool che(P h,P t,double d,double w,double a){
	P v=h-t;
	if(!(abs(v)<a))return false;
	
	P v1=P(a*cos((w+d/2)/180*PI),a*sin((w+d/2)/180*PI));
	P v2=P(a*cos((w-d/2)/180*PI),a*sin((w-d/2)/180*PI));
	
	if(cross(v1,v)<0 && cross(v2,v)>0)return true;
	else return false;
}

int main(){
	int h,r;
	
	while(cin>>h>>r && h&&r){
		house.clear();
		ume.push_back(P(0,0));
		for(int i=0;i<h;i++){
			int x,y;
			cin>>x>>y;
			house.push_back(P(x,y));
		}
		
		int U,M,S,du,dm,ds;
		cin>>U>>M>>S>>du>>dm>>ds;
		for(int i=0;i<U;i++){
			int x,y;
			cin>>x>>y;
			ume.push_back(P(x,y));
		}
		for(int i=0;i<M;i++){
			int x,y;
			cin>>x>>y;
			mo.push_back(P(x,y));
		}
		for(int i=0;i<S;i++){
			int x,y;
			cin>>x>>y;
			sak.push_back(P(x,y));
		}
		
		
		int data[120];
		for(int i=0;i<120;i++)data[i]=0;
		for(int z=0;z<r;z++){
			int w,a;
			cin>>w>>a;
			
			for(int i=0;i<house.size();i++){
				bool ok=false;
				if(che(house[i],ume[0],du,w,a))ok=true;
				else continue;
				for(int j=1;j<=U;j++){
					if(che(house[i],ume[j],du,w,a))ok=false;
				}
				for(int j=0;j<M;j++){
					if(che(house[i],mo[j],dm,w,a))ok=false;
				}
				for(int j=0;j<S;j++){
					if(che(house[i],sak[j],ds,w,a))ok=false;
				}
				
				if(ok)data[i]++;
			}
		}
		
			int ans=0;
			int tmp=-1;
			for(int i=0;i<h;i++){
				if(ans<=data[i]){
					ans=data[i];
					tmp=i;
				}
			}
			if (ans==0)cout<<"NA"<<endl;
			else {
				for(int i=0;i<h;i++){
					if(i==tmp)cout<<i+1;
					else if(data[i]==ans)cout<<i+1<<" ";
					
				}
				cout<<endl;
			}
			
		
	}
}