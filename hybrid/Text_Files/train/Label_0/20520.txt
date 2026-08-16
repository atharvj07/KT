#define INT_MAX 2147483647
#include<bits/stdc++.h>
using namespace std;

const int MAX_N=10000000;
 
int n;
int dat[MAX_N*2-1];
 
void init(){
    int i=n;
    n=1;

	while (n<i)n*=2;
	
	fill(dat,dat+n*2,INT_MAX);
}
 
void update(int i,int x){
	i+=n-1;
	dat[i]=x;
	while(i>0){
		i=(i-1)/2;
		dat[i]=min(dat[i*2+1],dat[i*2+2]);
	}
}
 
int query(int a,int b,int k,int l,int r){
	if(r<a||b<l)return INT_MAX;
	if(a<=l&&r<=b) return dat[k];
	else{
		int vl=query(a,b,k*2+1,l,(l+r)/2);
		int vr=query(a,b,k*2+2,(l+r)/2+1,r);
	    return min(vl,vr);
	}
}

int main(){
    int q,a,b,c;
    cin>>n>>q;
    
    init();
    
    while(q--){
        cin>>a>>b>>c;
        if(a)cout<<query(b,c,0,0,n-1)<<endl;
        else update(b,c);
        
        /*for(int i=0;i<n*2;i++){
            cout<<dat[i]<<" ";
        }
        cout<<endl;*/
    }
    
}