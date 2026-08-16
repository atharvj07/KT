import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader(new File("input.txt")));
		PrintWriter pw = new PrintWriter(new File("output.txt"));

		StringTokenizer st;

		st = new StringTokenizer(in.readLine());
		
		int n = Integer.parseInt(st.nextToken()),
			m = Integer.parseInt(st.nextToken()),
			k = Integer.parseInt(in.readLine());
		
		int[][] A = new int[n][m];
		
		st = new StringTokenizer(in.readLine());
		for (int i = 0 ; i < k ; i++) {
			int x1 = Integer.parseInt(st.nextToken()) - 1,
				y1 = Integer.parseInt(st.nextToken()) - 1;
			
			A[x1][y1] = -10000000;
			
			for (int j = 0 ; j < n ; j++) {
				for (int g = 0 ; g < m ; g++) {
					if (A[j][g] == 0 || (A[j][g] > (Math.abs(y1 - g) + Math.abs(x1 - j)))) {
						A[j][g] = (Math.abs(y1 - g) + Math.abs(x1 - j));
					}
				}
			}
		}
		
		int f = 0, h = 0;
		
		for (int i = 0 ; i < n ; i++) {
			for (int j = 0 ; j < m ; j++) {
				if (A[i][j] != -10000000) {
					f = i;
					h = j;
				}
			}
		}
		
		for (int i = 0 ; i < n ; i++) {
			for (int j = 0 ; j < m ; j++) {
				if (A[i][j] > A[f][h] && A[i][j] != -10000000) {
					f = i;
					h = j;
				}
			}
		}
	//	for (int i = 0 ; i < n ; i++) for (int j = 0 ; j < m ; j++) System.out.println(A[i][j]);
		pw.println((f + 1) + " " + (h + 1));
		pw.close();
	}
}
