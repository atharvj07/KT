import java.io.*;
import java.util.*;

public class Main implements Runnable{
    public static void main(String[] args) throws Exception {
        //new Thread(null,new Main(),"Thread-1",1024*1024*10).start();
        new Main().solve();
    }
    int[]s;
    int[]base=new int[32],rep=new int[32];
    void solve() throws Exception{
        InputReader in=new InputReader(System.in);
        PrintWriter out=new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n=in.nextInt();
        s=new int[n];
        int x;
        for(int i=0;i<n;i++)s[i]=in.nextInt();
        for(x=18;x>=1;x--){
            if(LinearBase(s,x))break;
        }
        int cur=0;
        out.println(x);
        out.print(0);
        for(int i=1;i<(1<<x);i++){
            cur^=rep[Integer.numberOfTrailingZeros(get(i)^get(i-1))];
            out.print(" "+cur);
        }
        out.flush();
    }
    int get(int x){
        return x^(x>>1);
    }
    public boolean LinearBase(int[]a,int n) {
        Arrays.fill(base,0);
        Arrays.fill(rep,0);
        int cnt=0;
        for (int x : a) {
            int tmp=x;
            if(x>=(1<<n))continue;
            for (int j = 30; j >= 0; j--) {
                if ((x >> j) != 0) {//第j位为1
                    if (base[j] == 0) {//对应线性基不存在就等于x
                        base[j] = x;cnt++;rep[j]=tmp;
                        break;
                    } else x ^= base[j];//存在就异或线性基
                }
            }
        }
        return cnt==n;
    }
    @Override
    public void run() {
        try {
            solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    void shuffle(int[]a,int l,int r){
        Random rnd=new Random();
        for (int i=r; i>l+1; i--) {
            int j=rnd.nextInt(i),tmp=a[j];
            a[j]=a[i-1];
            a[i-1]=tmp;
        }
    }
    void shuffle(Object[]a,int l,int r){
        Random rnd=new Random();
        for (int i=r; i>l+1; i--) {
            int j=rnd.nextInt(i);
            Object tmp=a[j];
            a[j]=a[i-1];
            a[i-1]=tmp;
        }
    }
    void shuffle(long[]a,int l,int r){
        Random rnd=new Random();
        for (int i=r; i>l+1; i--) {
            int j=rnd.nextInt(i);
            long tmp=a[j];
            a[j]=a[i-1];
            a[i-1]=tmp;
        }
    }
    class InputReader{
        StreamTokenizer tokenizer;
        public InputReader(InputStream stream){
            tokenizer=new StreamTokenizer(new BufferedReader(new InputStreamReader(stream)));
            tokenizer.ordinaryChars(33,126);
            tokenizer.wordChars(33,126);
        }
        public String next() throws IOException {
            tokenizer.nextToken();
            return tokenizer.sval;
        }
        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }
        public boolean hasNext() throws IOException {
            int res=tokenizer.nextToken();
            tokenizer.pushBack();
            return res!=tokenizer.TT_EOF;
        }
    }
}