#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
#include <utility>

const int drct[2][3][2] = {{{0, 1}, {-1, 0}, {1, 0}}, {{0, -1}, {1, 0}, {-1, 0}}};

int sd_x, sd_y, bottom;

struct State {
	int x, y, bot, up, step;
	
	State() {}
	State(int x, int y, int bot, int up, int step): 
		x(x), y(y), bot(bot), up(up), step(step) {}
};

int NEXT(int x, int t) {
	switch (t) {
		case 0:
			if (x < 5 || (x >= 10 && x < 15)) return x + 5;
			return x - 5;
		case 1:
			if (x < 5) return (x + 4) % 5;
			if (x < 10) return (x + 5 - 10 + 1) % 5 + 10;
			if (x < 15) return (x - 5 - 5 + 4) % 5 + 5;
			return (x - 15 + 1) % 5 + 15;
		case 2:
			if (x < 5) return (x + 1) % 5;
			if (x < 10) return x + 5;
			if (x < 15) return x - 5;
			return (x - 15 + 4) % 5 + 15;
	}
	
	return -1;
}

std::pair<int, int> NEXT(int x, int up, int t) {
	int a = NEXT(x, (up + t) % 3), b;
	switch ((up + t) % 3) {
		case 0:
			b = 0; break;
		case 1:
			if (x < 5 || x >= 15) b = 1;
			else b = 0;
			break;
		case 2:
			if (x < 5 || x >= 15) b = 2;
			else b = 0;
			break;
	}
	return std::make_pair(a, (b + up) % 3);
}

int dist[205][205][20][3];

void BFS() {
	static std::queue<State> que;
	static State now;
	
	que.push(State(0, 0, 0, 0, 0));
	dist[0 + 100][0 + 100][0][0] = 0;
	while (!que.empty()) {
		now = que.front(); que.pop();
		if (now.step >= 100) break;
		for (int t = 0; t < 3; ++t) {
			int xx = now.x + drct[(now.x + now.y) & 1][t][0], 
				yy = now.y + drct[(now.x + now.y) & 1][t][1];
			int fir = NEXT(now.bot, now.up, t).first, 
				sec = NEXT(now.bot, now.up, t).second;
			if (~dist[xx + 100][yy + 100][fir][sec]) continue;
			dist[xx + 100][yy + 100][fir][sec] = now.step + 1;
			que.push(State(xx, yy, fir, sec, now.step + 1));
		}
	}
}

int main() {
	memset(dist, -1, sizeof dist);
	BFS();
	
	while (~scanf("%d%d%d", &sd_x, &sd_y, &bottom) && (sd_x || sd_y || bottom)) {
		int ans = 0x3f3f3f3f;
		for (int t = 0; t < 3; ++t) if (~dist[sd_x + 100][sd_y + 100][bottom][t])
			ans = std::min(ans, dist[sd_x + 100][sd_y + 100][bottom][t]);
		printf("%d\n", ans);
	}
	
	return 0;
}