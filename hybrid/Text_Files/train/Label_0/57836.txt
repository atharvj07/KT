import java.io.BufferedInputStream;
import java.io.Closeable;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class P1535F {

    private static class LetterHist {
        private final int[] counts = new int[26];
        private final int length;
        private int hash;

        public LetterHist(byte[] b) {
            this.length = b.length;
            for (int i = 0; i < b.length; i++) {
                counts[b[i] - (byte) 'a']++;
            }
        }

        @Override
        public boolean equals(Object other) {
            if (other == this) {
                return true;
            }
            if (! (other instanceof LetterHist)) {
                return false;
            }
            final LetterHist that = (LetterHist) other;
            for (int i = 0; i < 26; i++) {
                if (this.counts[i] != that.counts[i]) {
                    return false;
                }
            }
            return true;
        }

        @Override
        public int hashCode() {
            if (hash == 0) {
                hash = 1;
                for (int i = 0; i < 26; i++) {
                    hash = 31 * hash + counts[i];
                }
            }
            return hash;
        }
    }

    private static class SS {
        public final byte[] string;
        public final int[] sort;

        public SS(byte[] string, int[] sort) {
            this.string = string;
            this.sort = sort;
        }
    }

    private static long compute2(int n, int m, byte[][] strings) {
        long total = 0;

        // Create lookup table of sorted runs of length > 1
        final SS[] sss = new SS[n];
        for (int i = 0; i < n; i++) {
            final byte[] string = strings[i];
            final int[] sort = new int[m];
            int j = 0;
            for (int k = 1; k < m; k++) {
                if (string[k] < string[k-1]) {
                    if (k > j+1) {
                        sort[j] = k;
                    }
                    j = k;
                }
            }
            if (m > j+1) {
                sort[j] = m;
            }
            sss[i] = new SS(string, sort);
        }

        // Sort strings by co-lexicographic order, descending
        Arrays.sort(sss, (ss1, ss2) -> {
            int c;
            for (int j = m-1; j >= 0; j--) {
                c = ss2.string[j] - ss1.string[j];
                if (c != 0) {
                    return c;
                }
            }
            return 0;
        });

        final int[] groups = new int[n];
        final int[][] jstack = new int[m][2];
        jstack[0][0] = n;
        jstack[0][1] = m;
        for (int j0 = 0; j0 < m; j0++) {
            final int j0_ = j0;
            int g = groups[0];
            int i0 = 0;
            int g1 = 0;
            int jsp = 0;
            for (int i = 0; i < n; i++) {
                final SS ss = sss[i];
                final byte[] string = ss.string;
                final int[] sort = ss.sort;
                while (i >= jstack[jsp][0]) {
                    jsp--;
                }
                if (groups[i] != g) {
                    // Re-collate previous group
                    Arrays.sort(sss, i0, i, (ss1, ss2) ->
                        (int) (ss1.string[j0_] - ss2.string[j0_]));
                    groups[i0++] = g1;
                    while(i0 < i) {
                        if (sss[i0-1].string[j0] != sss[i0].string[j0]) {
                            g1++;
                        }
                        groups[i0++] = g1;
                    }
                    g1++;
                    g = groups[i];
                    i0 = i;
                }
                if (sort[j0] > 0) {
                    final int j1 = sort[j0];
                    final int j2 = jstack[jsp][1];
                    final int i2 = jstack[jsp][0];
                    int i_;
                    outer:
                    for (i_ = i+1; i_ < i2 && groups[i_] == g; i_++) {
                        for (int j = j1; j < j2; j++) {
                            if (string[j] != sss[i_].string[j]) {
                                break outer;
                            }
                        }
                    }
                    total += i_ - i - 1;
                    if (i_ > i+1) {
                        jsp++;
                        jstack[jsp][0] = i_;
                        jstack[jsp][1] = j1;
                    }
                }
            }
            // Re-collate last group
            Arrays.sort(sss, i0, n, (ss1, ss2) ->
                (int) (ss1.string[j0_] - ss2.string[j0_]));
            groups[i0++] = g1;
            while (i0 < n) {
                if (sss[i0 - 1].string[j0] != sss[i0].string[j0]) {
                    g1++;
                }
                groups[i0++] = g1;
            }
        }

        return total;
    }

    private static long compute(int n, int m, byte[][] strings) {
        final Map<LetterHist, List<byte[]>> groups = new HashMap<>();
        for (int i = 0; i < n; i++) {
            final LetterHist key = new LetterHist(strings[i]);
            groups.computeIfAbsent(key, k -> new ArrayList<>())
                .add(strings[i]);
        }
        long total = 0;
        int ps = 0;
        for (List<byte[]> group : groups.values()) {
            int s = group.size();
            total += 1337L * (long) s * (long) ps;
            total += (long) s * (long) (s-1)
                - compute2(s, m, group.toArray(new byte[0][]));
            ps += s;
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        try {
            final FastReader fr = new FastReader(
                new BufferedInputStream(System.in));
            final int n = fr.readInt();
            byte[] buf = new byte[200000];
            final int m = fr.readLine(buf);
            byte[][] strings = new byte[n][m];
            for (int j = 0; j < m; j++) {
                strings[0][j] = buf[j];
            }
            for (int i = 1; i < n; i++) {
                fr.readLine(strings[i]);
            }
            System.out.println(compute(n, m, strings));
        } catch (Throwable t) {
            t.printStackTrace(System.out);
            System.exit(1);
        }
    }

    private static final void log(Object o) {
        System.err.println(o);
    }

    private static class FastReader implements Closeable {
        private static final byte B_SP = ' ';
        private static final byte B_CR = '\r';
        private static final byte B_LF = '\n';
        private static final byte B_0 = '0';
        private static final byte B_9 = '9';
        private static final byte B_DASH = '-';
        private static final byte B_EOF = -1;

        private final InputStream in;
        private byte prev;

        public FastReader(InputStream in) {
            this.in = in;
        }

        public byte read() throws IOException {
            return (prev = (byte) in.read());
        }

        public byte readNonWs() throws IOException {
            byte b;
            do {
                b = read();
            } while (b <= B_SP);
            return b;
        }

        public int readInt() throws IOException {
            byte b = readNonWs();
            final boolean neg = (b == B_DASH);
            if (neg) {
                b = read();
            }
            int i = (b - B_0);
            b = read();
            while (b >= B_0 && b <= B_9) {
                i = i * 10 + (b - B_0);
                b = read();
            }
            return neg ? -i : i;
        }

        public long readLong() throws IOException {
            byte b = readNonWs();
            final boolean neg = (b == B_DASH);
            if (neg) {
                b = read();
            }
            long i = (b - B_0);
            b = read();
            while (b >= B_0 && b <= B_9) {
                i = i * 10 + (b - B_0);
                b = read();
            }
            return neg ? -i : i;
        }

        public int readToken(byte[] tbuf) throws IOException {
            byte b = readNonWs();
            int i = 0;
            do {
                tbuf[i++] = b;
                b = read();
            } while (b >= B_SP);
            return i;
        }

        public int readLine(byte[] lbuf) throws IOException {
            byte b;
            if (prev == B_CR) {
                b = read();
                if (b == B_LF) {
                    b = read();
                }
            } else {
                b = read();
            }
            int i = 0;
            while (b >= B_SP) {
                lbuf[i++] = b;
                b = read();
            }
            return i;
        }

        @Override
        public void close() throws IOException {
            in.close();
        }
    }
}
