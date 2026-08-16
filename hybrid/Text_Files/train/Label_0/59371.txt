import java.util.Arrays;
import java.util.Scanner;

/**
 *
 * @author ganeshpachpind
 */
public class CodeForce447A {
    public static void main(String args[])
    {
        CodeForce447A process=new CodeForce447A();
        process.doProcess();
    }
    void doProcess()
    {
        Scanner sc=new Scanner(System.in);
        int p=sc.nextInt();
        int n=sc.nextInt();
        int a[]=new int[p];
        Arrays.fill(a,-1);
        System.out.println(check(p, a, sc,n));

    }
    int check(int p,int a[],Scanner sc,int n)
    {
        for(int i=0;i<n;i++)
        {
            int mod=(sc.nextInt())%p;
            if(a[mod]==-1)
            {
                a[mod]=mod;
            }
            else
            {                
                return i+1;                
            }            
        }
        return -1;
    }
    
}
