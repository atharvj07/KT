
/**
 * Date: 21 Apr, 2018
 * Link:
 *
 * @author Prasad-Chaudhari
 * @email prasadc8897@gmail.com
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class newProgram {

    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        FastIO2 in = new FastIO2();
        int t = in.ni();
        int m = in.ni();
        int a[] = new int[m];
        int segname = 1;
        outer:
        while (t-- > 0) {
            String s = in.next();
            if (s.equals("alloc")) {
                int n = in.ni();
                boolean q = true;
                for (int i = 0; i < m; i++) {
                    if (a[i] == 0) {
                        boolean p = true;
                        for (int j = i; j < i + n; j++) {
                            if (j == m || a[j] != 0) {
                                p = false;
                                break;
                            }
                        }
                        if (p) {
                            for (int j = i; j < n + i; j++) {
                                a[j] = segname;
                            }
                            System.out.println(segname++);
                            q = false;
                            break;
                        }
                    }
                }
//                System.out.println("Allocate");
//                for (int i = 0; i < m; i++) {
//                    System.out.print(a[i] + " ");
//                }
//                System.out.println("");
                if (q) {
                    System.out.println("NULL");
                }
            } else if (s.equals("erase")) {
                int n = in.ni();
                boolean q = true;
                for (int i = 0; i < m; i++) {
                    if (a[i] == n) {
                        int j = i;
                        while (j < m && a[j] == n) {
                            a[j] = 0;
                            j++;
                        }
                        q = false;
                    }
                }
//                System.out.println("Erase");
//                for (int i = 0; i < m; i++) {
//                    System.out.print(a[i] + " ");
//                }
//                System.out.println("");
                if (q||n<=0) {
                    System.out.println("ILLEGAL_ERASE_ARGUMENT");
                }
            } else {
                int put = 0;
                for (int i = 0; i < m; i++) {
                    if (a[i] != 0) {
//                            System.out.println(a[i]);
                        a[put++] = a[i];
                        if(put-1!=i)
                            a[i] = 0;
//                            System.out.println(i+"->"+(put-1));
                    }
                }
//                System.out.println("Defragment");
//                for (int i = 0; i < m; i++) {
//                    System.out.print(a[i] + " ");
//                }
//                System.out.println("");
            }
        }
    }

    static class FastIO2 {

        private final BufferedReader br;
        private String s[];
        private int index;

        public FastIO2() throws IOException {
            br = new BufferedReader(new InputStreamReader(System.in));
//            br = new BufferedReader(new FileReader(new File("input")));
            s = br.readLine().split(" ");
            index = 0;
        }

        public int ni() throws IOException {
            return Integer.parseInt(nextToken());
        }

        public double nd() throws IOException {
            return Double.parseDouble(nextToken());
        }

        public long nl() throws IOException {
            return Long.parseLong(nextToken());
        }

        public String next() throws IOException {
            return nextToken();
        }

        public String nli() throws IOException {
            try {
                return br.readLine();
            } catch (IOException ex) {

            }
            return null;
        }

        public int[] gia(int n) throws IOException {
            int a[] = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = ni();
            }
            return a;
        }

        public int[] gia(int n, int start, int end) throws IOException {
            validate(n, start, end);
            int a[] = new int[n];
            for (int i = start; i < end; i++) {
                a[i] = ni();
            }
            return a;
        }

        public double[] gda(int n) throws IOException {
            double a[] = new double[n];
            for (int i = 0; i < n; i++) {
                a[i] = nd();
            }
            return a;
        }

        public double[] gda(int n, int start, int end) throws IOException {
            validate(n, start, end);
            double a[] = new double[n];
            for (int i = start; i < end; i++) {
                a[i] = nd();
            }
            return a;
        }

        public long[] gla(int n) throws IOException {
            long a[] = new long[n];
            for (int i = 0; i < n; i++) {
                a[i] = ni();
            }
            return a;
        }

        public long[] gla(int n, int start, int end) throws IOException {
            validate(n, start, end);
            long a[] = new long[n];
            for (int i = start; i < end; i++) {
                a[i] = ni();
            }
            return a;
        }

        private String nextToken() throws IndexOutOfBoundsException, IOException {
            if (index == s.length) {
                s = br.readLine().split(" ");
                index = 0;
            }
            return s[index++];
        }

        private void validate(int n, int start, int end) {
            if (start < 0 || end >= n) {
                throw new IllegalArgumentException();
            }
        }
    }
}
