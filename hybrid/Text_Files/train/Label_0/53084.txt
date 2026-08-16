import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static final int BIG_NUM = 2000000000;
	public static final int MOD = 1000000007;

	public static void main(String[] args) {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input[] = new String[2];

		try {
			input = br.readLine().split("\\s+");
			int N = Integer.parseInt(input[0]);
			int T = Integer.parseInt(input[1]);

			int table[] = new int[T+1];
			for(int i = 0; i < table.length; i++){
				table[i] = 0;
			}

			int left,right;

			for(int loop = 0; loop < N; loop++){

				input = br.readLine().split("\\s+");

				left =  Integer.parseInt(input[0]);
				right = Integer.parseInt(input[1]);

				table[left]++;
				table[right]--;
			}

			int ans = table[0];
			for(int i = 1; i < table.length; i++){
				table[i] += table[i-1];
				ans = Math.max(ans, table[i]);
			}

			System.out.println(ans);

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}

