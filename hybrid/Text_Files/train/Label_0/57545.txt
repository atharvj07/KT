import java.util.*;
import java.math.*;
import static java.lang.Character.isDigit;
import static java.lang.Character.isLowerCase;
import static java.lang.Character.isUpperCase;
import static java.lang.Math.*;
import static java.math.BigInteger.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Character.isDigit;

public class Main{
    static void debug(Object...os){
        System.err.println(deepToString(os));
    }
    
    void run(){
        N=nextInt();K=nextInt();T=nextInt();
        String s = next();
        str=new int[N];
        for(int i=0;i<N;i++)str[i]=s.charAt(i)-'A';
        ts=new int[K];
        for(int i=0;i<K;i++)ts[i] = nextInt();
        graph=new int[K][K];
        for(int i=0;i<K;i++)for(int j=0;j<K;j++)graph[i][j] = nextInt();
        System.out.println(solve());
    }
    int N,K,T;
    int[] str;
    int[] ts;
    int[][] graph;
    class E implements Comparable<E>{
        int x,y;
        E(int x,int y){
            this.x=x;this.y=y;
        }
        public int compareTo(E o){
            return x-o.x;
        }
    }
    int solve() {
        String[] ss=new String[N];
        for(int i=0;i<N;i++)ss[i]="";
        int[] nxt=new int[K];
        fill(nxt,-1);
        long[] dp=new long[1<<K];// remove
        for(int i=N-1;i>=0;i--) {
            E[] es = new E[K];
            for(int j=0;j<K;j++)es[j] = new E(nxt[j],j);
            sort(es);
            for(int j=0,set=0;j<K;j++)if(es[j].x!=-1) {
                dp[set] += graph[str[i]][es[j].y];
                dp[set | 1<<str[i]] -= graph[str[i]][es[j].y];
                dp[set | 1<<es[j].y] -= graph[str[i]][es[j].y];
                dp[set | 1<<str[i] | 1<<es[j].y] += graph[str[i]][es[j].y];
                if(es[j].y==str[i])break;
                set |= 1<<es[j].y;
            }
            nxt[str[i]] = i;
        }
        for(int i=0;i<K;i++) {
            for(int j=0;j<1<<K;j++)if((j>>i&1)==0)dp[j|1<<i] += dp[j];
        }
        int[] bt=new int[1<<K];
        for(int i=0;i<K;i++)bt[1<<i] = ts[i];
        int[] t=new int[1<<K];
        for(int i=1;i<1<<K;i++) {
            int l = Integer.highestOneBit(i);
            t[i] = t[i^l] + bt[l];
        }
        
        int ex=0;
        for(int i=0;i<K;i++)for(int j=0;j<N;j++)if(str[j]==i)ex |= 1<<i;
        int res=0;
        for(int i=0;i<1<<K;i++)if((ex&i)==i && ex!=i)if(dp[i] + t[i] <= T)res++;
        return res;
    }
    
    int nextInt(){
        try{
            int c=System.in.read();
            if(c==-1) return c;
            while(c!='-'&&(c<'0'||'9'<c)){
                c=System.in.read();
                if(c==-1) return c;
            }
            if(c=='-') return -nextInt();
            int res=0;
            do{
                res*=10;
                res+=c-'0';
                c=System.in.read();
            }while('0'<=c&&c<='9');
            return res;
        }catch(Exception e){
            return -1;
        }
    }
    
    long nextLong(){
        try{
            int c=System.in.read();
            if(c==-1) return -1;
            while(c!='-'&&(c<'0'||'9'<c)){
                c=System.in.read();
                if(c==-1) return -1;
            }
            if(c=='-') return -nextLong();
            long res=0;
            do{
                res*=10;
                res+=c-'0';
                c=System.in.read();
            }while('0'<=c&&c<='9');
            return res;
        }catch(Exception e){
            return -1;
        }
    }
    
    double nextDouble(){
        return Double.parseDouble(next());
    }
    
    String next(){
        try{
            StringBuilder res=new StringBuilder("");
            int c=System.in.read();
            while(Character.isWhitespace(c))
                c=System.in.read();
            do{
                res.append((char)c);
            }while(!Character.isWhitespace(c=System.in.read()));
            return res.toString();
        }catch(Exception e){
            return null;
        }
    }
    
    String nextLine(){
        try{
            StringBuilder res=new StringBuilder("");
            int c=System.in.read();
            while(c=='\r'||c=='\n')
                c=System.in.read();
            do{
                res.append((char)c);
                c=System.in.read();
            }while(c!='\r'&&c!='\n');
            return res.toString();
        }catch(Exception e){
            return null;
        }
    }
    public static void main(String[] args){
        new Main().run();
    }
}