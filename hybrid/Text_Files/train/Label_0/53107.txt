//stan hu tao
//join nct ridin by first year culture reps
import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.Math.abs;
import java.util.*;
import java.io.*;
import java.math.*;

public class x1236D
{
    public static void main(String hi[]) throws Exception
    {
        BufferedReader infile = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(infile.readLine());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        TreeSet<Integer>[] rows = new TreeSet[X+1];
        TreeSet<Integer>[] cols = new TreeSet[Y+1];
        for(int i=1; i <= X; i++)
            rows[i] = new TreeSet<Integer>();
        for(int i=1; i <= Y; i++)
            cols[i] = new TreeSet<Integer>();
        for(int i=0; i < N; i++)
        {
            st = new StringTokenizer(infile.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            rows[a].add(b); cols[b].add(a);
        }
        int left = 1, right = Y;
        int up = 1, down = X;
        int dir = 0;
        int r = 1, c = 1;
        long tot = 1L;
        int lol = 5;
        while(left <= right && up <= down)
        {
            if(dir == 0)
            {
                TreeSet<Integer> set = rows[r];
                int stop = right+1;
                if(set.size() > 0 && c <= set.last())
                    stop = min(stop, set.ceiling(c));
                right = min(right, stop-1);
                tot += stop-c-1;
                c = stop-1;
                up = max(up, r+1);
            }
            else if(dir == 1)
            {
                TreeSet<Integer> set = cols[c];
                int stop = down+1;
                if(set.size() > 0 && r <= set.last())
                    stop = min(stop, set.ceiling(r));
                down = min(down, stop-1);
                tot += stop-r-1;
                r = stop-1;
                right = min(right, c-1);
            }
            else if(dir == 2)
            {
                TreeSet<Integer> set = rows[r];
                int stop = left-1;
                if(set.size() > 0 && c >= set.first())
                    stop = max(stop, set.floor(c));
                left = max(left, stop+1);
                tot += c-stop-1;
                c = stop+1;
                down = min(down, r-1);
            }
            else if(dir == 3)
            {
                TreeSet<Integer> set = cols[c];
                int stop = up-1;
                if(set.size() > 0 && r >= set.first())
                    stop = max(stop, set.floor(r));
                up = max(up, stop+1);
                tot += r-stop-1;
                r = stop+1;
                left = max(left, c+1);
            }
            dir = (dir+1)&3;
            if(debug) System.out.println(dir+" "+tot+" "+left+" "+c);
        }
        if(tot == (long)X*Y-N)
            System.out.println("Yes");
        else
            System.out.println("No");
    }
    static boolean debug = false;
}
/*
5 5 6
2 1
3 1
4 1
4 3
4 4
5 1

 */
class FastScanner
{
    private int BS = 1 << 16;
    private char NC = (char) 0;
    private byte[] buf = new byte[BS];
    private int bId = 0, size = 0;
    private char c = NC;
    private double cnt = 1;
    private BufferedInputStream in;

    public FastScanner() {
        in = new BufferedInputStream(System.in, BS);
    }

    public FastScanner(String s) {
        try {
            in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
        } catch (Exception e) {
            in = new BufferedInputStream(System.in, BS);
        }
    }

    private char getChar() {
        while (bId == size) {
            try {
                size = in.read(buf);
            } catch (Exception e) {
                return NC;
            }
            if (size == -1) return NC;
            bId = 0;
        }
        return (char) buf[bId++];
    }

    public int nextInt() {
        return (int) nextLong();
    }

    public int[] nextInts(int N) {
        int[] res = new int[N];
        for (int i = 0; i < N; i++) {
            res[i] = (int) nextLong();
        }
        return res;
    }

    public long[] nextLongs(int N) {
        long[] res = new long[N];
        for (int i = 0; i < N; i++) {
            res[i] = nextLong();
        }
        return res;
    }

    public long nextLong() {
        cnt = 1;
        boolean neg = false;
        if (c == NC) c = getChar();
        for (; (c < '0' || c > '9'); c = getChar()) {
            if (c == '-') neg = true;
        }
        long res = 0;
        for (; c >= '0' && c <= '9'; c = getChar()) {
            res = (res << 3) + (res << 1) + c - '0';
            cnt *= 10;
        }
        return neg ? -res : res;
    }

    public double nextDouble() {
        double cur = nextLong();
        return c != '.' ? cur : cur + nextLong() / cnt;
    }

    public double[] nextDoubles(int N) {
        double[] res = new double[N];
        for (int i = 0; i < N; i++) {
            res[i] = nextDouble();
        }
        return res;
    }

    public String next() {
        StringBuilder res = new StringBuilder();
        while (c <= 32) c = getChar();
        while (c > 32) {
            res.append(c);
            c = getChar();
        }
        return res.toString();
    }

    public String nextLine() {
        StringBuilder res = new StringBuilder();
        while (c <= 32) c = getChar();
        while (c != '\n') {
            res.append(c);
            c = getChar();
        }
        return res.toString();
    }

    public boolean hasNext() {
        if (c > 32) return true;
        while (true) {
            c = getChar();
            if (c == NC) return false;
            else if (c > 32) return true;
        }
    }
}