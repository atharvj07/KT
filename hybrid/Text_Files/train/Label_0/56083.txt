import java.io.*;
import java.util.*;
import java.math.*;

public class SalemAndSticks {
    static Scanner sc = new Scanner(System.in);
    static PrintWriter pw = new PrintWriter(System.out), pw2 = new PrintWriter(System.out);
    public static void main(String[] args) throws IOException {
        int n=sc.nextInt(),k=sc.nextInt();
        String s=sc.nextLine();
        String ans="";
        int max=0;
        int[] f=new int[27];
        for(int i=0;i<n;) {
            int j=i+1,c=1;
            while(j<s.length()&&s.charAt(j++)==s.charAt(i))
                c++;
            f[s.charAt(i)-'a']+=c/k;
            i+=c;
        }
        for(int x:f){
            max=Math.max(max,x);
        }
        System.out.println(max);
        pw.flush();
    }

    public static <E> void print2D(E[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                pw.println(arr[i][j]);
            }
        }
    }

    public static int digitSum(String s) {
        int toReturn = 0;
        for (int i = 0; i < s.length(); i++) toReturn += Integer.parseInt(s.charAt(i) + " ");
        return toReturn;
    }

    public static boolean isPrime(long n) {
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;

        if (n % 2 == 0 || n % 3 == 0)
            return false;

        for (long i = 5; i * i <= n; i = i + 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        return true;
    }

    public static long pow(long a, long pow) {
        return pow == 0 ? 1 : pow % 2 == 0 ? pow(a * a, pow >> 1) : a * pow(a * a, pow >> 1);
    }

    public static long sumNum(long a) {
        return a * (a + 1) / 2;
    }

    public static int gcd(int n1, int n2) {
        return n2 == 0 ? n1 : gcd(n2, n1 % n2);
    }

    public static long factorial(long a) {
        return a == 0 || a == 1 ? 1 : a * factorial(a - 1);
    }

    public static void sort(int arr[]) {
        shuffle(arr);
        Arrays.sort(arr);
    }

    public static void shuffle(int arr[]) {
        Random rnd = new Random();
        for (int i = arr.length - 1; i > 0; i--) {
            int index = rnd.nextInt(i + 1);
            int temp = arr[index];
            arr[index] = arr[i];
            arr[i] = temp;
        }
    }

    public static Double[] solveQuadratic(double a, double b, double c) {
        double result = (b * b) - 4.0 * a * c;
        double r1;
        if (result > 0.0) {
            r1 = ((double) (-b) + Math.pow(result, 0.5)) / (2.0 * a);
            double r2 = ((double) (-b) - Math.pow(result, 0.5)) / (2.0 * a);
            return new Double[]{r1, r2};
        } else if (result == 0.0) {
            r1 = (double) (-b) / (2.0 * a);
            return new Double[]{r1, r1};
        } else {
            return new Double[]{null, null};
        }
    }

    static class Scanner {
        StringTokenizer st;
        BufferedReader br;

        public Scanner(FileReader r) {
            br = new BufferedReader(r);
        }

        public Scanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public String nextLine() throws IOException {
            return br.readLine();
        }

        public double nextDouble() throws IOException {
            String x = next();
            StringBuilder sb = new StringBuilder("0");
            double res = 0, f = 1;
            boolean dec = false, neg = false;
            int start = 0;
            if (x.charAt(0) == '-') {
                neg = true;
                start++;
            }
            for (int i = start; i < x.length(); i++)
                if (x.charAt(i) == '.') {
                    res = Long.parseLong(sb.toString());
                    sb = new StringBuilder("0");
                    dec = true;
                } else {
                    sb.append(x.charAt(i));
                    if (dec)
                        f *= 10;
                }
            res += Long.parseLong(sb.toString()) / f;
            return res * (neg ? -1 : 1);
        }

        public boolean ready() throws IOException {
            return br.ready();
        }
    }

    static class pair<E1, E2> implements Comparable<pair> {
        E1 x;
        E2 y;

        pair(E1 x, E2 y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(pair o) {
            return x.equals(o.x) ? (Integer) y - (Integer) o.y : (Integer) x - (Integer) o.x;
        }

        @Override
        public String toString() {
            return x + " " + y;
        }

        public double pointDis(pair p1) {
            return Math.sqrt(((Integer) y - (Integer) p1.y) * ((Integer) y - (Integer) p1.y) + ((Integer) x - (Integer) p1.x) * ((Integer) x - (Integer) p1.x));
        }
    }

}
