//package codeforces.D666;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

/**
 * @author muhossain
 * @since 2020-08-14
 */

public class C {

    public static void main(String[] args) {
        FastReader fs = new FastReader();

        int n = fs.nextInt();
        int[] nums = new int[n + 1];

        for (int i = 0; i < n; i++) {
            nums[i] = fs.nextInt();
        }

        StringBuilder output = new StringBuilder();

        output.append(1).append(" ").append(n).append("\n");

        for (int i = 0; i < n; i++) {
            output.append(BigInteger.valueOf(-1).multiply(BigInteger.valueOf(nums[i]).multiply(BigInteger.valueOf(n))));

            if (i != n - 1) {
                output.append(" ");
            }
        }

        output.append("\n");

        if (n == 1) {
            output.append(1).append(" ").append(1).append("\n");
            output.append(0).append("\n");

            output.append(1).append(" ").append(1).append("\n");
            output.append(0);
        } else {
            output.append(1).append(" ").append(n - 1).append("\n");

            for (int i = 0; i < n - 1; i++) {
                output.append(BigInteger.valueOf(nums[i]).multiply(BigInteger.valueOf(n - 1)));

                if (i != n - 2) {
                    output.append(" ");
                }
            }

            output.append("\n");
            output.append(n).append(" ").append(n).append("\n");
            output.append(BigInteger.valueOf(nums[n - 1]).multiply(BigInteger.valueOf(n - 1)));
        }


        System.out.println(output);
    }


    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public static FastReader getFileReader(String fileName) throws FileNotFoundException {
            return new FastReader(new InputStreamReader(new FileInputStream(new File(fileName))));
        }

        public static FastReader getDefaultReader() throws FileNotFoundException {
            return new FastReader();
        }

        public FastReader(InputStreamReader inputStreamReader) {
            br = new BufferedReader(inputStreamReader);
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
