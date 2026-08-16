#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
//dp[i]:前i个位置染完的最小花费
//dp[0] = 0, dp[others] = INF
//if(a[i] == b[i]) dp[i] = dp[i-1]
//else dp[i] = min{dp[j] + cost(j+1, i)|max(0, i-k) <= j < i}
//cost(x, y):ceil((sum[i]-sum[j+1])/2)+1=(sum[i]-sum[j+1]+1)/2+1
//dp[i]=min{(2*dp[j]-sum[j+1]+sum[i]+3)/2|max(0, i-k) <= j < i}
//f[j] = 2*dp[j] - sum[j+1]//用长度为k的单调队列维护
//dp[i]=min{(f[j]+sum[i]+3)/2}
//f[i] = 2*dp[i]-sum[i+1]入队
const int maxn =  5e5 + 10;
const int INF = 0x3f3f3f3f;
int n, k;
char s[maxn], t[maxn];
int sum[maxn];
int dp[maxn];
struct Queue {
    struct Node {
        int pos, val;
    }node[maxn];
    int l, r;
    void init() { l = 1, r = 0; }
    void update(int pos, int val) {
        while (l <= r && val < node[r].val) r--;
        node[++r] = Node{pos, val};
        while (l <= r && node[r].pos - node[l].pos >= k) l++;
    }
    int query() {
        if (l > r) return INF;
        return node[l].val;
    }
}que;
int main() {
    scanf("%d%d", &n, &k);
    scanf("%s%s", s+1, t+1);
    sum[0] = 0, t[0] = '#';
    for (int i = 1; i <= n; i++) sum[i] = sum[i-1] + (t[i] != t[i-1]);
    dp[0] = 0;
    que.init();
    que.update(0, 2*dp[0]-sum[1]);
    for (int i = 1; i <= n; i++) {
        dp[i] = INF;
        if (s[i] == t[i]) dp[i] = dp[i-1];
        else {
            //cout << i << ":" << que.query() << endl;
            dp[i] = min(dp[i], (que.query()+sum[i]+3)/2);
        }
        que.update(i, 2*dp[i]-sum[i+1]);
        //cout << dp[i] << "test" << endl;
    }
    printf("%d\n", dp[n]);
    return 0;
}

