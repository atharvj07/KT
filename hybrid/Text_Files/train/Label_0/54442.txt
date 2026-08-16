import java.util.*;
import java.io.*;
public class Main
{
    public static void main(String args[])throws Exception
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw=new PrintWriter(System.out);
        int k=Integer.parseInt(br.readLine());
        Queue<Long> queue=new LinkedList<>();
        for(int i=1;i<=9;i++)
        queue.add((long)i);
        long temp=0;
        for(int i=1;i<=k;i++)
        {
            temp=queue.poll();
            if(temp%10!=0)
            {
                queue.add(10*temp+(temp%10)-1);
            }
            queue.add(10*temp+(temp%10));
            if(temp%10!=9)
            queue.add(10*temp+(temp%10)+1);
        }
        pw.println(temp);
        pw.flush();
        pw.close();
    }
}