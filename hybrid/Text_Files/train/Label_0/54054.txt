import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Iterator;
import java.util.Set;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            TaskD.Vertex[] vs = new TaskD.Vertex[n];
            for (int i = 0; i < n; ++i) {
                vs[i] = new TaskD.Vertex();
            }
            for (int i = 0; i < n - 1; ++i) {
                TaskD.Vertex a = vs[in.nextInt() - 1];
                TaskD.Vertex b = vs[in.nextInt() - 1];
                a.adj.add(b);
                b.adj.add(a);
            }
            List<TaskD.Vertex> degOne = new ArrayList<>();
            for (TaskD.Vertex v : vs)
                if (v.adj.size() == 1) {
                    degOne.add(v);
                }
            while (!degOne.isEmpty()) {
                Set<TaskD.Vertex> toKill = new HashSet<>();
                for (TaskD.Vertex v : degOne) {
                    toKill.add(v);
                    if (v.adj.isEmpty()) {
                        out.println("First");
                        return;
                    }
                    TaskD.Vertex u = v.adj.iterator().next();
                    if (u.adj.size() > 1) {
                        toKill.add(u);
                        ++u.numOnes;
                        if (u.numOnes > 1) {
                            out.println("First");
                            return;
                        }
                    }
                }
                for (TaskD.Vertex v : toKill) {
                    v.numOnes = 1;
                }
                degOne.clear();
                for (TaskD.Vertex v : toKill) {
                    for (TaskD.Vertex u : v.adj) {
                        if (u.numOnes == 0) {
                            u.adj.remove(v);
                            if (u.adj.size() == 1) degOne.add(u);
                        }
                    }
                }
            }
            out.println("Second");
        }

        static class Vertex {
            int numOnes;
            Set<TaskD.Vertex> adj = new HashSet<>();

        }

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

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

