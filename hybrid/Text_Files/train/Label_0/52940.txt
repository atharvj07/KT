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
            
        
    }
    
    private class TestCase {
        
        int n, k;
        int[][] adj;
        int[] Vt;
        int[] Vk;
        int[][] Kc;
        boolean[] Kf;
        int[] Kv;
        int[] Kp;
        
        int[] k_adjn;
        int[][] k_adjv;
        int[][] k_adjs;
        
        int[] q;
        
        public void dfs(int u, int c, int t)
        {
            Vk[u] = c;
            Vt[u] = t;
            
            int v;
            for (int i=0; i<k_adjn[u]; i++)
            {
                v = k_adjs[u][i];
                if (Vk[v]==-1)
                {
                    dfs(v, c, k_adjv[u][i]==0 ? 1-t : t);
                }
            }
        }
        
        public int getk(int u)
        {
            int s = 0;
            
            int c = Vk[u];
            while (Kp[c] != -1)
            {
                q[s++] = c;
                c = Kp[c];
            }
            
            for (int i=0; i<s; i++)
            {
                Kp[q[i]] = c;
            }
            
            return c;
        }
        

        public Object solve() {
            
            n = readInt();
            k = readInt();
            
            String s = readLn();
            
            q = new int[k];
            
            adj = new int[n][2];
            
            k_adjn = new int[k];
            k_adjs = new int[k][];
            k_adjv = new int[k][];
            Arrays.fill(k_adjn, 0);
            
            int j,i,c,u,v;
            for (i=0; i<n; i++)
            {
                adj[i][0] = -1;
                adj[i][1] = -1;
            }
            
            int[] C = new int[k];
            for (i=0; i<k; i++)
            {
                c = readInt();
                readIntArray(C, c);
                
                for (j=0; j<c; j++)
                {
                    u = C[j]-1;
                    if (adj[u][0]==-1)
                    {
                        adj[u][0] = i;
                    }
                    else
                    {
                        adj[u][1] = i;
                    }
                }
            }
            
            for (i=0; i<n; i++)
            {
                if (adj[i][1]!=-1)
                {
                    u = adj[i][0];
                    v = adj[i][1];
                    
                    k_adjn[u] ++;
                    k_adjn[v] ++;
                }
            }
            
            for (i=0; i<k; i++)
            {
                k_adjs[i] = new int[k_adjn[i]];
                k_adjv[i] = new int[k_adjn[i]];
            }
            
            Arrays.fill(k_adjn, 0);
            for (i=0; i<n; i++)
            {
                if (adj[i][1]!=-1)
                {
                    u = adj[i][0];
                    v = adj[i][1];
                    
                    c = s.charAt(i) - '0';
                    
                    k_adjv[u][k_adjn[u]] = c;
                    k_adjv[v][k_adjn[v]] = c;
                            
                    k_adjs[u][k_adjn[u]]  = v;
                    k_adjs[v][k_adjn[v]]  = u;
                    
                    k_adjn[u] ++;
                    k_adjn[v] ++;
                }
            }
            
            Vt = new int[k];
            Vk = new int[k];
            Kc = new int[k][2];
            Kf = new boolean[k];
            Kp = new int[k];
            Kv = new int[k];
            
            Arrays.fill(Vk, -1);
            c = 0;
            
            for (i=0; i<n; i++)
            {
                if ((adj[i][1]==-1) && (adj[i][0]!=-1) && (Vk[adj[i][0]]==-1)) 
                {
                    dfs(adj[i][0], c++, '1' - s.charAt(i));
                }
            }
            
            for (i=0; i<k; i++)
            {
                if (Vk[i]==-1)
                {
                    dfs(i, c++, 0);
                }
            }
            
            Arrays.fill(Vk, -1);
            Arrays.fill(Kf, false);
            Arrays.fill(Kp, -1);
            Arrays.fill(Kv, -1);
            for (i=0; i<k; i++)
            {
                Arrays.fill(Kc[i], 0);
            }
            
            for (i=0; i<k; i++)
            {
                Vk[i] = i;
                Kc[i][ Vt[i] ] = 1;
            }
            
            int S = 0;
            int[] R = new int[n];
            
            int c1, c2;
            for (i=0; i<n; i++)
            {
                if (adj[i][1] == -1)
                {
                    u = adj[i][0];
                    if (u>-1)
                    {
                        c = getk(u);
                    
                        if (!Kf[c])
                        {
                            if (Kv[c]>-1)
                            {
                                S -= Kc[c][Kv[c]];
                            }
                            S += Kc[c][1];
                            Kf[c] = true;
                            Kv[c] = 1;
                        }
                    }
                }
                else
                {
                    u = adj[i][0];
                    c1 = getk(u);
                    v = adj[i][1];
                    c2 = getk(v);
                    
                    if (c1 != c2)
                    {
                        if (Kv[c1]>-1)
                        {
                            S -= Kc[c1][Kv[c1]];
                        }
                        if (Kv[c2]>-1)
                        {
                            S -= Kc[c2][Kv[c2]];
                        }
                        
                        Kp[c2] = c1;
                        Kf[c1] = Kf[c1] || Kf[c2];
                        
                        Kc[c1][0] = Kc[c1][0] + Kc[c2][0];
                        Kc[c1][1] = Kc[c1][1] + Kc[c2][1];
                        
                        if (Kf[c1])
                        {
                            Kv[c1] = 1;
                        }
                        else
                        {
                            Kv[c1] = Kc[c1][0] < Kc[c1][1] ? 0 : 1;
                        }
                        
                        S += Kc[c1][Kv[c1]];
                    }
                }
                
                R[i] = S;
            }
            
            
            
            
            
            
            
            printArray(R, n);
            
            
            return null;
            
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
