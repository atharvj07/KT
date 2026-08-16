import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO ?????????????????????????????????????????????
		BufferedReader br =
				new BufferedReader(new InputStreamReader(System.in));
		int q = Integer.parseInt(br.readLine());

		String X, Y;
		StringBuilder ans = new StringBuilder();
		while (q-- > 0) {
			X = br.readLine();
			Y = br.readLine();
//			System.out.println( solvelcs(X, Y) );
			ans.append( solvelcs(X, Y) + "\n" );
		}

		System.out.print(ans);
	}

	static int[][] memo;

	static boolean[][] ismemoized;

	static int lcs(String X, String Y, int Xi, int Yi) {
		if (Xi == -1 || Yi == -1) return 0;

		if (ismemoized[Xi][Yi]) return memo[Xi][Yi];

		if ( X.charAt(Xi) == Y.charAt(Yi) ) {
			ismemoized[Xi][Yi] = true;
			return memo[Xi][Yi] = lcs(X, Y, Xi-1, Yi-1) + 1;
		}

		ismemoized[Xi][Yi] = true;
		return memo[Xi][Yi] = Math.max( lcs(X, Y, Xi, Yi-1), lcs(X, Y, Xi-1, Yi) );
	}

	public static int solvelcs(String X, String Y) {
		memo = new int[X.length()][Y.length()];
		ismemoized = new boolean[X.length()][Y.length()];

		return lcs(X, Y, X.length()-1, Y.length()-1);
	}
}