import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.System.exit;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Task5 {
	
	static void swap(int[] ind, int i, int j) {
		int tmp = ind[i];
		ind[i] = ind[j];
		ind[j] = tmp;
	}
	
	static void getAllPerm(int[] ind, int[][] opt){
		perm(ind, opt, 0);
	}
	
	static void perm(int[] ind, int[][] opt, int start) {
		if (start == 4) {
			System.arraycopy(ind, 0, opt[cnt], 0, 4);
			cnt++;
			return;
		}
		for(int i = start; i < 4; i++) {
			swap(ind, i, start);
			perm(ind, opt, start+1);
			swap(ind, i, start);
		}
	}
	
	static int[] getChoices(int[] low, int[] high) {
		Arrays.sort(low);//or use max/min;
		Arrays.sort(high);
		return new int[]{high[1] - low[0], high[0] - low[1]};
	}
	
	static int getMedian(int[] choice) {
		Arrays.sort(choice);
		
		return choice[1];
	}
	
	static long evaluate(int[] currX, int[] currY, int len) {
		currX[1] -= len;
		currX[3] -= len;
		currY[2] -= len;
		currY[3] -= len;
		int xMd = getMedian(currX); 
		int yMd = getMedian(currY);
		long answ = 0;
		for(int i = 0; i < 4; i++) {
			answ += Math.abs(currX[i] - xMd) + Math.abs(currY[i] - yMd);
		}
		
		return answ;
	}
	
	static int cnt;
	
	static void solve() throws IOException{
		int[] X = new int[4];
		int[] Y = new int[4];
		cnt = 0;
		for(int i = 0; i < 4; i++) {
			X[i] = scanInt();
			Y[i] = scanInt();
		}
		int[] ind = {0, 1, 2, 3};
		int[][] opt = new int[24][4];
		getAllPerm(ind, opt);
		long answ = Long.MAX_VALUE;
		for(int i = 0; i < 24; i++) {
			int[] currX = new int[4];
			int[] currY = new int[4];
			for(int j = 0; j < 4; j++) {
				int pos = opt[i][j];
				currX[j] = X[pos];
				currY[j] = Y[pos];
			}
			int[] xChoice = getChoices(new int[] {currX[0], currX[2]}, new int[]{currX[1], currX[3]}); 
			int[] yChoice = getChoices(new int[] {currY[0], currY[1]}, new int[]{currY[2], currY[3]});
			int[] choice = new int[] {xChoice[0], xChoice[1], yChoice[0], yChoice[1]};
			int md = getMedian(choice);
			int len = Math.max(md, 0);
			long tmp = evaluate(currX, currY, len);
			answ = Math.min(answ, tmp);
		}
		
		out.println(answ);
	}
	
	
	static int scanInt() throws IOException{
		return parseInt(scanString());
	}
	
	static long scanLong() throws IOException{
		return parseLong(scanString());
	}
	
	static String scanString() throws IOException{
		if(tok == null || !tok.hasMoreTokens()) {
			tok = new StringTokenizer(in.readLine());
		}
		return tok.nextToken();
	}
	
	static void printCase() {
		out.print("Case #" + test + ": ");
	}

	static void printlnCase() {
		out.println("Case #" + test + ":");
	}
	
	static BufferedReader in;
	static PrintWriter out;
	static StringTokenizer tok;
	static int test;
	
	public static void main(String[] args) {
		try {
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new PrintWriter(System.out);
			int tests = scanInt();
			for(test = 1; test <= tests; test++) {
				solve();
			}
			in.close();
			out.close();
		} catch(Throwable e) {
			e.printStackTrace();
			exit(1);
		}		
	}
}
