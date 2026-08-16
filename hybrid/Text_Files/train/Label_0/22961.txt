#include<iostream>
#include<string>
#include<algorithm>
#include<sstream>
using namespace std;
int stoi(string a){
		int b;
		stringstream ss;
		ss<<a;
		ss>>b;
		return b;
	}
	string itos(int a){
		stringstream ss;
		ss <<a;
		string b;
		b=ss.str();
		return b;
	}

int main(){
	string n;int t;
	while(cin>>n,n!="0000"){
		int ns=n.size();
		for(int i=0;i<4-ns;i++)n="0"+n;
		int ans=0;
		bool flag=true;
		if(n[0]==n[1]&&n[1]==n[2]&&n[2]==n[3])flag=false;
		
		if(flag){
			while(n!="6174"){
			//	cout<<n<<endl;
				//cin>>t;
				int a[4]={0},b[4]={0},ai,bi;
				for(int i=0;i<4;i++)a[i]=n[i]-'0',b[i]=n[i]-'0';
				sort(a,a+4);
				sort(b,b+4);
				reverse(b,b+4);
				int tmp=0,l,s;
				l=1000*b[0]+100*b[1]+10*b[2]+b[3];
				s=1000*a[0]+100*a[1]+10*a[2]+a[3];
			//	cout<<s<<" "<<l<<endl;
				tmp=l-s;
				n=itos(tmp);
				ns=n.size();
				for(int i=0;i<4-ns;i++)n="0"+n;
				ans++;
			}
		}
		if(flag)cout<<ans<<endl;
		else cout<<"NA"<<endl;
	}
	return 0;
}