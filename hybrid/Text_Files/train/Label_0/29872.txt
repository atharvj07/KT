#include <iostream>
#include <vector>
#include <queue>

struct Point {
	int x;
	int y;
	int cost;
	bool checked;
};
bool operator > (const Point& p, const Point& q) { return p.cost > q.cost; }

int main()
{
	int n, m;
	while (true) {
		std::cin >> n >> m;
		if (n==0) break;
		char** board = new char*[m+2];
		for (int i=0; i<m+2; i++) board[i] = new char[n+2];
		for (int i=0; i<m+2; i++) { board[i][0] = board[i][n+1] = '.'; }
		for (int j=1; j<m+1; j++) { board[0][j] = board[m+1][j] = '.'; }
		for (int i=1; i<=m; i++) {
			for (int j=1; j<=n; j++) std::cin >> board[i][j];
		}
		Point** points = new Point*[m+2];
		for (int i=0; i<m+2; i++) points[i] = new Point[n+2];
		for (int i=0; i<m+2; i++) {
			for (int j=0; j<n+2; j++) {
				points[i][j].x = i;
				points[i][j].y = j;
				points[i][j].cost = m+n;
				points[i][j].checked = false;
			}
		}
		points[0][0].cost = 0;
		std::priority_queue<Point, std::vector<Point>, std::greater<std::vector<Point>::value_type> > pq;
		pq.push(points[0][0]);
		while (!pq.empty()) {
			Point p = pq.top(); pq.pop();
			// std::cout << p.x << " " << p.y << " " << p.cost << " " << p.checked << std::endl;
			points[p.x][p.y].checked = true;
			char c = board[p.x][p.y];
			if (c == '&') {
				std::cout << points[p.x][p.y].cost << std::endl; break;
			}
			if (p.x > 0) {
				if (!points[p.x-1][p.y].checked) {
					char d = board[p.x-1][p.y];
					int cost = (c == '#' && d != '#') ? 1 : 0;
					if (points[p.x-1][p.y].cost > points[p.x][p.y].cost + cost) {
						points[p.x-1][p.y].cost = points[p.x][p.y].cost + cost;
						pq.push(points[p.x-1][p.y]);
					}
				}
			}
			if (p.y > 0) {
				if (!points[p.x][p.y-1].checked) {
					char d = board[p.x][p.y-1];
					int cost = (c == '#' && d != '#') ? 1 : 0;
					if (points[p.x][p.y-1].cost > points[p.x][p.y].cost + cost) {
						points[p.x][p.y-1].cost = points[p.x][p.y].cost + cost;
						pq.push(points[p.x][p.y-1]);
					}
				}
			}
			if (p.x < m+1) {
				if (!points[p.x+1][p.y].checked) {
					char d = board[p.x+1][p.y];
					int cost = (c == '#' && d != '#') ? 1 : 0;
					if (points[p.x+1][p.y].cost > points[p.x][p.y].cost + cost) {
						points[p.x+1][p.y].cost = points[p.x][p.y].cost + cost;
						pq.push(points[p.x+1][p.y]);
					}
				}
			}
			if (p.y < n+1) {
				if (!points[p.x][p.y+1].checked) {
					char d = board[p.x][p.y+1];
					int cost = (c == '#' && d != '#') ? 1 : 0;
					if (points[p.x][p.y+1].cost > points[p.x][p.y].cost + cost) {
						points[p.x][p.y+1].cost = points[p.x][p.y].cost + cost;
						pq.push(points[p.x][p.y+1]);
					}
				}
			}
		}
		for (int i=0; i<m+2; i++) { delete[] board[i]; delete[] points[i]; }
		delete[] board; delete[] points;
	}
	return 0;
}

