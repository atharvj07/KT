
import java.util.*;
import java.lang.Math.*;

public class Main {
	static Scanner in = new Scanner(System.in);
	static Coor[] p;
	static Coor ori;
	static int n;
	static int dp[];
	static Coor pre[];
	public static void main(String[] args) {
		ori = new Coor(in.nextInt(),in.nextInt());
		n = in.nextInt();
		p = new Coor[n];
		dp = new int[1<<n];
		pre = new Coor[1<<n];
		for (int i = 0;i < n;i++) {
			p[i] = new Coor(in.nextInt(),in.nextInt());
		}
		Arrays.fill(dp,-1);
		dp[0] = 0;
		System.out.println( getdp((1<<n)-1));
		//System.out.printf("%d",0);
		System.out.printf("%d",0);
		trace((1<<n)-1);
		System.out.println();
	}
	static void trace(int mask) {
		if (mask == 0) return;
		if (pre[mask].y == -1) {
			System.out.printf(" %d %d",pre[mask].x+1,0);
			trace( mask - ( 1<< pre[mask].x ) );
		} else {
			System.out.printf(" %d %d %d",pre[mask].x+1,pre[mask].y+1,0);
			trace( mask - ( 1<< pre[mask].x ) - (1<<pre[mask].y));
		}
	}
	static int getdp(int mask) {
		if (dp[mask] != -1) 
			return dp[mask];
		int fr = 0;
		for (int i = 0;i < n;i++) 
			if ( (mask & (1 << i)) != 0 ) {
				fr = i;
				break;
			}
		dp[mask] = getdp( mask - (1 << fr) ) + 2 * p[fr].dist(ori);
		pre[mask] = new Coor(fr,-1);
		for (int i = fr+1;i < n;i++) {
			int to = i;
			if ( (mask & (1 << i)) != 0) {
				int tmp = getdp( mask - (1<<fr) - (1<<i) ) + p[fr].dist(ori) + p[to].dist(ori) + p[fr].dist(p[to]);
				if (tmp < dp[mask]) {
					dp[mask] = tmp;
					pre[mask].y = i;
				}
			}
		}
		return dp[mask];
	}
}

class Coor {
	int x,y;
	Coor(int _x,int _y) {
		x = _x;y = _y;
	}
	int dist(Coor o) {
		return ( (x-o.x) * (x-o.x) + (y-o.y) * (y-o.y) );
	}
}
