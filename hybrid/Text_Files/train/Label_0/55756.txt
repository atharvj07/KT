import java.io.*;
import java.util.*;
import java.math.*;
// import java.awt.Point;
 
public class Main {
    InputStream is;
    PrintWriter out;
    String INPUT = "";
 
    static int mod = 1_000_000_007;
    // int mod = 998244353;
    long inf = Long.MAX_VALUE/2;

    void solve(){
        int x = ni();
        int y = ni();
        int z = ni();
        int k = ni();
        long[][] a = new long[x][2];
        long[][] b = new long[y][2];
        long[][] c = new long[z][2];
        for(int i = 0; i < x; i++){
            a[i][0] = nl();
            a[i][1] = i+1;
        }
        for(int i = 0; i < y; i++){
            b[i][0] = nl();
            b[i][1] = (i+1)*10000l;
        }
        for(int i = 0; i < z; i++){
            c[i][0] = nl();
            c[i][1] = (i+1)*100000000l;
        }
        Arrays.sort(a, (v,w)->Long.compare(w[0],v[0]));
        Arrays.sort(b, (v,w)->Long.compare(w[0],v[0]));
        Arrays.sort(c, (v,w)->Long.compare(w[0],v[0]));

        HashMap<Long,Long> map = new HashMap<>();
        // f(map,a,b,c);
        // f(map,a,c,b);
        // f(map,b,a,c);
        // f(map,b,c,a);
        // f(map,c,a,b);
        // f(map,c,b,a);
        for(int i = 0; i < x; i++){
            for(int j = 0; j < y; j++){
                for(int m = 0; m < z; m++){
                    if((i+1)*(j+1)*(m+1)>3000) break;
                    long val = a[i][0] + b[j][0] + c[m][0];
                    long key = a[i][1] + b[j][1] + c[m][1];
                    map.put(key,val);
                }
            }
        }
        long[] list = new long[map.size()];
        int idx = 0;
        for(long ret : map.keySet()){
            list[idx++] = map.get(ret);
        }
        Arrays.sort(list);
        idx = 0;
        for(int i = list.length-1; i >= 0; i--){
            out.println(list[i]);
            idx++;
            if(idx==k) break;
        }
    }

    void f(HashMap<Long,Long> map, long[][] a, long[][] b, long[][] c){
        int x = a.length;
        int y = b.length;
        int z = c.length;
        int count = 0;
        for(int i = 0; i < x; i++){
            for(int j = 0; j < y; j++){
                for(int k = 0; k < z; k++){
                    long val = a[i][0] + b[j][0] + c[k][0];
                    long key = a[i][1] + b[j][1] + c[k][1];
                    map.put(key,val);
                    count++;
                    if(count>3000) break;
                }
                if(count>3000) break;
            }
            if(count>3000) break;
        }
    }

    void run() throws Exception
    {
        is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
        out = new PrintWriter(System.out);
        long s = System.currentTimeMillis();
        solve();
        out.flush();
        if(!INPUT.isEmpty())tr(System.currentTimeMillis()-s+"ms");
    }
    
    public static void main(String[] args) throws Exception { new Main().run(); }
    
    private byte[] inbuf = new byte[1024];
    private int lenbuf = 0, ptrbuf = 0;
    
    private int readByte()
    {
        if(lenbuf == -1)throw new InputMismatchException();
        if(ptrbuf >= lenbuf){
            ptrbuf = 0;
            try { lenbuf = is.read(inbuf); } catch (IOException e) { throw new InputMismatchException(); }
            if(lenbuf <= 0)return -1;
        }
        return inbuf[ptrbuf++];
    }
    
    private boolean isSpaceChar(int c) { return !(c >= 33 && c <= 126); }
    private int skip() { int b; while((b = readByte()) != -1 && isSpaceChar(b)); return b; }
    
    private double nd() { return Double.parseDouble(ns()); }
    private char nc() { return (char)skip(); }
    
    private String ns()
    {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while(!(isSpaceChar(b) && b != ' ')){
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }
    
    private char[] ns(int n)
    {
        char[] buf = new char[n];
        int b = skip(), p = 0;
        while(p < n && !(isSpaceChar(b))){
            buf[p++] = (char)b;
            b = readByte();
        }
        return n == p ? buf : Arrays.copyOf(buf, p);
    }
    
    private char[][] nm(int n, int m)
    {
        char[][] map = new char[n][];
        for(int i = 0;i < n;i++)map[i] = ns(m);
        return map;
    }
    
    private int[] na(int n)
    {
        int[] a = new int[n];
        for(int i = 0;i < n;i++)a[i] = ni();
        return a;
    }
    
    private int ni()
    {
        int num = 0, b;
        boolean minus = false;
        while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if(b == '-'){
            minus = true;
            b = readByte();
        }
        
        while(true){
            if(b >= '0' && b <= '9'){
                num = num * 10 + (b - '0');
            }else{
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
    
    private long nl()
    {
        long num = 0;
        int b;
        boolean minus = false;
        while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if(b == '-'){
            minus = true;
            b = readByte();
        }
        
        while(true){
            if(b >= '0' && b <= '9'){
                num = num * 10 + (b - '0');
            }else{
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
    
    private static void tr(Object... o) { System.out.println(Arrays.deepToString(o)); }
 
}
