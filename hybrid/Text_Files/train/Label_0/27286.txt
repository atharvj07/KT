#include <bits/stdc++.h>
#define N 400500
#define int long long
using namespace std;
int Ans, mx[3][3][N << 2], X, Y, m, n, num[N], cnt;
struct Data{int c, l, r;}d[N];
bool cmpl(Data a, Data b){return a.l < b.l;}
void pushup(int rt, int c){
	for(int i = 0; i < 3; i++)
		mx[c][i][rt] = max(mx[c][i][rt << 1], mx[c][i][rt << 1 | 1]);
}
void build(int rt, int l, int r){
	if(l == r){
		for(int i = 0; i < 3; i++){
			mx[i][0][rt] = 0;
			mx[i][1][rt] = X * (-1 - num[l]);
			mx[i][2][rt] = (X + X + Y) * (-1 - num[l]);
		}
		return ;
	}
	int mid = (l + r) >> 1;
	build(rt << 1, l, mid);
	build(rt << 1 | 1, mid + 1, r);
	pushup(rt, 0);pushup(rt, 1);pushup(rt, 2);
}
void update(int rt, int l, int r, int x, int y, int c){
	if(l == r){
		mx[c][0][rt] = max(mx[c][0][rt], y);
		mx[c][1][rt] = mx[c][0][rt] + X * (-1 - num[l]);
		mx[c][2][rt] = mx[c][0][rt] + (X + X + Y) * (-1 - num[l]);
		return ;
	}
	int mid = (l + r) >> 1;
	if(x <= mid) update(rt << 1, l, mid, x, y, c);
	else update(rt << 1 | 1, mid + 1, r, x, y, c);
	pushup(rt, c);
}
int query(int rt, int l, int r, int x, int y, int c, int d){
	if(x <= l && r <= y) return mx[c][d][rt];
	int mid = (l + r) >> 1;
	if(y <= mid) return query(rt << 1, l, mid, x, y, c, d);
	if(x > mid) return query(rt << 1 | 1, mid + 1, r, x, y, c, d);
	return max(query(rt << 1, l, mid, x, y, c, d),
			   query(rt << 1 | 1, mid + 1, r, x, y, c, d));
}
signed main(){
	scanf("%lld%lld%lld%lld", &n, &m, &X, &Y);
	for(int i = 1; i <= m; i++){
		scanf("%lld%lld%lld", &d[i].c, &d[i].l, &d[i].r);
		d[i].c--;
		num[++cnt] = d[i].l;
		num[++cnt] = d[i].r;
	}
	sort(num + 1, num + cnt + 1);
	cnt = unique(num + 1, num + cnt + 1) - num - 1;
	sort(d + 1, d + m + 1, cmpl);
	for(int i = 1; i <= m; i++){
		d[i].l = lower_bound(num + 1, num + cnt + 1, d[i].l) - num;
		d[i].r = lower_bound(num + 1, num + cnt + 1, d[i].r) - num;
	}
	build(1, 0, cnt);
	for(int i = 1; i <= m; i++){
		int ans = LLONG_MIN;
		for(int j = 0; j < 3; j++){
			ans = max(ans, query(1, 0, cnt, 0, d[i].l - 1, j, 0));
			if(d[i].l < d[i].r){
				if(j == d[i].c) ans = max(ans, query(1, 0, cnt, d[i].l, d[i].r - 1, j, 1) + num[d[i].l] * X);
				else ans = max(ans, query(1, 0, cnt, d[i].l, d[i].r - 1, j, 2) + num[d[i].l] * (X + X + Y));
			}
		}
		ans += (num[d[i].r] - num[d[i].l] + 1) * X;
		update(1, 0, cnt, d[i].r, ans, d[i].c);
	}
	for(int i = 0; i < 3; i++)
		Ans = max(Ans, query(1, 0, cnt, 0, cnt, i, 0));
	printf("%lld\n", Ans);
	return 0;
}
