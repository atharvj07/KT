
import java.io.*;
import java.util.*;
import java.math.*;
import static java.lang.Math.*;
import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.Double.parseDouble;
import static java.lang.String.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
                                            //(new FileReader("input.in"));
        StringBuilder out = new StringBuilder();
        StringTokenizer tk;

        int n = parseInt(in.readLine());
        
        int [] a = new int[n];
        int [] b = new int[n];
        
        tk = new StringTokenizer(in.readLine());
        for(int i=0; i<n; i++)
            a[i] = parseInt(tk.nextToken());
        
        tk = new StringTokenizer(in.readLine());
        for(int i=0; i<n; i++)
            b[i] = parseInt(tk.nextToken());
        int L = log2(n)+1;
        
        int [][] dpa = new int[n][L];
        int [][] dpb = new int[n][L];
        
        for(int i=0; i<n; i++)
            dpa[i][0] = dpb[i][0] = i;
        
        for(int j=1; (1<<j)<=n; j++) {
            for(int i=0; i+(1<<j)<=n; i++) {
                if(a[dpa[i][j-1]] > a[dpa[i+(1<<(j-1))][j-1]])
                    dpa[i][j] = dpa[i][j-1];
                else dpa[i][j] = dpa[i+(1<<(j-1))][j-1];
                
                if(b[dpb[i][j-1]] < b[dpb[i+(1<<(j-1))][j-1]])
                    dpb[i][j] = dpb[i][j-1];
                else dpb[i][j] = dpb[i+(1<<(j-1))][j-1];
            }
        }
        
        
        long ans = 0;
        
        for(int l=0; l<n; l++) {
            int r1 = n+1, r2 = -1;
            
            int x = l,y = n-1,c;
            
            while(x <= y) {
                c = (x+y)/2;
        
                int j = log2(c-l+1);
                int mx = max(a[dpa[l][j]],a[dpa[c-(1<<j)+1][j]]),mn = min(b[dpb[l][j]],b[dpb[c-(1<<j)+1][j]]);
                
                if(mn == mx) {
                    r2 = max(r2, c);
                    x = c+1;
                } else if(mx > mn) y = c-1;
                else x = c+1;
            }
            
            if(r2==-1) continue;
            
            x = l;
            y = r2;
            
            while(x <= y) {
                c = (x+y)/2;
                
                int j = log2(c-l+1);
                int mx = max(a[dpa[l][j]],a[dpa[c-(1<<j)+1][j]]),mn = min(b[dpb[l][j]],b[dpb[c-(1<<j)+1][j]]);
                
                if(mn == mx) {
                    r1 = min(r1, c);
                    y = c-1;
                } else if(mx > mn) y = c-1;
                else x = c+1;
            }
            
            if(r1<n) {
                ans += (long)(r2-r1+1);
            }
        }
        
        System.out.println(ans);
    }
    
    static int log2(int n) {
        return (int)(log(n)/log(2));
    }
}

class SegmentTree {
    int mode,n;
    int [] seg;
    
    public SegmentTree(int n,int m) {
        this.seg = new int[4*n];
        this.mode = m;
        this.n = n;
    }
    
    public void insert(int i,int v) {
        if(mode == 0) insertMin(1,0,n-1,i,v);
        else insertMax(1,0,n-1,i,v);
    }
    
    public void insertMax(int p,int s,int e,int i,int v) {
        if(s == e) {
            seg[p] = v;
            return;
        }
        
        if(i <= (s+e)/2) insertMax(2*p,s,(s+e)/2,i,v);
        else insertMax(2*p+1,(s+e)/2+1,e,i,v);
        
        seg[p] = max(seg[2*p],seg[2*p+1]);
    }
    
    public void insertMin(int p,int s,int e,int i,int v) {
        if(s == e) {
            seg[p] = v;
            return;
        }
        
        if(i <= (s+e)/2) insertMin(2*p,s,(s+e)/2,i,v);
        else insertMin(2*p+1,(s+e)/2+1,e,i,v);
        
        seg[p] = min(seg[2*p],seg[2*p+1]);
    }
    
    public int getValue(int l,int r) {
        if(mode==0) return getMin(1,0,n-1,l,r);
        return getMax(1,0,n-1,l,r);
    }
    
    public int getMax(int p,int s,int e,int l,int r) {
        if(s>=l && e<=r)
            return seg[p];
        
        if(s>r || e<l)
            return Integer.MIN_VALUE;
        
        return max(getMax(2*p,s,(s+e)/2,l,r), getMax(2*p+1,(s+e)/2+1,e,l,r));
    }
    
    public int getMin(int p,int s,int e,int l,int r) {
        if(s>=l && e<=r)
            return seg[p];
        
        if(s>r || e<l)
            return Integer.MAX_VALUE;
        
        return min(getMin(2*p,s,(s+e)/2,l,r),getMin(2*p+1,(s+e)/2+1,e,l,r));
    }
}