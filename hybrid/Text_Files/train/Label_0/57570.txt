import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.AbstractCollection;
import java.util.StringTokenizer;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author Zyflair Griffane
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		PandaScanner in = new PandaScanner(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		A solver = new A();
		solver.solve(1, in, out);
		out.close();
	}
}

class A {
    public void solve(int testNumber, PandaScanner in, PrintWriter out) {
        int a = in.nextInt();
        String str = in.next();
        int post = str.indexOf("a++");
        int pre = str.indexOf("++a");
        while (post > -1 || pre > -1) {
            if (post > -1 && (pre == -1 || post < pre)) {
                str = str.substring(0, post) + "b" + str.substring(post + 3);
            }
            else {
                str = str.substring(0, pre) + "c" + str.substring(pre + 3);
            }
            post = str.indexOf("a++");
            pre = str.indexOf("++a");
        }
        String[] arr = str.split("\\+");
        PriorityQueue<Summand> q = new PriorityQueue<>();
        for (String sum: arr) {
            String[] parts = sum.split("-");
            int multiplier = 1;
            for (String part: parts) {
                String[] multiplicands = part.split("\\*");
                if (multiplicands.length == 1) {
                    q.add(new Summand(multiplier, multiplicands[0].charAt(0)));
                }
                else {
                    q.add(new Summand(multiplier * Integer.parseInt(multiplicands[0]), multiplicands[1].charAt(0)));
                }
                multiplier = -1;
            }
        }
        int total = 0;
        while (!q.isEmpty()) {
            Summand s = q.poll();
            if (s.first) {
                a++;
            }
            total += a * s.coeff;
            if (!s.first) {
                a++;
            }
        }
        out.println(total);
    }
    public class Summand implements Comparable<Summand> {
        int coeff;
        boolean first;
        public Summand(int coeff, char type) {
            this.coeff = coeff;
            first = type == 'c';
        }
        public int compareTo(Summand o) {
            return coeff - o.coeff;
        }
    }
}

class PandaScanner {
    public BufferedReader br;
    public StringTokenizer st;
    public InputStream in;

    public PandaScanner(InputStream in) {
        br = new BufferedReader(new InputStreamReader(this.in = in));
    }

    public String nextLine() {
        try {
            return br.readLine();
        }
        catch (Exception e) {
            return null;
        }
    }

    public String next() {
        if (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(nextLine().trim());
            return next();
        }
        return st.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    }

