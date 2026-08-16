
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;


public class Andryusha_and_Socks {
    
    public static void main(String[] args) {
        FastScanner sc = new FastScanner();
        int n = sc.nextInt()*2;
        
        Set<Integer> set = new HashSet<>();
        
        int maxSize = set.size();
        while(n-- >= 1)
        {
            int x = sc.nextInt();
            if( set.contains(x) )
            {
                set.remove(x);
            }
            else
            {
                set.add(x);
            }
            
            if( set.size() > maxSize )
                maxSize = set.size();
        }
        System.out.println( maxSize );
    }
    
    
}

class FastScanner {
    BufferedReader br;
    StringTokenizer st;

    public FastScanner() {
        try	{
            br = new BufferedReader(new InputStreamReader(System.in));
            st = new StringTokenizer("");
        } catch (Exception e){e.printStackTrace();}
    }

    public String next() {
        if (st.hasMoreTokens())	return st.nextToken();
        try {st = new StringTokenizer(br.readLine());}
        catch (Exception e) {e.printStackTrace();}
        return st.nextToken();
    }

    public int nextInt() {return Integer.parseInt(next());}

    public long nextLong() {return Long.parseLong(next());}

    public double nextDouble() {return Double.parseDouble(next());}

    public String nextLine() {
        String line = "";
        try {line = br.readLine();}
        catch (Exception e) {e.printStackTrace();}
        return line;
    }

    public Integer[] nextIntegerArray(int n) {
        Integer[] a = new Integer[n];
        for(int i = 0; i < n; i++) a[i] = nextInt();
        return a;
    }

    public int[] nextIntArray(int n) {
        int[] a = new int[n];
        for(int i = 0; i < n; i++) a[i] = nextInt();
        return a;
    }

    public char[] nextCharArray() {
        return nextLine().toCharArray();
    }
}
