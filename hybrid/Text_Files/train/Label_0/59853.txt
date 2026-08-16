
import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class Main {

	int INF = 1 << 28;
	//long INF = 1L << 62;
	double EPS = 1e-10;
	int n;
	String[] words;
	
	void run() {
		Scanner sc = new Scanner(System.in);
		for(;;) {
			n = sc.nextInt();
			if(n == 0) break;
			
			words = new String[n];
			for(int i=0;i<n;i++) words[i] = sc.next();
			sort(words, new Comp());
			ArrayList<String> list = new ArrayList<String>();
			for(int i=0;i<n;i++) {
				boolean f = true;
				for(int j=i+1;j<n;j++){
					if(words[j].indexOf(words[i]) >= 0 ) {
						f = false;
						break;
					}
				}
				if(f) list.add(words[i]);
			}
			list.add("");
			words = list.toArray(new String[]{});
			sort(words);
			n = words.length;
			int[][] es = new int[n][n];
			for(int i=0;i<n;i++) for(int j=0;j<n;j++) {
				es[i][j] = words[i].length() - wordsRap(words[i], words[j]);
			}
//			debug(words);
//			debug(es);
			String[][] dp = new String[1<<n][n]; 
			for(String[] a: dp)fill(a, "."); dp[1][0] = "";
			for(int i=1;i<1<<n;i++) for(int j=0;j<n;j++){
				if(dp[i][j].equals(".")) continue;
				for(int k=0;k<n;k++) if( ((i>>k)&1) == 0 ) {
//					debug(i, j, k, dp[i][j]);
					if(dp[i|(1<<k)][k].equals(".") || dp[i|(1<<k)][k].length() > dp[i][j].length() + words[k].length() - es[j][k]) {
						dp[i|(1<<k)][k] = dp[i][j].substring(0, dp[i][j].length()-es[j][k]) + words[k];
					}
					else if(dp[i|(1<<k)][k].length() == dp[i][j].length() + words[k].length() - es[j][k]) {
						String tmp = dp[i][j].substring(0, dp[i][j].length()-es[j][k]) + words[k];
						if(tmp.compareTo(dp[i|(1<<k)][k]) < 0) dp[i|(1<<k)][k] = tmp;
					}
				}
			}
			String ans = ".";
//			debug(dp[(1<<n)-1]);
			for(int i=0;i<n;i++) {
				if(ans.equals(".") || ans.length() > dp[(1<<n)-1][i].length()) ans = dp[(1<<n)-1][i];
				else if(ans.length() == dp[(1<<n)-1][i].length()) {
					if(ans.compareTo(dp[(1<<n)-1][i]) > 0) ans = dp[(1<<n)-1][i];
				}
			}
			
			System.out.println(ans);
		}
	}
	
	class Comp implements Comparator<String> {

		public int compare(String o1, String o2) {
			// TODO 自動生成されたメソッド・スタブ
			return o1.length() - o2.length();
		}
		
	}
	
	int wordsRap(String a, String b) {
//		debug(a.length());
		for(int i=0;i<a.length();i++) if(b.length() != 0 && a.charAt(i) == b.charAt(0)) {
			boolean f = true;
			for(int j=0;j<b.length();j++) {
				if(i+j>=a.length()) break;
				if(a.charAt(i+j) != b.charAt(j)) {
					f = false; break;
				}
			}
			if(!f) continue;
			return i;
		}
		return a.length();
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}