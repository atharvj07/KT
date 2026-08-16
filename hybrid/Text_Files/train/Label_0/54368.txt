import java.util.*;
import java.awt.image.BandedSampleModel;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Scanner;
public class B {

    static void sort(int[] A){

        int n = A.length;
        Random rnd = new Random();
        for(int i=0; i<n; ++i){
            int tmp = A[i];
            int randomPos = i + rnd.nextInt(n-i);
            A[i] = A[randomPos];
            A[randomPos] = tmp;
        }
        Arrays.sort(A);
    }

    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int cases = sc.nextInt();

        StringBuilder ans=new StringBuilder();
        for(int i=0;i<cases;i++)
        {
            Map<Long,Integer> map=new HashMap<>();
            int c=0;
            Map<Long,Integer> m2=new HashMap<>();
            int n = sc.nextInt();
             long u[] = new long[n];
            for(int j=0;j<n;j++)
            {
                u[j]=sc.nextLong();
                map.putIfAbsent(u[j],0);
                map.put(u[j],map.get(u[j])+1);
                if(m2.get(u[j])==null)
                {
                    m2.put(u[j],c);
                    c++;
                }
            }
            long s[]=new long[n];

            for(int j=0;j<n;j++)
            {
                s[j]=sc.nextLong();
            }

            long arr[][]=new long[map.size()][];
            long x[][]=new long[map.size()][];
            long sum[]=new long[map.size()];
            for(long j:map.keySet())
            {
                int key=(int)j;
                int val=m2.get(j);
                int num=map.get(j);
                arr[val]= new long[num];
                x[val]=new long[num];
            }

            int cons[]=new int[map.size()];
            //Arrays.fill(cons,-1);
            for(int j=0;j<n;j++)
            {
                int f=m2.get(u[j]);
                arr[f][cons[f]]=s[j];
               // x[f][cons[f]]=-1;
                sum[f]=s[j]+sum[f];
                cons[f]++;

            }

            for(int j=0;j<arr.length;j++)
            {
                Arrays.sort(arr[j]);
            }

            for(int j=0;j<map.size();j++)
            {
                for(int k=1;k<arr[j].length;k++)
                {
//                    if(k==0)
//                    {
//                        x[j][0]=arr[j][k];
//                    }
                    //else
                    {
                        x[j][k]=x[j][k-1]+arr[j][k-1];
                    }
                }
            }

            long fin[]=new long[n];
            for(int j=0;j<map.size();j++)
            {
                for(int k=0;k<n;k++)
                {
                    if(k>arr[j].length-1)
                    {
                        break;
                    }
                    else
                    {
                        int a=arr[j].length%(k+1);
                        //if(a<arr[j].length) {
                            fin[k] = fin[k] + sum[j] - x[j][a];

                    }
                }
            }

            for(int j=0;j<n;j++)
            {
                ans.append(fin[j]+" ");
            }

            ans.append("\n");


        }
        System.out.print(ans);

    }
}
