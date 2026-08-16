import java.util.*;
import java.io.*;
public class b {
public static void main(String[] args) throws IOException
{
    input.init(System.in);
    PrintWriter out = new PrintWriter(System.out);
    int n = input.nextInt(), a = input.nextInt(), b = input.nextInt();
    Num[] data = new Num[n];
    for(int i = 0; i<n; i++) data[i] = new Num(input.nextInt(), i);
    int[] res = new int[n];
    Arrays.fill(res,-1);
    Arrays.sort(data);
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    for(int i = 0; i<n; i++)
        map.put(data[i].x, data[i].i);
    boolean good = true;
    for(int i = 0; i<n; i++)
    {
        if(res[data[i].i] != -1) continue;
        int val = data[i].x;
        if(!map.containsKey(a-val) && !map.containsKey(b-val))
        {
            good = false;
            break;
        }
        if(!map.containsKey(a-val))
        {
            int other = map.get(b-val);
            if(res[other] == 0)
            {
                good = false;
                break;
            }
            res[other] = res[data[i].i] = 1;
        }
        else if(!map.containsKey(b-val))
        {
            int other = map.get(a-val);
            if(res[other] == 1)
            {
                good = false;
                break;
            }
            res[other] = res[data[i].i] = 0;
        }
        else
        {
            int cur = data[i].i;
            int otherB = map.get(b-val), otherA = map.get(a-val);
            if(b > a && res[otherB] != 0)
            {
                res[cur] = res[otherB] = 1;
            }
            else if(a>b && res[otherA] != 1)
            {
                res[cur] = res[otherA] = 0;
            }
            else if(b > a && res[otherA] != 1)
            {
                res[cur] = res[otherA] = 0;
            }
            else if(a > b && res[otherB] != 0)
            {
                res[cur] = res[otherB] = 1;
            }
            else if(b == a)
            {
                res[cur] = res[otherA] = 0;
            }
            else
            {
                good = false;
                break;
            }
        }
    }
    if(good)
    {
        out.println("YES");
        for(int x: res) out.print(x+" ");
    }
    else
        out.println("NO");
    
    out.close();
}
static class Num implements Comparable<Num>
{
    int x, i;
    public Num(int xx, int ii)
    {
        x = xx; i = ii;
    }
    @Override
    public int compareTo(Num o) {
        // TODO Auto-generated method stub
        return x - o.x;
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
