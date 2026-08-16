import javax.swing.*;
import java.io.*;
import java.sql.Struct;
import java.text.DecimalFormat;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        int[] arr = new int[n];
        StringTokenizer s = new StringTokenizer(rd.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(s.nextToken());
        }
        long[][] dp = new long[n + 1][n + 1];

        for (int i = 0; i < n; i++) {
            dp[i][i] = arr[i];
        }

        for (int i = 2; i < n + 1; i++) {
            for (int j = 0; j <= n - i; j++) {
                int start = j;
                int end = start + i - 1;
                dp[start][end] = Math.max(-dp[start + 1][end] + arr[start], -dp[start][end -1]+arr[end]);

            }
        }

        System.out.println(dp[0][n - 1]);
    }
}