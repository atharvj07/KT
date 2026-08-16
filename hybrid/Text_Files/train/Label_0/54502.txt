import java.util.*;
import java.math.*;
import java.io.*;
public class E{
  public static void main(String args[]) throws Exception{
    int magic=51;
    BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
    int n=Integer.parseInt(in.readLine());
    String s[]=in.readLine().split(" ");
    int[]a=new int[n];
    a[0]=1;
    for(int i=1;i<n;i++)a[i]=Integer.parseInt(s[i-1]);
    s=in.readLine().split(" ");
    int[]b=new int[n];
    for(int i=0;i<n;i++)b[i]=Integer.parseInt(s[i]);
    String sm=in.readLine();
    BigInteger M=new BigInteger(sm);
    int[]c=new int[n];
    for(int i=1;i<n;i++)if(a[i]!=1){
      BigInteger[]qr=M.divideAndRemainder(new BigInteger(a[i]+""));
      c[i]=(int)qr[1].longValue();
      M=qr[0];
    }
    long mod=(long)(1e9+7);
    int mx=(int)(3e5+10);
    long [][]f=new long[2][magic*mx];
    int rw=0;
    f[0][0]=1;
    int sbi=0;
    int bef=0;
    for(int i=0;i<n;i++){
      int nxt=(int)( (1l*a[i]*b[i]-c[i] + bef)/a[i] );
      for(int x=0;x<=bef;x++){
        if(x-a[i]>=0){
          f[rw][x]+=f[rw][x-a[i]];;
          if(f[rw][x]>=mod)f[rw][x]-=mod;
        }
      }
      rw^=1;
      for(int x=0;x<=nxt;x++){
        f[rw][x]=0;
        long from=1l*a[i]*x+c[i];
        long at=from;
        long m=0;
        if(from>bef){
          m=(from-bef+a[i]-1)/a[i];
          at=from-m*a[i];
        }
        if(m<=b[i] && at>=0){
          long inc=f[rw^1][(int)at];
          long old=at;
          at=from-1l*a[i]*(b[i]+1);
          if(at>=0)inc-=f[rw^1][(int)at];
          inc=(inc%mod+mod)%mod;
          f[rw][x]=inc;        
        }
      } 
      bef=nxt;
    }
    
    if(M.compareTo(new BigInteger(""+bef))>0)System.out.println("0");
    else System.out.println(f[rw][(int)M.longValue()]);
  }
}
