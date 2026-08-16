import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line;
        while (!(line = br.readLine()).equals("0")) {
            int n = Integer.parseInt(line);

            // 累積和配列を用いたアルゴリズムO(n^2)
            int[] s = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                s[i] = Integer.parseInt(br.readLine()) + s[i - 1];
            }
            
            int sum = Integer.MIN_VALUE;
            
            for (int l = 0; l <= n-1; l++) {
                for (int r = l+1; r <= n; r++) {
                    sum = Math.max(sum, s[r] - s[l]);
                }
            }

            System.out.println(sum);
        }

    }
}
