#include <bits/stdc++.h>
using namespace std;
#define MAX 100007
int r[MAX];
int a[MAX];
int b[MAX];
int k1[MAX];

int main(){
	int x,k,q;
	cin >> x >> k;
	for(int i=1; i<=k; i++)cin >> r[i];
	r[k+1]=INT_MAX;
	a[0]=0;
	b[0]=x;
	k1[0]=1;
	// printf("%d %d %d\n",a[0],b[0],k1[0]);
	for(int i=1; i<=k; i++){
		int dt=r[i]-r[i-1];
		if(i&1){
			a[i]=max(a[i-1]-dt,0);
			b[i]=max(b[i-1]-dt,0);
			if(a[i]==b[i])k1[i]=(x+1);
			else k1[i]=min(k1[i-1]+max(dt-a[i-1],0),x);
		}
		else{
			a[i]=min(a[i-1]+dt,x);
			b[i]=min(b[i-1]+dt,x);
			if(a[i]==b[i])k1[i]=(x+1);
			else k1[i]=max(k1[i-1]-max(dt-x+a[i-1]+1,0),0);
		}
		// printf("%d %d %d\n",a[i],b[i],k1[i]);
	}
	cin >> q; 
	for(int i=1; i<=q; i++){
		int tq, aq;
		cin >> tq >> aq;
		if(tq==0){cout << aq << endl; continue;}
		int p=lower_bound(r,r+k+2,tq)-r-1;
		int dt=tq-r[p];
		int	res=min(a[p]+max(aq-k1[p]+1,0),b[p]);
		// cout << dt << " " << res << " ";
		res= (p&1) ? min(res+dt,x) :max(res-dt,0);
		// cout << p << " " << res << endl;
		cout << res << endl;
	}
}