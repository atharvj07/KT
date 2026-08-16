#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int dat[1000000];
int max_idx[2*1000000-1];
int size;
void init(int _size) {
	size=1;
	while(_size>size) size*=2;
	for(int i=0;i<size;i++) {
		if(i<_size) dat[i]=0; else dat[i]=-(1<<30);
	}
	for(int i=size*2-2;i>=0;i--) {
		if(i>=size-1) {
			max_idx[i]=i-(size-1);
		}else {
			max_idx[i]=max_idx[i*2+1];
		}
	}
}
void update(int k,int a) {
	dat[k]+=a;
	k+=size-1;
	while(k>0) {
		k=(k-1)/2;
		if(dat[max_idx[k*2+1]]>=dat[max_idx[k*2+2]]) {
			max_idx[k]=max_idx[k*2+1];
		}else {
			max_idx[k]=max_idx[k*2+2];
		}
	}
}
int Time[1000000];
int main() {
	int N,R,L;
	scanf("%d %d %d",&N,&R,&L);
	init(N);
	int cur=0;
	for(int i=0;i<R;i++) {
		int d,t,x;
		scanf("%d %d %d",&d,&t,&x); d--;
		Time[max_idx[0]]+=t-cur;
		update(d,x);
		cur=t;
	}
	Time[max_idx[0]]+=L-cur;
	int max_time=0,max_id=0;
	for(int i=0;i<N;i++) {
		if(Time[i]>max_time) {
			max_time=Time[i];
			max_id=i;
		}
	}
	printf("%d\n",max_id+1);
}