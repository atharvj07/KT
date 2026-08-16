#include<cstdio>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;
long long n,h,d,p,y,x,z;
deque<pair<long long,long long> > w;

int main(){
  scanf("%lld%lld", &n, &p);
  y = p;
  for(int i = 0;i < n - 1;i++){
    scanf("%lld%lld", &d, &h);
    while(!w.empty() && w.back().first < h){
      w.pop_back();
    }
    w.push_back(make_pair(h, x));
    x += d;
    while(p <= x){
      long long int tmpp = p ;
      while(!w.empty() && tmpp + w.front().first - w.front().second > y){
	p = max(p, w.front().second + y);
	w.pop_front();
      }
      if(!w.empty()){
	p = max(p, tmpp + w.front().first);
	int tmp = max(0ll, min((x - p) / w.front().first, (w.front().second + y - p) / w.front().first));
	z += tmp;
	p += tmp * w.front().first;
      }
      z++;
    }
  }
  printf("%lld\n", z);
  return 0;
}