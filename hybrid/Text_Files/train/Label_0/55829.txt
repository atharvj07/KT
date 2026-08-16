



import java.io.*;
import java.util.*;

public class Main {

    private static int MOD = 1000000007;


    public static void main(String[] args) throws Exception {
        InputStream inS = System.in;
//        InputReader sc = new InputReader(inS);
        PrintStream out = System.out;
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();


        sc.nextLine();

        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            for (int j = 0; j < s.length(); j++) {
                int num = getValue(s.charAt(j));
                for (int k = 0; k < 4; k++) {
                    matrix[i][j*4 + 3 - k] = num & 1;
                    num >>= 1;
                }
            }
        }

//        for (int i = 0; i < n; i++) {
//            Helpers.display(matrix[i], 0, n-1);
//        }

        int x = n;

        for (int i = 0; i < n; i++) {
            int count = 1;
            for (int j = 1; j < n; j++) {
                if (matrix[i][j-1] != matrix[i][j]) {
                    x = gcd(x, count);
                    count = 1;
                } else {
                    count++;
                }

            }
        }

        for (int i = 0; i < n; i++) {
            int count = 1;
            for (int j = 1; j < n; j++) {
                if (matrix[j-1][i] != matrix[j][i]) {
                    x = gcd(x, count);
                    count = 1;
                } else {
                    count++;
                }
            }
        }

        out.println(x);

        out.close();
    }

    private static int gcd(int a, int b) {
        if (a <= b) {
            return gcdHelper(a, b);
        }

        return gcdHelper(b, a);
    }

    private static int gcdHelper(int a, int b) {
        if (b == 0)
            return a;
        return gcdHelper(b, a % b);

    }

    private static int getCompression(int startX, int startY, int n, char[][] matrix) {
        if (n == 1) {
            return 1;
        }

        int m = n / 2;

        // check 4 sub matrices
        // which have starting index as (startX, startY), (startX + m, startY + 0), (startX + 0, startY + m), (startX + m, startY + m)
        int upper = Math.min(getCompression(startX, startY, m, matrix), getCompression(startX, startY + m, m, matrix));
        int lower = Math.min(getCompression(startX + m, startY, m, matrix), getCompression(startX + m, startY + m, m, matrix));


        if (Math.min(upper, lower) < m) {
            return Math.min(upper, lower);
        }

        // check first bits of four sub matrices
        int one = getValue(startX, startY, matrix);
        int two = getValue(startX, startY + m, matrix);
        int three = getValue(startX+m, startY, matrix);
        int four = getValue(startX+m, startY+m, matrix);

        if ((one == two) && (one == three) && (one == four)) {
            return n;
        }

        return Math.min(upper, lower);
    }

    private static int getValue(int x, int y, char[][] matrix) {
        // y / 4 th bit
        // y % 4 th bit from left

        int bit = getValue(matrix[x][y / 4]);

        int mask = (3 - (y % 4));
        return (bit >> mask) & 1;
    }

    private static int getValue(char hexChar) {
        int bit;
        if (Character.isAlphabetic(hexChar)) {
            bit = (hexChar - 'A') + 10;
        } else {
            bit = hexChar - '0';
        }

        return bit;
    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }

}
