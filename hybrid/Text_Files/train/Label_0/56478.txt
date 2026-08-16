import java.util.*;
import java.lang.*;
public class Codeforces {
    static int t[][]=new int[5005][5005];
    static Scanner sr=new Scanner(System.in);
    static int gcd(int a, int b)
    {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
    public static void main(String[] args) throws java.lang.Exception {
        StringBuilder ans = new StringBuilder("");
        int T=sr.nextInt();
        while(T-->0)
        {
            int n=sr.nextInt();
            long a[]=new long[n];
            for(int i=0;i<n;i++)
                a[i]=sr.nextLong();
            HashMap<Long,Long>h=new HashMap<>();
            long A=0;
            for(int i=0;i<n;i++)
            {
                if(h.containsKey(a[i]))
                {
                    A+=h.get(a[i])*(n-i);
                    h.put(a[i],h.get(a[i])+i+1);
                }
                else
                {
                    h.put(a[i],(long)(i+1));
                }
            }
            ans.append(A);
            ans.append('\n');
        }
        System.out.println(ans);
    }
}