import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.io.IOException;
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
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskB {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            long tasks = in.nextInt(), subTasks = in.nextInt(), totalTime = in.nextInt(), times[] = in.nextLongArray((int) subTasks), taskTime = 0, globalAnswer = 0;
            for (int i = 0; i < subTasks; i++) taskTime += times[i];
            Arrays.sort(times);
            for (int solvedTasks = 0; solvedTasks <= tasks; solvedTasks++) {
                long remTime = totalTime - (solvedTasks * taskTime);
                if (remTime >= 0) {
                    long localAnswer = solvedTasks * (subTasks + 1);
                    for (int subTask = 0; subTask < subTasks; subTask++) {
                        long canSolve = Math.min(tasks - solvedTasks, remTime / times[subTask]);
                        localAnswer += canSolve;
                        remTime -= canSolve * times[subTask];
                    }
                    globalAnswer = Math.max(globalAnswer, localAnswer);
                }
            }
            out.println(globalAnswer);
        }

    }

    static class InputReader {
        private int lenbuf = 0;
        private int ptrbuf = 0;
        private InputStream in;
        private byte[] inbuf = new byte[1024];

        public InputReader(InputStream in) {
            this.in = in;
        }

        private int readByte() {
            if (lenbuf == -1) throw new InputMismatchException();
            if (ptrbuf >= lenbuf) {
                ptrbuf = 0;
                try {
                    lenbuf = in.read(inbuf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (lenbuf <= 0) return -1;
            }
            return inbuf[ptrbuf++];
        }

        public int nextInt() {
            int num = 0, b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }

            while (true) {
                if (b >= '0' && b <= '9') {
                    num = num * 10 + (b - '0');
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }

        public long nextLong() {
            long num = 0;
            int b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }

            while (true) {
                if (b >= '0' && b <= '9') {
                    num = num * 10 + (b - '0');
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }

        public long[] nextLongArray(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = nextLong();
            return a;
        }

    }
}

