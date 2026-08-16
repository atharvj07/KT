import java.util.*;
import java.io.*;
public class e {
public static void main(String[] args) throws IOException
{
    input.init(System.in);
    PrintWriter out = new PrintWriter(System.out);
    int n = input.nextInt();
    int[] as = new int[n];
    for(int i = 0; i<n; i++) as[i] = input.nextInt();
    int[] fs = new int[n];
    int m = input.nextInt();
    for(int i = 0; i<m; i++) fs[input.nextInt()-1]++;
    int min = 400000;
    for(int i = 1; i<n-1; i++) min = Math.min(min, fs[i]);
    min = Math.min(min, fs[0]*2);
    min = Math.min(min, fs[n-1]*2);
    int diff = min - 2;
    long tot = 0;
    for(int i = 0; i<n-1; i++) tot += as[i+1] - as[i];
    if(diff%2 == 1) diff++;
    boolean good = true;
    for(int i = 0; i<n; i++)
    {
        if(diff > 0) fs[i] -= (i == 0 || i == n-1) ? diff/2 : diff;
        if(fs[i] > 6) good = false;
    }
    //out.println(Arrays.toString(fs));
    if(good)
    {
        int sum = 0;
        for(int i = 0; i<n; i++) sum += fs[i];
        //System.out.println(sum+" "+Arrays.toString(fs));
        HashSet<Long> poss = new HashSet<Long>();
        poss.add(good(as, fs, sum, 0, 1));
        poss.add(good(as, fs, sum, n-1, -1));
        poss.add(good(as, fs, sum, 1, -1));
        poss.add(good(as, fs, sum, n-2, 1));
        ArrayList<Integer> biggerThanNext = new ArrayList<Integer>(), biggerThanPrev = new ArrayList<Integer>();
        for(int i = 0; i<n; i++)
        {
            if(i > 0 && fs[i] > fs[i-1]) biggerThanPrev.add(i);
            if(i < n - 1 && fs[i] > fs[i+1]) biggerThanNext.add(i);
        }
        if(biggerThanNext.size() > 3 || biggerThanPrev.size() > 3) good = false;
        else
        {
            for(int x : biggerThanPrev)
                if(x != n-1)
                    poss.add(good(as, fs, sum, x, 1));
            for(int x : biggerThanNext)
                if(x != 0)
                    poss.add(good(as, fs, sum, x, -1));
            if(poss.contains(-1l)) poss.remove(-1l);
            //for(long x : poss) out.println(x);
            //out.println(poss.size());
            if(poss.size() == 0 || poss.size() > 1) good = false;
            //out.println(good);
        }
        long res = -2;
        for(long x : poss)
        {
            res = x;
        }
        if(good) out.println(res + tot * (diff > 0 ? diff : 0));
    }
    if(!good) out.println(-1);
    out.close();
}
static long good(int[] as, int[] fs, int sum, int start, int d)
{
    int done = 0;
    int at = start;
    int[] copy = new int[fs.length];
    for(int i = 0; i<fs.length; i++) copy[i] = fs[i];
    long res = 0;
    while(true)
    {
        copy[at]--;
        if(copy[at] < 0) return -1;
        done++;
        //System.out.println(done+" "+sum);
        if(done == sum) return res;
        int next = at + d;
        res += Math.abs(as[at] - as[next]);
        if(next == 0 || next == fs.length - 1) d *= -1;
        at = next;
    }
}
public static class input {
    static BufferedReader reader;
    static StringTokenizer tokenizer;

    /** call this method to initialize reader for InputStream */
    static void init(InputStream input) {
        reader = new BufferedReader(
                     new InputStreamReader(input) );
        tokenizer = new StringTokenizer("");
    }

    /** get next word */
    static String next() throws IOException {
        while ( ! tokenizer.hasMoreTokens() ) {
            //TODO add check for eof if necessary
            tokenizer = new StringTokenizer(
                   reader.readLine() );
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt( next() );
    }
    
    static double nextDouble() throws IOException {
        return Double.parseDouble( next() );
    }
    static long nextLong() throws IOException {
        return Long.parseLong( next() );
    }
}
}
