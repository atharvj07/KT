import java.io.*;
import java.lang.Math;
import java.util.*;

public class Main  {

    public BufferedReader in;
    public PrintStream out;

    public boolean log_enabled = false;
    
    public boolean multiply_tests = false;

    public static boolean do_gen_test = false;
    
    public void gen_test() {
        out.println(2);
        int i, n = 1000000;
        char[] ch = new char[n];
        
        for (i=0; i<n; i++)
        {
            ch[i] = (i<10) || (i%2==0) ? 'a' : 'b';
        }
        //ch[3] = 'x';
        ch[n-1] = 'z';
        
        out.println(new String(ch));
        
        //ch[3] = 'a';
        ch[n-1] = 'a';
        
        out.println(new String(ch));
        
    }
    
    public void gen_test2() {
        
        int i,j,k = 7;
        
        int r, cnt = 0;
        for (i=1; i<=k; i++)
        {
            r = 1;
            for (j=0; j<i; j++)
            {
                r *= 3;
            }
            
            cnt += r;
        }
        
        String[] list = new String[cnt];
        String w;
        
        int u, x, c = 0;
        
        for (i=1; i<=k; i++)
        {
            r = 1;
            for (j=0; j<i; j++)
            {
                r *= 3;
            }
            
            for (u=0; u<r; u++)
            {
                w = "";
                
                x = u;
                for (j=0; j<i; j++)
                {
                    w = w.concat(  String.valueOf((char)( x % 3 + 'a'  )) );
                    x /= 3;
                }
                
                list[c++] = w;
            }
        }
        
        
        out.println(2*cnt*cnt);
        
        for (i=0; i<cnt; i++)
        {
            for (j=0; j<cnt; j++)
            {
                out.println(list[i]);
                out.println(list[j]);
            }
        }
        
        
        
    }
    
    public int N;
    public int[][] D;
    public int[][] U;
    public int[] D_cnt;
    
    public String[] words;
    public int [][] dfpos;
    
    public long GGG = 0;
    
    private class TestCase {
        
        public int charAtPos(int k, int j)
        {
            return (j>=0) && (j<words[k].length()) ? (int)words[k].charAt(j) : 0;
        }
        
        public void get_d_list(String s, int k)
        {
            int i, cnt = 2, n = s.length();
            for (i=1; i<n; i++)
            {
                if (s.charAt(i)!=s.charAt(i-1))
                {
                    cnt ++;
                }
            }
            
            D_cnt[k] = cnt;
            
            D[k] = new int[cnt];
            U[k] = new int[cnt];
            
            int l = 0, r = cnt-1;
            
            int u = 1;
            for (i=0; i<n; i++)
            {
                if ((i+1<n)&&(s.charAt(i)==s.charAt(i+1)))
                {
                    u++;
                    continue;
                }
                
                if ((i+1 == n) || s.charAt(i+1) < s.charAt(i))
                {
                    U[k][l] = u;
                    D[k][l++] = i;
                }
                else
                {
                    U[k][r] = u;
                    D[k][r--] = i;
                }
                
                u = 1;
            }
            
            D[k][l] = n;
            U[k][l] = 1;
        }
        
        public int _cmp(int k, int d1, int d2)
        {
            String w1 = words[k];
            if (d1<w1.length())
            {
                w1 = w1.substring(0, d1).concat(
                    w1.substring(d1+1)
                );
            }
            
            String w2 = words[k+1];
            if (d2<w2.length())
            {
                w2 = w2.substring(0, d2).concat(
                    w2.substring(d2+1)
                );
            }
            
            int c1 = _cmp(k, d1, d2);
            //c = _cmp(k, d1, d2);
            
            int c2 = w1.compareTo(w2);
            
            if ((c1*c2<0)|| (c1*c1+c2*c2 == 1) )
            {
                int c3 = _cmp(k, d1, d2);
            }
            
            return w1.compareTo(w2);
        }
                
