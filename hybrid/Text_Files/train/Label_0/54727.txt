import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UncheckedIOException;
import java.util.StringTokenizer;

public class Main{
	static int H,W;
	static int rokkaku;
	public static int[][] tower;
	static int[][][] sixpoint=new int[2][6][2];
	public static void main(String[] args) {
		sixpoint[0][0][0]=-1;
		sixpoint[0][0][1]=-1;
		sixpoint[0][1][0]=0;
		sixpoint[0][1][1]=-1;
		sixpoint[0][2][0]=1;
		sixpoint[0][2][1]=-1;
		sixpoint[0][3][0]=-1;
		sixpoint[0][3][1]=0;
		sixpoint[0][4][0]=1;
		sixpoint[0][4][1]=0;
		sixpoint[0][5][0]=0;
		sixpoint[0][5][1]=1;
		sixpoint[1][0][0]=0;
		sixpoint[1][0][1]=-1;
		sixpoint[1][1][0]=-1;
		sixpoint[1][1][1]=0;
		sixpoint[1][2][0]=1;
		sixpoint[1][2][1]=0;
		sixpoint[1][3][0]=-1;
		sixpoint[1][3][1]=1;
		sixpoint[1][4][0]=0;
		sixpoint[1][4][1]=1;
		sixpoint[1][5][0]=1;
		sixpoint[1][5][1]=1;
		SC sc=new SC(System.in);
		W=sc.nextInt();
		H=sc.nextInt();
		tower=new int[H+2][W+2];
		for(int i=0; i<=H+1; i++) {
			for(int j=0; j<=W+1; j++) {
				tower[i][j]=0;
			}
		}
		for(int i=0; i<H; i++) {
			for(int j=0; j<W; j++) {
				tower[i+1][j+1]=sc.nextInt();
			}
		}
		rokkaku=0;
		dfs(0,0);
		for(int i=0; i<=H+1; i++) {
			for(int j=0; j<=W+1; j++) {
				if(tower[i][j]==0) {
					tower[i][j]=1;	//埋め立て
				}
				if(tower[i][j]==1) {
					rokkaku++;
				}
			}
		}
		rokkaku*=6;
		for(int i=0; i<=H+1; i++) {
			for(int j=0; j<=W+1; j++) {
				if(tower[i][j]==1) {
					rinsetu(i,j);
				}
			}
		}
		pl(rokkaku);
	}
	public static void dfs(int y,int x) {
		tower[y][x]=2;	//塗りつぶして、外から見えない部分の塗りつぶしで浮き上がらせる
		for(int i=0; i<6; i++) {
			if(y%2==0) {
				if(0<=y+sixpoint[0][i][0] && y+sixpoint[0][i][0]<=H+1) {
					if(0<=x+sixpoint[0][i][1] && x+sixpoint[0][i][1]<=W+1) {
						if(tower[y+sixpoint[0][i][0]][x+sixpoint[0][i][1]]==0) {
							dfs(y+sixpoint[0][i][0],x+sixpoint[0][i][1]);
						}
					}
				}
			}
			else if(y%2==1) {
				if(0<=y+sixpoint[1][i][0] && y+sixpoint[1][i][0]<=H+1) {
					if(0<=x+sixpoint[1][i][1] && x+sixpoint[1][i][1]<=W+1) {
						if(tower[y+sixpoint[1][i][0]][x+sixpoint[1][i][1]]==0) {
							dfs(y+sixpoint[1][i][0],x+sixpoint[1][i][1]);
						}
					}
				}
			}
		}
	}
	public static void rinsetu(int y,int x) {
		int a=0;
		for(int i=0; i<6; i++) {
			if(y%2==0) {
				if(tower[y+sixpoint[0][i][0]][x+sixpoint[0][i][1]]==1) {
					rokkaku--;
					a++;
				}
			}
			else if(y%2==1) {
				if(tower[y+sixpoint[1][i][0]][x+sixpoint[1][i][1]]==1) {
					rokkaku--;
					a++;
				}
			}
		}
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
