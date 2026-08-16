import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;
import java.util.ArrayList;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Aviously
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public static ArrayList<Integer> prime = new ArrayList<>();
        public final int N = 2 * 1000 * 1000;

        public void solve(int testNumber, Scanner in, PrintWriter out) {
            prime.add(2);
            for (int i = 3; i <= N; i += 2) {
                if (isPrime(i)) {
//                out.print(i + " ");
                    prime.add(i);
                }
            }
            int n = in.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = in.nextInt();
            }
            Arrays.sort(a);
            if (a.length > 1 && a[0] == 1 && a[1] == 1) {
                int cnt = 1;
                while (cnt < a.length && a[cnt] == 1)
                    cnt++;
                int p = 0;
                for (int i = cnt; i < a.length; i++) {
                    if (findPrime(a[i] + 1)) {
                        p = a[i];
                        break;
                    }
                }
                out.println(cnt + (p > 0 ? 1 : 0));
                for (int i = 0; i < cnt; i++) {
                    out.print(a[i] + " ");
                }
                if (p > 0)
                    out.print(p);
                return;
            }
            for (int i = 0; i < n; i++) {
                if (i > 0 && a[i] == a[i - 1])
                    continue;
                for (int j = i + 1; j < n; j++) {
                    if (j > i + 1 && a[j] == a[j - 1])
                        continue;
                    if (findPrime(a[i] + a[j])) {
                        out.println(2);
                        out.println(a[i] + " " + a[j]);
                        return;
                    }
                }
            }
            out.println(1);
            out.println(a[0]);
        }

        public boolean isPrime(int n) {
            for (int a : prime) {
                if (a > Math.sqrt(n))
                    break;
                if (n % a == 0)
                    return false;
            }
            return true;
        }

        public boolean findPrime(int n) {
            int l = 0;
            int r = prime.size() - 1;
            while (l < r) {
                int mid = (l + r) / 2;
                if (prime.get(mid) < n) {
                    l = mid + 1;
                } else {
                    r = mid;
                }
            }
            if (prime.get(l) == n)
                return true;
            return false;
        }

    }
}