        public int cmp(int k, int d1, int d2)
        {
            if (d1==d2)
            {
                if (dfpos[k][0]==d1)
                {
                    return charAtPos(k, dfpos[k][1]) - charAtPos(k+1, dfpos[k][1]);
                }
                
                if ( (dfpos[k][0]<d1) ||  (charAtPos(k, d1+1) == charAtPos(k+1, d2+1)) )
                {
                    return charAtPos(k, dfpos[k][0]) - charAtPos(k+1, dfpos[k][0]);
                }
                
                return charAtPos(k, d1+1) - charAtPos(k+1, d2+1);
            }
            
            int k1 = k;
            int k2 = k+1;
            int z = 1;
            
            if (d1 > d2)
            {
                z = d1;
                d1 = d2;
                d2 =z;
                z = -1;
                k1 = k+1;
                k2 = k;
            }
                
            if ( (dfpos[k][0]>=0) && (dfpos[k][0] < d1))
            {
                return z*(charAtPos(k1, dfpos[k][0]) - charAtPos(k2, dfpos[k][0]));
            }

            if ((dfpos[k][0]==-1) || (d1 < dfpos[k][0]))
            {
                return z*(charAtPos(k1, d1+1) - charAtPos(k2, d1));
            }
            
            int p2 = dfpos[k][ z==1 ? 2 : 3 ];
            int p1 = p2+1;
            
            if (d2<p2)
            {
                p1 = d2+1;
                p2 = d2+1;
            }
            else if (d2==p2)
            {
                p1 = dfpos[k][ z==1 ? 4 : 5 ];
                p2 = p1;
            }

            /*int p1 = d1+1;
            int p2 = d1;
            
            while (charAtPos(k1, p1)==charAtPos(k2,p2))
            {
                GGG ++;
                
                if (p1>= words[k1].length() && p2>= words[k2].length() )
                {
                    return 0;
                }

                p1++;
                p2++;
                if (p2==d2)
                {
                    p2++;
                }
            }*/

            return z*(charAtPos(k1, p1) - charAtPos(k2,p2));
        }

        public Object solve() {
            
            int i,j,N = readInt();
            words = new String[N];
            
            for (i=0; i<N; i++)
            {
                words[i] = readLn();
            }
            
            D_cnt = new int[N];
            D = new int[N][];
            U = new int[N][];
            
            for (i=0; i<N; i++)
            {
                get_d_list(words[i], i);
            }
            
            dfpos = new int[N][6];
            
            for (i=0; i+1<N; i++)
            {
                dfpos[i][0] = -1;
                dfpos[i][1] = -1;
                
                j = 0;
                while ( (j<words[i].length()) || (j<words[i+1].length()) )
                {
                    if (charAtPos(i,j) != charAtPos(i+1,j)) 
                    {
                        if (dfpos[i][0] == -1)
                        {
                            dfpos[i][0] = j;
                        }
                        else 
                        {
                            dfpos[i][1] = j;
                            break;
                        }
                    }
                    j ++;
                }
                
                if (dfpos[i][0]>-1)
                {
                    j = dfpos[i][0];
                    while ( ((j+1<words[i].length()) || (j<words[i+1].length())) && (charAtPos(i,j+1) == charAtPos(i+1,j))  )
                    {
                        j ++;
                    }
                    dfpos[i][2] = j;
                    
                    j = dfpos[i][0];
                    while ( ((j<words[i].length()) || (j+1<words[i+1].length())) && (charAtPos(i,j) == charAtPos(i+1,j+1))  )
                    {
                        j ++;
                    }
                    dfpos[i][3] = j; 
                    
                    j = dfpos[i][2]+1;
                    while ( ((j<words[i].length()) || (j<words[i+1].length())) && (charAtPos(i,j) == charAtPos(i+1,j))  )
                    {
                        j ++;
                    }
                    dfpos[i][4] = j;
                    
                    j = dfpos[i][3]+1;
                    while ( ((j<words[i].length()) || (j<words[i+1].length())) && (charAtPos(i,j) == charAtPos(i+1,j))  )
                    {
                        j ++;
                    }
                    dfpos[i][5] = j;
                    
                    
                    
                }
                
                
                
                
            }
            
            int[][] next = new int[N-1][];
            
            int p;
            for (i=0; i<N-1; i++)
            {
                next[i] = new int[D_cnt[i]];
                
                p = 0;
                for (j=0; j<D_cnt[i]; j++)
                {
                    while ( (p<D_cnt[i+1]) && (cmp(i, D[i][j], D[i+1][p])>0) )
                    {
                        p ++;
                    }
                    
                    next[i][j] = p;
                }
            }
            
            long[][] R = new long[N][];
            long M = 1000000007;
            
            R[N-1] = new long[ D_cnt[N-1]+1 ];
            R[N-1][D_cnt[N-1]] = 0;
            
            for (i=D_cnt[N-1]-1; i>=0; i--)
            {
                R[N-1][i] = (R[N-1][i+1] + U[N-1][i]) % M;
            }
            
            for (i=N-2; i>=0; i--)
            {
                R[i] = new long[ D_cnt[i]+1 ];
                R[i][D_cnt[i]] = 0;
                
                for (j=D_cnt[i]-1; j>=0; j--)
                {
                    R[i][j] =  (R[i][j+1] + U[i][j] * R[i+1][next[i][j]]) % M;
                }
            }
                                      
            
            return R[0][0];
            
            //return strf("%f", 0);
            
            //out.printf("Case #%d: \n", caseNumber);
            //return null;
        }
        
