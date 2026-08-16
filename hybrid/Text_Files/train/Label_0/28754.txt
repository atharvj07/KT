#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <complex>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#define debug(x) cerr << __LINE__ << " : " << #x << " = " << (x) << endl;

#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 100010

/* Starry Sky Tree */
//0-index

struct StarrySkyTree{
  typedef int Type;
  int segn2;
  vector<Type> data,s_data;
  
  StarrySkyTree(int n){
    for(segn2=1;segn2<n;segn2*=2);
    data.assign(segn2*2,0);
    s_data.assign(segn2*2,0);
  }
  
  //get maximum value of [a,b]
  Type query(int a,int b,int l=0,int r=-1,int k=0){
    if(r==-1) r+=segn2;
    if(r<a || b<l) return -INF; //大きさに注意
    if(a<=l && r<=b) return data[k] + s_data[k];
    return max(query(a,b,l,(l+r)/2,k*2+1),query(a,b,(l+r)/2+1,r,k*2+2))+s_data[k];
  }
  
  //add x to [a,b]
  Type add(int a,int b,Type x,int l=0,int r=-1,int k=0){
    if(r==-1) r+=segn2;
    if(a<=l && r<=b){
      s_data[k]+=x;
    }else if(a<=r && l<=b){
      data[k] = max(add(a,b,x,l,(l+r)/2,k*2+1),add(a,b,x,(l+r)/2+1,r,k*2+2));
    }
    return data[k] + s_data[k];
  }
  
};

bool hasnext[SIZE], hasown[SIZE];
int prevmax[SIZE];

int main(){
  int n, m, x;

  scanf("%d", &n);

  for(int i=0;i<n;i++) prevmax[i] = -1;
  
  for(int i=0;i<n;i++){
    scanf("%d", &m);
    for(int j=0;j<m;j++){
      scanf("%d", &x);
      x--;
      hasnext[i] |= x == i+1;
      hasown[i] |= x == i;
      if(x < i) prevmax[i] = max(prevmax[i], x);
    }
  }

  StarrySkyTree seg(n+1);

  seg.add(1,n, -INF);
  
  for(int i=0;i<n;i++){
    if(!hasown[i] && !hasnext[i]){
      seg.add(prevmax[i]+1, i, 1);
    }

    int res = seg.query(0,i);
    
    seg.add(i+1, i+1, res - seg.query(i+1, i+1));

    if(!hasown[i] && hasnext[i]){
      seg.add(prevmax[i]+1, i, 1);
    }
  }

  cout << n - seg.query(0,n) << endl;
  
  return 0;
}

