
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author workzone
 */
public class soldier_fact {
    public static void main(String[] args) throws IOException {
        PrintWriter writer=new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

        Scanner sc=new Scanner(System.in);
        
        FastReader s=new FastReader();
        int q;
        q=s.nextInt();
        int divisor[]=new int[5000009];
        divisor[0]=0;
        divisor[1]=0;
        int temp[]=new int[5000009];
        
        for(int i=2;i<=5000000;i++)
        {
            if(i%2!=0)
            {
                temp[i]=0;
            }
            else
            {
                temp[i]=temp[i/2]+1;
            }
        }
        for(int i=2;i<=5000000;++i)
        {
            divisor[i]=temp[i];
            temp[i]=0;
        }
        for(int i=3;i<=5000000;i+=2)
        {
            if(divisor[i]==0)
            {
                //making temp
                for(int j=i;j<=5000000;j+=i)
                {
                    temp[j]=temp[j/i]+1;
                }
                //adding temp to divisor
                for(int j=i;j<=5000000;j+=i)
                {
                    divisor[j]=divisor[j]+temp[j];
                    temp[j]=0;
                }
            }
        }
        int dp[]=new int[5000009];
        dp[0]=0;
        for(int i=1;i<=5000000;++i)
        {
            dp[i]=dp[i-1]+divisor[i];
        }
       
        /*
        int x,y;
        x=1000001;y=1000010;
        for(int i=x;i<=y;++i)
        {
            System.out.println(i+" "+divisor[i]);
        }
        */
        //working with queries
        int start,end;
        /*
        ArrayList<Integer> end1=new ArrayList<Integer> ();
        ArrayList<Integer> start1=new ArrayList<Integer> ();
        for(int i=0;i<q;++i)
        {
            
            end1.add(sc.nextInt());
            start1.add(sc.nextInt());
            
        }
        */
     
        for(int i=0;i<q;++i)
        {
            //System.out.println(dp[end]-dp[start]);
            end=s.nextInt();
            start=s.nextInt();
            writer.println(dp[end]-dp[start]);

        }
        writer.flush();
        writer.close();
    }
}

class FastReader
    {
        BufferedReader br;
        StringTokenizer st;
 
        public FastReader()
        {
            br = new BufferedReader(new
                     InputStreamReader(System.in));
        }
 
        String next()
        {
            while (st == null || !st.hasMoreElements())
            {
                try
                {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException  e)
                {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt()
        {
            return Integer.parseInt(next());
        }
 
        long nextLong()
        {
            return Long.parseLong(next());
        }
 
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
 
        String nextLine()
        {
            String str = "";
            try
            {
                str = br.readLine();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return str;
        }
    }
/*
fastening the output...


PrintWriter writer=new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

writer.print(ar.get(i).val+" ");

writer.flush();
writer.close();
*/

/*
BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
String line;
while ((line = bi.readLine()) != null)
    for (String numStr: line.split("\\s"))
        sum += Integer.parseInt(numStr);
*/