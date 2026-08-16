import java.util.*;
public class ytdchgcjgcvg{
    public static void main(String[] A){
        Scanner s=new Scanner(System.in);
        int l=s.nextInt();
        int sum=0;
        boolean f=false;
        boolean g=true;
        for (int i=0;i<l;i++) {
        int a=s.nextInt();
        int b=s.nextInt();
        int x[]=new int [a];
        int y[]=new int [b];
        for (int j=0;j<a;j++) {
        	x[j]=s.nextInt();
        }
        for(int j=0;j<b;j++) {
        	y[j]=s.nextInt();
        }
        for (int j=0;j<a-1&&!f;j++) {
        	if (x[j]>x[j+1]) {
        		for(int l1=0;l1<b;l1++) {
        			if (j+1==y[l1]) {
        				int temp=x[j];
        				x[j]=x[j+1];
        				x[j+1]=temp;
        				f=true;
        				j=-1;
        				
        			}
        		}
        		
        		if (!f) {
        			g=false;
        			
        		}
        	 f=false;
        	}
        	
        	
        }if (g) {
        	System.out.println("YES");}
        	else {
        		System.out.println("NO");
        		
        		
        }
    	g=true;
        	}}}
 