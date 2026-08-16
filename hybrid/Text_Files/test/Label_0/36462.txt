import java.io.*;
import java.util.*;

public class CodeForce{
   
	public static void main(String[] args) throws IOException {
           
	    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
            
                String[] str=br.readLine().split(" ");
               int n=Integer.parseInt(str[0]);
               double r=Double.parseDouble(str[1]);
               String[] s=br.readLine().split(" ");
               double[] arr=new double[n];
               for(int i=0;i<n;i++){
                   arr[i]=Double.parseDouble(s[i]);
               }
               double[][] c=new double[n][2];
               c[0][0]=arr[0];
               c[0][1]=r;
               int t=1;
               int flag=0;
               double max=Double.MIN_VALUE;
               for(int i=1;i<n;i++){
                   for(int j=i-1;j>=0;j--){
                       if(Math.abs(arr[i]-c[j][0])<=2*r){
                           //System.out.println(arr[i]+" "+i);
                           c[i][0]=arr[i];
                           c[i][1]=Math.sqrt((2*2*r*r)-((arr[i]-c[j][0])*(arr[i]-c[j][0])))+c[j][1];
                           flag=1;
                           max=Math.max(max,c[i][1]);
                       }
                   }
                   if(flag==0){
                       c[i][0]=arr[i];
                       //System.out.println(r);
                       c[i][1]=r;
                   }
                   else{
                       c[i][1]=max;
                   }
                   max=Double.MIN_VALUE;
                   flag=0;
               }
               
               for(int i=0;i<n;i++){
                   System.out.print(c[i][1]+" ");
               }
            
        }
            }