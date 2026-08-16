#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll OF_MAX = (1LL<<36)-1;
const ll LEN_MAX = 11;
ll LENGTH[LEN_MAX+1];

inline ll mul(const ll &a, const ll &b){
  if(!a || !b)return 0;
  if( b > OF_MAX/a )return OF_MAX+1;
  return a*b;
}

inline int len(const ll &a){
  return upper_bound(LENGTH,LENGTH+LEN_MAX+1,a) - LENGTH;
}

ll N;
int res;
map<ll,int> pows;
vector<ll> power[LEN_MAX+1];

inline int len_cp(const ll &a){
  return (pows.find(a)!=pows.end())?pows[a]:len(a);
}

//0:+ 1:- 2:* 3:/
inline int check(const ll &n, const ll &x, const int &op){
  switch(op){
  case 0:
    return (n>=x)?len_cp(n-x):LEN_MAX;
  case 1:
    return (x>=n)?len_cp(x-n):LEN_MAX;
  case 2:
    return (x && x*(n/x) == n)?len_cp(n/x):LEN_MAX;
  default:
    return (n && x/n && x/(x/n) == n)?len_cp(x/n):LEN_MAX;
  }
}

inline int check_con(const ll &n, const ll &x, const int &op){
  switch(op){
  case 0:
    return (n>=x)?len(n-x):LEN_MAX;
  case 1:
    return (x>=n)?len(x-n):LEN_MAX;
  case 2:
    return (x && x*(n/x) == n)?len(n/x):LEN_MAX;
  default:
    return (n && x/n && x/(x/n) == n)?len(x/n):LEN_MAX;
  }
}

int main(){
  //init LENGTH to measure the length of numbers
  LENGTH[0] = -1; LENGTH[1] = 10;
  for(int i=2;i<=LEN_MAX;i++)LENGTH[i] = LENGTH[i-1]*10; 

  //calculate short powers
  for(ll a=2;mul(a,a)<=OF_MAX;a++){
    ll tmp = a;
    for(ll p=2;(tmp = mul(a,tmp))<=OF_MAX;p++){
      int tmp_len = len(a) + len(p) + 1; 
      if(len(tmp) <= tmp_len)continue;

      if(pows.find(tmp) == pows.end() || pows[tmp] > tmp_len){
	pows[tmp] = tmp_len;
      }
    }
  }

  //divide efficient powers based on length
  for(map<ll,int>::iterator it=pows.begin();it!=pows.end();it++){
    power[it->second].push_back(it->first);
  }

  //possible formula:
  //1: c
  //3: p
  //5: p op c
  //7: p op c op c, p op p
  //9: p op p op c, p op c op p, p op c op c op c, (p - c) * c

  while( scanf("%lld",&N) && (N>=0) ){
    //c and p
    res = len_cp(N);

    //first term of other cases must be p
    for(int l1=3;l1<res-2;l1++)for(ll fp : power[l1]){
	//p op c and p op p
	for(int op=0;op<4;op++)res = min(res, l1+1+check(N,fp,op));
	
	//p +- p op c
	for(int l2=3;l2<res-3-l1;l2++)for(ll sp :power[l2]){	    
	    // p +- p +- c
	    for(int op=0;op<2;op++){
	      if(fp+sp<=OF_MAX)res = min(res, l1+l2+2+check_con(N,fp+sp,op));
	      if(fp-sp>=0)res = min(res, l1+l2+2+check_con(N,fp-sp,op));
	    }

	    // p +- p */ c
	    for(int op=2;op<4;op++){
	      res = min(res, l1+l2+2+check_con(abs(N-fp),sp,op));
	    }
	  }
	if(l1+2>=res)break;

	// p * p op c
	for(int l2=3;l2<res-3-l1;l2++)for(ll sp :power[l2]){
	    if(len(fp*sp)<l1+l2+1)break;
	    if(mul(fp,sp)>OF_MAX)break;
	    for(int op=0;op<4;op++){
	      res = min(res, l1+l2+2+check_con(N,fp*sp,op));
	    }
	  }

	// p / p op c : not needed
	if(l1+2>=res)break;            

	//p * c op cp
	for(ll a=2;;a++){
	  int l2 = len(a);
	  if(l2>=res-3-l1)break;
	  if(mul(fp,a)>OF_MAX)break;
	  if(len(fp*a)<=l1+l2+1)break;
	  for(int op=0;op<4;op++){
	    res = min(res, l1+l2+2+check(N,fp*a,op));
	  }
	}

	if(l1+2>=res)break;

	//p / c op cp
	for(ll a=2;;a++){
	  int l2 = len(a);
	  if(len(fp/a)<=l1+l2+1)break;
	  if(l2>=res-3-l1)break;
	  for(int op=0;op<4;op++){
	    res = min(res,l1+l2+2+check(N,fp/a,op));
	  }
	}

	if(l1+2>=res)break;

	//p +- c op cp is not needed, except p-c+p (the order must be fixed to avoid overflow)
	//in fact, there is no case such that p-c+p is valid but p+p-c is overflow "under constraint [0,2^36-1]"


	if(l1>4)continue;
	if(res<=9)continue;

	//p */ c */ c op c
	int la = 1;
	for(ll a=2;a<100;a++){
	  if(a==10)la++;
	  int lb = 1;
	  if(mul(fp,a)<=OF_MAX && len(fp*a)>l1+la+1){
	    //p * c * c: not needed
	    //p * c / c
	    for(ll b=2;b<100;b++){
	      if(b==10)lb++;
	      if(7<=l1+la+lb)break;
	      for(int op=0;op<4;op++){
		res = min(res, l1+la+lb+3+check_con(N,fp*a/b,op));
	      }
	    }
	  }

	  //p / c * c
	  if(fp>a && len(fp/a)>l1+la+1){
	    lb = 1;
	    for(ll b=2;b<100;b++){
	      if(b==10)lb++;
	      if(7<=l1+la+lb)break;
	      if(mul(fp/a,b)>OF_MAX)break;
	      for(int op=0;op<4;op++){
		res = min(res, l1+la+lb+3+check_con(N,fp/a*b,op));
	      }
	    }

	    //p / c / c
	    lb = 1;
	    for(ll b=2;b<100;b++){
	      if(b==10)lb++;
	      if(7<=l1+la+lb)break;
	      for(int op=0;op<4;op++){
		res = min(res, l1+la+lb+3+check_con(N,fp/a/b,op));
	      }
	    }
	  }

	}

	if(l1<4)continue;
	if(res<=10)continue;
	//(p - c) * c
	//Note that |p| = 4 and |c| = 1 must hold, thus |formula|=10
	for(ll a=1;a<10;a++)for(ll b=1;b<10;b++){
	    if( (fp-a)*b == N )res = min(res,10);
	  }
      }
    printf("%d\n",res);
  }
}