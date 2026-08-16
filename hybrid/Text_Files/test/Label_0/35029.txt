// Working program using Reader Class
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main1
{
    static class Reader
    {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader()
        {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public Reader(String file_name) throws IOException
        {
            din = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public String readLine() throws IOException
        {
            byte[] buf = new byte[64]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1)
            {
                if (c == '\n')
                    break;
                buf[cnt++] = (byte) c;
            }
            return new String(buf, 0, cnt);
        }

        public int nextInt() throws IOException
        {
            int ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do
            {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

            if (neg)
                return -ret;
            return ret;
        }

        public long nextLong() throws IOException
        {
            long ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            }
            while ((c = read()) >= '0' && c <= '9');
            if (neg)
                return -ret;
            return ret;
        }

        public double nextDouble() throws IOException
        {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();

            do {
                ret = ret * 10 + c - '0';
            }
            while ((c = read()) >= '0' && c <= '9');

            if (c == '.')
            {
                while ((c = read()) >= '0' && c <= '9')
                {
                    ret += (c - '0') / (div *= 10);
                }
            }

            if (neg)
                return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException
        {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }

        private void close() throws IOException
        {
            if (din == null)
                return;
            din.close();
        }
    }

    static class Hero{
        int pow, end;
        Hero(int a, int b){
            pow=a;
            end=b;
        }
    }
    static class Tree{
        Tree left, right;
        int st, en, max;
        Tree(int a, int b, int c){
            st=a;
            en=b;
            max=c;
        }
    }
    private static void upd(Tree tr, int pos, int val){
        tr.max=Math.max(tr.max, val);
        if(tr.st==tr.en){
            return;
        }
        int mid=(tr.st+tr.en)/2;
        if(pos<=mid){
            if(tr.left==null){
                tr.left=new Tree(tr.st, mid, 0);
            }
            upd(tr.left, pos, val);
        }
        else{
            if(tr.right==null){
                tr.right=new Tree(mid+1, tr.en, 0);
            }
            upd(tr.right, pos, val);
        }
    }
    private static int query(Tree tr, int lo, int hi){
        if(tr==null){
            return 0;
        }
        if(tr.st==lo && tr.en==hi){
            return tr.max;
        }
        int mid=(tr.st+tr.en)/2;
        if(hi<=mid){
            return query(tr.left, lo, hi);
        }
        if(lo>mid){
            return query(tr.right, lo, hi);
        }
        return Math.max(query(tr.left, lo, mid), query(tr.right, mid+1, hi));
    }
    private static long gcd(long a, long b){
        if(b==0){
            return a;
        }
        return gcd(b, a%b);
    }
    static int find(int a, int[] par){
        if(par[a]==0){
            return a;
        }
        return par[a]=find(par[a], par);
    }
    static void union(int a, int b, int[] par, int[] rank){
        if(rank[a]>=rank[b]){
            par[b]=a;
            rank[a]+=rank[b];
        }
        else{
            par[a]=b;
            rank[b]+=rank[a];
        }
    }
    public static void main(String[] args) throws IOException
    {
        Reader z = new Reader();
        int t = z.nextInt();
        while(t-->0){
            int n=z.nextInt(), m=z.nextInt(), a=z.nextInt(), b=z.nextInt(), i, j, k, p, q;
            int[][] c = new int[m][2];
            for(i=0;i<m;i++){
                c[i][0]=z.nextInt();
                c[i][1]=z.nextInt();
            }
            int[] par = new int[n+1];
            int[] rank = new int[n+1];
            for(i=1;i<=n;i++){
                rank[i]=1;
            }
            for(i=0;i<m;i++){
                if(c[i][0]==b || c[i][1]==b){
                    continue;
                }
                j=find(c[i][0], par);
                k=find(c[i][1], par);
                if(j!=k){
                    union(j, k, par, rank);
                }
            }
            p=n-rank[find(a, par)]-1;
            par = new int[n+1];
            rank = new int[n+1];
            for(i=1;i<=n;i++){
                rank[i]=1;
            }
            for(i=0;i<m;i++){
                if(c[i][0]==a || c[i][1]==a){
                    continue;
                }
                j=find(c[i][0], par);
                k=find(c[i][1], par);
                if(j!=k){
                    union(j, k, par, rank);
                }
            }
            q=n-rank[find(b, par)]-1;
            System.out.println(1L*p*q);
        }
        z.close();
    }
}