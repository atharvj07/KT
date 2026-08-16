#include<cstdio>
#include<vector>
#include<utility>
#include<algorithm>
typedef long long LL;
#define pii pair<LL,LL>
using namespace std;
const LL mod=1e9+7;
LL a,b,c,d,ans=0;
LL nowx,nowy,nowz,disx,disy,disz,prex,prey,prez;
vector<pii> vec;
bool cmp(pii a,pii b){
	return a.first*b.second<a.second*b.first;
}
int main(){
	scanf("%lld%lld%lld%lld",&a,&b,&c,&d);
	for (int i=0;i<=d;i++){
		if (i<a){
			vec.push_back(make_pair(i,a));
			vec.push_back(make_pair(a-i-1,a));
		}
		if (i<b){
			vec.push_back(make_pair(i,b));
			vec.push_back(make_pair(b-i-1,b));
		}
		if (i<c){
			vec.push_back(make_pair(i,c));
			vec.push_back(make_pair(c-i-1,c));
		}
	}
	sort(vec.begin(),vec.end(),cmp);
	for (int i=0;i<vec.size();i++){
		nowx=a*vec[i].first/vec[i].second;
		nowy=b*vec[i].first/vec[i].second;
		nowz=c*vec[i].first/vec[i].second;
		disx=min(a-1,prex+d)-max(0LL,prex-d)+1;
		disy=min(b-1,prey+d)-max(0LL,prey-d)+1;
		disz=min(c-1,prez+d)-max(0LL,prez-d)+1;
		if (nowx+d<a) ans=(ans+(nowx-prex)*disy%mod*disz%mod)%mod;
		if (nowy+d<b) ans=(ans+(nowy-prey)*disx%mod*disz%mod)%mod;
		if (nowz+d<c) ans=(ans+(nowz-prez)*disx%mod*disy%mod)%mod;
		prex=nowx,prey=nowy,prez=nowz;
	}
	ans=(ans+(min(a-1,d)+1)*(min(b-1,d)+1)%mod*(min(c-1,d)+1)%mod)%mod;
	printf("%lld",ans);
	return 0;
}