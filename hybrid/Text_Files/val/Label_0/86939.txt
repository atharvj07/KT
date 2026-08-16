import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

public class D1105 {
	
	private static class Element implements Comparable<Element>{
		int x;
		int y;
		int dist;
		int pr;
		int pl;

		public Element(int x, int y, int pl, int dist) {
			this.x = x;
			this.y = y;
			this.pl = pl;
			this.dist = dist;
			pr = this.dist/pc[this.pl-1];
			pr = (dist%pc[pl-1]!=0)?pr+1:pr;
		}

		@Override
		public int compareTo(Element e) {
			if(this.pr!=e.pr) return this.pr-e.pr;
			if(this.pl!=e.pl) return this.pl-e.pl;
			return this.dist-e.dist;
		}
	}
	
	private static int[] pc = null;
	
	private static long st = System.currentTimeMillis();

	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new FileReader("F:/books/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s1 = br.readLine().split(" ");
		Integer n = Integer.parseInt(s1[0]);
		Integer m = Integer.parseInt(s1[1]);
		Integer p = Integer.parseInt(s1[2]);
		pc = new int[p];
		String[] s2 = br.readLine().split(" ");
		for (int i = 0; i < s2.length; i++) {
			pc[i] = Integer.parseInt(s2[i]);
		}
		PriorityQueue<Element> Q = new PriorityQueue<Element>();
		char[][] G = new char[n][m];
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			String s3 = br.readLine();
			for (int j = 0; j < m; j++) {
				G[i][j] = s3.charAt(j);
				if(G[i][j]=='#') cnt++;
				if(G[i][j]>=48 && G[i][j]<58) {
					Element e = new Element(i,j,(int)(G[i][j]-48),0);
					Q.add(e);
				}
			}
		}
		Arrays.stream(bfs(Q,G,cnt)).forEach((x)->System.out.print(x+" "));
	}

	private static int[] bfs(PriorityQueue<Element> Q, char[][] G,int cnt) {
		int n = G.length;
		int m = G[0].length;
		int tot = n*m;
		int[][] d = {{-1,0},{0,-1},{1,0},{0,1}};
		int[] ret = new int[pc.length];
		while(!Q.isEmpty()) {
			long en = System.currentTimeMillis();
			if((en-st)>1800) {
				System.out.println(cnt + " " + Q.size());
				return null;
			}
			Element e = Q.poll();
			int x = e.x;
			int y = e.y;
			int dist = e.dist;
			int pl = e.pl;
			if(G[x][y]!='.' && dist != 0) continue;
//			System.out.println(pl + " " + x + " " + y + " " + dist + " " + e.pr);
			G[x][y] = (char)(pl+48);
			ret[pl-1]++;
			cnt++;
			if(cnt>=tot) return ret;
			Arrays.stream(d).forEach((f)->addElement(Q,G,x+f[0],y+f[1],pl,dist+1));
		}
		return ret;
	}

	private static void addElement(PriorityQueue<Element> Q, char[][] G, 
			int x, int y, int pl, int dist) {
		int n = G.length;
		int m = G[0].length;
		if(x<0 || y<0 || x>=n || y>=m) return;
		if(G[x][y]!='.') return;
		Q.add(new Element(x,y,pl,dist));
	}

}
