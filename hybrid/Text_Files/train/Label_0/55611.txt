import java.util.Scanner;
import java.io.OutputStream;
import java.io.IOException;
import java.util.Arrays;
import java.io.PrintWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author Dumbear (dumbear@163.com)
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
}

class TaskD {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int n = in.nextInt();
        int[] p = new int[n];
        for (int i = 0; i < n; ++i) {
            p[i] = in.nextInt() - 1;
        }
        int m = in.nextInt();
        int[] groups = getGroups(p);
        int numSwaps = 0;
        for (int i = 0; i < groups.length; i += 2) {
            numSwaps += groups[i] - 1;
        }
        if (numSwaps < m) {
            int[] s = new int[groups.length / 2];
            for (int i = 1; i < groups.length; i += 2) {
                s[i / 2] = groups[i];
            }
            Arrays.sort(s);
            int[] swaps = new int[n * 2];
            int count = 0;
            for (int i = 1; i <= m - numSwaps; ++i) {
                swaps[count++] = s[0];
                swaps[count++] = s[i];
            }
            out.println(count / 2);
            for (int i = 0; i < count; ++i) {
                out.print((swaps[i] + 1) + (i + 1 == count ? "\n" : " "));
            }
        } else {
            int[] swaps = outputSwaps(p, numSwaps - m);
            out.println(swaps.length / 2);
            for (int i = 0; i < swaps.length; ++i) {
                out.print((swaps[i] + 1) + (i + 1 == swaps.length ? "\n" : " "));
            }
        }
    }

    private int[] getGroups(int[] p) {
        boolean[] used = new boolean[p.length];
        int[] groups = new int[p.length * 2];
        int count = 0;
        for (int i = 0; i < p.length; ++i) {
            if (used[i]) {
                continue;
            }
            int length = 0;
            for (int j = i; !used[j]; j = p[j]) {
                used[j] = true;
                ++length;
            }
            groups[count++] = length;
            groups[count++] = i;
        }
        return Arrays.copyOf(groups, count);
    }

    private int[] outputSwaps(int[] p, int num) {
        int[] q = new int[p.length];
        for (int i = 0; i < p.length; ++i) {
            q[p[i]] = i;
        }
        int[] swaps = new int[p.length * 2];
        int count = 0;
        for (int i = 0; i < p.length; ) {
            if (num == 0) {
                break;
            }
            if (p[i] == i) {
                ++i;
                continue;
            }
            int best = Integer.MAX_VALUE;
            for (int j = p[i]; j != i; j = p[j]) {
                best = Math.min(best, j);
            }
            swaps[count++] = i;
            swaps[count++] = best;
            int t = p[i];
            p[i] = p[best];
            p[best] = t;
            q[p[i]] = i;
            q[p[best]] = best;
            --num;
        }
        return Arrays.copyOf(swaps, count);
    }
}

