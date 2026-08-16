////////////////////---------------------------SHUBHAM CHAUDHARI-------------------------------///////////////////////


import java.util.*;

public class Main {
    static int mod=100000000;
    static HashMap<Integer,Integer>map;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n=in.nextInt();
        int k=in.nextInt();
        long A[]=new long[n];
        for(int i=0;i<n;i++)
        {
            A[i]=in.nextInt();
        }
        HashMap<Long,Long>map1=new HashMap<>();
        HashMap<Long,Long>map2=new HashMap<>();
        long res=0;
        for(int i=0;i<n;i++)
        {
            if(A[i]%k==0)
            {
                if(map2.containsKey(A[i]/k))
                {
                    res+=map2.get(A[i]/k);
                }
                if(map1.containsKey(A[i]/k))
                {
                    if(map2.containsKey(A[i]))map2.put(A[i],map2.get(A[i])+map1.get(A[i]/k));
                    else map2.put(A[i],map1.get(A[i]/k));
                }
            }
            if(map1.containsKey(A[i]))map1.put(A[i],map1.get(A[i])+1);
            else map1.put(A[i],1L);
        }

        System.out.println(res);
    }


}