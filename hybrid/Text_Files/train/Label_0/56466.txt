
import java.util.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main {

	int INF = 1 << 28;
	int[] ret;
	int[] val = {500, 100, 50, 10, 5, 1};
	int plus = 500;
	void run() {
		Scanner sc = new Scanner(System.in);
		ret = new int[plus];
		fill(ret, INF);
		ret[0] = 0;
		for(int i=0;i<plus;i++) for(int j=0;j<val.length;j++) {
			if( i+val[j] < plus ) ret[i+val[j]] = min(ret[i+val[j]], ret[i]+1);
		}
		
		for(;;) {
			int P = sc.nextInt();
			if(P == 0) break;
			int[] coins = new int[val.length];
			for(int i=val.length-1;i>=0;i--) coins[i] = sc.nextInt();
			int min = INF;
			for(int i = P;i<P+plus;i++) {
				int pay = i;
				int coin = 0;
				for(int j=0;j<val.length;j++) {
					int c = min(pay/val[j], coins[j]);
					pay -= c * val[j];
					coin += c;
				}
				if(pay == 0) min = min(min, coin+ret[i-P]);
//				debug(i, coin);
			}
			
			System.out.println(min);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}
}