
import java.util.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main {

	int INF = 1 << 28;
	int dx[] = {-1,0,1,1,1,0,-1,-1};
	int dy[] = {-1,-1,-1,0,1,1,1,0};

	void run() {
		Scanner sc = new Scanner(System.in);
		for(;;) {
			int n = sc.nextInt();
			if( n == 0) break;
			boolean[][] map = new boolean[n+2][n+2];
			for(int i=1;i<=n;i++) {
				String str = sc.next();
				for(int j=1;j<=n;j++) {
					if(str.charAt(j-1) == '1')
						map[i][j] = true;
				}
			}
			int cnt = 0;
			for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) {
				
				if(map[i][j]) for(int k=0;k<8;k++) {
					int d = 0;
					for(int l=0;;l++) {
						if(map[i+dy[k]*l][j-dx[k]*l]) d++;
						else break;
					}
					cnt = max(cnt, d);
				}
			}
			
			System.out.println(cnt);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}
}