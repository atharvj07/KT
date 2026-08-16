import java.io.*;
import java.util.*;
public class Ishu
{
    static Scanner scan = new Scanner(System.in);
    static BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out)); 
    static long find(int[] a, int beg, int end) throws Exception
    {
    long ans = Long.MAX_VALUE;
    int i;
    
    int cnt = 0;
    long sum = 0l;
    
    long[] dp = new long[end-beg+1];
    long[] ds = new long[end-beg+1];
    
    for(i=beg;i<=end;++i)
        {
        sum += cnt;
        dp[i-beg] = sum;
        if(a[i] == 1)
            ++cnt; 
        }
        
    cnt = 0;
    sum = 0l;
    int j = end - beg;
    for(i=end;i>=beg;--i,--j)
        {
        sum += cnt;
        ds[j] = sum;
        if(a[i] == 1)
            ++cnt;
        }
        
    for(i=0;i<=end-beg;++i)
        {
        long ca = dp[i] + ds[i];
        ans = Math.min(ans, ca);
        }
    
//    for(i=0;i<end-beg+1;++i)
//        output.write(dp[i] + " ");
//    output.write("\n");
//    for(i=0;i<end-beg+1;++i)
//        output.write(ds[i] + " ");
//    output.write("\n");    
    return ans;
    }
    static long solve(int[] a, int f) throws Exception
    {
    int n = a.length;
    int i;
    
    long ans = 0;
    int cnt = 0;
    int pre = -1;
    
    for(i=0;i<n;++i)
        {
        if(a[i] == 0)
            continue;
            
        if(cnt == 0)
            pre = i;
            
        ++cnt;
        
        if(cnt < f)
            continue;
         
        ans += find(a, pre, i);
        cnt = 0;
        }
    return ans;
    }
    static void tc() throws Exception
    {
    int n = scan.nextInt();
    int i;
    int[] a = new int[n];
    int cnt = 0;
    for(i=0;i<n;++i)
        {
        a[i] = scan.nextInt();
        cnt += a[i];
        }
    if(cnt == 1)
        {
        output.write("-1\n");
        output.flush();
        return;
        }    
    
    long ans = Long.MAX_VALUE;    
    for(int f=2;f*f<=cnt;++f) 
        {
        if(cnt % f > 0)
            continue;
            
        int one = f;
        int two = cnt / f;
        
        ans = Math.min(ans, solve(a, one));
        ans = Math.min(ans, solve(a, two));    
        }   
        
    ans = Math.min(ans, solve(a, cnt));
    output.write(ans + "\n");
    output.flush();
    }
    public static void main(String[] args) throws Exception
    {
    int t = 1;
    //t = scan.nextInt();
    while(t-- > 0)
        tc();
    }
}