        public int caseNumber;
        
        TestCase(int number) {
            caseNumber = number;
        }
        
        public void run(){
            Object r = this.solve();
            
            if ((r != null))
            {
                //outputCaseNumber(r);
                out.println(r);
            }
        }
        
        public String impossible(){
            return "IMPOSSIBLE";
        }
        
        public String strf(String format, Object... args)
        {
            return String.format(format, args);
        }
        
//        public void outputCaseNumber(Object r){
//            //out.printf("Case #%d:", caseNumber);
//            if (r != null)
//            {
//              //  out.print(" ");
//                out.print(r);
//            }
//            out.print("\n");
//        }
    }

    public void run() {
        //while (true)
        {
            int t = multiply_tests ?  readInt() : 1;
            for (int i = 0; i < t; i++) {
                TestCase T = new TestCase(i + 1);
                T.run();
            }
        }
    }
    

    
    public Main(BufferedReader _in, PrintStream _out){
        in = _in;
        out = _out;
    }
    

    public static void main(String args[]) {
        Locale.setDefault(Locale.US);
        Main S;
        try {
            S = new Main(
                        new BufferedReader(new InputStreamReader(System.in)),
                        System.out
                );
        } catch (Exception e) {
            return;
        }
        
        S.run();
        
    }

    private StringTokenizer tokenizer = null;

    public int readInt() {
        return Integer.parseInt(readToken());
    }

    public long readLong() {
        return Long.parseLong(readToken());
    }

    public double readDouble() {
        return Double.parseDouble(readToken());
    }

    public String readLn() {
        try {
            String s;
            while ((s = in.readLine()).length() == 0);
            return s;
        } catch (Exception e) {
            return "";
        }
    }

