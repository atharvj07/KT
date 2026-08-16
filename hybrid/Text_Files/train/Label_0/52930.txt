
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
        n=nextInt();
        cs=next().toCharArray();
        int res=solve();
        for(int i=0;i<4;i++){
            if((res>>i&1)==1){
                System.out.println(SS[i]);
            }
        }
    }
    int n;
    char[] cs;
    String[] SS={"Gryffindor","Hufflepuff","Ravenclaw","Slytherin"};
    String S="GHRS";
    
    class Array{
        int[] is;
        Array(int[] is){
            this.is=is;
        }
        public int hashCode(){
            return Arrays.hashCode(is);
        }
        public boolean equals(Object obj){
            Array other=(Array)obj;
            if(!Arrays.equals(is,other.is)) return false;
            return true;
        }
    }
    
    int solve(){
        Array init=new Array(new int[4]);
        HashSet<Array>[] sets=new HashSet[2];
        for(int i=0;i<2;i++)
            sets[i]=new HashSet<Array>();
        sets[0].add(init);
        for(int i=0;i<n;i++){
            int cur=i%2,nxt=(i+1)%2;
            sets[nxt].clear();
            for(Array a:sets[cur]){
                if(cs[i]=='?'){
                    int min=Integer.MAX_VALUE;
                    for(int j=0;j<4;j++)
                        min=min(min,a.is[j]);
                    for(int j=0;j<4;j++)
                        if(a.is[j]==min){
                            int[] is=a.is.clone();
                            is[j]++;
                            sets[nxt].add(new Array(is));
                        }
                }else {
                    int[] is = a.is.clone();
                    is[S.indexOf(cs[i])]++;
                    sets[nxt].add(new Array(is));
                }
            }
        }
        
        int res=0;
        for(Array a:sets[n%2]){
            int min=Integer.MAX_VALUE;
            for(int j=0;j<4;j++)
                min=min(min,a.is[j]);
            for(int j=0;j<4;j++)
                if(a.is[j]==min){
                    res|=1<<j;
                }
        }
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
