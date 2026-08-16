#include<cstdio>
#include<cstring>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int n,star;
int cnt[12]; // 数字 i が書かれた牌はあと i 個
int rem[12]; // * が i に成れるのは rem[i] 個まで

bool dfs(int i){
	if(i==12) return star==0;

	if(cnt[i]==0){
		if(dfs(i+1)) return true;
	}

	// i, i, i
	if(cnt[i]+min(star,rem[i])>=3){
		int tmp=min(cnt[i],3);
		cnt[i]-=tmp;
		star-=3-tmp;
		rem[i]-=3-tmp;
		bool res=dfs(i);
		cnt[i]+=tmp;
		star+=3-tmp;
		rem[i]+=3-tmp;
		if(res) return true;
	}

	// i, i+1, i+2
	if(i<=9){
		bool b=true; // i, i+1, i+2 の割り当てが可能かどうか
		int minus=0;
		rep(j,3){
			if(cnt[i+j]==0 && min(star-minus,rem[i+j])==0) b=false;
			if(cnt[i+j]==0) minus++;
		}
		if(b){
			bool used[3]={};
			rep(j,3){
				if(cnt[i+j]>0) cnt[i+j]--, used[j]=true;
				else           star--, rem[i+j]--;
			}
			bool res=dfs(i);
			rep(j,3){
				if(used[j]) cnt[i+j]++;
				else        star++, rem[i+j]++;
			}
			if(res) return true;
		}
	}

	return false;
}

int main(){
	scanf("%d",&n);
	int hai[47],star=0;
	rep(i,3*n+1){
		char s[4]; scanf("%s",s);
		if(s[0]=='*'){
			hai[i]=-1;
			star++;
		}
		else{
			hai[i]=atoi(s)-1;
			cnt[hai[i]]++;
		}
	}

	bool none=true;
	rep(a,12) if(cnt[a]<4) { // 3*n+2 枚目の牌
		hai[3*n+1]=a;
		cnt[a]++;

		rep(i,12) rem[i]=4-cnt[i];

		bool ok=false;
		rep(b,12) if(cnt[b]+star>=2) { // 最後の二つの牌
			int tmp1[47],tmp2[12],tmp3[12];
			memcpy(tmp1,hai,sizeof hai);
			memcpy(tmp2,cnt,sizeof cnt);
			memcpy(tmp3,rem,sizeof rem);

			::star=star;
			int m=3*n+2,two=2;
			rep(i,m) if(two>0 && hai[i]== b) swap(hai[i],hai[m-1]), i--, m--, two--, cnt[b]--;
			rep(i,m) if(two>0 && hai[i]==-1) swap(hai[i],hai[m-1]), i--, m--, two--, rem[b]--, ::star--;
			ok=dfs(0);

			memcpy(hai,tmp1,sizeof hai);
			memcpy(cnt,tmp2,sizeof cnt);
			memcpy(rem,tmp3,sizeof rem);

			if(ok) break;
		}

		if(ok) printf("%d\n",a+1), none=false;

		cnt[a]--;
	}
	if(none) puts("-1");

	return 0;
}