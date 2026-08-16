
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {

	/*
	 * 問題URL : https://onlinejudge.u-aizu.ac.jp/#/problems/0117
	 */

	private static final int INFINITY = Integer.MAX_VALUE/2;

	public static void main(String[] args) throws Exception {
		//入力
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int K[][] = new int[N][N];
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				K[i][j] = INFINITY;
			}
		}
		int m = Integer.parseInt(br.readLine());
		for(int i=0; i<m; i++) {
			String str[] = br.readLine().trim().split(",");
			int a = Integer.parseInt(str[0])-1;
			int b = Integer.parseInt(str[1])-1;
			K[a][b] = Integer.parseInt(str[2]);
			K[b][a] = Integer.parseInt(str[3]);
		}
		String str[] = br.readLine().split(",");
		int start = Integer.parseInt(str[0])-1;
		int goal = Integer.parseInt(str[1])-1;
		int V = Integer.parseInt(str[2]);
		int P = Integer.parseInt(str[3]);

		//Floyd-Warshall法
		for(int k=0; k<N; k++) {
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(K[i][j] > K[i][k] +K[k][j]) {//Integer.MAX_VALUEを使っているとここでオーバーフローを起こしておかしくなる
						K[i][j] = K[i][k] +K[k][j];
					}
				}
			}
		}

		//出力
		System.out.println(V -P -K[start][goal] -K[goal][start]);
	}

}

