import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        try {
            // 標準入力
            InputStreamReader isr = new InputStreamReader(System.in);
            BufferedReader br = new BufferedReader(isr);
            String strArr[] = br.readLine().split(" ");
            int n  = Integer.parseInt(strArr[0]) - 1;
            int k = Integer.parseInt(strArr[1]) - 1;
            strArr = br.readLine().split(" ");
            int ans = n / k;
            if (n % k != 0) {
                ans++;
            }
            System.out.println(ans);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
