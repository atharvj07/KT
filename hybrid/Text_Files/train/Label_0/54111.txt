import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UncheckedIOException;
import java.util.StringTokenizer;
//http://www.ipsj.or.jp/07editj/promenade/4304.pdf
//http://algorithms.blog55.fc2.com/blog-entry-131.html
public class Main{
	public static void main(String[] args) {
		SC sc=new SC(System.in);
		int h=sc.nextInt();
		int w=sc.nextInt();
		int[][] plate=new int[h][w];
		int[][] dp=new int[h][w];
		for(int i=0; i<h; i++) {
			for(int j=0; j<w; j++) {
				plate[i][j]=0;
				dp[i][j]=0;
			}
		}
		String s="";
		for(int i=0; i<h; i++) {
			s=sc.nextLine();
			for(int j=0; j<w; j++) {
				if(s.charAt(j*2)=='0') {
					plate[i][j]=0;
				}
				else {
					plate[i][j]=1;
				}
			}
		}
		for(int i=0; i<h; i++) {		//dpループ
			for(int j=0; j<w; j++) {
				if(i>=1 && j>=1) {		//3方向見えるときは、正方形のサイズの制限はない
					if(plate[i][j-1]==1 || plate[i-1][j]==1 || plate[i-1][j-1]==1) {
						//上、左、左上のどれかに壁があるならできる正方形は高々1
						if(plate[i][j]==1) {
							dp[i][j]=0;	//いま見ているところが壁なら正方形はそこにはできない
						}
						else {
							dp[i][j]=1;	//まわりのどれかが壁の時できる正方形は高々1
						}
					}
					else if(plate[i][j]==0){
						dp[i][j]=Math.min(Math.min(dp[i-1][j], dp[i-1][j-1]), Math.min(dp[i-1][j], dp[i][j-1]))+1;
					}
					else if(plate[i][j]==1) {
						dp[i][j]=0;
					}
				}
				else {//もしもいま見ている座標の上、左上、左のいづれかが見ることできないなら　できる正方形のサイズは高々1
					if(plate[i][j]==1) {
						dp[i][j]=0;
					}
					else if(plate[i][j]==0){
						dp[i][j]=1;
					}
				}
			}
		}
		int max=0;
		for(int i=0; i<h; i++) {
			for(int j=0; j<w; j++) {
				max=Math.max(dp[i][j], max);
			}
		}
		pl(max*max);
	}
	public static void pl(Object o) {
		System.out.println(o);
	}
	public static void pl() {
		System.out.println();
	}
	public static void p(Object o) {
		System.out.print(o);
	}
	static class SC {
		private BufferedReader reader = null;
		private StringTokenizer tokenizer = null;
		public SC(InputStream in) {
			reader = new BufferedReader(new InputStreamReader(in));
		}
		public String next() {
			if (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					throw new UncheckedIOException(e);
				}
			}
			return tokenizer.nextToken();
		}
		public int nextInt() {
			return Integer.parseInt(next());
		}
		public long nextLong() {
			return Long.parseLong(next());
		}
		public double nextDouble() {
			return Double.parseDouble(next());
		}
		public String nextLine() {
			try {
				return reader.readLine();
			} catch (IOException e) {
				throw new UncheckedIOException(e);
			}
		}
	}
}
