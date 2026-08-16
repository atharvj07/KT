import java.io.*;
import java.util.*;
public class Q1 {
    public static void main(String[] args) throws Exception{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        PrintWriter w=new PrintWriter(System.out);
        int i,j,n,k,c=2;
        double temp=0,ans=Double.MIN_VALUE;
        String s[]=br.readLine().split(" ");
        n=Integer.parseInt(s[0]);
        k=Integer.parseInt(s[1]);
        int a[]=new int[n];
        Vector<Integer> v=new Vector<>();
        String s1[]=br.readLine().split(" ");
        for(i=0;i<n;i++){
            a[i]=Integer.parseInt(s1[i]);
            v.add(a[i]);
        }
        for(i=0;i<n;i++){
            if((i-1)>=0 && (a[i]-k)>=(a[i-1]+k) && !v.contains(a[i]-k)) {
                v.add(a[i]-k);
                c++;
            }
            if((i+1)<n && (a[i]+k)<=(a[i+1]-k) && !v.contains(a[i]+k)){
                v.add(a[i]+k);
                c++;
            }
        }
        w.print(c);
        w.flush();
        w.close();
    }
}