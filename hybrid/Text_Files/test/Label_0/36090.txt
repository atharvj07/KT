import java.util.*;
import java.math.*;
public class Main{
        private static int max=200*1000+5;
        public static void main(String args[]){
                Scanner sc=new Scanner(System.in);
                int n=sc.nextInt();
                int k=sc.nextInt();
                int a[]=new int[n];
                for(int i=0;i<n;i++){
                        a[i]=sc.nextInt();
                }
                List<Integer> [] vals=new ArrayList[max];
                for(int i=0;i<max;i++){
                        vals[i]=new ArrayList<Integer>();
                }
                for(int i:a){
                        int y=i;
                        int cur=0;
                        while(y>0){
                                
                                vals[y].add(cur);
                                y=y/2;
                                cur++;
                        }
                }
                int res=Integer.MAX_VALUE;
                for(List<Integer> l:vals){
                        if(l.size()>=k){
                                Collections.sort(l);
                                int t=0;
                                for(int i=0;i<k;i++){
                                        t+=l.get(i);
                                }
                                 res=Math.min(t,res);
                        }
                       
                }
                System.out.println(res);
        }
}