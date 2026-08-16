import java.util.*;
import java.io.*;
 
public class mahakal{


    public static void main(String[] args) { 
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0)
        {

         int n=sc.nextInt();
           int a[]=new int[n];
           int l=0;
            int r=n-1;
            int ansl=0;
            int ansr=0;
            int suml=0;
            int sumr=0;
            int cnt=0;
            for(int i=0;i<n;i++)
            {
                a[i]=sc.nextInt();
            }
            for(int i=0;i<n;i++)
            {
                 
            while(l<=r )
            {
                if(cnt%2==0)
                {
                    int nsuml=0;
                    while(nsuml<=sumr && l<=r)
                    {
                        nsuml=nsuml+a[l];
                        l=l+1;
                    }
                    ansl=ansl+nsuml;
                    suml=nsuml;
                }
                else
                {
                    int nsumr=0;
                    while(l<=r && nsumr<=suml)
                    {
                        nsumr=nsumr+a[r];
                        r=r-1;
                    }
                
                ansr=ansr+nsumr;
                sumr=nsumr;
            }
            cnt++;
            }
        }
        System.out.println(cnt+" "+ansl+" "+ansr);


}
       }
   }
   




   
    
                