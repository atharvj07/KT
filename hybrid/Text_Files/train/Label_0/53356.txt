import java.util.*;
public class C638B
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0)
        {
            int n=sc.nextInt();
            int k=sc.nextInt();
            int[] ar =new int[n];
            for(int x=0;x<n;x++)
            {
                ar[x]=sc.nextInt();
            }
                solve(ar,n,k);
        }
    }

    public static void solve(int[] ar, int n, int k)
    {
        Set<Integer> set=new HashSet<>();
        for(int x=0;x<n;x++)
        {
            set.add(ar[x]);
        }
        if(set.size()>k)
        {
            System.out.println(-1);
            return;
        }
        System.out.println(n*k);
        for(int x=0;x<n;x++)
        {
            for(int a:set)
            {
                System.out.print(a+" ");
            }
            for(int y=0;y<k-set.size();y++)
            {
                System.out.print("1 ");
            }
        }
        System.out.println();
    }
}