import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;





public class abc {
    public static void main(String args[])throws IOException
    {
       BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
       int n=Integer.parseInt(br.readLine());
		String s[]=br.readLine().trim().split("\\ ");
		int a[]=new int[n];
		for(int i=0;i<n;i++)
		a[i]= Integer.parseInt(s[i]);
		double min=((double)a[0])*(double)10.0;
		double max=min+(double)10;
		for(int i=1;i<n;i++){
			double min1=(double)a[i]*(double)10.0;
			double max1=min1+(double)10.0;
			max1/=(double)(i+1);
			min1/=(double)(i+1);
			if(max1<max)
				max=max1;
			if(min1>min)
				min=min1;
		}
//		System.out.println(max-(double)0.0000001+" "+min);
		double totalTailMax=(max-(double)0.0000001)*(double)(n+1);
		double totalTailMin=min*(double)(n+1);
//		System.out.println(totalTailMax+" "+totalTailMin);
		long ansMax=(long)totalTailMax/(long)10;
		long ansMin=(long)totalTailMin/(long)10;
//		System.out.println(ansMax+" "+ansMin);
		if(ansMax==ansMin){
			System.out.println("unique"+"\n"+ansMax);
		}
		else
			System.out.println("not unique");
    }
}