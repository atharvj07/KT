#include <bits/stdc++.h>
using namespace std;
#define FOR(i,k,n) for(int i = (int)(k); i < (int)(n); i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(), a.end()
#define MS(m,v) memset(m,v,sizeof(m))
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
const int MOD = 1000000007;
const int INF = MOD + 1;
const ld EPS = 1e-12;
template<class T> T &chmin(T &a, const T &b) { return a = min(a, b); }
template<class T> T &chmax(T &a, const T &b) { return a = max(a, b); }

/*--------------------template--------------------*/


int n, m, l;
vector<vi> dist, nx;
typedef pair<int, string> Item;

struct Event
{
	int time, office;
	int eve; //  0 -> ??°??£?????????, 1 -> ???????????????????????????
	Item item;

	bool operator < (const Event& e) const 
	{ 
		if (time != e.time) return time > e.time;
		else return eve > e.eve;
	}
};

vector<Item> getItem(int office, set<pair<Item, int>> &que)
{
	ll time = LLONG_MAX / 100; int to = 10000;
	for (auto i : que)
	{
		if (i.second < time)
		{
			time = i.second;
			to = nx[office][i.first.first];
		}
		else if (i.second == time)
		{
			chmin(to, nx[office][i.first.first]);
		}
	}
	vector<Item> res;
	vector<pair<Item, int>> er;
	for (auto i : que)
	{
		if (nx[office][i.first.first] == to)
		{
			er.push_back(i);
			res.push_back(i.first);
		}
	}
	for (auto i : er) que.erase(i);
	return res;
}

int main()
{
	cin.sync_with_stdio(false); cout << fixed << setprecision(10);
	bool start = true;
	while (cin >> n >> m, n)
	{
		if (!start) cout << endl;
		start = false;
		dist.clear(), nx.clear();
		dist.resize(n, vi(n, INF));
		nx.resize(n, vi(n));
		REP(i, n)REP(j, n)
		{
			if (i == j) dist[i][j] = 0;
			nx[i][j] = j;
		}
		REP(i, m)
		{
			int a, b, c; cin >> a >> b >> c;
			a--; b--;
			dist[a][b] = c;
			dist[b][a] = c;
		}
		REP(k, n)REP(i, n)REP(j, n)
		{
			if (dist[i][j] > dist[i][k] + dist[k][j])
			{
				dist[i][j] = dist[i][k] + dist[k][j];
				nx[i][j] = nx[i][k];
			}
			else if (k != i && dist[i][j] == dist[i][k] + dist[k][j])
			{
				nx[i][j] = min(nx[i][j], nx[i][k]);
			}
		}
	
		priority_queue<Event> events;
		cin >> l;
		REP(i, l)
		{
			int a, b, t; string s;
			cin >> a >> b >> t >> s;
			a--; b--;
			events.push(Event{ t,a,1,Item(b, s) });
		}
		vector<bool> officer(n, true);
		vector<set<pair<Item, int>>> que(n); //????????¨??????

		int now = -1;
		vs reach;
		while (1)
		{
			if (events.empty())
			{
				bool f = true;
				REP(i, que.size()) if (!que.empty()) f = false;
				if(f) break;
			}
			if (events.empty() || events.top().time != now)
			{
				bool f = true;
				sort(ALL(reach));
				for(auto i: reach)
				{ 
					cout << i << " " << now << endl;
				}
				reach.clear();
				REP(i, n)
				{
					if (!officer[i] || que[i].empty()) continue;
					f = false;
					vector<Item> send = getItem(i, que[i]);
					int next_office = nx[i][get<0>(send[0])];
					int d = dist[i][next_office];
					officer[i] = false;
					events.push(Event{ now + d * 2 ,i, 0 });
					for (auto item : send)
					{
						events.push(Event{ now + d, next_office,  1, item });
					}
				}
				if (f)
				{
					if (events.empty()) break;
					else now = events.top().time;
				}
				else continue;
			}

			Event tmp = events.top();
			events.pop();
			if (tmp.eve == 0)
			{
				officer[tmp.office] = true;
			}
			else
			{
				if (tmp.item.first == tmp.office)
				{
					reach.push_back(tmp.item.second);
				}
				else
				{
					que[tmp.office].emplace(tmp.item, tmp.time);
				}
			}
		}
	}
	return 0;
}