    public String readToken() {
        try {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                tokenizer = new StringTokenizer(in.readLine());
            }
            return tokenizer.nextToken();
        } catch (Exception e) {
            return "";
        }
    }

    public int[] readIntArray(int n) {
        int[] x = new int[n];
        readIntArray(x, n);
        return x;
    }
    
    public int[] readIntArrayBuf(int n) {
        int[] x = new int[n];
        readIntArrayBuf(x, n);
        return x;
    }

    public void readIntArray(int[] x, int n) {
        for (int i = 0; i < n; i++) {
            x[i] = readInt();
        }
    }
    
    public long[] readLongArray(int n) {
        long[] x = new long[n];
        readLongArray(x, n);
        return x;
    }
    
    public long[] readLongArrayBuf(int n) {
        long[] x = new long[n];
        readLongArrayBuf(x, n);
        return x;
    }

    public void readLongArray(long[] x, int n) {
        for (int i = 0; i < n; i++) {
            x[i] = readLong();
        }
    }

    public void logWrite(String format, Object... args) {
        if (!log_enabled) {
            return;
        }

        out.printf(format, args);
    }
    
    public void readLongArrayBuf(long[] x, int n) {
        
        char[]buf = new char[1000000];
        long r = -1;
        int k= 0, l = 0;
        long d;
        
        while (true)
        {
            try{
                l = in.read(buf, 0, 1000000);
            }
            catch(Exception E){};
            
            for (int i=0; i<l; i++)
            {
                if (('0'<=buf[i])&&(buf[i]<='9'))
                {
                    if (r == -1)
                    {
                        r = 0;
                    }
                    d = buf[i] - '0';
                    r = 10 * r + d;
                }
                else
                {
                    if (r != -1)
                    {
                        x[k++] = r;
                    }
                    
                    r = -1;
                }
            }
            
            if (l<1000000)
                return;
        }
    }
    
    public void readIntArrayBuf(int[] x, int n) {
        
        char[]buf = new char[1000000];
        int r = -1;
        int k= 0, l = 0;
        int d;
        
        while (true)
        {
            try{
                l = in.read(buf, 0, 1000000);
            }
            catch(Exception E){};
            
            for (int i=0; i<l; i++)
            {
                if (('0'<=buf[i])&&(buf[i]<='9'))
                {
                    if (r == -1)
                    {
                        r = 0;
                    }
                    d = buf[i] - '0';
                    r = 10 * r + d;
                }
                else
                {
                    if (r != -1)
                    {
                        x[k++] = r;
                    }
                    
                    r = -1;
                }
            }
            
            if (l<1000000)
                return;
        }
    }
    
    public void printArray(long[] a, int n)
    {
        printArray(a, n, ' ');
    }
    
    public void printArray(int[] a, int n)
    {
        printArray(a, n, ' ');
    }
            
    public void printArray(long[] a, int n, char dl)
    {
        long x; 
        int i, l = 0;
        for (i=0; i<n; i++)
        {
            x = a[i];
            
            if (x<0)
            {
                x = -x;
                l++;
            }
            
            if (x==0)
            {
                l++;
            }
            else
            {
                while (x>0)
                {
                    x /= 10;
                    l++;
                }
            }
        }
        
        l += n-1;
        
        char[] s = new char[l];
        
        l--;
        boolean z;
        for (i=n-1; i>=0;  i--)
        {
            x = a[i];
            z = false;            
            if (x<0)
            {
                x = -x;
                z = true;
            }
            
            do{
                s[l--] = (char)('0' + (x % 10));
                x /= 10;
            } while (x>0);
            
            if (z)
            {
                s[l--] = '-';
            }
            
            if (i>0)
            {
                s[l--] = dl;
            }
        }
        
        out.println(new String(s));
    }
    
    public void printArray(int[] a, int n, char dl)
    {
        int x; 
        int i, l = 0;
        for (i=0; i<n; i++)
        {
            x = a[i];
            
            if (x<0)
            {
                x = -x;
                l++;
            }
            
            if (x==0)
            {
                l++;
            }
            else
            {
                while (x>0)
                {
                    x /= 10;
                    l++;
                }
            }
        }
        
        l += n-1;
        
        char[] s = new char[l];
        
        l--;
        boolean z;
        for (i=n-1; i>=0;  i--)
        {
            x = a[i];
            z = false;            
            if (x<0)
            {
                x = -x;
                z = true;
            }
            
            do{
                s[l--] = (char)('0' + (x % 10));
                x /= 10;
            } while (x>0);
            
            if (z)
            {
                s[l--] = '-';
            }
            
            if (i>0)
            {
                s[l--] = dl;
            }
        }
        
        out.println(new String(s));
    }
    
    public void printMatrix(int[][] a, int n, int m)
    {
        int x; 
        int i,j, l = 0;
        for (i=0; i<n; i++)
        {
            for (j=0; j<m; j++)
            {
                x = a[i][j];
            
                if (x<0)
                {
                    x = -x;
                    l++;
                }

                if (x==0)
                {
                    l++;
                }
                else
                {
                    while (x>0)
                    {
                        x /= 10;
                        l++;
                    }
                }
            }
            
            l += m-1;
        }
        
        l += n-1;
        
        
        char[] s = new char[l];
        
        l--;
        boolean z;
        for (i=n-1; i>=0;  i--)
        {
            for (j=m-1; j>=0;  j--)
            {
                x = a[i][j];
                z = false;            
                if (x<0)
                {
                    x = -x;
                    z = true;
                }

                do{
                    s[l--] = (char)('0' + (x % 10));
                    x /= 10;
                } while (x>0);

                if (z)
                {
                    s[l--] = '-';
                }

                if (j>0)
                {
                    s[l--] = ' ';
                }
            }
            
            if (i>0)
            {
                 s[l--] = '\n';
            }
        }
        
        out.println(new String(s));
    }
    
    public void printMatrix(long[][] a, int n, int m)
    {
        long x; 
        int i,j, l = 0;
        for (i=0; i<n; i++)
        {
            for (j=0; j<m; j++)
            {
                x = a[i][j];
            
                if (x<0)
                {
                    x = -x;
                    l++;
                }

                if (x==0)
                {
                    l++;
                }
                else
                {
                    while (x>0)
                    {
                        x /= 10;
                        l++;
                    }
                }
            }
            
            l += m-1;
        }
        
        l += n-1;
        
        
        char[] s = new char[l];
        
        l--;
        boolean z;
        for (i=n-1; i>=0;  i--)
        {
            for (j=m-1; j>=0;  j--)
            {
                x = a[i][j];
                z = false;            
                if (x<0)
                {
                    x = -x;
                    z = true;
                }

                do{
                    s[l--] = (char)('0' + (x % 10));
                    x /= 10;
                } while (x>0);

                if (z)
                {
                    s[l--] = '-';
                }

                if (j>0)
                {
                    s[l--] = ' ';
                }
            }
            
            if (i>0)
            {
                 s[l--] = '\n';
            }
        }
        
        out.println(new String(s));
    }
    
    
}
