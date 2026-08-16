
import java.io.*;
import java.util.*;

public class Main{
    public static void main(String args[]){
        Solver s=new Solver();
        s.run();
    }
}

class Solver {
    PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
    FastReader in=new FastReader();
    public long pow(long a, long b){
        long ans=1;
        while(b>0){
            if(b%2==1){
                ans*=a;
            }
            a*=a;
            b/=2;
        }
        return ans;
    }
    public int gcd(int a, int b){
        while (b>0) {
            a %= b;
            int temp=b;
            b=a;
            a=temp;
        }
        return a;
    }

    int mod=(int)1e9 +7;


    public boolean compare(char[] s, char[] p, int i){
        int j=0;
        while(i<s.length && j<p.length){
            if(s[i] != p[j]) return false;
            i++;j++;
        }

        if(j!=p.length) return false;
        return true;
    }

    public void solve() {
        char[] s= in.nextLine().toCharArray();
        char[] p= in.nextLine().toCharArray();

        int[] lps= new int[p.length];

        for(int i=1;i<p.length;i++){
            int j= lps[i-1];
            while(j>0 && p[i] != p[j]){
                j=lps[j-1];
            }
            if(p[i] == p[j]){
                j++;
            }
            lps[i]= j;
        }

        int ans=0;
        for(int i=0, j=0;i<s.length;i++){
            if(s[i]==p[j]){
                j++;
            }else{
                while(j>0 && s[i] != p[j]){
                    j= lps[j-1];
                }
                if(s[i] == p[j]){
                    j++;
                }
            }
            if(j==p.length){
                ans++;
                j=0;
            }
        }


        out.println(ans);
    }

    public void run(){
        int t=1;
        for(int i=0;i<t;i++){
            solve();
            out.println();
        }
        out.close();
    }
}


//class FastReader {
//    final private int BUFFER_SIZE = 1 << 16;
//    private DataInputStream din;
//    private byte[] buffer;
//    private int bufferPointer, bytesRead;
//
//    public FastReader() {
//        din = new DataInputStream(System.in);
//        buffer = new byte[BUFFER_SIZE];
//        bufferPointer = bytesRead = 0;
//    }
//
//    public FastReader(String file_name) throws IOException{
//        din = new DataInputStream(new FileInputStream(file_name));
//        buffer = new byte[BUFFER_SIZE];
//        bufferPointer = bytesRead = 0;
//    }
//
//    public String nextLine() {
//        try{
//            byte[] buf = new byte[10000]; // line length
//            int cnt = 0, c;
//            while ((c = read()) != -1) {
//                if (c == '\n')
//                    break;
//                buf[cnt++] = (byte) c;
//            }
//            return new String(buf, 0, cnt);
//        }catch (Exception e){
//            System.out.println(e.getMessage());
//            return null;
//        }
//    }
//
//    public int nextInt()  {
//        int ret = 0;
//        try {
//            byte c = read();
//            while (c <= ' ')
//                c = read();
//            boolean neg = (c == '-');
//            if (neg) c = read();
//            do{
//                ret = ret * 10 + c - '0';
//            } while ((c = read()) >= '0' && c <= '9');
//            if (neg) return -ret;
//            return ret;
//        } catch (Exception e) {
//            System.out.println(e.getMessage());
//            return -1;
//        }
//    }
//
//    public long nextLong()   {
//        try {
//            long ret = 0;
//            byte c = read();
//            while (c <= ' ') c = read();
//            boolean neg = (c == '-');
//            if (neg)
//                c = read();
//            do {
//                ret = ret * 10 + c - '0';
//            }
//            while ((c = read()) >= '0' && c <= '9');
//            if (neg)
//                return -ret;
//            return ret;
//        } catch (Exception e) {
//            System.out.println(e.getMessage());
//            return -1;
//        }
//    }
//
//    public double nextDouble()  {
//        try {
//            double ret = 0, div = 1;
//            byte c = read();
//            while (c <= ' ')
//                c = read();
//            boolean neg = (c == '-');
//            if (neg) c = read();
//            do {
//                ret = ret * 10 + c - '0';
//            }
//            while ((c = read()) >= '0' && c <= '9');
//            if (c == '.') {
//                while ((c = read()) >= '0' && c <= '9') {
//                    ret += (c - '0') / (div *= 10);
//                }
//            }
//            if (neg) return -ret;
//            return ret;
//        } catch (Exception e) {
//            System.out.println(e.getMessage());
//            return -1;
//        }
//    }
//
//    private void fillBuffer() throws IOException{
//        bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
//        if (bytesRead == -1)
//            buffer[0] = -1;
//    }
//
//    private byte read() throws IOException  {
//        try{
//            if (bufferPointer == bytesRead)
//                fillBuffer();
//            return buffer[bufferPointer++];
//        }catch(Exception e){
//            System.out.println(e.getMessage());
//            return -1;
//        }
//    }
//
//    public void close() throws IOException {
//        if (din == null)
//            return;
//        din.close();
//    }
//}


class FastReader {
    BufferedReader br;
    StringTokenizer st;

    public FastReader() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }

    int nextInt() {
        return Integer.parseInt(next());
    }

    long nextLong() {
        return Long.parseLong(next());
    }

    double nextDouble() {
        return Double.parseDouble(next());
    }

    String nextLine() {
        String str = "";
        try {
            str = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str;
    }
}
