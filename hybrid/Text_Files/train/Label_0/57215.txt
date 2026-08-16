import java.io.*;
import java.util.*;

public class Drogon {
    public static void main(String[] args) throws Exception {
        FastReader sc = new FastReader();
        int t=sc.nextInt();
        while (t-->0){
            String s=sc.next();
            String re=(new StringBuilder(s)).reverse().toString();
            int  n=s.length();
            Hash h=new Hash(s,57,1000000007);
            Hash hr=new Hash(re,57,1000000007);
            int ind=0;
            int max=1;
            int a1=0,a2=-1;
            for (int i=0;i<n/2;i++){
                if (h.isEq(h,0,i,hr,0,i)){
                    ind=i;
                    if (max<(i+1)*2){
                        max=(i+1)*2;
                        a1=i;a2=n-1-i;
                    }
                }
            }
            int max2=max;
            int st=max==1?0:ind+1;
            int en=max==1?n:n-ind-1;
            for (int i=st;i<en;i++){
                int mn=Math.min(n-1-(i+1),n-1-(i+i-st+1));
                int mx=Math.max(n-1-(i+1),n-1-(i+i-st+1));
                if (i+(i-st+1)<en && h.isEq(h,st,i,hr,mn,mx)){
                    if(max<2*st+i+i-st+1-st+1){
                        max=2*st+i+i-st+1-st+1;
                        a1=i+i-st+1;
                    }
                }
                mn=Math.min(n-1-(i+2),n-1-(i+i-st+2));
                mx=Math.max(n-1-(i+2),n-1-(i+i-st+2));
                if (i+(i-st+2)<en && h.isEq(h,st,i,hr,mn,mx)){
                    if(max<2*st+i+i-st+2-st+1){
                        max=2*st+i+i-st+2-st+1;
                        a1=i+(i-st+2);
                    }
                }
            }
            for (int i=en-1;i>=st;i--){
                int l=en-i;
                int mn=Math.min(n-1-i,n-1-(en-1));
                int mx=Math.max(n-1-i,n-1-(en-1));
                if (i-l>=st && h.isEq(h,i-l,i-1,hr,mn,mx)){
                    if(max<2*st+en-1-(i-l)+1){
                        a1=st-1;
                        a2=i-l;
                        max=2*st+en-1-(i-l)+1;
                    }
                }
                if (i-l-1>=st && h.isEq(h,i-l-1,i-2,hr,mn,mx)){
                    if(max<2*st+en-1-(i-l-1)+1){
                        a1=st-1;
                        a2=i-l-1;
                        max=2*st+en-1-(i-l-1)+1;
                    }
                }
            }
            if (max2==max && max!=1 && max2!=s.length()){
                System.out.println(s.substring(0,a1+2) + s.substring(a2));
                continue;
            }
            if (a2==-1){
                System.out.println(s.substring(0,a1+1));
            }else if (a1==-1){
                System.out.println(s.substring(a2));
            }else {
                StringBuilder sb=new StringBuilder();
                sb.append(s.substring(0,a1+1)+s.substring(a2));
                System.out.println(sb);
            }
        }
    }
    static class Hash{
        long p;
        long mod;
        long pow[];
        long hash[];
        Hash(String s,long p,long mod){
            int n=s.length();
            pow=new long[n+1];
            this.mod=mod;
            this.p=p;
            hash=new long[n+1];
            pow[0]=1;
            for (int i=1;i<=n;i++){
                int c=s.charAt(i-1)-'a';
                hash[i]=(hash[i-1]+pow[i-1]*c)%mod;
                pow[i]=(pow[i-1]*p)%mod;
            }
        }
        boolean isEq(Hash ha,int la,int ra,Hash hb,int lb,int rb){
            la++;ra++;rb++;lb++;
            if (lb>la){
                int tmp=la;
                la=lb;
                lb=tmp;
                tmp=ra;
                ra=rb;
                rb=tmp;
                Hash h=ha;
                ha=hb;
                hb=h;
            }
            return (ha.hash[ra]-ha.hash[la-1]+mod)%mod==(((hb.hash[rb]-hb.hash[lb-1]+mod)*pow[la-lb])%mod+mod)%mod;
        }

    }
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
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
}