import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Codef{
    public static void main(String[] args) throws IOException{
        BufferedReader vod=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s=new StringTokenizer(vod.readLine());
        int n=Integer.parseInt(s.nextToken());
        int m=Integer.parseInt(s.nextToken());
        s=new StringTokenizer(vod.readLine());
        int[] ar=new int[n];
        int[] an=new int[n+1];
        int[] ax=new int[n+1];
        for (int i=0; i<ax.length; i++) ax[i]=1000000;
        for (int i=0; i<n; i++){
            ar[i]=Integer.parseInt(s.nextToken());
        }
        for (int i=0; i<n; i++)
            an[ar[i]]=i+1;
        int a=0,b=0,min=0,max=0;
        for (int i=0; i<m; i++){
            s=new StringTokenizer(vod.readLine());
            a=Integer.parseInt(s.nextToken());
            b=Integer.parseInt(s.nextToken());
            min=Math.min(an[a], an[b]);
            max=Math.max(an[a], an[b]);
            ax[min]=Math.min(ax[min],max);
        }
        long ans=0;
        int c=n;
        for (int i=n; i>=1; i--){
            if (ax[i]<1000000) c=Math.min(c,ax[i]-1);
            ans+=(long)(c-i+1);
        }
        System.out.print(ans);
    }
}