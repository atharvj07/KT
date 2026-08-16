/*BY:-PRASANG*/
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;
public class ImportantThings {
    static int[] a,b,c;
    static int temp,n,temp1,count;
    public static void main(String[]args)throws NumberFormatException,IOException
    {
        try{
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        a=new int[n];
        c=new int[n];       
        for(int i=0;i<n;i++)
            c[i]=i+1;
        for(int i=0;i<n;i++)
        a[i]=sc.nextInt();        
        b=Arrays.copyOf(a, n);
        a=InsertionSort(a);
        for(int i=0;i<n-1;i++)
        {            
            if(a[i]==a[i+1])            
            count++;            
        }
        if(count>=2)
        {   
        count=0;
        System.out.print("YES");
        for(int i=0;i<n-1;i++)
        {            
            if(a[i]==a[i+1])                                          
            print(i);                            
        }
        }
        else
            System.out.println("NO");
        }
        catch(Exception e)
        {
            System.out.println("oops ..."+e.getMessage());
        }
}
    public static int[] InsertionSort(int[] data){
  int len = data.length;  
  int i = 0;
  for(int j = 0;j<len;j++)
  {
    for(i=j+1;i<len;i++)
    {
        if(data[j]>data[i])
        {temp=data[j];
        data[j]=data[i];
        data[i]=temp;
        temp1=c[j];
        c[j]=c[i];
        c[i]=temp1;
        }
    }
  }
  return data;
}
    public static void print(int i)
    {
        if(count<2)
        {
            System.out.println();
            for(int b=0;b<n;b++)
        { 
        if(b==i)           
           System.out.print(c[i]+"\t");
        else if(b==i+1)
            System.out.print(c[i+1]+"\t");
        else
            System.out.print(c[b]+"\t");}
        }
        System.out.println();
        count++;        
        if(count<=3)
        {
        for(int b=0;b<n;b++)
        { 
        if(b==i)           
           System.out.print(c[i+1]+"\t");
        else if(b==i+1)
            System.out.print(c[i]+"\t");
        else
            System.out.print(c[b]+"\t");}
        }
        count++;       
    }
}