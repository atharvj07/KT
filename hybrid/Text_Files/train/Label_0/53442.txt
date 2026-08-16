import java.awt.Point;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
	public static final int[] dx = {1,0,-1,0};
	public static final int[] dy = {0,-1,0,1};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true) {
			int w = sc.nextInt();
			int h = sc.nextInt();
			if (w == 0) {
				break;
			}
			int[][] m = new int[h][w];
			boolean[][] used = new boolean[h][w];
			for(int i=0;i<h;i++) {
				String s = sc.next();
				for(int j=0;j<w;j++) {
					m[i][j] = s.charAt(j) == '.' ? 0 : s.charAt(j) - '0';
				}
			}
			ArrayList<Piece> pieces = new ArrayList<Piece>();
			for(int i=0;i<h;i++) {
				for(int j=0;j<w;j++) {
					if (m[i][j] != 0 && !used[i][j]) {
						Piece piece = new Piece();
						int blocks = 0;
						int n = m[i][j];
						used[i][j] = true;
						Deque<Point> q = new ArrayDeque<Point>();
						q.offer(new Point(j,i));
						while(!q.isEmpty()) {
							Point p = q.poll();
							piece.shape[blocks++] = p;
							for(int k=0;k<4;k++) {
								int ni = p.y + dy[k];
								int nj = p.x + dx[k];
								if (ni < 0 || ni >= h || nj < 0 || nj >= w) {
									continue;
								}
								if (m[ni][nj] == n && !used[ni][nj]) {
									used[ni][nj] = true;
									q.offer(new Point(nj,ni));
								}
							}
						}
						pieces.add(piece);
					}
				}
			}
			for(int l=0;l<pieces.size();l++) {
				Piece p = pieces.get(l);
				for(int k=0;k<4;k++) {
					m[p.shape[k].y][p.shape[k].x] = l+1; 
				}
			}
			for(Piece p:pieces) {
				for(int k=0;k<4;k++) {
					int pi = p.shape[k].y;
					int pj = p.shape[k].x;
					if (pi >= 1 && m[pi-1][pj] != 0 && m[pi-1][pj] != m[pi][pj]) {
						if (!p.child.contains(m[pi-1][pj]-1)) {
							p.child.add(m[pi-1][pj]-1);
						}
					}
					if (pi == h-1 || (m[pi+1][pj] != 0 && m[pi+1][pj] != m[pi][pj])) {
						p.xr = Math.max(p.xr,pj);
						p.xl = Math.min(p.xl,pj);
					}
					p.xg_x4 += pj;
				}
			}
			boolean stable = true;
			for(int i=0;i<pieces.size();i++) {
				Piece p = pieces.get(i);
				HashSet<Integer> childs = new HashSet<Integer>();
				childs.add(i);
				childs(childs, pieces, p);
				int xgsum = 0;
				for(int j:childs) {
					xgsum += pieces.get(j).xg_x4;
				}
				int n = childs.size();
				stable &= 4 * n * p.xl < xgsum + 2 * n && xgsum + 2 * n < 4 * n * (p.xr+1);
				if (stable == false) {
					break;
				}
			}
			System.out.println(stable ? "STABLE" : "UNSTABLE");
		}
	}
	
	public static void childs(HashSet<Integer> ret,ArrayList<Piece> al,Piece p) {
		for(int i=0;i<p.child.size();i++) {
			int c = p.child.get(i);
			ret.add(c);
			childs(ret, al, al.get(c));
		}
	}
	
	static class Piece {
		Point[] shape = new Point[4];
		int xg_x4 = 0;
		int xl = Integer.MAX_VALUE;
		int xr = Integer.MIN_VALUE;
		ArrayList<Integer> child = new ArrayList<Integer>();
	}

}